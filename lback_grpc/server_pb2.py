# Generated by the protocol buffer compiler.  DO NOT EDIT!
# source: server.proto

import sys
_b=sys.version_info[0]<3 and (lambda x:x) or (lambda x:x.encode('latin1'))
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from google.protobuf import reflection as _reflection
from google.protobuf import symbol_database as _symbol_database
from google.protobuf import descriptor_pb2
# @@protoc_insertion_point(imports)

_sym_db = _symbol_database.Default()


import shared_pb2 as shared__pb2


DESCRIPTOR = _descriptor.FileDescriptor(
  name='server.proto',
  package='lbackgrpc',
  syntax='proto3',
  serialized_pb=_b('\n\x0cserver.proto\x12\tlbackgrpc\x1a\x0cshared.proto2\x81\x02\n\x06Server\x12\x41\n\x0bRouteBackup\x12\x14.lbackgrpc.BackupCmd\x1a\x1a.lbackgrpc.BackupCmdStatus\"\x00\x12\x35\n\x07RouteMv\x12\x10.lbackgrpc.MvCmd\x1a\x16.lbackgrpc.MvCmdStatus\"\x00\x12\x44\n\x0cRouteRestore\x12\x15.lbackgrpc.RestoreCmd\x1a\x1b.lbackgrpc.RestoreCmdStatus\"\x00\x12\x37\n\x07RouteRm\x12\x10.lbackgrpc.RmCmd\x1a\x16.lbackgrpc.RmCmdStatus\"\x00\x30\x01\x42\x1e\n\x12io.grpc.lback.grpcB\x06ServerP\x01\x62\x06proto3')
  ,
  dependencies=[shared__pb2.DESCRIPTOR,])
_sym_db.RegisterFileDescriptor(DESCRIPTOR)





