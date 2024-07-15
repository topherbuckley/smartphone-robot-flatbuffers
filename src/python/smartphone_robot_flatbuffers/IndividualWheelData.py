# automatically generated by the FlatBuffers compiler, do not modify

# namespace: fbclasses

import flatbuffers
from flatbuffers.compat import import_numpy
np = import_numpy()

class IndividualWheelData(object):
    __slots__ = ['_tab']

    @classmethod
    def GetRootAs(cls, buf, offset=0):
        n = flatbuffers.encode.Get(flatbuffers.packer.uoffset, buf, offset)
        x = IndividualWheelData()
        x.Init(buf, n + offset)
        return x

    @classmethod
    def GetRootAsIndividualWheelData(cls, buf, offset=0):
        """This method is deprecated. Please switch to GetRootAs."""
        return cls.GetRootAs(buf, offset)
    # IndividualWheelData
    def Init(self, buf, pos):
        self._tab = flatbuffers.table.Table(buf, pos)

    # IndividualWheelData
    def Timestamps(self, j):
        o = flatbuffers.number_types.UOffsetTFlags.py_type(self._tab.Offset(4))
        if o != 0:
            a = self._tab.Vector(o)
            return self._tab.Get(flatbuffers.number_types.Int64Flags, a + flatbuffers.number_types.UOffsetTFlags.py_type(j * 8))
        return 0

    # IndividualWheelData
    def TimestampsAsNumpy(self):
        o = flatbuffers.number_types.UOffsetTFlags.py_type(self._tab.Offset(4))
        if o != 0:
            return self._tab.GetVectorAsNumpy(flatbuffers.number_types.Int64Flags, o)
        return 0

    # IndividualWheelData
    def TimestampsLength(self):
        o = flatbuffers.number_types.UOffsetTFlags.py_type(self._tab.Offset(4))
        if o != 0:
            return self._tab.VectorLen(o)
        return 0

    # IndividualWheelData
    def TimestampsIsNone(self):
        o = flatbuffers.number_types.UOffsetTFlags.py_type(self._tab.Offset(4))
        return o == 0

    # IndividualWheelData
    def Counts(self, j):
        o = flatbuffers.number_types.UOffsetTFlags.py_type(self._tab.Offset(6))
        if o != 0:
            a = self._tab.Vector(o)
            return self._tab.Get(flatbuffers.number_types.Int32Flags, a + flatbuffers.number_types.UOffsetTFlags.py_type(j * 4))
        return 0

    # IndividualWheelData
    def CountsAsNumpy(self):
        o = flatbuffers.number_types.UOffsetTFlags.py_type(self._tab.Offset(6))
        if o != 0:
            return self._tab.GetVectorAsNumpy(flatbuffers.number_types.Int32Flags, o)
        return 0

    # IndividualWheelData
    def CountsLength(self):
        o = flatbuffers.number_types.UOffsetTFlags.py_type(self._tab.Offset(6))
        if o != 0:
            return self._tab.VectorLen(o)
        return 0

    # IndividualWheelData
    def CountsIsNone(self):
        o = flatbuffers.number_types.UOffsetTFlags.py_type(self._tab.Offset(6))
        return o == 0

    # IndividualWheelData
    def Distances(self, j):
        o = flatbuffers.number_types.UOffsetTFlags.py_type(self._tab.Offset(8))
        if o != 0:
            a = self._tab.Vector(o)
            return self._tab.Get(flatbuffers.number_types.Float64Flags, a + flatbuffers.number_types.UOffsetTFlags.py_type(j * 8))
        return 0

    # IndividualWheelData
    def DistancesAsNumpy(self):
        o = flatbuffers.number_types.UOffsetTFlags.py_type(self._tab.Offset(8))
        if o != 0:
            return self._tab.GetVectorAsNumpy(flatbuffers.number_types.Float64Flags, o)
        return 0

    # IndividualWheelData
    def DistancesLength(self):
        o = flatbuffers.number_types.UOffsetTFlags.py_type(self._tab.Offset(8))
        if o != 0:
            return self._tab.VectorLen(o)
        return 0

    # IndividualWheelData
    def DistancesIsNone(self):
        o = flatbuffers.number_types.UOffsetTFlags.py_type(self._tab.Offset(8))
        return o == 0

    # IndividualWheelData
    def SpeedsInstantaneous(self, j):
        o = flatbuffers.number_types.UOffsetTFlags.py_type(self._tab.Offset(10))
        if o != 0:
            a = self._tab.Vector(o)
            return self._tab.Get(flatbuffers.number_types.Float64Flags, a + flatbuffers.number_types.UOffsetTFlags.py_type(j * 8))
        return 0

    # IndividualWheelData
    def SpeedsInstantaneousAsNumpy(self):
        o = flatbuffers.number_types.UOffsetTFlags.py_type(self._tab.Offset(10))
        if o != 0:
            return self._tab.GetVectorAsNumpy(flatbuffers.number_types.Float64Flags, o)
        return 0

    # IndividualWheelData
    def SpeedsInstantaneousLength(self):
        o = flatbuffers.number_types.UOffsetTFlags.py_type(self._tab.Offset(10))
        if o != 0:
            return self._tab.VectorLen(o)
        return 0

    # IndividualWheelData
    def SpeedsInstantaneousIsNone(self):
        o = flatbuffers.number_types.UOffsetTFlags.py_type(self._tab.Offset(10))
        return o == 0

    # IndividualWheelData
    def SpeedsBuffered(self, j):
        o = flatbuffers.number_types.UOffsetTFlags.py_type(self._tab.Offset(12))
        if o != 0:
            a = self._tab.Vector(o)
            return self._tab.Get(flatbuffers.number_types.Float64Flags, a + flatbuffers.number_types.UOffsetTFlags.py_type(j * 8))
        return 0

    # IndividualWheelData
    def SpeedsBufferedAsNumpy(self):
        o = flatbuffers.number_types.UOffsetTFlags.py_type(self._tab.Offset(12))
        if o != 0:
            return self._tab.GetVectorAsNumpy(flatbuffers.number_types.Float64Flags, o)
        return 0

    # IndividualWheelData
    def SpeedsBufferedLength(self):
        o = flatbuffers.number_types.UOffsetTFlags.py_type(self._tab.Offset(12))
        if o != 0:
            return self._tab.VectorLen(o)
        return 0

    # IndividualWheelData
    def SpeedsBufferedIsNone(self):
        o = flatbuffers.number_types.UOffsetTFlags.py_type(self._tab.Offset(12))
        return o == 0

    # IndividualWheelData
    def SpeedsExpavg(self, j):
        o = flatbuffers.number_types.UOffsetTFlags.py_type(self._tab.Offset(14))
        if o != 0:
            a = self._tab.Vector(o)
            return self._tab.Get(flatbuffers.number_types.Float64Flags, a + flatbuffers.number_types.UOffsetTFlags.py_type(j * 8))
        return 0

    # IndividualWheelData
    def SpeedsExpavgAsNumpy(self):
        o = flatbuffers.number_types.UOffsetTFlags.py_type(self._tab.Offset(14))
        if o != 0:
            return self._tab.GetVectorAsNumpy(flatbuffers.number_types.Float64Flags, o)
        return 0

    # IndividualWheelData
    def SpeedsExpavgLength(self):
        o = flatbuffers.number_types.UOffsetTFlags.py_type(self._tab.Offset(14))
        if o != 0:
            return self._tab.VectorLen(o)
        return 0

    # IndividualWheelData
    def SpeedsExpavgIsNone(self):
        o = flatbuffers.number_types.UOffsetTFlags.py_type(self._tab.Offset(14))
        return o == 0

