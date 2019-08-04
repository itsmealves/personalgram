import grpc
import time
from concurrent import futures

from stream import Stream
from protocols.camera_pb2 import *
from protocols.camera_pb2_grpc import *


class CameraService(CameraServicer):
	def __init__(self):
		self.__stream = Stream.get_instance()

	def getFrame(self, request, context):
		data = self.__stream.read_bytes()
		return FrameResponse(data=data)


if __name__ == '__main__':
    server = grpc.server(futures.ThreadPoolExecutor(max_workers=10))
    add_CameraServicer_to_server(CameraService(), server)
    server.add_insecure_port('[::]:50051')
    server.start()

    try:
        while True:
            time.sleep(86400)
    except KeyboardInterrupt:
        server.stop(0)
        Stream.release()