DESCRIPTOR.has_options = True
DESCRIPTOR._options = _descriptor._ParseOptions(descriptor_pb2.FileOptions(), _b('\n\022io.grpc.lback.grpcB\006ServerP\001'))
try:
  # THESE ELEMENTS WILL BE DEPRECATED.
  # Please use the generated *_pb2_grpc.py files instead.
  import grpc
  from grpc.framework.common import cardinality
  from grpc.framework.interfaces.face import utilities as face_utilities
  from grpc.beta import implementations as beta_implementations
  from grpc.beta import interfaces as beta_interfaces


  class ServerStub(object):
    """Interface exported by the server.
    """

    def __init__(self, channel):
      """Constructor.

      Args:
        channel: A grpc.Channel.
      """
      self.RouteBackup = channel.unary_unary(
          '/lbackgrpc.Server/RouteBackup',
          request_serializer=shared__pb2.BackupCmd.SerializeToString,
          response_deserializer=shared__pb2.BackupCmdStatus.FromString,
          )
      self.RouteMv = channel.unary_unary(
          '/lbackgrpc.Server/RouteMv',
          request_serializer=shared__pb2.MvCmd.SerializeToString,
          response_deserializer=shared__pb2.MvCmdStatus.FromString,
          )
      self.RouteRestore = channel.unary_unary(
          '/lbackgrpc.Server/RouteRestore',
          request_serializer=shared__pb2.RestoreCmd.SerializeToString,
          response_deserializer=shared__pb2.RestoreCmdStatus.FromString,
          )
      self.RouteRm = channel.unary_stream(
          '/lbackgrpc.Server/RouteRm',
          request_serializer=shared__pb2.RmCmd.SerializeToString,
          response_deserializer=shared__pb2.RmCmdStatus.FromString,
          )


  class ServerServicer(object):
    """Interface exported by the server.
    """

    def RouteBackup(self, request, context):
      """A Bidirectional streaming RPC.

      Accepts a stream of RouteNotes sent while a route is being traversed,
      while receiving other RouteNotes (e.g. from other users).
      """
      context.set_code(grpc.StatusCode.UNIMPLEMENTED)
      context.set_details('Method not implemented!')
      raise NotImplementedError('Method not implemented!')

    def RouteMv(self, request, context):
      context.set_code(grpc.StatusCode.UNIMPLEMENTED)
      context.set_details('Method not implemented!')
      raise NotImplementedError('Method not implemented!')

    def RouteRestore(self, request, context):
      context.set_code(grpc.StatusCode.UNIMPLEMENTED)
      context.set_details('Method not implemented!')
      raise NotImplementedError('Method not implemented!')

    def RouteRm(self, request, context):
      context.set_code(grpc.StatusCode.UNIMPLEMENTED)
      context.set_details('Method not implemented!')
      raise NotImplementedError('Method not implemented!')


  def add_ServerServicer_to_server(servicer, server):
    rpc_method_handlers = {
        'RouteBackup': grpc.unary_unary_rpc_method_handler(
            servicer.RouteBackup,
            request_deserializer=shared__pb2.BackupCmd.FromString,
            response_serializer=shared__pb2.BackupCmdStatus.SerializeToString,
        ),
        'RouteMv': grpc.unary_unary_rpc_method_handler(
            servicer.RouteMv,
            request_deserializer=shared__pb2.MvCmd.FromString,
            response_serializer=shared__pb2.MvCmdStatus.SerializeToString,
        ),
        'RouteRestore': grpc.unary_unary_rpc_method_handler(
            servicer.RouteRestore,
            request_deserializer=shared__pb2.RestoreCmd.FromString,
            response_serializer=shared__pb2.RestoreCmdStatus.SerializeToString,
        ),
        'RouteRm': grpc.unary_stream_rpc_method_handler(
            servicer.RouteRm,
            request_deserializer=shared__pb2.RmCmd.FromString,
            response_serializer=shared__pb2.RmCmdStatus.SerializeToString,
        ),
    }
    generic_handler = grpc.method_handlers_generic_handler(
        'lbackgrpc.Server', rpc_method_handlers)
    server.add_generic_rpc_handlers((generic_handler,))


  class BetaServerServicer(object):
    """The Beta API is deprecated for 0.15.0 and later.

    It is recommended to use the GA API (classes and functions in this
    file not marked beta) for all further purposes. This class was generated
    only to ease transition from grpcio<0.15.0 to grpcio>=0.15.0."""
    """Interface exported by the server.
    """
    def RouteBackup(self, request, context):
      """A Bidirectional streaming RPC.

      Accepts a stream of RouteNotes sent while a route is being traversed,
      while receiving other RouteNotes (e.g. from other users).
      """
      context.code(beta_interfaces.StatusCode.UNIMPLEMENTED)
    def RouteMv(self, request, context):
      context.code(beta_interfaces.StatusCode.UNIMPLEMENTED)
    def RouteRestore(self, request, context):
      context.code(beta_interfaces.StatusCode.UNIMPLEMENTED)
    def RouteRm(self, request, context):
      context.code(beta_interfaces.StatusCode.UNIMPLEMENTED)


  class BetaServerStub(object):
    """The Beta API is deprecated for 0.15.0 and later.

    It is recommended to use the GA API (classes and functions in this
    file not marked beta) for all further purposes. This class was generated
    only to ease transition from grpcio<0.15.0 to grpcio>=0.15.0."""
    """Interface exported by the server.
    """
    def RouteBackup(self, request, timeout, metadata=None, with_call=False, protocol_options=None):
      """A Bidirectional streaming RPC.

      Accepts a stream of RouteNotes sent while a route is being traversed,
      while receiving other RouteNotes (e.g. from other users).
      """
      raise NotImplementedError()
    RouteBackup.future = None
    def RouteMv(self, request, timeout, metadata=None, with_call=False, protocol_options=None):
      raise NotImplementedError()
    RouteMv.future = None
    def RouteRestore(self, request, timeout, metadata=None, with_call=False, protocol_options=None):
      raise NotImplementedError()
    RouteRestore.future = None
    def RouteRm(self, request, timeout, metadata=None, with_call=False, protocol_options=None):
      raise NotImplementedError()


  def beta_create_Server_server(servicer, pool=None, pool_size=None, default_timeout=None, maximum_timeout=None):
    """The Beta API is deprecated for 0.15.0 and later.

    It is recommended to use the GA API (classes and functions in this
    file not marked beta) for all further purposes. This function was
    generated only to ease transition from grpcio<0.15.0 to grpcio>=0.15.0"""
    request_deserializers = {
      ('lbackgrpc.Server', 'RouteBackup'): shared__pb2.BackupCmd.FromString,
      ('lbackgrpc.Server', 'RouteMv'): shared__pb2.MvCmd.FromString,
      ('lbackgrpc.Server', 'RouteRestore'): shared__pb2.RestoreCmd.FromString,
      ('lbackgrpc.Server', 'RouteRm'): shared__pb2.RmCmd.FromString,
    }
    response_serializers = {
      ('lbackgrpc.Server', 'RouteBackup'): shared__pb2.BackupCmdStatus.SerializeToString,
      ('lbackgrpc.Server', 'RouteMv'): shared__pb2.MvCmdStatus.SerializeToString,
      ('lbackgrpc.Server', 'RouteRestore'): shared__pb2.RestoreCmdStatus.SerializeToString,
      ('lbackgrpc.Server', 'RouteRm'): shared__pb2.RmCmdStatus.SerializeToString,
    }
    method_implementations = {
      ('lbackgrpc.Server', 'RouteBackup'): face_utilities.unary_unary_inline(servicer.RouteBackup),
      ('lbackgrpc.Server', 'RouteMv'): face_utilities.unary_unary_inline(servicer.RouteMv),
      ('lbackgrpc.Server', 'RouteRestore'): face_utilities.unary_unary_inline(servicer.RouteRestore),
      ('lbackgrpc.Server', 'RouteRm'): face_utilities.unary_stream_inline(servicer.RouteRm),
    }
    server_options = beta_implementations.server_options(request_deserializers=request_deserializers, response_serializers=response_serializers, thread_pool=pool, thread_pool_size=pool_size, default_timeout=default_timeout, maximum_timeout=maximum_timeout)
    return beta_implementations.server(method_implementations, options=server_options)


  def beta_create_Server_stub(channel, host=None, metadata_transformer=None, pool=None, pool_size=None):
    """The Beta API is deprecated for 0.15.0 and later.

    It is recommended to use the GA API (classes and functions in this
    file not marked beta) for all further purposes. This function was
    generated only to ease transition from grpcio<0.15.0 to grpcio>=0.15.0"""
    request_serializers = {
      ('lbackgrpc.Server', 'RouteBackup'): shared__pb2.BackupCmd.SerializeToString,
      ('lbackgrpc.Server', 'RouteMv'): shared__pb2.MvCmd.SerializeToString,
      ('lbackgrpc.Server', 'RouteRestore'): shared__pb2.RestoreCmd.SerializeToString,
      ('lbackgrpc.Server', 'RouteRm'): shared__pb2.RmCmd.SerializeToString,
    }
    response_deserializers = {
      ('lbackgrpc.Server', 'RouteBackup'): shared__pb2.BackupCmdStatus.FromString,
      ('lbackgrpc.Server', 'RouteMv'): shared__pb2.MvCmdStatus.FromString,
      ('lbackgrpc.Server', 'RouteRestore'): shared__pb2.RestoreCmdStatus.FromString,
      ('lbackgrpc.Server', 'RouteRm'): shared__pb2.RmCmdStatus.FromString,
    }
    cardinalities = {
      'RouteBackup': cardinality.Cardinality.UNARY_UNARY,
      'RouteMv': cardinality.Cardinality.UNARY_UNARY,
      'RouteRestore': cardinality.Cardinality.UNARY_UNARY,
      'RouteRm': cardinality.Cardinality.UNARY_STREAM,
    }
    stub_options = beta_implementations.stub_options(host=host, metadata_transformer=metadata_transformer, request_serializers=request_serializers, response_deserializers=response_deserializers, thread_pool=pool, thread_pool_size=pool_size)
    return beta_implementations.dynamic_stub(channel, 'lbackgrpc.Server', cardinalities, options=stub_options)
except ImportError:
  pass
# @@protoc_insertion_point(module_scope)