def Start(builder): builder.StartObject(6)
def IndividualWheelDataStart(builder):
    """This method is deprecated. Please switch to Start."""
    return Start(builder)
def AddTimestamps(builder, timestamps): builder.PrependUOffsetTRelativeSlot(0, flatbuffers.number_types.UOffsetTFlags.py_type(timestamps), 0)
def IndividualWheelDataAddTimestamps(builder, timestamps):
    """This method is deprecated. Please switch to AddTimestamps."""
    return AddTimestamps(builder, timestamps)
def StartTimestampsVector(builder, numElems): return builder.StartVector(8, numElems, 8)
def IndividualWheelDataStartTimestampsVector(builder, numElems):
    """This method is deprecated. Please switch to Start."""
    return StartTimestampsVector(builder, numElems)
def AddCounts(builder, counts): builder.PrependUOffsetTRelativeSlot(1, flatbuffers.number_types.UOffsetTFlags.py_type(counts), 0)
def IndividualWheelDataAddCounts(builder, counts):
    """This method is deprecated. Please switch to AddCounts."""
    return AddCounts(builder, counts)
def StartCountsVector(builder, numElems): return builder.StartVector(4, numElems, 4)
def IndividualWheelDataStartCountsVector(builder, numElems):
    """This method is deprecated. Please switch to Start."""
    return StartCountsVector(builder, numElems)
