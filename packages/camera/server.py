import os
import grpc
import time
import dotenv
from concurrent import futures

from stream import Stream
from protocols.camera_pb2 import *
from protocols.camera_pb2_grpc import *


dotenv.load_dotenv()


class CameraService(CameraServicer):
    def __init__(self):
        self.__stream = Stream.get_instance()

    def getFrame(self, request, context):
        data, extension = self.__stream.read_bytes()
        return FrameResponse(data=data, type=extension)

    def getStream(self, request, context):
        while True:
            data, extension = self.__stream.read_bytes()
            yield FrameResponse(data=data, type=extension)


if __name__ == '__main__':
    port = os.environ.get('CAMERA_PORT')
    server = grpc.server(futures.ThreadPoolExecutor(max_workers=10))
    add_CameraServicer_to_server(CameraService(), server)
    server.add_insecure_port('[::]:{}'.format(port))
    server.start()

    try:
        while True:
            time.sleep(86400)
    except KeyboardInterrupt:
        server.stop(0)
        Stream.release()

