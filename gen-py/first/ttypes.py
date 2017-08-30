#
# Autogenerated by Thrift Compiler (0.10.0)
#
# DO NOT EDIT UNLESS YOU ARE SURE THAT YOU KNOW WHAT YOU ARE DOING
#
#  options string: py
#

from thrift.Thrift import TType, TMessageType, TFrozenDict, TException, TApplicationException
from thrift.protocol.TProtocol import TProtocolException
import sys

from thrift.transport import TTransport


class MyEnum(object):
    ENUM1 = 0
    ENUM2 = 1
    ENUM3 = 2

    _VALUES_TO_NAMES = {
        0: "ENUM1",
        1: "ENUM2",
        2: "ENUM3",
    }

    _NAMES_TO_VALUES = {
        "ENUM1": 0,
        "ENUM2": 1,
        "ENUM3": 2,
    }


class MyStruct(object):
    """
    Attributes:
     - mybool
     - mybyte
     - myi16
     - myi32
     - myi64
     - mydouble
     - mystring
     - mylist
     - myset
     - mymap
    """

    thrift_spec = (
        None,  # 0
        (1, TType.BOOL, 'mybool', None, None, ),  # 1
        (2, TType.BYTE, 'mybyte', None, None, ),  # 2
        (3, TType.I16, 'myi16', None, None, ),  # 3
        (4, TType.I32, 'myi32', None, None, ),  # 4
        (5, TType.I64, 'myi64', None, None, ),  # 5
        (6, TType.DOUBLE, 'mydouble', None, None, ),  # 6
        (7, TType.STRING, 'mystring', 'UTF8', None, ),  # 7
        (8, TType.LIST, 'mylist', (TType.I32, None, False), None, ),  # 8
        (9, TType.SET, 'myset', (TType.I32, None, False), None, ),  # 9
        (10, TType.MAP, 'mymap', (TType.I32, None, TType.I32, None, False), None, ),  # 10
    )

    def __init__(self, mybool=None, mybyte=None, myi16=None, myi32=None, myi64=None, mydouble=None, mystring=None, mylist=None, myset=None, mymap=None,):
        self.mybool = mybool
        self.mybyte = mybyte
        self.myi16 = myi16
        self.myi32 = myi32
        self.myi64 = myi64
        self.mydouble = mydouble
        self.mystring = mystring
        self.mylist = mylist
        self.myset = myset
        self.mymap = mymap

    def read(self, iprot):
        if iprot._fast_decode is not None and isinstance(iprot.trans, TTransport.CReadableTransport) and self.thrift_spec is not None:
            iprot._fast_decode(self, iprot, (self.__class__, self.thrift_spec))
            return
        iprot.readStructBegin()
        while True:
            (fname, ftype, fid) = iprot.readFieldBegin()
            if ftype == TType.STOP:
                break
            if fid == 1:
                if ftype == TType.BOOL:
                    self.mybool = iprot.readBool()
                else:
                    iprot.skip(ftype)
            elif fid == 2:
                if ftype == TType.BYTE:
                    self.mybyte = iprot.readByte()
                else:
                    iprot.skip(ftype)
            elif fid == 3:
                if ftype == TType.I16:
                    self.myi16 = iprot.readI16()
                else:
                    iprot.skip(ftype)
            elif fid == 4:
                if ftype == TType.I32:
                    self.myi32 = iprot.readI32()
                else:
                    iprot.skip(ftype)
            elif fid == 5:
                if ftype == TType.I64:
                    self.myi64 = iprot.readI64()
                else:
                    iprot.skip(ftype)
            elif fid == 6:
                if ftype == TType.DOUBLE:
                    self.mydouble = iprot.readDouble()
                else:
                    iprot.skip(ftype)
            elif fid == 7:
                if ftype == TType.STRING:
                    self.mystring = iprot.readString().decode('utf-8') if sys.version_info[0] == 2 else iprot.readString()
                else:
                    iprot.skip(ftype)
            elif fid == 8:
                if ftype == TType.LIST:
                    self.mylist = []
                    (_etype3, _size0) = iprot.readListBegin()
                    for _i4 in range(_size0):
                        _elem5 = iprot.readI32()
                        self.mylist.append(_elem5)
                    iprot.readListEnd()
                else:
                    iprot.skip(ftype)
            elif fid == 9:
                if ftype == TType.SET:
                    self.myset = set()
                    (_etype9, _size6) = iprot.readSetBegin()
                    for _i10 in range(_size6):
                        _elem11 = iprot.readI32()
                        self.myset.add(_elem11)
                    iprot.readSetEnd()
                else:
                    iprot.skip(ftype)
            elif fid == 10:
                if ftype == TType.MAP:
                    self.mymap = {}
                    (_ktype13, _vtype14, _size12) = iprot.readMapBegin()
                    for _i16 in range(_size12):
                        _key17 = iprot.readI32()
                        _val18 = iprot.readI32()
                        self.mymap[_key17] = _val18
                    iprot.readMapEnd()
                else:
                    iprot.skip(ftype)
            else:
                iprot.skip(ftype)
            iprot.readFieldEnd()
        iprot.readStructEnd()

    def write(self, oprot):
        if oprot._fast_encode is not None and self.thrift_spec is not None:
            oprot.trans.write(oprot._fast_encode(self, (self.__class__, self.thrift_spec)))
            return
        oprot.writeStructBegin('MyStruct')
        if self.mybool is not None:
            oprot.writeFieldBegin('mybool', TType.BOOL, 1)
            oprot.writeBool(self.mybool)
            oprot.writeFieldEnd()
        if self.mybyte is not None:
            oprot.writeFieldBegin('mybyte', TType.BYTE, 2)
            oprot.writeByte(self.mybyte)
            oprot.writeFieldEnd()
        if self.myi16 is not None:
            oprot.writeFieldBegin('myi16', TType.I16, 3)
            oprot.writeI16(self.myi16)
            oprot.writeFieldEnd()
        if self.myi32 is not None:
            oprot.writeFieldBegin('myi32', TType.I32, 4)
            oprot.writeI32(self.myi32)
            oprot.writeFieldEnd()
        if self.myi64 is not None:
            oprot.writeFieldBegin('myi64', TType.I64, 5)
            oprot.writeI64(self.myi64)
            oprot.writeFieldEnd()
        if self.mydouble is not None:
            oprot.writeFieldBegin('mydouble', TType.DOUBLE, 6)
            oprot.writeDouble(self.mydouble)
            oprot.writeFieldEnd()
        if self.mystring is not None:
            oprot.writeFieldBegin('mystring', TType.STRING, 7)
            oprot.writeString(self.mystring.encode('utf-8') if sys.version_info[0] == 2 else self.mystring)
            oprot.writeFieldEnd()
        if self.mylist is not None:
            oprot.writeFieldBegin('mylist', TType.LIST, 8)
            oprot.writeListBegin(TType.I32, len(self.mylist))
            for iter19 in self.mylist:
                oprot.writeI32(iter19)
            oprot.writeListEnd()
            oprot.writeFieldEnd()
        if self.myset is not None:
            oprot.writeFieldBegin('myset', TType.SET, 9)
            oprot.writeSetBegin(TType.I32, len(self.myset))
            for iter20 in self.myset:
                oprot.writeI32(iter20)
            oprot.writeSetEnd()
            oprot.writeFieldEnd()
        if self.mymap is not None:
            oprot.writeFieldBegin('mymap', TType.MAP, 10)
            oprot.writeMapBegin(TType.I32, TType.I32, len(self.mymap))
            for kiter21, viter22 in self.mymap.items():
                oprot.writeI32(kiter21)
                oprot.writeI32(viter22)
            oprot.writeMapEnd()
            oprot.writeFieldEnd()
        oprot.writeFieldStop()
        oprot.writeStructEnd()

    def validate(self):
        return

    def __repr__(self):
        L = ['%s=%r' % (key, value)
             for key, value in self.__dict__.items()]
        return '%s(%s)' % (self.__class__.__name__, ', '.join(L))

    def __eq__(self, other):
        return isinstance(other, self.__class__) and self.__dict__ == other.__dict__

    def __ne__(self, other):
        return not (self == other)


