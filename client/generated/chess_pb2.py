# -*- coding: utf-8 -*-
# Generated by the protocol buffer compiler.  DO NOT EDIT!
# source: chess.proto
"""Generated protocol buffer code."""
from google.protobuf.internal import builder as _builder
from google.protobuf import descriptor as _descriptor
from google.protobuf import descriptor_pool as _descriptor_pool
from google.protobuf import symbol_database as _symbol_database
# @@protoc_insertion_point(imports)

_sym_db = _symbol_database.Default()




DESCRIPTOR = _descriptor_pool.Default().AddSerializedFile(b'\n\x0b\x63hess.proto\x12\x0e\x63hess.standard\" \n\x08Position\x12\t\n\x01x\x18\x01 \x01(\x05\x12\t\n\x01y\x18\x02 \x01(\x05\"\x99\x01\n\x05Piece\x12\n\n\x02id\x18\x01 \x01(\x05\x12-\n\npiece_type\x18\x02 \x01(\x0e\x32\x19.chess.standard.PieceType\x12)\n\x05\x63olor\x18\x03 \x01(\x0e\x32\x1a.chess.standard.PieceColor\x12*\n\x08position\x18\x04 \x01(\x0b\x32\x18.chess.standard.Position\"3\n\nBoardState\x12%\n\x06pieces\x18\x01 \x03(\x0b\x32\x15.chess.standard.Piece\"f\n\x04Move\x12\x10\n\x08piece_id\x18\x01 \x01(\x05\x12&\n\x04\x66rom\x18\x02 \x01(\x0b\x32\x18.chess.standard.Position\x12$\n\x02to\x18\x03 \x01(\x0b\x32\x18.chess.standard.Position\"1\n\x0bMoveMessage\x12\"\n\x04move\x18\x01 \x01(\x0b\x32\x14.chess.standard.Move\"\x8b\x01\n\x11MoveResultMessage\x12\"\n\x04move\x18\x01 \x01(\x0b\x32\x14.chess.standard.Move\x12/\n\x0b\x62oard_state\x18\x02 \x01(\x0b\x32\x1a.chess.standard.BoardState\x12\r\n\x05valid\x18\x03 \x01(\x08\x12\x12\n\nerror_code\x18\x04 \x01(\r\"r\n\x0fGameOverMessage\x12\x30\n\x0cwinner_color\x18\x01 \x01(\x0e\x32\x1a.chess.standard.PieceColor\x12-\n\x06reason\x18\x02 \x01(\x0e\x32\x1d.chess.standard.GameEndReason\"\xfc\x01\n\x07Message\x12\x31\n\x0cmessage_type\x18\x01 \x01(\x0e\x32\x1b.chess.standard.MessageType\x12\x33\n\x0cmove_message\x18\x02 \x01(\x0b\x32\x1b.chess.standard.MoveMessageH\x00\x12@\n\x13move_result_message\x18\x03 \x01(\x0b\x32!.chess.standard.MoveResultMessageH\x00\x12<\n\x11game_over_message\x18\x04 \x01(\x0b\x32\x1f.chess.standard.GameOverMessageH\x00\x42\t\n\x07\x63ontent*L\n\tPieceType\x12\x08\n\x04PAWN\x10\x00\x12\x08\n\x04ROOK\x10\x01\x12\n\n\x06KNIGHT\x10\x02\x12\n\n\x06\x42ISHOP\x10\x03\x12\t\n\x05QUEEN\x10\x04\x12\x08\n\x04KING\x10\x05*\"\n\nPieceColor\x12\t\n\x05WHITE\x10\x00\x12\t\n\x05\x42LACK\x10\x01*7\n\x0bMessageType\x12\x08\n\x04MOVE\x10\x00\x12\x0f\n\x0bMOVE_RESULT\x10\x01\x12\r\n\tGAME_OVER\x10\x02*]\n\rGameEndReason\x12\r\n\tCHECKMATE\x10\x00\x12\r\n\tSTALEMATE\x10\x01\x12\x0f\n\x0bRESIGNATION\x10\x02\x12\x0f\n\x0b\x41GREED_DRAW\x10\x03\x12\x0c\n\x08TIME_OUT\x10\x04\x32\xa2\x01\n\x0c\x43hessService\x12\x43\n\x08MakeMove\x12\x14.chess.standard.Move\x1a!.chess.standard.MoveResultMessage\x12M\n\x07\x45ndGame\x12\x1f.chess.standard.GameOverMessage\x1a!.chess.standard.MoveResultMessageb\x06proto3')

_builder.BuildMessageAndEnumDescriptors(DESCRIPTOR, globals())
_builder.BuildTopDescriptorsAndMessages(DESCRIPTOR, 'chess_pb2', globals())
if _descriptor._USE_C_DESCRIPTORS == False:

  DESCRIPTOR._options = None
  _PIECETYPE._serialized_start=942
  _PIECETYPE._serialized_end=1018
  _PIECECOLOR._serialized_start=1020
  _PIECECOLOR._serialized_end=1054
  _MESSAGETYPE._serialized_start=1056
  _MESSAGETYPE._serialized_end=1111
  _GAMEENDREASON._serialized_start=1113
  _GAMEENDREASON._serialized_end=1206
  _POSITION._serialized_start=31
  _POSITION._serialized_end=63
  _PIECE._serialized_start=66
  _PIECE._serialized_end=219
  _BOARDSTATE._serialized_start=221
  _BOARDSTATE._serialized_end=272
  _MOVE._serialized_start=274
  _MOVE._serialized_end=376
  _MOVEMESSAGE._serialized_start=378
  _MOVEMESSAGE._serialized_end=427
  _MOVERESULTMESSAGE._serialized_start=430
  _MOVERESULTMESSAGE._serialized_end=569
  _GAMEOVERMESSAGE._serialized_start=571
  _GAMEOVERMESSAGE._serialized_end=685
  _MESSAGE._serialized_start=688
  _MESSAGE._serialized_end=940
  _CHESSSERVICE._serialized_start=1209
  _CHESSSERVICE._serialized_end=1371
# @@protoc_insertion_point(module_scope)
