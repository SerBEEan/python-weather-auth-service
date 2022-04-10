import grpc
import auth_pb2
import auth_pb2_grpc

def run():
    # NOTE(gRPC Python Team): .close() is possible on a channel and should be
    # used in circumstances in which the with statement does not fit the needs
    # of the code.
    with grpc.insecure_channel('localhost:8080') as channel:
        stub = auth_pb2_grpc.AuthServiceStub(channel)
        response = stub.Auth(auth_pb2.RequestAuth(name="kek"))
    print("Server: " + str(response.isAuth))

run()
