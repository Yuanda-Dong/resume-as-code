# Resume as Code

View my resume: [here](https://yuanda-dong.github.io/resume-as-code/)

After years of rewriting resumes in Microsoft Word, Adobe Photoshop, and LaTeX, I decided to start maintaining my resume as a static web page with the content stored in a simple YAML file.


The [resume data](resume_data.yaml) file makes it easy to update resume information without messing up the formatting. Additionally, web apps separate content from styling, so many different layouts/designs can be applied to the same resume by just using a different [styles.css](wasm-app/styles.css). Storing a resume as code also benefits from Git versioning, making it possible go back in time to previous views.


### Contents
* [Overview](#overview)
* [Build Instructions](#building)
* [Development Setup](#dev-setup)
* [Docker Development](#docker-dev)


<a name="overview"></a>
## Overview

* Resume content is kept in [resume_data.yaml](resume_data.yaml).
* The schema of this data is described in the protocol buffer [protos/resume.proto](protos/resume.proto).
* Content from [resume_data.yaml](resume_data.yaml) is serialized to binary protocol buffers via generated Python.
* Rust code is auto-generated to read the binary content.
* The resume content compiled into a rust-based web assembly app to provide some interactivity using [Yew](https://yew.rs/docs/en/intro/).
* A PDF resume is rendered using headless Chrome.
* The static web app is uploaded to S3 for hosting.

In general, the only piece that needs to be updated is [resume_data.yaml](resume_data.yaml) for content. Occasionally [wasm-app/styles.css](wasm-app/styles.css) is updated to modify the layout.


<a name="building"></a>
## Build Instructions

Instructions for building the components of the resume. The full build pipeline (minus PDF generation and hosting) can be quickly ran with:
```
make all
```

1. Generate the Python protobuf code in `yaml-parser/`. Required if changing `proto/resume.proto`.
```
make python
```

2. Generate the Rust protobuf code in `wasm-app/src/protos`. Required if changing `proto/resume.proto`.
```
make rust
```

3. Compile the `resume_data.yaml` into binary. Required if changing `resume_data.yaml`.
```
make build
```

4. Compile the web assembly application. Required if any changes are made.
```
make wasm
```

5. Render a PDF from the web assembly app.
```
make pdf
```
Note: this operation may sometimes not correctly render fonts/icons. Always inspect the output pdf and rerun if incorrect.

6. Publish to S3
```
./scripts/sync_s3.sh <name-of-bucket>
```



<a name="dev-setup"></a>
## Development Setup

The following tools are used for end-to-end building of this project:
* [cargo](#cargo)
* [wasm-pack](#wasm-pack)
* [python](#python)
* [protobuf](#protobuf)
* [rollup](#rollup)
* [chrome](#chrome)
* [AWS CLI](#aws-cli)

A brief explanation of how each tool is used:

<a name="cargo"></a>
#### [cargo](https://github.com/rust-lang/cargo)
Rust's Cargo tool chain is used to compile the Rust/wasm components of this project. Can be installed following [Install Rust](https://www.rust-lang.org/tools/install).

<a name="wasm-pack"></a>
#### [wasm-pack](https://github.com/rustwasm/wasm-pack)
This tool is used to build Rust-based web assembly projects and compile to JavaScript-compatible targets. Can be installed along via cargo:
```
cargo install wasm-pack wasm-bindgen-cli
```

<a name="python"></a>
#### [python](https://www.python.org/)
Python 3 is used to parse the YAML resume description into a binary message that is included in the compiled web assembly binary. It also is used as an HTTP server when rendering PDFs from the static wasm application. To install the required Python libraries:
```
pip install -r requirements.txt
```

<a name="protobuf"></a>
#### [protobuf](https://developers.google.com/protocol-buffers)
The `protoc` tool is used to compile the resume proto and generate the Python classes in "./yaml-parser". These can be installed following the [Protocol Buffers Documentation](https://developers.google.com/protocol-buffers/docs/downloads).

<a name="rollup"></a>
#### [rollup](https://www.npmjs.com/package/rollup)
Rollup is a module bundler used to package the compiled web app generated by wasm-pack into the static webpage for serving. Rollup can be [installed from npm](https://www.npmjs.com/package/rollup).

<a name="chrome"></a>
#### [chrome](https://www.google.com/chrome/)
Headless Chrome is used to render the static page into a PDF document that is exportable from the hosted web app. This is how the PDF resume is generated.

<a name="aws-cli"></a>
#### [AWS CLI](https://aws.amazon.com/cli/)
I host the compiled web app on AWS, serving it from an S3 bucket via CloudFront. AWS CLI is required to upload the compiled artifacts to S3. Can be installed from [documentation](https://docs.aws.amazon.com/cli/latest/userguide/cli-chap-install.html), or via `pip install awscli`.



<a name="docker-dev"></a>
## Docker Development

Included is a [Dockerfile](Dockerfile) containing all of the [above](#dev-setup) tools installed. To develop and run the [build processes](#building) in a Docker container:

```
docker build -t resume .
docker run --rm -it -v $(pwd):/home/root resume
```
This will launch the Docker container with an interactive bash shell and this repo mounted to the container home directory.