class MyUnion(object):
    """
    Attributes:
     - mybool
     - mystring
    """

    thrift_spec = (
        None,  # 0
        (1, TType.BOOL, 'mybool', None, None, ),  # 1
        (2, TType.STRING, 'mystring', 'UTF8', None, ),  # 2
    )

    def __init__(self, mybool=None, mystring=None,):
        self.mybool = mybool
        self.mystring = mystring

    def read(self, iprot):
        if iprot._fast_decode is not None and isinstance(iprot.trans, TTransport.CReadableTransport) and self.thrift_spec is not None:
            iprot._fast_decode(self, iprot, (self.__class__, self.thrift_spec))
            return
        iprot.readStructBegin()
        while True:
            (fname, ftype, fid) = iprot.readFieldBegin()
            if ftype == TType.STOP:
                break
            if fid == 1:
                if ftype == TType.BOOL:
                    self.mybool = iprot.readBool()
                else:
                    iprot.skip(ftype)
            elif fid == 2:
                if ftype == TType.STRING:
                    self.mystring = iprot.readString().decode('utf-8') if sys.version_info[0] == 2 else iprot.readString()
                else:
                    iprot.skip(ftype)
            else:
                iprot.skip(ftype)
            iprot.readFieldEnd()
        iprot.readStructEnd()

    def write(self, oprot):
        if oprot._fast_encode is not None and self.thrift_spec is not None:
            oprot.trans.write(oprot._fast_encode(self, (self.__class__, self.thrift_spec)))
            return
        oprot.writeStructBegin('MyUnion')
        if self.mybool is not None:
            oprot.writeFieldBegin('mybool', TType.BOOL, 1)
            oprot.writeBool(self.mybool)
            oprot.writeFieldEnd()
        if self.mystring is not None:
            oprot.writeFieldBegin('mystring', TType.STRING, 2)
            oprot.writeString(self.mystring.encode('utf-8') if sys.version_info[0] == 2 else self.mystring)
            oprot.writeFieldEnd()
        oprot.writeFieldStop()
        oprot.writeStructEnd()

    def validate(self):
        return

    def __repr__(self):
        L = ['%s=%r' % (key, value)
             for key, value in self.__dict__.items()]
        return '%s(%s)' % (self.__class__.__name__, ', '.join(L))

    def __eq__(self, other):
        return isinstance(other, self.__class__) and self.__dict__ == other.__dict__

    def __ne__(self, other):
        return not (self == other)


