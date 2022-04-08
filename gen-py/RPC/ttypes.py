#
# Autogenerated by Thrift Compiler (0.16.0)
#
# DO NOT EDIT UNLESS YOU ARE SURE THAT YOU KNOW WHAT YOU ARE DOING
#
#  options string: py
#

from thrift.Thrift import TType, TMessageType, TFrozenDict, TException, TApplicationException
from thrift.protocol.TProtocol import TProtocolException
from thrift.TRecursive import fix_spec

import sys

from thrift.transport import TTransport
all_structs = []


class RESULT(object):
    """
    Attributes:
     - percent: Процент выполнения задачи
     - intermediate: Промежуточный или конечный результат

    """


    def __init__(self, percent=None, intermediate=None,):
        self.percent = percent
        self.intermediate = intermediate

    def read(self, iprot):
        if iprot._fast_decode is not None and isinstance(iprot.trans, TTransport.CReadableTransport) and self.thrift_spec is not None:
            iprot._fast_decode(self, iprot, [self.__class__, self.thrift_spec])
            return
        iprot.readStructBegin()
        while True:
            (fname, ftype, fid) = iprot.readFieldBegin()
            if ftype == TType.STOP:
                break
            if fid == 1:
                if ftype == TType.DOUBLE:
                    self.percent = iprot.readDouble()
                else:
                    iprot.skip(ftype)
            elif fid == 2:
                if ftype == TType.DOUBLE:
                    self.intermediate = iprot.readDouble()
                else:
                    iprot.skip(ftype)
            else:
                iprot.skip(ftype)
            iprot.readFieldEnd()
        iprot.readStructEnd()

    def write(self, oprot):
        if oprot._fast_encode is not None and self.thrift_spec is not None:
            oprot.trans.write(oprot._fast_encode(self, [self.__class__, self.thrift_spec]))
            return
        oprot.writeStructBegin('RESULT')
        if self.percent is not None:
            oprot.writeFieldBegin('percent', TType.DOUBLE, 1)
            oprot.writeDouble(self.percent)
            oprot.writeFieldEnd()
        if self.intermediate is not None:
            oprot.writeFieldBegin('intermediate', TType.DOUBLE, 2)
            oprot.writeDouble(self.intermediate)
            oprot.writeFieldEnd()
        oprot.writeFieldStop()
        oprot.writeStructEnd()

    def validate(self):
        if self.percent is None:
            raise TProtocolException(message='Required field percent is unset!')
        if self.intermediate is None:
            raise TProtocolException(message='Required field intermediate is unset!')
        return

    def __repr__(self):
        L = ['%s=%r' % (key, value)
             for key, value in self.__dict__.items()]
        return '%s(%s)' % (self.__class__.__name__, ', '.join(L))

    def __eq__(self, other):
        return isinstance(other, self.__class__) and self.__dict__ == other.__dict__

    def __ne__(self, other):
        return not (self == other)


