# automatically generated by the FlatBuffers compiler, do not modify

# namespace: fbclasses

import flatbuffers
from flatbuffers.compat import import_numpy
np = import_numpy()

class MotionAction(object):
    __slots__ = ['_tab']

    @classmethod
    def GetRootAs(cls, buf, offset=0):
        n = flatbuffers.encode.Get(flatbuffers.packer.uoffset, buf, offset)
        x = MotionAction()
        x.Init(buf, n + offset)
        return x

    @classmethod
    def GetRootAsMotionAction(cls, buf, offset=0):
        """This method is deprecated. Please switch to GetRootAs."""
        return cls.GetRootAs(buf, offset)
    # MotionAction
    def Init(self, buf, pos):
        self._tab = flatbuffers.table.Table(buf, pos)

    # MotionAction
    def ActionByte(self):
        o = flatbuffers.number_types.UOffsetTFlags.py_type(self._tab.Offset(4))
        if o != 0:
            return self._tab.Get(flatbuffers.number_types.Int8Flags, o + self._tab.Pos)
        return 0

    # MotionAction
    def ActionName(self):
        o = flatbuffers.number_types.UOffsetTFlags.py_type(self._tab.Offset(6))
        if o != 0:
            return self._tab.String(o + self._tab.Pos)
        return None

    # MotionAction
    def LeftWheelSpeed(self):
        o = flatbuffers.number_types.UOffsetTFlags.py_type(self._tab.Offset(8))
        if o != 0:
            return self._tab.Get(flatbuffers.number_types.Float32Flags, o + self._tab.Pos)
        return 0.0

    # MotionAction
    def RightWheelSpeed(self):
        o = flatbuffers.number_types.UOffsetTFlags.py_type(self._tab.Offset(10))
        if o != 0:
            return self._tab.Get(flatbuffers.number_types.Float32Flags, o + self._tab.Pos)
        return 0.0

    # MotionAction
    def LeftWheelBrake(self):
        o = flatbuffers.number_types.UOffsetTFlags.py_type(self._tab.Offset(12))
        if o != 0:
            return bool(self._tab.Get(flatbuffers.number_types.BoolFlags, o + self._tab.Pos))
        return False

    # MotionAction
    def RightWheelBrake(self):
        o = flatbuffers.number_types.UOffsetTFlags.py_type(self._tab.Offset(14))
        if o != 0:
            return bool(self._tab.Get(flatbuffers.number_types.BoolFlags, o + self._tab.Pos))
        return False

def Start(builder): builder.StartObject(6)
def MotionActionStart(builder):
    """This method is deprecated. Please switch to Start."""
    return Start(builder)
def AddActionByte(builder, actionByte): builder.PrependInt8Slot(0, actionByte, 0)
def MotionActionAddActionByte(builder, actionByte):
    """This method is deprecated. Please switch to AddActionByte."""
    return AddActionByte(builder, actionByte)
def AddActionName(builder, actionName): builder.PrependUOffsetTRelativeSlot(1, flatbuffers.number_types.UOffsetTFlags.py_type(actionName), 0)
def MotionActionAddActionName(builder, actionName):
    """This method is deprecated. Please switch to AddActionName."""
    return AddActionName(builder, actionName)
def AddLeftWheelSpeed(builder, leftWheelSpeed): builder.PrependFloat32Slot(2, leftWheelSpeed, 0.0)
def MotionActionAddLeftWheelSpeed(builder, leftWheelSpeed):
    """This method is deprecated. Please switch to AddLeftWheelSpeed."""
    return AddLeftWheelSpeed(builder, leftWheelSpeed)
def AddRightWheelSpeed(builder, rightWheelSpeed): builder.PrependFloat32Slot(3, rightWheelSpeed, 0.0)
def MotionActionAddRightWheelSpeed(builder, rightWheelSpeed):
    """This method is deprecated. Please switch to AddRightWheelSpeed."""
    return AddRightWheelSpeed(builder, rightWheelSpeed)
def AddLeftWheelBrake(builder, leftWheelBrake): builder.PrependBoolSlot(4, leftWheelBrake, 0)
def MotionActionAddLeftWheelBrake(builder, leftWheelBrake):
    """This method is deprecated. Please switch to AddLeftWheelBrake."""
    return AddLeftWheelBrake(builder, leftWheelBrake)
def AddRightWheelBrake(builder, rightWheelBrake): builder.PrependBoolSlot(5, rightWheelBrake, 0)
def MotionActionAddRightWheelBrake(builder, rightWheelBrake):
    """This method is deprecated. Please switch to AddRightWheelBrake."""
    return AddRightWheelBrake(builder, rightWheelBrake)
def End(builder): return builder.EndObject()
def MotionActionEnd(builder):
    """This method is deprecated. Please switch to End."""
    return End(builder)