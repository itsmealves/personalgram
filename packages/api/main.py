import grpc
from protocols.camera_pb2 import *
from protocols.camera_pb2_grpc import *


def run():
    with grpc.insecure_channel('localhost:50051') as channel:
        stub = CameraStub(channel)
        response = stub.getFrame(FrameRequest())
    
if __name__ == '__main__':
    run()