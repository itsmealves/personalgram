# -*- coding: utf-8 -*-
# Generated by the protocol buffer compiler.  DO NOT EDIT!
# source: auth.proto

import sys
_b=sys.version_info[0]<3 and (lambda x:x) or (lambda x:x.encode('latin1'))
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from google.protobuf import reflection as _reflection
from google.protobuf import symbol_database as _symbol_database
# @@protoc_insertion_point(imports)

_sym_db = _symbol_database.Default()


from google.protobuf import empty_pb2 as google_dot_protobuf_dot_empty__pb2


DESCRIPTOR = _descriptor.FileDescriptor(
  name='auth.proto',
  package='personalgram.auth',
  syntax='proto3',
  serialized_options=None,
  serialized_pb=_b('\n\nauth.proto\x12\x11personalgram.auth\x1a\x1bgoogle/protobuf/empty.proto\"1\n\x0b\x41uthRequest\x12\x10\n\x08username\x18\x01 \x01(\t\x12\x10\n\x08password\x18\x02 \x01(\t\"\x1d\n\x0c\x41uthResponse\x12\r\n\x05token\x18\x01 \x01(\t2\xdd\x01\n\x06\x43\x61mera\x12H\n\x05login\x12\x1e.personalgram.auth.AuthRequest\x1a\x1f.personalgram.auth.AuthResponse\x12\x41\n\x06logout\x12\x16.google.protobuf.Empty\x1a\x1f.personalgram.auth.AuthResponse\x12\x46\n\x0b\x63urrentUser\x12\x16.google.protobuf.Empty\x1a\x1f.personalgram.auth.AuthResponseb\x06proto3')
  ,
  dependencies=[google_dot_protobuf_dot_empty__pb2.DESCRIPTOR,])




_AUTHREQUEST = _descriptor.Descriptor(
  name='AuthRequest',
  full_name='personalgram.auth.AuthRequest',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='username', full_name='personalgram.auth.AuthRequest.username', index=0,
      number=1, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=_b("").decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='password', full_name='personalgram.auth.AuthRequest.password', index=1,
      number=2, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=_b("").decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
  ],
  extensions=[
  ],
  nested_types=[],
  enum_types=[
  ],
  serialized_options=None,
  is_extendable=False,
  syntax='proto3',
  extension_ranges=[],
  oneofs=[
  ],
  serialized_start=62,
  serialized_end=111,
)


_AUTHRESPONSE = _descriptor.Descriptor(
  name='AuthResponse',
  full_name='personalgram.auth.AuthResponse',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='token', full_name='personalgram.auth.AuthResponse.token', index=0,
      number=1, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=_b("").decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
  ],
  extensions=[
  ],
  nested_types=[],
  enum_types=[
  ],
  serialized_options=None,
  is_extendable=False,
  syntax='proto3',
  extension_ranges=[],
  oneofs=[
  ],
  serialized_start=113,
  serialized_end=142,
)

DESCRIPTOR.message_types_by_name['AuthRequest'] = _AUTHREQUEST
DESCRIPTOR.message_types_by_name['AuthResponse'] = _AUTHRESPONSE
_sym_db.RegisterFileDescriptor(DESCRIPTOR)

AuthRequest = _reflection.GeneratedProtocolMessageType('AuthRequest', (_message.Message,), {
  'DESCRIPTOR' : _AUTHREQUEST,
  '__module__' : 'auth_pb2'
  # @@protoc_insertion_point(class_scope:personalgram.auth.AuthRequest)
  })
_sym_db.RegisterMessage(AuthRequest)

AuthResponse = _reflection.GeneratedProtocolMessageType('AuthResponse', (_message.Message,), {
  'DESCRIPTOR' : _AUTHRESPONSE,
  '__module__' : 'auth_pb2'
  # @@protoc_insertion_point(class_scope:personalgram.auth.AuthResponse)
  })
_sym_db.RegisterMessage(AuthResponse)



_CAMERA = _descriptor.ServiceDescriptor(
  name='Camera',
  full_name='personalgram.auth.Camera',
  file=DESCRIPTOR,
  index=0,
  serialized_options=None,
  serialized_start=145,
  serialized_end=366,
  methods=[
  _descriptor.MethodDescriptor(
    name='login',
    full_name='personalgram.auth.Camera.login',
    index=0,
    containing_service=None,
    input_type=_AUTHREQUEST,
    output_type=_AUTHRESPONSE,
    serialized_options=None,
  ),
  _descriptor.MethodDescriptor(
    name='logout',
    full_name='personalgram.auth.Camera.logout',
    index=1,
    containing_service=None,
    input_type=google_dot_protobuf_dot_empty__pb2._EMPTY,
    output_type=_AUTHRESPONSE,
    serialized_options=None,
  ),
  _descriptor.MethodDescriptor(
    name='currentUser',
    full_name='personalgram.auth.Camera.currentUser',
    index=2,
    containing_service=None,
    input_type=google_dot_protobuf_dot_empty__pb2._EMPTY,
    output_type=_AUTHRESPONSE,
    serialized_options=None,
  ),
])
_sym_db.RegisterServiceDescriptor(_CAMERA)

DESCRIPTOR.services_by_name['Camera'] = _CAMERA

# @@protoc_insertion_point(module_scope)
