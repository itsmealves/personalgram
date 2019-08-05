import os
import grpc
import time
import dotenv
from threading import Lock
from functools import wraps
from concurrent import futures

from protocols.auth_pb2 import *
from protocols.auth_pb2_grpc import *


dotenv.load_dotenv()


def with_lock(lock):
    def wrapper(fn):
        @wraps(fn)
        def wrapped_fn(*args, **kwargs):
            lock.acquire()
            
            try:
                response = fn(*args, **kwargs)
            finally:
                lock.release()
            return response
        return wrapped_fn
    return wrapper


class AuthService(AuthServicer):
    __lock = Lock()

    def __init__(self):
        self.__user = None

    def __get_auth_response(self):
        response = AuthResponse()

        response.loggedIn = self.__user is not None
        response.token = 'sem pena'

        return response

    @with_lock(__lock)
    def login(self, request, context):
        return self.__get_auth_response()

    @with_lock(__lock)
    def logout(self, request, context):
        self.__user = None
        return self.__get_auth_response()
        
    @with_lock(__lock)
    def currentUser(self, request, context):
        return self.__get_auth_response()


if __name__ == '__main__':
    port = os.environ.get('AUTH_PORT')
    server = grpc.server(futures.ThreadPoolExecutor(max_workers=10))
    add_AuthServicer_to_server(AuthService(), server)
    server.add_insecure_port('[::]:{}'.format(port))
    server.start()

    try:
        while True:
            time.sleep(86400)
    except KeyboardInterrupt:
        server.stop(0)
