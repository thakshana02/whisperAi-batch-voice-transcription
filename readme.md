# Whisper AI Batch Voice Transcription

A high-performance batch transcription system powered by OpenAI's Whisper model with GPU acceleration. Designed for processing multiple audio files efficiently while preserving authentic speech patterns and nuances.

## Features

- **GPU Acceleration**: Optimized for NVIDIA GPUs (RTX series recommended)
- **Batch Processing**: Transcribe multiple audio files in one operation
- **High Accuracy**: Uses Whisper's large model for maximum transcription quality
- **Multiple Formats**: Supports WAV, MP3, M4A, FLAC, and other common audio formats
- **Organized Output**: Clean file structure with separate folders for audio and transcripts
- **Progress Tracking**: Real-time feedback during batch processing
- **Error Handling**: Robust processing with detailed error reporting

## Requirements

- Python 3.8+
- NVIDIA GPU with CUDA support (recommended for speed)
- FFmpeg (for audio processing)
- 4GB+ available disk space for models

## Installation

1. **Clone the repository**
   ```bash
   git clone https://github.com/thakshana02/whisperAi-batch-voice-transcription.git
   cd whisperAi-batch-voice-transcription
   ```

2. **Create virtual environment**
   ```bash
   python -m venv venv
   # Windows
   .\venv\Scripts\Activate.ps1
   # Linux/Mac
   source venv/bin/activate
   ```

3. **Install dependencies**
   ```bash
   # Install PyTorch with CUDA support
   pip install torch torchvision torchaudio --index-url https://download.pytorch.org/whl/cu118
   
   # Install Whisper
   pip install openai-whisper
   ```

4. **Install FFmpeg**
   - Download from [FFmpeg website](https://ffmpeg.org/download.html)
   - Add to system PATH
   - Verify with `ffmpeg -version`

## Usage

### Quick Start

1. **Place audio files** in the `audio/` directory or create subdirectories
2. **Run batch transcription**:
   ```bash
   python batch_transcribe.py
   ```
3. **Find transcripts** in the `transcripts/` folder

### Command Line Alternative

For direct Whisper usage:
```bash
# Single file
whisper "audio/audio_file.wav" --model large --device cuda --output_dir transcripts

# Batch processing
whisper "audio/*.wav" --model large --device cuda --output_dir transcripts --language en
```

### Customization

Edit `batch_transcribe.py` to modify:
- **Model size**: Change `"large"` to `"medium"` or `"small"` for faster processing
- **Language**: Specify language for better accuracy
- **Output format**: Add SRT, VTT, or other subtitle formats
- **Quality settings**: Adjust `fp16` and other parameters

## Project Structure

```
whisperAi-batch-voice-transcription/
├── audio/                          # Place audio files here
│   ├── sampleAudio/               # Sample files (tracked in git)
│   └── [audio-folders]/            # audio files (ignored by git)
├── transcripts/                    # Generated transcriptions
│   ├── sampleTranscript/          # Sample outputs (tracked in git)
│   └── [generated-files]/         # transcripts (ignored by git)
├── batch_transcribe.py            # Main batch processing script
├── .gitignore                     # Protects audio files
└── README.md                      # This file
```

## Performance

**Expected processing speeds** (RTX 3080 Ti):
- **Large model**: ~15-25x real-time speed
- **Medium model**: ~30-50x real-time speed
- **Small model**: ~50-100x real-time speed

**1 hour of audio** typically processes in 2-4 minutes with GPU acceleration.

## Configuration Options

### Model Sizes
- **Large**: Best accuracy, slower processing
- **Medium**: Good balance of speed and accuracy
- **Small**: Fastest, lower accuracy

### Language Support
Whisper supports 99+ languages. Specify language for better accuracy:
```python
result = model.transcribe(audio_path, language="en")  # English
result = model.transcribe(audio_path, language="es")  # Spanish
```

## Privacy & Security

- Audio files are processed locally on machine
- No data is sent to external services
- `.gitignore` configured to prevent accidental upload of audio files
- Only sample files and code are tracked in version control

## Troubleshooting

### Common Issues

**GPU not detected**:
```bash
python -c "import torch; print(torch.cuda.is_available())"
```

**FFmpeg not found**:
- Ensure FFmpeg is installed and in system PATH
- Restart terminal after installation

**Out of memory**:
- Use smaller model (`medium` or `small`)
- Process files individually instead of batch
- Reduce `fp16` to `False`

**Slow processing**:
- Verify GPU acceleration: `--device cuda`
- Check CUDA installation
- Monitor GPU usage with `nvidia-smi`

## Contributing

1. Fork the repository
2. Create a feature branch
3. Make changes
4. Test with sample audio files
5. Submit a pull request

## License

This project is open source. Please check the license file for details.

## Acknowledgments

- [OpenAI Whisper](https://github.com/openai/whisper) for the incredible transcription model
- [PyTorch](https://pytorch.org/) for GPU acceleration framework
- [FFmpeg](https://ffmpeg.org/) for audio processing capabilities

---

**Note**: This tool is designed for legitimate transcription purposes. Please respect copyright and privacy laws when processing audio content.