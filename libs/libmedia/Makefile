include $(BASE_DIR)/common.mk

SRCS := \
    AudioTrack.cpp \
    AudioTrackShared.cpp \
    IAudioFlinger.cpp \
    IAudioFlingerClient.cpp \
    IAudioTrack.cpp \
    IAudioRecord.cpp \
    AudioRecord.cpp \
    AudioParameter.cpp \
    AudioSystem.cpp \
    IMediaPlayerService.cpp \
    IMediaPlayerClient.cpp \
    IMediaRecorderClient.cpp \
    IMediaPlayer.cpp \
    IStreamSource.cpp \
    Metadata.cpp \
    ToneGenerator.cpp \
    IOMX.cpp \
    IAudioPolicyService.cpp \
    autodetect.cpp \
    IMediaDeathNotifier.cpp \
    IEffect.cpp \
    IEffectClient.cpp \
    AudioEffect.cpp \
    Visualizer.cpp \
    MemoryLeakTrackUtil.cpp \
    SoundPoolThread.cpp \
    SoundPool.cpp

OBJS = $(patsubst %.cpp,%.o, $(SRCS))

TARGET = $(BASE_DIR)/libmedia.so

.PHONY: all clean $(TARGET)

all: print $(TARGET)

%.o : %.cpp
	@echo Compiling $<
	@$(CXX) $(CFLAGS) -c -o $@ $<

%.o : %.c
	@echo Compiling $<
	@$(CC) $(CFLAGS) -c -o $@ $<

$(TARGET): $(OBJS) 
	@echo Building executable files for $(TARGET)
	$(CXX) $(CFLAGS) $(LDFLAGS) -shared -fpic -o $(TARGET) $(OBJS)
	@echo "Successfully built $@"

print:
	@echo "****************************************************"
	@echo "*** Start building speex resampler               ***"
	@echo "****************************************************"

clean:
	@echo Cleaning up previous object files
	@rm -f $(TARGET) $(OBJS)