class MyError(TException):
    """
    Attributes:
     - error_code
     - error_description
    """

    thrift_spec = (
        None,  # 0
        (1, TType.I32, 'error_code', None, None, ),  # 1
        (2, TType.STRING, 'error_description', 'UTF8', None, ),  # 2
    )

    def __init__(self, error_code=None, error_description=None,):
        self.error_code = error_code
        self.error_description = error_description

    def read(self, iprot):
        if iprot._fast_decode is not None and isinstance(iprot.trans, TTransport.CReadableTransport) and self.thrift_spec is not None:
            iprot._fast_decode(self, iprot, (self.__class__, self.thrift_spec))
            return
        iprot.readStructBegin()
        while True:
            (fname, ftype, fid) = iprot.readFieldBegin()
            if ftype == TType.STOP:
                break
            if fid == 1:
                if ftype == TType.I32:
                    self.error_code = iprot.readI32()
                else:
                    iprot.skip(ftype)
            elif fid == 2:
                if ftype == TType.STRING:
                    self.error_description = iprot.readString().decode('utf-8') if sys.version_info[0] == 2 else iprot.readString()
                else:
                    iprot.skip(ftype)
            else:
                iprot.skip(ftype)
            iprot.readFieldEnd()
        iprot.readStructEnd()

    def write(self, oprot):
        if oprot._fast_encode is not None and self.thrift_spec is not None:
            oprot.trans.write(oprot._fast_encode(self, (self.__class__, self.thrift_spec)))
            return
        oprot.writeStructBegin('MyError')
        if self.error_code is not None:
            oprot.writeFieldBegin('error_code', TType.I32, 1)
            oprot.writeI32(self.error_code)
            oprot.writeFieldEnd()
        if self.error_description is not None:
            oprot.writeFieldBegin('error_description', TType.STRING, 2)
            oprot.writeString(self.error_description.encode('utf-8') if sys.version_info[0] == 2 else self.error_description)
            oprot.writeFieldEnd()
        oprot.writeFieldStop()
        oprot.writeStructEnd()

    def validate(self):
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
