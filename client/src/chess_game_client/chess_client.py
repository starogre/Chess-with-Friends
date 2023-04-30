import grpc
import chess_pb2
import chess_pb2_grpc


def run():
    # Create a channel to the server
    channel = grpc.insecure_channel('localhost:50051')

    # Instantiate the chess service stub
    stub = chess_pb2_grpc.ChessServiceStub(channel)

    # Create a Move message
    move = chess_pb2.Move(
        piece_id=1,
        from_position=chess_pb2.Position(x=0, y=1),
        to_position=chess_pb2.Position(x=0, y=8),
    )

    # Send move request to server
    response = stub.MakeMove(move)

    # Print the received response
    print("Response valid: ", response.valid)
    print("EC:", response.error_code)


if __name__ == "__main__":
    run()