class calcResult(object):
    """
    структура результата задачи

    Attributes:
     - id: UUID задачи
     - status: статус выполнения задачи (строка константа)
     - pushqtime: время постановки задачи в очередь
     - starttime: время начала вычисления (опционально)
     - stoptime: время завершения вычисления (опционально)
     - result: текущий результат (опционально)

    """


    def __init__(self, id=None, status=None, pushqtime=None, starttime=None, stoptime=None, result=None,):
        self.id = id
        self.status = status
        self.pushqtime = pushqtime
        self.starttime = starttime
        self.stoptime = stoptime
        self.result = result

    def read(self, iprot):
        if iprot._fast_decode is not None and isinstance(iprot.trans, TTransport.CReadableTransport) and self.thrift_spec is not None:
            iprot._fast_decode(self, iprot, [self.__class__, self.thrift_spec])
            return
        iprot.readStructBegin()
        while True:
            (fname, ftype, fid) = iprot.readFieldBegin()
            if ftype == TType.STOP:
                break
            if fid == 1:
                if ftype == TType.STRING:
                    self.id = iprot.readString().decode('utf-8', errors='replace') if sys.version_info[0] == 2 else iprot.readString()
                else:
                    iprot.skip(ftype)
            elif fid == 2:
                if ftype == TType.STRING:
                    self.status = iprot.readString().decode('utf-8', errors='replace') if sys.version_info[0] == 2 else iprot.readString()
                else:
                    iprot.skip(ftype)
            elif fid == 3:
                if ftype == TType.STRING:
                    self.pushqtime = iprot.readString().decode('utf-8', errors='replace') if sys.version_info[0] == 2 else iprot.readString()
                else:
                    iprot.skip(ftype)
            elif fid == 4:
                if ftype == TType.STRING:
                    self.starttime = iprot.readString().decode('utf-8', errors='replace') if sys.version_info[0] == 2 else iprot.readString()
                else:
                    iprot.skip(ftype)
            elif fid == 5:
                if ftype == TType.STRING:
                    self.stoptime = iprot.readString().decode('utf-8', errors='replace') if sys.version_info[0] == 2 else iprot.readString()
                else:
                    iprot.skip(ftype)
            elif fid == 6:
                if ftype == TType.STRUCT:
                    self.result = RESULT()
                    self.result.read(iprot)
                else:
                    iprot.skip(ftype)
            else:
                iprot.skip(ftype)
            iprot.readFieldEnd()
        iprot.readStructEnd()

    def write(self, oprot):
        if oprot._fast_encode is not None and self.thrift_spec is not None:
            oprot.trans.write(oprot._fast_encode(self, [self.__class__, self.thrift_spec]))
            return
        oprot.writeStructBegin('calcResult')
        if self.id is not None:
            oprot.writeFieldBegin('id', TType.STRING, 1)
            oprot.writeString(self.id.encode('utf-8') if sys.version_info[0] == 2 else self.id)
            oprot.writeFieldEnd()
        if self.status is not None:
            oprot.writeFieldBegin('status', TType.STRING, 2)
            oprot.writeString(self.status.encode('utf-8') if sys.version_info[0] == 2 else self.status)
            oprot.writeFieldEnd()
        if self.pushqtime is not None:
            oprot.writeFieldBegin('pushqtime', TType.STRING, 3)
            oprot.writeString(self.pushqtime.encode('utf-8') if sys.version_info[0] == 2 else self.pushqtime)
            oprot.writeFieldEnd()
        if self.starttime is not None:
            oprot.writeFieldBegin('starttime', TType.STRING, 4)
            oprot.writeString(self.starttime.encode('utf-8') if sys.version_info[0] == 2 else self.starttime)
            oprot.writeFieldEnd()
        if self.stoptime is not None:
            oprot.writeFieldBegin('stoptime', TType.STRING, 5)
            oprot.writeString(self.stoptime.encode('utf-8') if sys.version_info[0] == 2 else self.stoptime)
            oprot.writeFieldEnd()
        if self.result is not None:
            oprot.writeFieldBegin('result', TType.STRUCT, 6)
            self.result.write(oprot)
            oprot.writeFieldEnd()
        oprot.writeFieldStop()
        oprot.writeStructEnd()

    def validate(self):
        if self.id is None:
            raise TProtocolException(message='Required field id is unset!')
        if self.status is None:
            raise TProtocolException(message='Required field status is unset!')
        if self.pushqtime is None:
            raise TProtocolException(message='Required field pushqtime is unset!')
        return

    def __repr__(self):
        L = ['%s=%r' % (key, value)
             for key, value in self.__dict__.items()]
        return '%s(%s)' % (self.__class__.__name__, ', '.join(L))

    def __eq__(self, other):
        return isinstance(other, self.__class__) and self.__dict__ == other.__dict__

    def __ne__(self, other):
        return not (self == other)


