# Generated by the gRPC Python protocol compiler plugin. DO NOT EDIT!
"""Client and server classes corresponding to protobuf-defined services."""
import grpc
import warnings

from protos.app1.service1 import service1_pb2 as protos_dot_app1_dot_service1_dot_service1__pb2

GRPC_GENERATED_VERSION = '1.64.1'
GRPC_VERSION = grpc.__version__
EXPECTED_ERROR_RELEASE = '1.65.0'
SCHEDULED_RELEASE_DATE = 'June 25, 2024'
_version_not_supported = False

try:
    from grpc._utilities import first_version_is_lower
    _version_not_supported = first_version_is_lower(GRPC_VERSION, GRPC_GENERATED_VERSION)
except ImportError:
    _version_not_supported = True

if _version_not_supported:
    warnings.warn(
        f'The grpc package installed is at version {GRPC_VERSION},'
        + f' but the generated code in protos/app1/service1/service1_pb2_grpc.py depends on'
        + f' grpcio>={GRPC_GENERATED_VERSION}.'
        + f' Please upgrade your grpc module to grpcio>={GRPC_GENERATED_VERSION}'
        + f' or downgrade your generated code using grpcio-tools<={GRPC_VERSION}.'
        + f' This warning will become an error in {EXPECTED_ERROR_RELEASE},'
        + f' scheduled for release on {SCHEDULED_RELEASE_DATE}.',
        RuntimeWarning
    )


class TestTrafficStub(object):
    """Missing associated documentation comment in .proto file."""

    def __init__(self, channel):
        """Constructor.

        Args:
            channel: A grpc.Channel.
        """
        self.build_test = channel.unary_unary(
                '/TestTraffic/build_test',
                request_serializer=protos_dot_app1_dot_service1_dot_service1__pb2.AccessToken.SerializeToString,
                response_deserializer=protos_dot_app1_dot_service1_dot_service1__pb2.Response.FromString,
                _registered_method=True)


class TestTrafficServicer(object):
    """Missing associated documentation comment in .proto file."""

    def build_test(self, request, context):
        """Missing associated documentation comment in .proto file."""
        context.set_code(grpc.StatusCode.UNIMPLEMENTED)
        context.set_details('Method not implemented!')
        raise NotImplementedError('Method not implemented!')


def add_TestTrafficServicer_to_server(servicer, server):
    rpc_method_handlers = {
            'build_test': grpc.unary_unary_rpc_method_handler(
                    servicer.build_test,
                    request_deserializer=protos_dot_app1_dot_service1_dot_service1__pb2.AccessToken.FromString,
                    response_serializer=protos_dot_app1_dot_service1_dot_service1__pb2.Response.SerializeToString,
            ),
    }
    generic_handler = grpc.method_handlers_generic_handler(
            'TestTraffic', rpc_method_handlers)
    server.add_generic_rpc_handlers((generic_handler,))
    server.add_registered_method_handlers('TestTraffic', rpc_method_handlers)


 # This class is part of an EXPERIMENTAL API.
class TestTraffic(object):
    """Missing associated documentation comment in .proto file."""

    @staticmethod
    def build_test(request,
            target,
            options=(),
            channel_credentials=None,
            call_credentials=None,
            insecure=False,
            compression=None,
            wait_for_ready=None,
            timeout=None,
            metadata=None):
        return grpc.experimental.unary_unary(
            request,
            target,
            '/TestTraffic/build_test',
            protos_dot_app1_dot_service1_dot_service1__pb2.AccessToken.SerializeToString,
            protos_dot_app1_dot_service1_dot_service1__pb2.Response.FromString,
            options,
            channel_credentials,
            insecure,
            call_credentials,
            compression,
            wait_for_ready,
            timeout,
            metadata,
            _registered_method=True)
