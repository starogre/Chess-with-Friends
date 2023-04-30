// Generated by the gRPC C++ plugin.
// If you make any local change, they will be lost.
// source: chess.proto
#ifndef GRPC_chess_2eproto__INCLUDED
#define GRPC_chess_2eproto__INCLUDED

#include "chess.pb.h"

#include <functional>
#include <grpcpp/generic/async_generic_service.h>
#include <grpcpp/support/async_stream.h>
#include <grpcpp/support/async_unary_call.h>
#include <grpcpp/support/client_callback.h>
#include <grpcpp/client_context.h>
#include <grpcpp/completion_queue.h>
#include <grpcpp/support/message_allocator.h>
#include <grpcpp/support/method_handler.h>
#include <grpcpp/impl/proto_utils.h>
#include <grpcpp/impl/rpc_method.h>
#include <grpcpp/support/server_callback.h>
#include <grpcpp/impl/server_callback_handlers.h>
#include <grpcpp/server_context.h>
#include <grpcpp/impl/service_type.h>
#include <grpcpp/support/status.h>
#include <grpcpp/support/stub_options.h>
#include <grpcpp/support/sync_stream.h>

namespace chess {
namespace standard {

// Service definition
class ChessService final {
 public:
  static constexpr char const* service_full_name() {
    return "chess.standard.ChessService";
  }
  class StubInterface {
   public:
    virtual ~StubInterface() {}
    virtual ::grpc::Status MakeMove(::grpc::ClientContext* context, const ::chess::standard::Move& request, ::chess::standard::MoveResultMessage* response) = 0;
    std::unique_ptr< ::grpc::ClientAsyncResponseReaderInterface< ::chess::standard::MoveResultMessage>> AsyncMakeMove(::grpc::ClientContext* context, const ::chess::standard::Move& request, ::grpc::CompletionQueue* cq) {
      return std::unique_ptr< ::grpc::ClientAsyncResponseReaderInterface< ::chess::standard::MoveResultMessage>>(AsyncMakeMoveRaw(context, request, cq));
    }
    std::unique_ptr< ::grpc::ClientAsyncResponseReaderInterface< ::chess::standard::MoveResultMessage>> PrepareAsyncMakeMove(::grpc::ClientContext* context, const ::chess::standard::Move& request, ::grpc::CompletionQueue* cq) {
      return std::unique_ptr< ::grpc::ClientAsyncResponseReaderInterface< ::chess::standard::MoveResultMessage>>(PrepareAsyncMakeMoveRaw(context, request, cq));
    }
    virtual ::grpc::Status EndGame(::grpc::ClientContext* context, const ::chess::standard::GameOverMessage& request, ::chess::standard::MoveResultMessage* response) = 0;
    std::unique_ptr< ::grpc::ClientAsyncResponseReaderInterface< ::chess::standard::MoveResultMessage>> AsyncEndGame(::grpc::ClientContext* context, const ::chess::standard::GameOverMessage& request, ::grpc::CompletionQueue* cq) {
      return std::unique_ptr< ::grpc::ClientAsyncResponseReaderInterface< ::chess::standard::MoveResultMessage>>(AsyncEndGameRaw(context, request, cq));
    }
    std::unique_ptr< ::grpc::ClientAsyncResponseReaderInterface< ::chess::standard::MoveResultMessage>> PrepareAsyncEndGame(::grpc::ClientContext* context, const ::chess::standard::GameOverMessage& request, ::grpc::CompletionQueue* cq) {
      return std::unique_ptr< ::grpc::ClientAsyncResponseReaderInterface< ::chess::standard::MoveResultMessage>>(PrepareAsyncEndGameRaw(context, request, cq));
    }
    class async_interface {
     public:
      virtual ~async_interface() {}
      virtual void MakeMove(::grpc::ClientContext* context, const ::chess::standard::Move* request, ::chess::standard::MoveResultMessage* response, std::function<void(::grpc::Status)>) = 0;
      virtual void MakeMove(::grpc::ClientContext* context, const ::chess::standard::Move* request, ::chess::standard::MoveResultMessage* response, ::grpc::ClientUnaryReactor* reactor) = 0;
      virtual void EndGame(::grpc::ClientContext* context, const ::chess::standard::GameOverMessage* request, ::chess::standard::MoveResultMessage* response, std::function<void(::grpc::Status)>) = 0;
      virtual void EndGame(::grpc::ClientContext* context, const ::chess::standard::GameOverMessage* request, ::chess::standard::MoveResultMessage* response, ::grpc::ClientUnaryReactor* reactor) = 0;
    };
    typedef class async_interface experimental_async_interface;
    virtual class async_interface* async() { return nullptr; }
    class async_interface* experimental_async() { return async(); }
   private:
    virtual ::grpc::ClientAsyncResponseReaderInterface< ::chess::standard::MoveResultMessage>* AsyncMakeMoveRaw(::grpc::ClientContext* context, const ::chess::standard::Move& request, ::grpc::CompletionQueue* cq) = 0;
    virtual ::grpc::ClientAsyncResponseReaderInterface< ::chess::standard::MoveResultMessage>* PrepareAsyncMakeMoveRaw(::grpc::ClientContext* context, const ::chess::standard::Move& request, ::grpc::CompletionQueue* cq) = 0;
    virtual ::grpc::ClientAsyncResponseReaderInterface< ::chess::standard::MoveResultMessage>* AsyncEndGameRaw(::grpc::ClientContext* context, const ::chess::standard::GameOverMessage& request, ::grpc::CompletionQueue* cq) = 0;
    virtual ::grpc::ClientAsyncResponseReaderInterface< ::chess::standard::MoveResultMessage>* PrepareAsyncEndGameRaw(::grpc::ClientContext* context, const ::chess::standard::GameOverMessage& request, ::grpc::CompletionQueue* cq) = 0;
  };
  class Stub final : public StubInterface {
   public:
    Stub(const std::shared_ptr< ::grpc::ChannelInterface>& channel, const ::grpc::StubOptions& options = ::grpc::StubOptions());
    ::grpc::Status MakeMove(::grpc::ClientContext* context, const ::chess::standard::Move& request, ::chess::standard::MoveResultMessage* response) override;
    std::unique_ptr< ::grpc::ClientAsyncResponseReader< ::chess::standard::MoveResultMessage>> AsyncMakeMove(::grpc::ClientContext* context, const ::chess::standard::Move& request, ::grpc::CompletionQueue* cq) {
      return std::unique_ptr< ::grpc::ClientAsyncResponseReader< ::chess::standard::MoveResultMessage>>(AsyncMakeMoveRaw(context, request, cq));
    }
    std::unique_ptr< ::grpc::ClientAsyncResponseReader< ::chess::standard::MoveResultMessage>> PrepareAsyncMakeMove(::grpc::ClientContext* context, const ::chess::standard::Move& request, ::grpc::CompletionQueue* cq) {
      return std::unique_ptr< ::grpc::ClientAsyncResponseReader< ::chess::standard::MoveResultMessage>>(PrepareAsyncMakeMoveRaw(context, request, cq));
    }
    ::grpc::Status EndGame(::grpc::ClientContext* context, const ::chess::standard::GameOverMessage& request, ::chess::standard::MoveResultMessage* response) override;
    std::unique_ptr< ::grpc::ClientAsyncResponseReader< ::chess::standard::MoveResultMessage>> AsyncEndGame(::grpc::ClientContext* context, const ::chess::standard::GameOverMessage& request, ::grpc::CompletionQueue* cq) {
      return std::unique_ptr< ::grpc::ClientAsyncResponseReader< ::chess::standard::MoveResultMessage>>(AsyncEndGameRaw(context, request, cq));
    }
    std::unique_ptr< ::grpc::ClientAsyncResponseReader< ::chess::standard::MoveResultMessage>> PrepareAsyncEndGame(::grpc::ClientContext* context, const ::chess::standard::GameOverMessage& request, ::grpc::CompletionQueue* cq) {
      return std::unique_ptr< ::grpc::ClientAsyncResponseReader< ::chess::standard::MoveResultMessage>>(PrepareAsyncEndGameRaw(context, request, cq));
    }
    class async final :
      public StubInterface::async_interface {
     public:
      void MakeMove(::grpc::ClientContext* context, const ::chess::standard::Move* request, ::chess::standard::MoveResultMessage* response, std::function<void(::grpc::Status)>) override;
      void MakeMove(::grpc::ClientContext* context, const ::chess::standard::Move* request, ::chess::standard::MoveResultMessage* response, ::grpc::ClientUnaryReactor* reactor) override;
      void EndGame(::grpc::ClientContext* context, const ::chess::standard::GameOverMessage* request, ::chess::standard::MoveResultMessage* response, std::function<void(::grpc::Status)>) override;
      void EndGame(::grpc::ClientContext* context, const ::chess::standard::GameOverMessage* request, ::chess::standard::MoveResultMessage* response, ::grpc::ClientUnaryReactor* reactor) override;
     private:
      friend class Stub;
      explicit async(Stub* stub): stub_(stub) { }
      Stub* stub() { return stub_; }
      Stub* stub_;
    };
    class async* async() override { return &async_stub_; }

