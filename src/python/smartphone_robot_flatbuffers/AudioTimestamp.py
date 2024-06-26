# automatically generated by the FlatBuffers compiler, do not modify

# namespace: fbclasses

import flatbuffers
from flatbuffers.compat import import_numpy
np = import_numpy()

class AudioTimestamp(object):
    __slots__ = ['_tab']

    @classmethod
    def GetRootAs(cls, buf, offset=0):
        n = flatbuffers.encode.Get(flatbuffers.packer.uoffset, buf, offset)
        x = AudioTimestamp()
        x.Init(buf, n + offset)
        return x

    @classmethod
    def GetRootAsAudioTimestamp(cls, buf, offset=0):
        """This method is deprecated. Please switch to GetRootAs."""
        return cls.GetRootAs(buf, offset)
    # AudioTimestamp
    def Init(self, buf, pos):
        self._tab = flatbuffers.table.Table(buf, pos)

    # AudioTimestamp
    def FramePosition(self):
        o = flatbuffers.number_types.UOffsetTFlags.py_type(self._tab.Offset(4))
        if o != 0:
            return self._tab.Get(flatbuffers.number_types.Int64Flags, o + self._tab.Pos)
        return 0

    # AudioTimestamp
    def Nanotime(self):
        o = flatbuffers.number_types.UOffsetTFlags.py_type(self._tab.Offset(6))
        if o != 0:
            return self._tab.Get(flatbuffers.number_types.Int64Flags, o + self._tab.Pos)
        return 0

def Start(builder): builder.StartObject(2)
def AudioTimestampStart(builder):
    """This method is deprecated. Please switch to Start."""
    return Start(builder)
def AddFramePosition(builder, framePosition): builder.PrependInt64Slot(0, framePosition, 0)
def AudioTimestampAddFramePosition(builder, framePosition):
    """This method is deprecated. Please switch to AddFramePosition."""
    return AddFramePosition(builder, framePosition)
def AddNanotime(builder, nanotime): builder.PrependInt64Slot(1, nanotime, 0)
def AudioTimestampAddNanotime(builder, nanotime):
    """This method is deprecated. Please switch to AddNanotime."""
    return AddNanotime(builder, nanotime)
def End(builder): return builder.EndObject()
def AudioTimestampEnd(builder):
    """This method is deprecated. Please switch to End."""
    return End(builder)