import wave
import json
from vosk import Model, KaldiRecognizer

# Load Vosk model
model = Model("models/vosk-model-small-en-us-0.15")

# Open WAV file
wf = wave.open("recordings/sample.wav", "rb")

# Create recognizer
rec = KaldiRecognizer(model, wf.getframerate())

print("Processing audio...\n")

while True:
    data = wf.readframes(4000)

    if len(data) == 0:
        break

    if rec.AcceptWaveform(data):
        result = json.loads(rec.Result())
        print(result.get("text", ""))

final_result = json.loads(rec.FinalResult())

print("\nFinal Text:")
print(final_result.get("text", ""))