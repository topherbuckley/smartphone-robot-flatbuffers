# automatically generated by the FlatBuffers compiler, do not modify

# namespace: fbclasses

import flatbuffers
from flatbuffers.compat import import_numpy
np = import_numpy()

class BatteryData(object):
    __slots__ = ['_tab']

    @classmethod
    def GetRootAs(cls, buf, offset=0):
        n = flatbuffers.encode.Get(flatbuffers.packer.uoffset, buf, offset)
        x = BatteryData()
        x.Init(buf, n + offset)
        return x

    @classmethod
    def GetRootAsBatteryData(cls, buf, offset=0):
        """This method is deprecated. Please switch to GetRootAs."""
        return cls.GetRootAs(buf, offset)
    # BatteryData
    def Init(self, buf, pos):
        self._tab = flatbuffers.table.Table(buf, pos)

    # BatteryData
    def Timestamps(self, j):
        o = flatbuffers.number_types.UOffsetTFlags.py_type(self._tab.Offset(4))
        if o != 0:
            a = self._tab.Vector(o)
            return self._tab.Get(flatbuffers.number_types.Int64Flags, a + flatbuffers.number_types.UOffsetTFlags.py_type(j * 8))
        return 0

    # BatteryData
    def TimestampsAsNumpy(self):
        o = flatbuffers.number_types.UOffsetTFlags.py_type(self._tab.Offset(4))
        if o != 0:
            return self._tab.GetVectorAsNumpy(flatbuffers.number_types.Int64Flags, o)
        return 0

    # BatteryData
    def TimestampsLength(self):
        o = flatbuffers.number_types.UOffsetTFlags.py_type(self._tab.Offset(4))
        if o != 0:
            return self._tab.VectorLen(o)
        return 0

    # BatteryData
    def TimestampsIsNone(self):
        o = flatbuffers.number_types.UOffsetTFlags.py_type(self._tab.Offset(4))
        return o == 0

    # BatteryData
    def Voltage(self, j):
        o = flatbuffers.number_types.UOffsetTFlags.py_type(self._tab.Offset(6))
        if o != 0:
            a = self._tab.Vector(o)
            return self._tab.Get(flatbuffers.number_types.Float64Flags, a + flatbuffers.number_types.UOffsetTFlags.py_type(j * 8))
        return 0

    # BatteryData
    def VoltageAsNumpy(self):
        o = flatbuffers.number_types.UOffsetTFlags.py_type(self._tab.Offset(6))
        if o != 0:
            return self._tab.GetVectorAsNumpy(flatbuffers.number_types.Float64Flags, o)
        return 0

    # BatteryData
    def VoltageLength(self):
        o = flatbuffers.number_types.UOffsetTFlags.py_type(self._tab.Offset(6))
        if o != 0:
            return self._tab.VectorLen(o)
        return 0

    # BatteryData
    def VoltageIsNone(self):
        o = flatbuffers.number_types.UOffsetTFlags.py_type(self._tab.Offset(6))
        return o == 0

def Start(builder): builder.StartObject(2)
def BatteryDataStart(builder):
    """This method is deprecated. Please switch to Start."""
    return Start(builder)
def AddTimestamps(builder, timestamps): builder.PrependUOffsetTRelativeSlot(0, flatbuffers.number_types.UOffsetTFlags.py_type(timestamps), 0)
def BatteryDataAddTimestamps(builder, timestamps):
    """This method is deprecated. Please switch to AddTimestamps."""
    return AddTimestamps(builder, timestamps)
def StartTimestampsVector(builder, numElems): return builder.StartVector(8, numElems, 8)
def BatteryDataStartTimestampsVector(builder, numElems):
    """This method is deprecated. Please switch to Start."""
    return StartTimestampsVector(builder, numElems)
def AddVoltage(builder, voltage): builder.PrependUOffsetTRelativeSlot(1, flatbuffers.number_types.UOffsetTFlags.py_type(voltage), 0)
def BatteryDataAddVoltage(builder, voltage):
    """This method is deprecated. Please switch to AddVoltage."""
    return AddVoltage(builder, voltage)
def StartVoltageVector(builder, numElems): return builder.StartVector(8, numElems, 8)
def BatteryDataStartVoltageVector(builder, numElems):
    """This method is deprecated. Please switch to Start."""
    return StartVoltageVector(builder, numElems)
def End(builder): return builder.EndObject()
def BatteryDataEnd(builder):
    """This method is deprecated. Please switch to End."""
    return End(builder)