# automatically generated by the FlatBuffers compiler, do not modify

# namespace: fbclasses

import flatbuffers
from flatbuffers.compat import import_numpy
np = import_numpy()

class SoundData(object):
    __slots__ = ['_tab']

    @classmethod
    def GetRootAs(cls, buf, offset=0):
        n = flatbuffers.encode.Get(flatbuffers.packer.uoffset, buf, offset)
        x = SoundData()
        x.Init(buf, n + offset)
        return x

    @classmethod
    def GetRootAsSoundData(cls, buf, offset=0):
        """This method is deprecated. Please switch to GetRootAs."""
        return cls.GetRootAs(buf, offset)
    # SoundData
    def Init(self, buf, pos):
        self._tab = flatbuffers.table.Table(buf, pos)

    # SoundData
    def StartTime(self):
        o = flatbuffers.number_types.UOffsetTFlags.py_type(self._tab.Offset(4))
        if o != 0:
            x = self._tab.Indirect(o + self._tab.Pos)
            from jp.oist.abcvlib.core.learning.fbclasses.AudioTimestamp import AudioTimestamp
            obj = AudioTimestamp()
            obj.Init(self._tab.Bytes, x)
            return obj
        return None

    # SoundData
    def EndTime(self):
        o = flatbuffers.number_types.UOffsetTFlags.py_type(self._tab.Offset(6))
        if o != 0:
            x = self._tab.Indirect(o + self._tab.Pos)
            from jp.oist.abcvlib.core.learning.fbclasses.AudioTimestamp import AudioTimestamp
            obj = AudioTimestamp()
            obj.Init(self._tab.Bytes, x)
            return obj
        return None

    # SoundData
    def TotalTime(self):
        o = flatbuffers.number_types.UOffsetTFlags.py_type(self._tab.Offset(8))
        if o != 0:
            return self._tab.Get(flatbuffers.number_types.Float64Flags, o + self._tab.Pos)
        return 0.0

    # SoundData
    def SampleRate(self):
        o = flatbuffers.number_types.UOffsetTFlags.py_type(self._tab.Offset(10))
        if o != 0:
            return self._tab.Get(flatbuffers.number_types.Int32Flags, o + self._tab.Pos)
        return 0

    # SoundData
    def TotalSamples(self):
        o = flatbuffers.number_types.UOffsetTFlags.py_type(self._tab.Offset(12))
        if o != 0:
            return self._tab.Get(flatbuffers.number_types.Int64Flags, o + self._tab.Pos)
        return 0

    # SoundData
    def Levels(self, j):
        o = flatbuffers.number_types.UOffsetTFlags.py_type(self._tab.Offset(14))
        if o != 0:
            a = self._tab.Vector(o)
            return self._tab.Get(flatbuffers.number_types.Float32Flags, a + flatbuffers.number_types.UOffsetTFlags.py_type(j * 4))
        return 0

    # SoundData
    def LevelsAsNumpy(self):
        o = flatbuffers.number_types.UOffsetTFlags.py_type(self._tab.Offset(14))
        if o != 0:
            return self._tab.GetVectorAsNumpy(flatbuffers.number_types.Float32Flags, o)
        return 0

    # SoundData
    def LevelsLength(self):
        o = flatbuffers.number_types.UOffsetTFlags.py_type(self._tab.Offset(14))
        if o != 0:
            return self._tab.VectorLen(o)
        return 0

    # SoundData
    def LevelsIsNone(self):
        o = flatbuffers.number_types.UOffsetTFlags.py_type(self._tab.Offset(14))
        return o == 0

def Start(builder): builder.StartObject(6)
def SoundDataStart(builder):
    """This method is deprecated. Please switch to Start."""
    return Start(builder)
def AddStartTime(builder, startTime): builder.PrependUOffsetTRelativeSlot(0, flatbuffers.number_types.UOffsetTFlags.py_type(startTime), 0)
def SoundDataAddStartTime(builder, startTime):
    """This method is deprecated. Please switch to AddStartTime."""
    return AddStartTime(builder, startTime)
def AddEndTime(builder, endTime): builder.PrependUOffsetTRelativeSlot(1, flatbuffers.number_types.UOffsetTFlags.py_type(endTime), 0)
def SoundDataAddEndTime(builder, endTime):
    """This method is deprecated. Please switch to AddEndTime."""
    return AddEndTime(builder, endTime)
def AddTotalTime(builder, totalTime): builder.PrependFloat64Slot(2, totalTime, 0.0)
def SoundDataAddTotalTime(builder, totalTime):
    """This method is deprecated. Please switch to AddTotalTime."""
    return AddTotalTime(builder, totalTime)
def AddSampleRate(builder, sampleRate): builder.PrependInt32Slot(3, sampleRate, 0)
def SoundDataAddSampleRate(builder, sampleRate):
    """This method is deprecated. Please switch to AddSampleRate."""
    return AddSampleRate(builder, sampleRate)
def AddTotalSamples(builder, totalSamples): builder.PrependInt64Slot(4, totalSamples, 0)
def SoundDataAddTotalSamples(builder, totalSamples):
    """This method is deprecated. Please switch to AddTotalSamples."""
    return AddTotalSamples(builder, totalSamples)
def AddLevels(builder, levels): builder.PrependUOffsetTRelativeSlot(5, flatbuffers.number_types.UOffsetTFlags.py_type(levels), 0)
def SoundDataAddLevels(builder, levels):
    """This method is deprecated. Please switch to AddLevels."""
    return AddLevels(builder, levels)
def StartLevelsVector(builder, numElems): return builder.StartVector(4, numElems, 4)
def SoundDataStartLevelsVector(builder, numElems):
    """This method is deprecated. Please switch to Start."""
    return StartLevelsVector(builder, numElems)
def End(builder): return builder.EndObject()
def SoundDataEnd(builder):
    """This method is deprecated. Please switch to End."""
    return End(builder)