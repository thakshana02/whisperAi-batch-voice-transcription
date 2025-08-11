import whisper
import os
import glob
from pathlib import Path

def transcribe_batch():
    # Load the large model (best accuracy for capturing exact speech patterns)
    print("Loading Whisper large model...")
    model = whisper.load_model("large")
    
    # Set up paths
    audio_folder = "audio/New Set - Manual Clone Prep"
    output_folder = "transcripts/New Set - Manual Clone Prep"
    
    # Create output folder if it doesn't exist
    os.makedirs(output_folder, exist_ok=True)
    
    # Find all audio files
    audio_files = glob.glob(f"{audio_folder}/*.wav") + glob.glob(f"{audio_folder}/*.WAV")
    
    if not audio_files:
        print(f"No audio files found in {audio_folder}")
        return
    
    print(f"Found {len(audio_files)} audio files to transcribe")
    print("Using GPU acceleration with your RTX 3080 Ti")
    print("-" * 50)
    
    # Process each file
    for i, audio_path in enumerate(audio_files, 1):
        filename = Path(audio_path).stem
        print(f"[{i}/{len(audio_files)}] Processing: {filename}")
        
        try:
            # Transcribe with GPU acceleration
            result = model.transcribe(
                audio_path,
                language="en",  # Specify English for better accuracy
                task="transcribe",
                fp16=True,  # Use half precision for faster processing
                verbose=False
            )
            
            # Save transcript
            output_path = f"{output_folder}/{filename}.txt"
            with open(output_path, "w", encoding="utf-8") as f:
                f.write(result["text"].strip())
            
            print(f"   ✓ Saved: {output_path}")
            print(f"   Preview: {result['text'][:100]}...")
            print()
            
        except Exception as e:
            print(f"   ✗ Error processing {filename}: {str(e)}")
            print()
    
    print("Batch transcription complete!")
    print(f"All transcripts saved in '{output_folder}/' folder")

if __name__ == "__main__":
    transcribe_batch()