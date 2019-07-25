# Generated by the gRPC Python protocol compiler plugin. DO NOT EDIT!
import grpc

from . import gnes_pb2 as gnes__pb2


class GnesRPCStub(object):
  # missing associated documentation comment in .proto file
  pass

  def __init__(self, channel):
    """Constructor.

    Args:
      channel: A grpc.Channel.
    """
    self.Train = channel.unary_unary(
        '/gnes.GnesRPC/Train',
        request_serializer=gnes__pb2.Request.SerializeToString,
        response_deserializer=gnes__pb2.Response.FromString,
        )
    self.Index = channel.unary_unary(
        '/gnes.GnesRPC/Index',
        request_serializer=gnes__pb2.Request.SerializeToString,
        response_deserializer=gnes__pb2.Response.FromString,
        )
    self.Query = channel.unary_unary(
        '/gnes.GnesRPC/Query',
        request_serializer=gnes__pb2.Request.SerializeToString,
        response_deserializer=gnes__pb2.Response.FromString,
        )
    self.Call = channel.unary_unary(
        '/gnes.GnesRPC/Call',
        request_serializer=gnes__pb2.Request.SerializeToString,
        response_deserializer=gnes__pb2.Response.FromString,
        )
    self.RequestStreamCall = channel.stream_unary(
        '/gnes.GnesRPC/RequestStreamCall',
        request_serializer=gnes__pb2.Request.SerializeToString,
        response_deserializer=gnes__pb2.Response.FromString,
        )


class GnesRPCServicer(object):
  # missing associated documentation comment in .proto file
  pass

  def Train(self, request, context):
    """option (rpc_core.method_no_deadline) = true;
    option (rpc_core.service_default_deadline_ms) = 5000;
    """
    context.set_code(grpc.StatusCode.UNIMPLEMENTED)
    context.set_details('Method not implemented!')
    raise NotImplementedError('Method not implemented!')

  def Index(self, request, context):
    # missing associated documentation comment in .proto file
    pass
    context.set_code(grpc.StatusCode.UNIMPLEMENTED)
    context.set_details('Method not implemented!')
    raise NotImplementedError('Method not implemented!')

  def Query(self, request, context):
    # missing associated documentation comment in .proto file
    pass
    context.set_code(grpc.StatusCode.UNIMPLEMENTED)
    context.set_details('Method not implemented!')
    raise NotImplementedError('Method not implemented!')

  def Call(self, request, context):
    # missing associated documentation comment in .proto file
    pass
    context.set_code(grpc.StatusCode.UNIMPLEMENTED)
    context.set_details('Method not implemented!')
    raise NotImplementedError('Method not implemented!')

  def RequestStreamCall(self, request_iterator, context):
    # missing associated documentation comment in .proto file
    pass
    context.set_code(grpc.StatusCode.UNIMPLEMENTED)
    context.set_details('Method not implemented!')
    raise NotImplementedError('Method not implemented!')


def add_GnesRPCServicer_to_server(servicer, server):
  rpc_method_handlers = {
      'Train': grpc.unary_unary_rpc_method_handler(
          servicer.Train,
          request_deserializer=gnes__pb2.Request.FromString,
          response_serializer=gnes__pb2.Response.SerializeToString,
      ),
      'Index': grpc.unary_unary_rpc_method_handler(
          servicer.Index,
          request_deserializer=gnes__pb2.Request.FromString,
          response_serializer=gnes__pb2.Response.SerializeToString,
      ),
      'Query': grpc.unary_unary_rpc_method_handler(
          servicer.Query,
          request_deserializer=gnes__pb2.Request.FromString,
          response_serializer=gnes__pb2.Response.SerializeToString,
      ),
      'Call': grpc.unary_unary_rpc_method_handler(
          servicer.Call,
          request_deserializer=gnes__pb2.Request.FromString,
          response_serializer=gnes__pb2.Response.SerializeToString,
      ),
      'RequestStreamCall': grpc.stream_unary_rpc_method_handler(
          servicer.RequestStreamCall,
          request_deserializer=gnes__pb2.Request.FromString,
          response_serializer=gnes__pb2.Response.SerializeToString,
      ),
  }
  generic_handler = grpc.method_handlers_generic_handler(
      'gnes.GnesRPC', rpc_method_handlers)
  server.add_generic_rpc_handlers((generic_handler,))
