.PHONY: help python rust build wasm pdf
help:
	@echo "Resume as Code"
	@echo "========================"
	@grep -E '^[a-zA-Z0-9_%/-]+:.*?## .*$$' $(MAKEFILE_LIST) | sort | awk \
		'BEGIN {FS = ":.*?## "}; {printf "\033[36m%-30s\033[0m %s\n", $$1, $$2}'

python:  ## Build the Python protobuf interface
	cd protos && protoc resume.proto --python_out=../yaml-parser

rust:  ## Build the Rust protobuf interface
	cd proto-codegen && cargo run -- --crate-dir ../wasm-app --proto-dir ../protos

build:  ## Compile the resume data into protobuf binary
	python yaml-parser/build_resume.py

wasm:  ## Compiile the WASM rust app
	cd wasm-app && $(MAKE) build
	cd wasm-app && cp pkg/wasm_app_bg.wasm ../pkg/


all: python rust build wasm  ## Run both Python & Rust codegens, build the resume, build the wasm app

pdf:  ## Create a rendered PDF of the resume based on the wasm app
	./scripts/generate_pdf.sh

serve:  ## Serve the `wasm-app` directory on port 8080
	cd wasm-app && $(MAKE) serve
