from concurrent import futures
import time

import grpc

from proto.images_pb2 import ReplyRequest
from proto.images_pb2 import ReplyResponse
from proto.images_pb2_grpc import GatewayServicer
from proto.images_pb2_grpc import add_GatewayServicer_to_server

_ONE_DAY_IN_SECONDS = 60 * 60 * 24
_INSECURE_PORT = '50051'

class ImagesGatewayServicer(GatewayServicer):
    def Reply(self, request, context):
        print('reply')
        return ReplyResponse(message='001.png')

def serve():
    print('starting server...')
    server = grpc.server(futures.ThreadPoolExecutor(max_workers=10))
    add_GatewayServicer_to_server(
            GatewayServicer(), server)
    server.add_insecure_port('[::]:' + _INSECURE_PORT)
    server.start()
    print('started on port:' + _INSECURE_PORT)
    try:
        while True:
            time.sleep(_ONE_DAY_IN_SECONDS)
    except KeyboardInterrupt:
        server.stop(0)

if __name__ == '__main__':
    serve()