class BadTask(TException):
    """
    Attributes:
     - uuid: The problem uuid
     - error_code: Сервисный код

    """


    def __init__(self, uuid=None, error_code=None,):
        super(BadTask, self).__setattr__('uuid', uuid)
        super(BadTask, self).__setattr__('error_code', error_code)

    def __setattr__(self, *args):
        raise TypeError("can't modify immutable instance")

    def __delattr__(self, *args):
        raise TypeError("can't modify immutable instance")

    def __hash__(self):
        return hash(self.__class__) ^ hash((self.uuid, self.error_code, ))

    @classmethod
    def read(cls, iprot):
        if iprot._fast_decode is not None and isinstance(iprot.trans, TTransport.CReadableTransport) and cls.thrift_spec is not None:
            return iprot._fast_decode(None, iprot, [cls, cls.thrift_spec])
        iprot.readStructBegin()
        uuid = None
        error_code = None
        while True:
            (fname, ftype, fid) = iprot.readFieldBegin()
            if ftype == TType.STOP:
                break
            if fid == 1:
                if ftype == TType.STRING:
                    uuid = iprot.readString().decode('utf-8', errors='replace') if sys.version_info[0] == 2 else iprot.readString()
                else:
                    iprot.skip(ftype)
            elif fid == 2:
                if ftype == TType.I16:
                    error_code = iprot.readI16()
                else:
                    iprot.skip(ftype)
            else:
                iprot.skip(ftype)
            iprot.readFieldEnd()
        iprot.readStructEnd()
        return cls(
            uuid=uuid,
            error_code=error_code,
        )

    def write(self, oprot):
        if oprot._fast_encode is not None and self.thrift_spec is not None:
            oprot.trans.write(oprot._fast_encode(self, [self.__class__, self.thrift_spec]))
            return
        oprot.writeStructBegin('BadTask')
        if self.uuid is not None:
            oprot.writeFieldBegin('uuid', TType.STRING, 1)
            oprot.writeString(self.uuid.encode('utf-8') if sys.version_info[0] == 2 else self.uuid)
            oprot.writeFieldEnd()
        if self.error_code is not None:
            oprot.writeFieldBegin('error_code', TType.I16, 2)
            oprot.writeI16(self.error_code)
            oprot.writeFieldEnd()
        oprot.writeFieldStop()
        oprot.writeStructEnd()

    def validate(self):
        if self.uuid is None:
            raise TProtocolException(message='Required field uuid is unset!')
        if self.error_code is None:
            raise TProtocolException(message='Required field error_code is unset!')
        return

    def __str__(self):
        return repr(self)

    def __repr__(self):
        L = ['%s=%r' % (key, value)
             for key, value in self.__dict__.items()]
        return '%s(%s)' % (self.__class__.__name__, ', '.join(L))

    def __eq__(self, other):
        return isinstance(other, self.__class__) and self.__dict__ == other.__dict__

    def __ne__(self, other):
        return not (self == other)
all_structs.append(RESULT)
RESULT.thrift_spec = (
    None,  # 0
    (1, TType.DOUBLE, 'percent', None, None, ),  # 1
    (2, TType.DOUBLE, 'intermediate', None, None, ),  # 2
)
all_structs.append(calcResult)
calcResult.thrift_spec = (
    None,  # 0
    (1, TType.STRING, 'id', 'UTF8', None, ),  # 1
    (2, TType.STRING, 'status', 'UTF8', None, ),  # 2
    (3, TType.STRING, 'pushqtime', 'UTF8', None, ),  # 3
    (4, TType.STRING, 'starttime', 'UTF8', None, ),  # 4
    (5, TType.STRING, 'stoptime', 'UTF8', None, ),  # 5
    (6, TType.STRUCT, 'result', [RESULT, None], None, ),  # 6
)
all_structs.append(BadTask)
BadTask.thrift_spec = (
    None,  # 0
    (1, TType.STRING, 'uuid', 'UTF8', None, ),  # 1
    (2, TType.I16, 'error_code', None, None, ),  # 2
)
fix_spec(all_structs)
del all_structs
