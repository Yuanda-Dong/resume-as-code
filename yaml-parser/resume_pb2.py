# -*- coding: utf-8 -*-
# Generated by the protocol buffer compiler.  DO NOT EDIT!
# source: resume.proto
"""Generated protocol buffer code."""
from google.protobuf.internal import builder as _builder
from google.protobuf import descriptor as _descriptor
from google.protobuf import descriptor_pool as _descriptor_pool
from google.protobuf import symbol_database as _symbol_database
# @@protoc_insertion_point(imports)

_sym_db = _symbol_database.Default()


from google.protobuf import timestamp_pb2 as google_dot_protobuf_dot_timestamp__pb2


DESCRIPTOR = _descriptor_pool.Default().AddSerializedFile(b'\n\x0cresume.proto\x1a\x1fgoogle/protobuf/timestamp.proto\"\xb2\x02\n\x06Resume\x12\x0c\n\x04name\x18\x01 \x01(\t\x12\r\n\x05\x65mail\x18\x02 \x01(\t\x12\x13\n\x0bsource_code\x18\x03 \x01(\t\x12\x11\n\thost_link\x18\x04 \x01(\t\x12\"\n\x0cphone_number\x18\x05 \x01(\x0b\x32\x0c.PhoneNumber\x12\x1b\n\x08location\x18\x06 \x01(\x0b\x32\t.Location\x12\x18\n\x10linkedin_profile\x18\x07 \x01(\t\x12\x16\n\x0egithub_profile\x18\x08 \x01(\t\x12\x10\n\x08\x61\x62out_me\x18\t \x01(\t\x12\x1d\n\teducation\x18\n \x03(\x0b\x32\n.Education\x12\x1f\n\nexperience\x18\x0b \x03(\x0b\x32\x0b.Experience\x12\x1e\n\x06skills\x18\x0c \x03(\x0b\x32\x0e.SkillCategory\"3\n\x0bPhoneNumber\x12\x14\n\x0c\x63ountry_code\x18\x01 \x01(\r\x12\x0e\n\x06number\x18\x02 \x01(\x04\"8\n\x08Location\x12\x0c\n\x04\x63ity\x18\x01 \x01(\t\x12\r\n\x05state\x18\x02 \x01(\t\x12\x0f\n\x07\x63ountry\x18\x03 \x01(\t\"_\n\tDateRange\x12)\n\x05start\x18\x01 \x01(\x0b\x32\x1a.google.protobuf.Timestamp\x12\'\n\x03\x65nd\x18\x02 \x01(\x0b\x32\x1a.google.protobuf.Timestamp\"\xc6\x01\n\tEducation\x12\x13\n\x0binstitution\x18\x01 \x01(\t\x12\r\n\x05major\x18\x02 \x01(\t\x12\x13\n\x0b\x64\x65scription\x18\x03 \x01(\t\x12\x1a\n\x06period\x18\x04 \x01(\x0b\x32\n.DateRange\x12!\n\x06\x64\x65gree\x18\x05 \x01(\x0e\x32\x11.Education.Degree\x12\x1b\n\x08location\x18\x06 \x01(\x0b\x32\t.Location\"$\n\x06\x44\x65gree\x12\r\n\tBACHELORS\x10\x00\x12\x0b\n\x07MASTERS\x10\x01\"\x90\x01\n\nExperience\x12\r\n\x05title\x18\x01 \x01(\t\x12\x14\n\x0corganization\x18\x02 \x01(\t\x12\x0f\n\x07website\x18\x03 \x01(\t\x12\x1a\n\x06period\x18\x04 \x01(\x0b\x32\n.DateRange\x12\x1b\n\x08location\x18\x05 \x01(\x0b\x32\t.Location\x12\x13\n\x04\x64uty\x18\x06 \x03(\x0b\x32\x05.Duty\"7\n\x04\x44uty\x12\x13\n\x0b\x64\x65scription\x18\x01 \x01(\t\x12\x0c\n\x04tags\x18\x02 \x03(\t\x12\x0c\n\x04link\x18\x03 \x01(\t\"/\n\rSkillCategory\x12\x10\n\x08\x63\x61tegory\x18\x01 \x01(\t\x12\x0c\n\x04tags\x18\x02 \x03(\tb\x06proto3')

_builder.BuildMessageAndEnumDescriptors(DESCRIPTOR, globals())
_builder.BuildTopDescriptorsAndMessages(DESCRIPTOR, 'resume_pb2', globals())
if _descriptor._USE_C_DESCRIPTORS == False:

  DESCRIPTOR._options = None
  _RESUME._serialized_start=50
  _RESUME._serialized_end=356
  _PHONENUMBER._serialized_start=358
  _PHONENUMBER._serialized_end=409
  _LOCATION._serialized_start=411
  _LOCATION._serialized_end=467
  _DATERANGE._serialized_start=469
  _DATERANGE._serialized_end=564
  _EDUCATION._serialized_start=567
  _EDUCATION._serialized_end=765
  _EDUCATION_DEGREE._serialized_start=729
  _EDUCATION_DEGREE._serialized_end=765
  _EXPERIENCE._serialized_start=768
  _EXPERIENCE._serialized_end=912
  _DUTY._serialized_start=914
  _DUTY._serialized_end=969
  _SKILLCATEGORY._serialized_start=971
  _SKILLCATEGORY._serialized_end=1018
# @@protoc_insertion_point(module_scope)
