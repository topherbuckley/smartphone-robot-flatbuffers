# automatically generated by the FlatBuffers compiler, do not modify

# namespace: fbclasses

import flatbuffers
from flatbuffers.compat import import_numpy
np = import_numpy()

class OrientationData(object):
    __slots__ = ['_tab']

    @classmethod
    def GetRootAs(cls, buf, offset=0):
        n = flatbuffers.encode.Get(flatbuffers.packer.uoffset, buf, offset)
        x = OrientationData()
        x.Init(buf, n + offset)
        return x

    @classmethod
    def GetRootAsOrientationData(cls, buf, offset=0):
        """This method is deprecated. Please switch to GetRootAs."""
        return cls.GetRootAs(buf, offset)
    # OrientationData
    def Init(self, buf, pos):
        self._tab = flatbuffers.table.Table(buf, pos)

    # OrientationData
    def Timestamps(self, j):
        o = flatbuffers.number_types.UOffsetTFlags.py_type(self._tab.Offset(4))
        if o != 0:
            a = self._tab.Vector(o)
            return self._tab.Get(flatbuffers.number_types.Int64Flags, a + flatbuffers.number_types.UOffsetTFlags.py_type(j * 8))
        return 0

    # OrientationData
    def TimestampsAsNumpy(self):
        o = flatbuffers.number_types.UOffsetTFlags.py_type(self._tab.Offset(4))
        if o != 0:
            return self._tab.GetVectorAsNumpy(flatbuffers.number_types.Int64Flags, o)
        return 0

    # OrientationData
    def TimestampsLength(self):
        o = flatbuffers.number_types.UOffsetTFlags.py_type(self._tab.Offset(4))
        if o != 0:
            return self._tab.VectorLen(o)
        return 0

    # OrientationData
    def TimestampsIsNone(self):
        o = flatbuffers.number_types.UOffsetTFlags.py_type(self._tab.Offset(4))
        return o == 0

    # OrientationData
    def Tiltangle(self, j):
        o = flatbuffers.number_types.UOffsetTFlags.py_type(self._tab.Offset(6))
        if o != 0:
            a = self._tab.Vector(o)
            return self._tab.Get(flatbuffers.number_types.Float64Flags, a + flatbuffers.number_types.UOffsetTFlags.py_type(j * 8))
        return 0

    # OrientationData
    def TiltangleAsNumpy(self):
        o = flatbuffers.number_types.UOffsetTFlags.py_type(self._tab.Offset(6))
        if o != 0:
            return self._tab.GetVectorAsNumpy(flatbuffers.number_types.Float64Flags, o)
        return 0

    # OrientationData
    def TiltangleLength(self):
        o = flatbuffers.number_types.UOffsetTFlags.py_type(self._tab.Offset(6))
        if o != 0:
            return self._tab.VectorLen(o)
        return 0

    # OrientationData
    def TiltangleIsNone(self):
        o = flatbuffers.number_types.UOffsetTFlags.py_type(self._tab.Offset(6))
        return o == 0

    # OrientationData
    def Tiltvelocity(self, j):
        o = flatbuffers.number_types.UOffsetTFlags.py_type(self._tab.Offset(8))
        if o != 0:
            a = self._tab.Vector(o)
            return self._tab.Get(flatbuffers.number_types.Float64Flags, a + flatbuffers.number_types.UOffsetTFlags.py_type(j * 8))
        return 0

    # OrientationData
    def TiltvelocityAsNumpy(self):
        o = flatbuffers.number_types.UOffsetTFlags.py_type(self._tab.Offset(8))
        if o != 0:
            return self._tab.GetVectorAsNumpy(flatbuffers.number_types.Float64Flags, o)
        return 0

    # OrientationData
    def TiltvelocityLength(self):
        o = flatbuffers.number_types.UOffsetTFlags.py_type(self._tab.Offset(8))
        if o != 0:
            return self._tab.VectorLen(o)
        return 0

    # OrientationData
    def TiltvelocityIsNone(self):
        o = flatbuffers.number_types.UOffsetTFlags.py_type(self._tab.Offset(8))
        return o == 0

def Start(builder): builder.StartObject(3)
def OrientationDataStart(builder):
    """This method is deprecated. Please switch to Start."""
    return Start(builder)
def AddTimestamps(builder, timestamps): builder.PrependUOffsetTRelativeSlot(0, flatbuffers.number_types.UOffsetTFlags.py_type(timestamps), 0)
def OrientationDataAddTimestamps(builder, timestamps):
    """This method is deprecated. Please switch to AddTimestamps."""
    return AddTimestamps(builder, timestamps)
def StartTimestampsVector(builder, numElems): return builder.StartVector(8, numElems, 8)
def OrientationDataStartTimestampsVector(builder, numElems):
    """This method is deprecated. Please switch to Start."""
    return StartTimestampsVector(builder, numElems)
def AddTiltangle(builder, tiltangle): builder.PrependUOffsetTRelativeSlot(1, flatbuffers.number_types.UOffsetTFlags.py_type(tiltangle), 0)
def OrientationDataAddTiltangle(builder, tiltangle):
    """This method is deprecated. Please switch to AddTiltangle."""
    return AddTiltangle(builder, tiltangle)
def StartTiltangleVector(builder, numElems): return builder.StartVector(8, numElems, 8)
def OrientationDataStartTiltangleVector(builder, numElems):
    """This method is deprecated. Please switch to Start."""
    return StartTiltangleVector(builder, numElems)
def AddTiltvelocity(builder, tiltvelocity): builder.PrependUOffsetTRelativeSlot(2, flatbuffers.number_types.UOffsetTFlags.py_type(tiltvelocity), 0)
def OrientationDataAddTiltvelocity(builder, tiltvelocity):
    """This method is deprecated. Please switch to AddTiltvelocity."""
    return AddTiltvelocity(builder, tiltvelocity)
def StartTiltvelocityVector(builder, numElems): return builder.StartVector(8, numElems, 8)
def OrientationDataStartTiltvelocityVector(builder, numElems):
    """This method is deprecated. Please switch to Start."""
    return StartTiltvelocityVector(builder, numElems)
def End(builder): return builder.EndObject()
def OrientationDataEnd(builder):
    """This method is deprecated. Please switch to End."""
    return End(builder)