import grpc
from proto import images_pb2
from proto import images_pb2_grpc

_HOST = 'localhost'
_PORT = '50051'

def run():
    channel = grpc.insecure_channel(_HOST + ':' + _PORT)
    stub = images_pb2_grpc.GatewayStub(channel)
    request = images_pb2.ReplyRequest(path='image/001')
    response = stub.Reply(request)
    print(11111)

if __name__ == '__main__':
    run()
