cmake_minimum_required(VERSION 3.13)

project(ChessServer)

set(CMAKE_CXX_STANDARD 14)

find_package(Protobuf REQUIRED)
find_package(gRPC REQUIRED)

include_directories(${PROTOBUF_INCLUDE_DIRS} ${GRPC_INCLUDE_DIRS})

add_executable(chess_server
        server/src/chess_server.cpp
        server/generated/chess.pb.cc
        server/generated/chess.grpc.pb.cc
        )

target_link_libraries(chess_server
        gRPC::grpc++ gRPC::grpc++_reflection protobuf::libprotobuf
        )
