#include <grpcpp/grpcpp.h>
#include "../generated/chess.pb.h"
#include "../generated/chess.grpc.pb.h"

using grpc::Server;
using grpc::ServerBuilder;
using grpc::ServerContext;
using grpc::Status;
using chess::standard::MoveMessage;
using chess::standard::MoveResultMessage;
using chess::standard::ChessService;
using chess::standard::GameOverMessage;


class ChessServiceImpl final : public ChessService::Service {
    Status MakeMove(ServerContext* context, const chess::standard::Move* move,
                    chess::standard::MoveResultMessage* result) override {
        // Check if the move is within board boundaries
        if (move->to_position().x() < 0 || move->to_position().x() > 7 ||
            move->to_position().y() < 0 || move->to_position().y() > 7) {
            result->set_valid(false);
            result->set_error_code(1);  // Let's say 1 is the code for out of bounds
        } else {
            // If the move is valid, set the result as successful
            result->set_valid(true);
            result->set_error_code(0);
        }
        return Status::OK;
    }

    Status EndGame(ServerContext* context, const chess::standard::GameOverMessage* game_over,
                   chess::standard::MoveResultMessage* result) override {
        // TODO: Implement your end game logic here

        return Status::OK;
    }
};

void RunServer() {
    std::string server_address("0.0.0.0:50051");
    ChessServiceImpl service;

    ServerBuilder builder;
    builder.AddListeningPort(server_address, grpc::InsecureServerCredentials());
    builder.RegisterService(&service);

    std::unique_ptr<Server> server(builder.BuildAndStart());
    std::cout << "Server listening on " << server_address << std::endl;

    server->Wait();
}

int main(int argc, char** argv) {
    RunServer();

    return 0;
}
