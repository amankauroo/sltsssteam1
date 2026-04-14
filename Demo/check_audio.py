import pyaudio

p = pyaudio.PyAudio()
info = p.get_default_input_device_info()
print("Default input:", info["name"], "- index:", info["index"])
print()
print("All input devices:")
for i in range(p.get_device_count()):
    d = p.get_device_info_by_index(i)
    if d["maxInputChannels"] > 0:
        print(f"  [{i}] {d['name']} (inputs: {d['maxInputChannels']})")
p.terminate()
