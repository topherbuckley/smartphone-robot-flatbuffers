# automatically generated by the FlatBuffers compiler, do not modify

# namespace: fbclasses

import flatbuffers
from flatbuffers.compat import import_numpy
np = import_numpy()

class CommAction(object):
    __slots__ = ['_tab']

    @classmethod
    def GetRootAs(cls, buf, offset=0):
        n = flatbuffers.encode.Get(flatbuffers.packer.uoffset, buf, offset)
        x = CommAction()
        x.Init(buf, n + offset)
        return x

    @classmethod
    def GetRootAsCommAction(cls, buf, offset=0):
        """This method is deprecated. Please switch to GetRootAs."""
        return cls.GetRootAs(buf, offset)
    # CommAction
    def Init(self, buf, pos):
        self._tab = flatbuffers.table.Table(buf, pos)

    # CommAction
    def ActionByte(self):
        o = flatbuffers.number_types.UOffsetTFlags.py_type(self._tab.Offset(4))
        if o != 0:
            return self._tab.Get(flatbuffers.number_types.Int8Flags, o + self._tab.Pos)
        return 0

    # CommAction
    def ActionName(self):
        o = flatbuffers.number_types.UOffsetTFlags.py_type(self._tab.Offset(6))
        if o != 0:
            return self._tab.String(o + self._tab.Pos)
        return None

def Start(builder): builder.StartObject(2)
def CommActionStart(builder):
    """This method is deprecated. Please switch to Start."""
    return Start(builder)
def AddActionByte(builder, actionByte): builder.PrependInt8Slot(0, actionByte, 0)
def CommActionAddActionByte(builder, actionByte):
    """This method is deprecated. Please switch to AddActionByte."""
    return AddActionByte(builder, actionByte)
def AddActionName(builder, actionName): builder.PrependUOffsetTRelativeSlot(1, flatbuffers.number_types.UOffsetTFlags.py_type(actionName), 0)
def CommActionAddActionName(builder, actionName):
    """This method is deprecated. Please switch to AddActionName."""
    return AddActionName(builder, actionName)
def End(builder): return builder.EndObject()
def CommActionEnd(builder):
    """This method is deprecated. Please switch to End."""
    return End(builder)