   private:
    std::shared_ptr< ::grpc::ChannelInterface> channel_;
    class async async_stub_{this};
    ::grpc::ClientAsyncResponseReader< ::chess::standard::MoveResultMessage>* AsyncMakeMoveRaw(::grpc::ClientContext* context, const ::chess::standard::Move& request, ::grpc::CompletionQueue* cq) override;
    ::grpc::ClientAsyncResponseReader< ::chess::standard::MoveResultMessage>* PrepareAsyncMakeMoveRaw(::grpc::ClientContext* context, const ::chess::standard::Move& request, ::grpc::CompletionQueue* cq) override;
    ::grpc::ClientAsyncResponseReader< ::chess::standard::MoveResultMessage>* AsyncEndGameRaw(::grpc::ClientContext* context, const ::chess::standard::GameOverMessage& request, ::grpc::CompletionQueue* cq) override;
    ::grpc::ClientAsyncResponseReader< ::chess::standard::MoveResultMessage>* PrepareAsyncEndGameRaw(::grpc::ClientContext* context, const ::chess::standard::GameOverMessage& request, ::grpc::CompletionQueue* cq) override;
    const ::grpc::internal::RpcMethod rpcmethod_MakeMove_;
    const ::grpc::internal::RpcMethod rpcmethod_EndGame_;
  };
  static std::unique_ptr<Stub> NewStub(const std::shared_ptr< ::grpc::ChannelInterface>& channel, const ::grpc::StubOptions& options = ::grpc::StubOptions());

