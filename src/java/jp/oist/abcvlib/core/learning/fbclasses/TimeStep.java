// automatically generated by the FlatBuffers compiler, do not modify

package jp.oist.abcvlib.core.learning.fbclasses;

import java.nio.*;
import java.lang.*;
import java.util.*;
import com.google.flatbuffers.*;

@SuppressWarnings("unused")
public final class TimeStep extends Table {
  public static void ValidateVersion() { Constants.FLATBUFFERS_1_12_0(); }
  public static TimeStep getRootAsTimeStep(ByteBuffer _bb) { return getRootAsTimeStep(_bb, new TimeStep()); }
  public static TimeStep getRootAsTimeStep(ByteBuffer _bb, TimeStep obj) { _bb.order(ByteOrder.LITTLE_ENDIAN); return (obj.__assign(_bb.getInt(_bb.position()) + _bb.position(), _bb)); }
  public void __init(int _i, ByteBuffer _bb) { __reset(_i, _bb); }
  public TimeStep __assign(int _i, ByteBuffer _bb) { __init(_i, _bb); return this; }

  public jp.oist.abcvlib.core.learning.fbclasses.WheelData wheelData() { return wheelData(new jp.oist.abcvlib.core.learning.fbclasses.WheelData()); }
  public jp.oist.abcvlib.core.learning.fbclasses.WheelData wheelData(jp.oist.abcvlib.core.learning.fbclasses.WheelData obj) { int o = __offset(4); return o != 0 ? obj.__assign(__indirect(o + bb_pos), bb) : null; }
  public jp.oist.abcvlib.core.learning.fbclasses.OrientationData orientationData() { return orientationData(new jp.oist.abcvlib.core.learning.fbclasses.OrientationData()); }
  public jp.oist.abcvlib.core.learning.fbclasses.OrientationData orientationData(jp.oist.abcvlib.core.learning.fbclasses.OrientationData obj) { int o = __offset(6); return o != 0 ? obj.__assign(__indirect(o + bb_pos), bb) : null; }
  public jp.oist.abcvlib.core.learning.fbclasses.ChargerData chargerData() { return chargerData(new jp.oist.abcvlib.core.learning.fbclasses.ChargerData()); }
  public jp.oist.abcvlib.core.learning.fbclasses.ChargerData chargerData(jp.oist.abcvlib.core.learning.fbclasses.ChargerData obj) { int o = __offset(8); return o != 0 ? obj.__assign(__indirect(o + bb_pos), bb) : null; }
  public jp.oist.abcvlib.core.learning.fbclasses.BatteryData batteryData() { return batteryData(new jp.oist.abcvlib.core.learning.fbclasses.BatteryData()); }
  public jp.oist.abcvlib.core.learning.fbclasses.BatteryData batteryData(jp.oist.abcvlib.core.learning.fbclasses.BatteryData obj) { int o = __offset(10); return o != 0 ? obj.__assign(__indirect(o + bb_pos), bb) : null; }
  public jp.oist.abcvlib.core.learning.fbclasses.ImageData imageData() { return imageData(new jp.oist.abcvlib.core.learning.fbclasses.ImageData()); }
  public jp.oist.abcvlib.core.learning.fbclasses.ImageData imageData(jp.oist.abcvlib.core.learning.fbclasses.ImageData obj) { int o = __offset(12); return o != 0 ? obj.__assign(__indirect(o + bb_pos), bb) : null; }
  public jp.oist.abcvlib.core.learning.fbclasses.SoundData soundData() { return soundData(new jp.oist.abcvlib.core.learning.fbclasses.SoundData()); }
  public jp.oist.abcvlib.core.learning.fbclasses.SoundData soundData(jp.oist.abcvlib.core.learning.fbclasses.SoundData obj) { int o = __offset(14); return o != 0 ? obj.__assign(__indirect(o + bb_pos), bb) : null; }
  public jp.oist.abcvlib.core.learning.fbclasses.RobotAction actions() { return actions(new jp.oist.abcvlib.core.learning.fbclasses.RobotAction()); }
  public jp.oist.abcvlib.core.learning.fbclasses.RobotAction actions(jp.oist.abcvlib.core.learning.fbclasses.RobotAction obj) { int o = __offset(16); return o != 0 ? obj.__assign(__indirect(o + bb_pos), bb) : null; }

  public static int createTimeStep(FlatBufferBuilder builder,
      int wheel_dataOffset,
      int orientation_dataOffset,
      int charger_dataOffset,
      int battery_dataOffset,
      int image_dataOffset,
      int sound_dataOffset,
      int actionsOffset) {
    builder.startTable(7);
    TimeStep.addActions(builder, actionsOffset);
    TimeStep.addSoundData(builder, sound_dataOffset);
    TimeStep.addImageData(builder, image_dataOffset);
    TimeStep.addBatteryData(builder, battery_dataOffset);
    TimeStep.addChargerData(builder, charger_dataOffset);
    TimeStep.addOrientationData(builder, orientation_dataOffset);
    TimeStep.addWheelData(builder, wheel_dataOffset);
    return TimeStep.endTimeStep(builder);
  }

  public static void startTimeStep(FlatBufferBuilder builder) { builder.startTable(7); }
  public static void addWheelData(FlatBufferBuilder builder, int wheelDataOffset) { builder.addOffset(0, wheelDataOffset, 0); }
  public static void addOrientationData(FlatBufferBuilder builder, int orientationDataOffset) { builder.addOffset(1, orientationDataOffset, 0); }
  public static void addChargerData(FlatBufferBuilder builder, int chargerDataOffset) { builder.addOffset(2, chargerDataOffset, 0); }
  public static void addBatteryData(FlatBufferBuilder builder, int batteryDataOffset) { builder.addOffset(3, batteryDataOffset, 0); }
  public static void addImageData(FlatBufferBuilder builder, int imageDataOffset) { builder.addOffset(4, imageDataOffset, 0); }
  public static void addSoundData(FlatBufferBuilder builder, int soundDataOffset) { builder.addOffset(5, soundDataOffset, 0); }
  public static void addActions(FlatBufferBuilder builder, int actionsOffset) { builder.addOffset(6, actionsOffset, 0); }
  public static int endTimeStep(FlatBufferBuilder builder) {
    int o = builder.endTable();
    return o;
  }

  public static final class Vector extends BaseVector {
    public Vector __assign(int _vector, int _element_size, ByteBuffer _bb) { __reset(_vector, _element_size, _bb); return this; }

    public TimeStep get(int j) { return get(new TimeStep(), j); }
    public TimeStep get(TimeStep obj, int j) {  return obj.__assign(__indirect(__element(j), bb), bb); }
  }
}

