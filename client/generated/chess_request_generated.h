// automatically generated by the FlatBuffers compiler, do not modify


#ifndef FLATBUFFERS_GENERATED_CHESSREQUEST_CHESS_REQUEST_H_
#define FLATBUFFERS_GENERATED_CHESSREQUEST_CHESS_REQUEST_H_

#include "flatbuffers/flatbuffers.h"

// Ensure the included flatbuffers.h is the same version as when this file was
// generated, otherwise it may not be compatible.
static_assert(FLATBUFFERS_VERSION_MAJOR == 23 &&
              FLATBUFFERS_VERSION_MINOR == 3 &&
              FLATBUFFERS_VERSION_REVISION == 3,
             "Non-compatible flatbuffers version included");

#include "chess_common_generated.h"

namespace chess {
namespace request {

struct Move;
struct MoveBuilder;

struct Request;
struct RequestBuilder;

enum RequestType : int8_t {
  RequestType_MOVE = 0,
  RequestType_RESIGN = 1,
  RequestType_MIN = RequestType_MOVE,
  RequestType_MAX = RequestType_RESIGN
};

inline const RequestType (&EnumValuesRequestType())[2] {
  static const RequestType values[] = {
    RequestType_MOVE,
    RequestType_RESIGN
  };
  return values;
}

inline const char * const *EnumNamesRequestType() {
  static const char * const names[3] = {
    "MOVE",
    "RESIGN",
    nullptr
  };
  return names;
}

inline const char *EnumNameRequestType(RequestType e) {
  if (::flatbuffers::IsOutRange(e, RequestType_MOVE, RequestType_RESIGN)) return "";
  const size_t index = static_cast<size_t>(e);
  return EnumNamesRequestType()[index];
}

enum RequestContent : uint8_t {
  RequestContent_NONE = 0,
  RequestContent_Move = 1,
  RequestContent_MIN = RequestContent_NONE,
  RequestContent_MAX = RequestContent_Move
};

inline const RequestContent (&EnumValuesRequestContent())[2] {
  static const RequestContent values[] = {
    RequestContent_NONE,
    RequestContent_Move
  };
  return values;
}

inline const char * const *EnumNamesRequestContent() {
  static const char * const names[3] = {
    "NONE",
    "Move",
    nullptr
  };
  return names;
}

inline const char *EnumNameRequestContent(RequestContent e) {
  if (::flatbuffers::IsOutRange(e, RequestContent_NONE, RequestContent_Move)) return "";
  const size_t index = static_cast<size_t>(e);
  return EnumNamesRequestContent()[index];
}

template<typename T> struct RequestContentTraits {
  static const RequestContent enum_value = RequestContent_NONE;
};

template<> struct RequestContentTraits<chess::request::Move> {
  static const RequestContent enum_value = RequestContent_Move;
};

bool VerifyRequestContent(::flatbuffers::Verifier &verifier, const void *obj, RequestContent type);
bool VerifyRequestContentVector(::flatbuffers::Verifier &verifier, const ::flatbuffers::Vector<::flatbuffers::Offset<void>> *values, const ::flatbuffers::Vector<uint8_t> *types);

struct Move FLATBUFFERS_FINAL_CLASS : private ::flatbuffers::Table {
  typedef MoveBuilder Builder;
  enum FlatBuffersVTableOffset FLATBUFFERS_VTABLE_UNDERLYING_TYPE {
    VT_PIECE_ID = 4,
    VT_FROM = 6,
    VT_TO = 8
  };
  uint32_t piece_id() const {
    return GetField<uint32_t>(VT_PIECE_ID, 0);
  }
  const chess::common::Position *from() const {
    return GetStruct<const chess::common::Position *>(VT_FROM);
  }
  const chess::common::Position *to() const {
    return GetStruct<const chess::common::Position *>(VT_TO);
  }
  bool Verify(::flatbuffers::Verifier &verifier) const {
    return VerifyTableStart(verifier) &&
           VerifyField<uint32_t>(verifier, VT_PIECE_ID, 4) &&
           VerifyField<chess::common::Position>(verifier, VT_FROM, 1) &&
           VerifyField<chess::common::Position>(verifier, VT_TO, 1) &&
           verifier.EndTable();
  }
};

struct MoveBuilder {
  typedef Move Table;
  ::flatbuffers::FlatBufferBuilder &fbb_;
  ::flatbuffers::uoffset_t start_;
  void add_piece_id(uint32_t piece_id) {
    fbb_.AddElement<uint32_t>(Move::VT_PIECE_ID, piece_id, 0);
  }
  void add_from(const chess::common::Position *from) {
    fbb_.AddStruct(Move::VT_FROM, from);
  }
  void add_to(const chess::common::Position *to) {
    fbb_.AddStruct(Move::VT_TO, to);
  }
  explicit MoveBuilder(::flatbuffers::FlatBufferBuilder &_fbb)
        : fbb_(_fbb) {
    start_ = fbb_.StartTable();
  }
  ::flatbuffers::Offset<Move> Finish() {
    const auto end = fbb_.EndTable(start_);
    auto o = ::flatbuffers::Offset<Move>(end);
    return o;
  }
};

inline ::flatbuffers::Offset<Move> CreateMove(
    ::flatbuffers::FlatBufferBuilder &_fbb,
    uint32_t piece_id = 0,
    const chess::common::Position *from = nullptr,
    const chess::common::Position *to = nullptr) {
  MoveBuilder builder_(_fbb);
  builder_.add_to(to);
  builder_.add_from(from);
  builder_.add_piece_id(piece_id);
  return builder_.Finish();
}

struct Request FLATBUFFERS_FINAL_CLASS : private ::flatbuffers::Table {
  typedef RequestBuilder Builder;
  enum FlatBuffersVTableOffset FLATBUFFERS_VTABLE_UNDERLYING_TYPE {
    VT_REQUEST_TYPE = 4,
    VT_CONTENT_TYPE = 6,
    VT_CONTENT = 8
  };
  chess::request::RequestType request_type() const {
    return static_cast<chess::request::RequestType>(GetField<int8_t>(VT_REQUEST_TYPE, 0));
  }
  chess::request::RequestContent content_type() const {
    return static_cast<chess::request::RequestContent>(GetField<uint8_t>(VT_CONTENT_TYPE, 0));
  }
  const void *content() const {
    return GetPointer<const void *>(VT_CONTENT);
  }
  template<typename T> const T *content_as() const;
  const chess::request::Move *content_as_Move() const {
    return content_type() == chess::request::RequestContent_Move ? static_cast<const chess::request::Move *>(content()) : nullptr;
  }
  bool Verify(::flatbuffers::Verifier &verifier) const {
    return VerifyTableStart(verifier) &&
           VerifyField<int8_t>(verifier, VT_REQUEST_TYPE, 1) &&
           VerifyField<uint8_t>(verifier, VT_CONTENT_TYPE, 1) &&
           VerifyOffset(verifier, VT_CONTENT) &&
           VerifyRequestContent(verifier, content(), content_type()) &&
           verifier.EndTable();
  }
};

template<> inline const chess::request::Move *Request::content_as<chess::request::Move>() const {
  return content_as_Move();
}

struct RequestBuilder {
  typedef Request Table;
  ::flatbuffers::FlatBufferBuilder &fbb_;
  ::flatbuffers::uoffset_t start_;
  void add_request_type(chess::request::RequestType request_type) {
    fbb_.AddElement<int8_t>(Request::VT_REQUEST_TYPE, static_cast<int8_t>(request_type), 0);
  }
  void add_content_type(chess::request::RequestContent content_type) {
    fbb_.AddElement<uint8_t>(Request::VT_CONTENT_TYPE, static_cast<uint8_t>(content_type), 0);
  }
  void add_content(::flatbuffers::Offset<void> content) {
    fbb_.AddOffset(Request::VT_CONTENT, content);
  }
  explicit RequestBuilder(::flatbuffers::FlatBufferBuilder &_fbb)
        : fbb_(_fbb) {
    start_ = fbb_.StartTable();
  }
  ::flatbuffers::Offset<Request> Finish() {
    const auto end = fbb_.EndTable(start_);
    auto o = ::flatbuffers::Offset<Request>(end);
    return o;
  }
};

inline ::flatbuffers::Offset<Request> CreateRequest(
    ::flatbuffers::FlatBufferBuilder &_fbb,
    chess::request::RequestType request_type = chess::request::RequestType_MOVE,
    chess::request::RequestContent content_type = chess::request::RequestContent_NONE,
    ::flatbuffers::Offset<void> content = 0) {
  RequestBuilder builder_(_fbb);
  builder_.add_content(content);
  builder_.add_content_type(content_type);
  builder_.add_request_type(request_type);
  return builder_.Finish();
}

inline bool VerifyRequestContent(::flatbuffers::Verifier &verifier, const void *obj, RequestContent type) {
  switch (type) {
    case RequestContent_NONE: {
      return true;
    }
    case RequestContent_Move: {
      auto ptr = reinterpret_cast<const chess::request::Move *>(obj);
      return verifier.VerifyTable(ptr);
    }
    default: return true;
  }
}

inline bool VerifyRequestContentVector(::flatbuffers::Verifier &verifier, const ::flatbuffers::Vector<::flatbuffers::Offset<void>> *values, const ::flatbuffers::Vector<uint8_t> *types) {
  if (!values || !types) return !values && !types;
  if (values->size() != types->size()) return false;
  for (::flatbuffers::uoffset_t i = 0; i < values->size(); ++i) {
    if (!VerifyRequestContent(
        verifier,  values->Get(i), types->GetEnum<RequestContent>(i))) {
      return false;
    }
  }
  return true;
}

inline const chess::request::Request *GetRequest(const void *buf) {
  return ::flatbuffers::GetRoot<chess::request::Request>(buf);
}

inline const chess::request::Request *GetSizePrefixedRequest(const void *buf) {
  return ::flatbuffers::GetSizePrefixedRoot<chess::request::Request>(buf);
}

inline bool VerifyRequestBuffer(
    ::flatbuffers::Verifier &verifier) {
  return verifier.VerifyBuffer<chess::request::Request>(nullptr);
}

inline bool VerifySizePrefixedRequestBuffer(
    ::flatbuffers::Verifier &verifier) {
  return verifier.VerifySizePrefixedBuffer<chess::request::Request>(nullptr);
}

inline void FinishRequestBuffer(
    ::flatbuffers::FlatBufferBuilder &fbb,
    ::flatbuffers::Offset<chess::request::Request> root) {
  fbb.Finish(root);
}

inline void FinishSizePrefixedRequestBuffer(
    ::flatbuffers::FlatBufferBuilder &fbb,
    ::flatbuffers::Offset<chess::request::Request> root) {
  fbb.FinishSizePrefixed(root);
}

}  // namespace request
}  // namespace chess

#endif  // FLATBUFFERS_GENERATED_CHESSREQUEST_CHESS_REQUEST_H_
