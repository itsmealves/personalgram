import os
import grpc
import time
import dotenv
from concurrent import futures

from protocols.sync_pb2 import *
from protocols.sync_pb2_grpc import *


dotenv.load_dotenv()


class SyncService(SyncServicer):
    def __init__(self):
        pass

    def __store(self, frame):


    def storeFrame(self, request, context):
        success = self.__store(request.frame, request.extension)
        return StoreResponse(success=success)


if __name__ == '__main__':
    port = os.environ.get('SYNC_PORT')
    server = grpc.server(futures.ThreadPoolExecutor(max_workers=10))
    add_SyncServicer_to_server(SyncService(), server)
    server.add_insecure_port('[::]:{}'.format(port))
    server.start()

    try:
        while True:
            time.sleep(86400)
    except KeyboardInterrupt:
        server.stop(0)
