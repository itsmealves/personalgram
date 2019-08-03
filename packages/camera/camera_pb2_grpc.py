# Generated by the gRPC Python protocol compiler plugin. DO NOT EDIT!
import grpc

import camera_pb2 as camera__pb2
from google.protobuf import empty_pb2 as google_dot_protobuf_dot_empty__pb2


class CameraStub(object):
  # missing associated documentation comment in .proto file
  pass

  def __init__(self, channel):
    """Constructor.

    Args:
      channel: A grpc.Channel.
    """
    self.getFrame = channel.unary_unary(
        '/personalgram.camera.Camera/getFrame',
        request_serializer=google_dot_protobuf_dot_empty__pb2.Empty.SerializeToString,
        response_deserializer=camera__pb2.FrameResponse.FromString,
        )


class CameraServicer(object):
  # missing associated documentation comment in .proto file
  pass

  def getFrame(self, request, context):
    # missing associated documentation comment in .proto file
    pass
    context.set_code(grpc.StatusCode.UNIMPLEMENTED)
    context.set_details('Method not implemented!')
    raise NotImplementedError('Method not implemented!')


def add_CameraServicer_to_server(servicer, server):
  rpc_method_handlers = {
      'getFrame': grpc.unary_unary_rpc_method_handler(
          servicer.getFrame,
          request_deserializer=google_dot_protobuf_dot_empty__pb2.Empty.FromString,
          response_serializer=camera__pb2.FrameResponse.SerializeToString,
      ),
  }
  generic_handler = grpc.method_handlers_generic_handler(
      'personalgram.camera.Camera', rpc_method_handlers)
  server.add_generic_rpc_handlers((generic_handler,))
