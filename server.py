from concurrent import futures

import grpc
import auth_pb2
import auth_pb2_grpc

from db.hashTable import db

class Auth(auth_pb2_grpc.AuthService):

    def Auth(self, request, context):
        isAuthUser = db.get(request.name) != None
        return auth_pb2.ResponseAuth(isAuth = isAuthUser)


def serve():
    server = grpc.server(futures.ThreadPoolExecutor(max_workers=10))
    auth_pb2_grpc.add_AuthServiceServicer_to_server(Auth(), server)
    server.add_insecure_port('[::]:8080')
    server.start()
    server.wait_for_termination()

serve()