def AddDistances(builder, distances): builder.PrependUOffsetTRelativeSlot(2, flatbuffers.number_types.UOffsetTFlags.py_type(distances), 0)
def IndividualWheelDataAddDistances(builder, distances):
    """This method is deprecated. Please switch to AddDistances."""
    return AddDistances(builder, distances)
def StartDistancesVector(builder, numElems): return builder.StartVector(8, numElems, 8)
def IndividualWheelDataStartDistancesVector(builder, numElems):
    """This method is deprecated. Please switch to Start."""
    return StartDistancesVector(builder, numElems)
def AddSpeedsInstantaneous(builder, speedsInstantaneous): builder.PrependUOffsetTRelativeSlot(3, flatbuffers.number_types.UOffsetTFlags.py_type(speedsInstantaneous), 0)
def IndividualWheelDataAddSpeedsInstantaneous(builder, speedsInstantaneous):
    """This method is deprecated. Please switch to AddSpeedsInstantaneous."""
    return AddSpeedsInstantaneous(builder, speedsInstantaneous)
def StartSpeedsInstantaneousVector(builder, numElems): return builder.StartVector(8, numElems, 8)
def IndividualWheelDataStartSpeedsInstantaneousVector(builder, numElems):
    """This method is deprecated. Please switch to Start."""
    return StartSpeedsInstantaneousVector(builder, numElems)
def AddSpeedsBuffered(builder, speedsBuffered): builder.PrependUOffsetTRelativeSlot(4, flatbuffers.number_types.UOffsetTFlags.py_type(speedsBuffered), 0)
def IndividualWheelDataAddSpeedsBuffered(builder, speedsBuffered):
    """This method is deprecated. Please switch to AddSpeedsBuffered."""
    return AddSpeedsBuffered(builder, speedsBuffered)
def StartSpeedsBufferedVector(builder, numElems): return builder.StartVector(8, numElems, 8)
def IndividualWheelDataStartSpeedsBufferedVector(builder, numElems):
    """This method is deprecated. Please switch to Start."""
    return StartSpeedsBufferedVector(builder, numElems)
def AddSpeedsExpavg(builder, speedsExpavg): builder.PrependUOffsetTRelativeSlot(5, flatbuffers.number_types.UOffsetTFlags.py_type(speedsExpavg), 0)
def IndividualWheelDataAddSpeedsExpavg(builder, speedsExpavg):
    """This method is deprecated. Please switch to AddSpeedsExpavg."""
    return AddSpeedsExpavg(builder, speedsExpavg)
def StartSpeedsExpavgVector(builder, numElems): return builder.StartVector(8, numElems, 8)
def IndividualWheelDataStartSpeedsExpavgVector(builder, numElems):
    """This method is deprecated. Please switch to Start."""
    return StartSpeedsExpavgVector(builder, numElems)
def End(builder): return builder.EndObject()
def IndividualWheelDataEnd(builder):
    """This method is deprecated. Please switch to End."""
    return End(builder)