  class Service : public ::grpc::Service {
   public:
    Service();
    virtual ~Service();
    virtual ::grpc::Status MakeMove(::grpc::ServerContext* context, const ::chess::standard::Move* request, ::chess::standard::MoveResultMessage* response);
    virtual ::grpc::Status EndGame(::grpc::ServerContext* context, const ::chess::standard::GameOverMessage* request, ::chess::standard::MoveResultMessage* response);
  };
  template <class BaseClass>
  class WithAsyncMethod_MakeMove : public BaseClass {
   private:
    void BaseClassMustBeDerivedFromService(const Service* /*service*/) {}
   public:
    WithAsyncMethod_MakeMove() {
      ::grpc::Service::MarkMethodAsync(0);
    }
    ~WithAsyncMethod_MakeMove() override {
      BaseClassMustBeDerivedFromService(this);
    }
    // disable synchronous version of this method
    ::grpc::Status MakeMove(::grpc::ServerContext* /*context*/, const ::chess::standard::Move* /*request*/, ::chess::standard::MoveResultMessage* /*response*/) override {
      abort();
      return ::grpc::Status(::grpc::StatusCode::UNIMPLEMENTED, "");
    }
    void RequestMakeMove(::grpc::ServerContext* context, ::chess::standard::Move* request, ::grpc::ServerAsyncResponseWriter< ::chess::standard::MoveResultMessage>* response, ::grpc::CompletionQueue* new_call_cq, ::grpc::ServerCompletionQueue* notification_cq, void *tag) {
      ::grpc::Service::RequestAsyncUnary(0, context, request, response, new_call_cq, notification_cq, tag);
    }
  };
  template <class BaseClass>
  class WithAsyncMethod_EndGame : public BaseClass {
   private:
    void BaseClassMustBeDerivedFromService(const Service* /*service*/) {}
   public:
    WithAsyncMethod_EndGame() {
      ::grpc::Service::MarkMethodAsync(1);
    }
    ~WithAsyncMethod_EndGame() override {
      BaseClassMustBeDerivedFromService(this);
    }
    // disable synchronous version of this method
    ::grpc::Status EndGame(::grpc::ServerContext* /*context*/, const ::chess::standard::GameOverMessage* /*request*/, ::chess::standard::MoveResultMessage* /*response*/) override {
      abort();
      return ::grpc::Status(::grpc::StatusCode::UNIMPLEMENTED, "");
    }
    void RequestEndGame(::grpc::ServerContext* context, ::chess::standard::GameOverMessage* request, ::grpc::ServerAsyncResponseWriter< ::chess::standard::MoveResultMessage>* response, ::grpc::CompletionQueue* new_call_cq, ::grpc::ServerCompletionQueue* notification_cq, void *tag) {
      ::grpc::Service::RequestAsyncUnary(1, context, request, response, new_call_cq, notification_cq, tag);
    }
  };
  typedef WithAsyncMethod_MakeMove<WithAsyncMethod_EndGame<Service > > AsyncService;
  template <class BaseClass>
  class WithCallbackMethod_MakeMove : public BaseClass {
   private:
    void BaseClassMustBeDerivedFromService(const Service* /*service*/) {}
   public:
    WithCallbackMethod_MakeMove() {
      ::grpc::Service::MarkMethodCallback(0,
          new ::grpc::internal::CallbackUnaryHandler< ::chess::standard::Move, ::chess::standard::MoveResultMessage>(
            [this](
                   ::grpc::CallbackServerContext* context, const ::chess::standard::Move* request, ::chess::standard::MoveResultMessage* response) { return this->MakeMove(context, request, response); }));}
    void SetMessageAllocatorFor_MakeMove(
        ::grpc::MessageAllocator< ::chess::standard::Move, ::chess::standard::MoveResultMessage>* allocator) {
      ::grpc::internal::MethodHandler* const handler = ::grpc::Service::GetHandler(0);
      static_cast<::grpc::internal::CallbackUnaryHandler< ::chess::standard::Move, ::chess::standard::MoveResultMessage>*>(handler)
              ->SetMessageAllocator(allocator);
    }
    ~WithCallbackMethod_MakeMove() override {
      BaseClassMustBeDerivedFromService(this);
    }
    // disable synchronous version of this method
    ::grpc::Status MakeMove(::grpc::ServerContext* /*context*/, const ::chess::standard::Move* /*request*/, ::chess::standard::MoveResultMessage* /*response*/) override {
      abort();
      return ::grpc::Status(::grpc::StatusCode::UNIMPLEMENTED, "");
    }
    virtual ::grpc::ServerUnaryReactor* MakeMove(
      ::grpc::CallbackServerContext* /*context*/, const ::chess::standard::Move* /*request*/, ::chess::standard::MoveResultMessage* /*response*/)  { return nullptr; }
  };
  template <class BaseClass>
  class WithCallbackMethod_EndGame : public BaseClass {
   private:
    void BaseClassMustBeDerivedFromService(const Service* /*service*/) {}
   public:
    WithCallbackMethod_EndGame() {
      ::grpc::Service::MarkMethodCallback(1,
          new ::grpc::internal::CallbackUnaryHandler< ::chess::standard::GameOverMessage, ::chess::standard::MoveResultMessage>(
            [this](
                   ::grpc::CallbackServerContext* context, const ::chess::standard::GameOverMessage* request, ::chess::standard::MoveResultMessage* response) { return this->EndGame(context, request, response); }));}
    void SetMessageAllocatorFor_EndGame(
        ::grpc::MessageAllocator< ::chess::standard::GameOverMessage, ::chess::standard::MoveResultMessage>* allocator) {
      ::grpc::internal::MethodHandler* const handler = ::grpc::Service::GetHandler(1);
      static_cast<::grpc::internal::CallbackUnaryHandler< ::chess::standard::GameOverMessage, ::chess::standard::MoveResultMessage>*>(handler)
              ->SetMessageAllocator(allocator);
    }
    ~WithCallbackMethod_EndGame() override {
      BaseClassMustBeDerivedFromService(this);
    }
    // disable synchronous version of this method
    ::grpc::Status EndGame(::grpc::ServerContext* /*context*/, const ::chess::standard::GameOverMessage* /*request*/, ::chess::standard::MoveResultMessage* /*response*/) override {
      abort();
      return ::grpc::Status(::grpc::StatusCode::UNIMPLEMENTED, "");
    }
    virtual ::grpc::ServerUnaryReactor* EndGame(
      ::grpc::CallbackServerContext* /*context*/, const ::chess::standard::GameOverMessage* /*request*/, ::chess::standard::MoveResultMessage* /*response*/)  { return nullptr; }
  };
  typedef WithCallbackMethod_MakeMove<WithCallbackMethod_EndGame<Service > > CallbackService;
  typedef CallbackService ExperimentalCallbackService;
  template <class BaseClass>
  class WithGenericMethod_MakeMove : public BaseClass {
   private:
    void BaseClassMustBeDerivedFromService(const Service* /*service*/) {}
   public:
    WithGenericMethod_MakeMove() {
      ::grpc::Service::MarkMethodGeneric(0);
    }
    ~WithGenericMethod_MakeMove() override {
      BaseClassMustBeDerivedFromService(this);
    }
    // disable synchronous version of this method
    ::grpc::Status MakeMove(::grpc::ServerContext* /*context*/, const ::chess::standard::Move* /*request*/, ::chess::standard::MoveResultMessage* /*response*/) override {
      abort();
      return ::grpc::Status(::grpc::StatusCode::UNIMPLEMENTED, "");
    }
  };
  template <class BaseClass>
  class WithGenericMethod_EndGame : public BaseClass {
   private:
    void BaseClassMustBeDerivedFromService(const Service* /*service*/) {}
   public:
    WithGenericMethod_EndGame() {
      ::grpc::Service::MarkMethodGeneric(1);
    }
    ~WithGenericMethod_EndGame() override {
      BaseClassMustBeDerivedFromService(this);
    }
    // disable synchronous version of this method
    ::grpc::Status EndGame(::grpc::ServerContext* /*context*/, const ::chess::standard::GameOverMessage* /*request*/, ::chess::standard::MoveResultMessage* /*response*/) override {
      abort();
      return ::grpc::Status(::grpc::StatusCode::UNIMPLEMENTED, "");
    }
  };
  template <class BaseClass>
  class WithRawMethod_MakeMove : public BaseClass {
   private:
    void BaseClassMustBeDerivedFromService(const Service* /*service*/) {}
   public:
    WithRawMethod_MakeMove() {
      ::grpc::Service::MarkMethodRaw(0);
    }
    ~WithRawMethod_MakeMove() override {
      BaseClassMustBeDerivedFromService(this);
    }
    // disable synchronous version of this method
    ::grpc::Status MakeMove(::grpc::ServerContext* /*context*/, const ::chess::standard::Move* /*request*/, ::chess::standard::MoveResultMessage* /*response*/) override {
      abort();
      return ::grpc::Status(::grpc::StatusCode::UNIMPLEMENTED, "");
    }
    void RequestMakeMove(::grpc::ServerContext* context, ::grpc::ByteBuffer* request, ::grpc::ServerAsyncResponseWriter< ::grpc::ByteBuffer>* response, ::grpc::CompletionQueue* new_call_cq, ::grpc::ServerCompletionQueue* notification_cq, void *tag) {
      ::grpc::Service::RequestAsyncUnary(0, context, request, response, new_call_cq, notification_cq, tag);
    }
  };
  template <class BaseClass>
  class WithRawMethod_EndGame : public BaseClass {
   private:
    void BaseClassMustBeDerivedFromService(const Service* /*service*/) {}
   public:
    WithRawMethod_EndGame() {
      ::grpc::Service::MarkMethodRaw(1);
    }
    ~WithRawMethod_EndGame() override {
      BaseClassMustBeDerivedFromService(this);
    }
    // disable synchronous version of this method
    ::grpc::Status EndGame(::grpc::ServerContext* /*context*/, const ::chess::standard::GameOverMessage* /*request*/, ::chess::standard::MoveResultMessage* /*response*/) override {
      abort();
      return ::grpc::Status(::grpc::StatusCode::UNIMPLEMENTED, "");
    }
    void RequestEndGame(::grpc::ServerContext* context, ::grpc::ByteBuffer* request, ::grpc::ServerAsyncResponseWriter< ::grpc::ByteBuffer>* response, ::grpc::CompletionQueue* new_call_cq, ::grpc::ServerCompletionQueue* notification_cq, void *tag) {
      ::grpc::Service::RequestAsyncUnary(1, context, request, response, new_call_cq, notification_cq, tag);
    }
  };
  template <class BaseClass>
  class WithRawCallbackMethod_MakeMove : public BaseClass {
   private:
    void BaseClassMustBeDerivedFromService(const Service* /*service*/) {}
   public:
    WithRawCallbackMethod_MakeMove() {
      ::grpc::Service::MarkMethodRawCallback(0,
          new ::grpc::internal::CallbackUnaryHandler< ::grpc::ByteBuffer, ::grpc::ByteBuffer>(
            [this](
                   ::grpc::CallbackServerContext* context, const ::grpc::ByteBuffer* request, ::grpc::ByteBuffer* response) { return this->MakeMove(context, request, response); }));
    }
    ~WithRawCallbackMethod_MakeMove() override {
      BaseClassMustBeDerivedFromService(this);
    }
    // disable synchronous version of this method
    ::grpc::Status MakeMove(::grpc::ServerContext* /*context*/, const ::chess::standard::Move* /*request*/, ::chess::standard::MoveResultMessage* /*response*/) override {
      abort();
      return ::grpc::Status(::grpc::StatusCode::UNIMPLEMENTED, "");
    }
    virtual ::grpc::ServerUnaryReactor* MakeMove(
      ::grpc::CallbackServerContext* /*context*/, const ::grpc::ByteBuffer* /*request*/, ::grpc::ByteBuffer* /*response*/)  { return nullptr; }
  };
  template <class BaseClass>
  class WithRawCallbackMethod_EndGame : public BaseClass {
   private:
    void BaseClassMustBeDerivedFromService(const Service* /*service*/) {}
   public:
    WithRawCallbackMethod_EndGame() {
      ::grpc::Service::MarkMethodRawCallback(1,
          new ::grpc::internal::CallbackUnaryHandler< ::grpc::ByteBuffer, ::grpc::ByteBuffer>(
            [this](
                   ::grpc::CallbackServerContext* context, const ::grpc::ByteBuffer* request, ::grpc::ByteBuffer* response) { return this->EndGame(context, request, response); }));
    }
    ~WithRawCallbackMethod_EndGame() override {
      BaseClassMustBeDerivedFromService(this);
    }
    // disable synchronous version of this method
    ::grpc::Status EndGame(::grpc::ServerContext* /*context*/, const ::chess::standard::GameOverMessage* /*request*/, ::chess::standard::MoveResultMessage* /*response*/) override {
      abort();
      return ::grpc::Status(::grpc::StatusCode::UNIMPLEMENTED, "");
    }
    virtual ::grpc::ServerUnaryReactor* EndGame(
      ::grpc::CallbackServerContext* /*context*/, const ::grpc::ByteBuffer* /*request*/, ::grpc::ByteBuffer* /*response*/)  { return nullptr; }
  };
  template <class BaseClass>
  class WithStreamedUnaryMethod_MakeMove : public BaseClass {
   private:
    void BaseClassMustBeDerivedFromService(const Service* /*service*/) {}
   public:
    WithStreamedUnaryMethod_MakeMove() {
      ::grpc::Service::MarkMethodStreamed(0,
        new ::grpc::internal::StreamedUnaryHandler<
          ::chess::standard::Move, ::chess::standard::MoveResultMessage>(
            [this](::grpc::ServerContext* context,
                   ::grpc::ServerUnaryStreamer<
                     ::chess::standard::Move, ::chess::standard::MoveResultMessage>* streamer) {
                       return this->StreamedMakeMove(context,
                         streamer);
                  }));
    }
    ~WithStreamedUnaryMethod_MakeMove() override {
      BaseClassMustBeDerivedFromService(this);
    }
    // disable regular version of this method
    ::grpc::Status MakeMove(::grpc::ServerContext* /*context*/, const ::chess::standard::Move* /*request*/, ::chess::standard::MoveResultMessage* /*response*/) override {
      abort();
      return ::grpc::Status(::grpc::StatusCode::UNIMPLEMENTED, "");
    }
    // replace default version of method with streamed unary
    virtual ::grpc::Status StreamedMakeMove(::grpc::ServerContext* context, ::grpc::ServerUnaryStreamer< ::chess::standard::Move,::chess::standard::MoveResultMessage>* server_unary_streamer) = 0;
  };
  template <class BaseClass>
  class WithStreamedUnaryMethod_EndGame : public BaseClass {
   private:
    void BaseClassMustBeDerivedFromService(const Service* /*service*/) {}
   public:
    WithStreamedUnaryMethod_EndGame() {
      ::grpc::Service::MarkMethodStreamed(1,
        new ::grpc::internal::StreamedUnaryHandler<
          ::chess::standard::GameOverMessage, ::chess::standard::MoveResultMessage>(
            [this](::grpc::ServerContext* context,
                   ::grpc::ServerUnaryStreamer<
                     ::chess::standard::GameOverMessage, ::chess::standard::MoveResultMessage>* streamer) {
                       return this->StreamedEndGame(context,
                         streamer);
                  }));
    }
    ~WithStreamedUnaryMethod_EndGame() override {
      BaseClassMustBeDerivedFromService(this);
    }
    // disable regular version of this method
    ::grpc::Status EndGame(::grpc::ServerContext* /*context*/, const ::chess::standard::GameOverMessage* /*request*/, ::chess::standard::MoveResultMessage* /*response*/) override {
      abort();
      return ::grpc::Status(::grpc::StatusCode::UNIMPLEMENTED, "");
    }
    // replace default version of method with streamed unary
    virtual ::grpc::Status StreamedEndGame(::grpc::ServerContext* context, ::grpc::ServerUnaryStreamer< ::chess::standard::GameOverMessage,::chess::standard::MoveResultMessage>* server_unary_streamer) = 0;
  };
  typedef WithStreamedUnaryMethod_MakeMove<WithStreamedUnaryMethod_EndGame<Service > > StreamedUnaryService;
  typedef Service SplitStreamedService;
  typedef WithStreamedUnaryMethod_MakeMove<WithStreamedUnaryMethod_EndGame<Service > > StreamedService;
};

}  // namespace standard
}  // namespace chess


#endif  // GRPC_chess_2eproto__INCLUDED
