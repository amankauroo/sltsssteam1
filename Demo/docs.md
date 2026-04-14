# Blind Spectacles - Documentation

## Table of Contents

1. [Overview](#overview)
2. [What This Program Does](#what-this-program-does)
3. [How It Works](#how-it-works)
4. [Setup Instructions](#setup-instructions)
5. [How to Use It](#how-to-use-it)
6. [Understanding the Code](#understanding-the-code)
7. [Key Concepts Explained](#key-concepts-explained)
8. [Troubleshooting](#troubleshooting)

---

## Overview

**Blind Spectacles** is a real-time AI assistant that combines vision and speech. It's like having a smart companion that can:

- 👁️ **See** what your camera sees
- 👂 **Hear** what you say through your microphone
- 🗣️ **Speak back** to you with natural-sounding voice

The program uses Google's Gemini AI to understand everything it sees and hears, then responds with helpful spoken answers.

---

## What This Program Does

### Simple Explanation

Imagine wearing smart glasses that can see and talk to you. That's what this program does, but on your computer:

1. Your **camera** shows things to the AI
2. Your **microphone** lets you talk to the AI
3. The AI **thinks** about what it sees and hears
4. The AI **speaks back** through your speakers

### Real-World Examples

**Example 1: Reading Helper**

- Point your camera at a book
- Ask: "What does this page say?"
- The AI reads the text aloud to you

**Example 2: Learning Assistant**

- Show the AI a diagram or chart
- Ask: "Can you explain what this shows?"
- The AI describes and explains what it sees

---

## How It Works

### The Big Picture

```
┌─────────────┐       ┌──────────────┐       ┌─────────────┐
│   Camera    │──────▶│              │──────▶│  Speakers   │
│             │       │   Gemini AI  │       │             │
│             │       │   (Google)   │       │ (AI talks)  │
└─────────────┘       │              │       └─────────────┘
                      │              │
┌─────────────┐       │              │
│ Microphone  │──────▶│              │
│             │       └──────────────┘
│ (You talk)  │
└─────────────┘
```

### Step-by-Step Process

1. **Capture Video**: Every 0.8 seconds, the program takes a picture from your camera
2. **Record Audio**: Continuously records your voice in small chunks
3. **Send to AI**: Both video and audio are sent to Google's Gemini AI over the internet
4. **AI Processing**: The AI analyzes what it sees and hears
5. **Generate Response**: The AI creates a spoken answer
6. **Play Audio**: The response comes through your speakers

### Why It's Called "Real-Time"

"Real-time" means everything happens almost instantly. There's no waiting around - you speak, the AI hears and sees, and responds right away (usually within 1-2 seconds).

---

## Setup Instructions

### Requirements

You need:

- A computer with **Windows, Mac, or Linux**
- A **webcam** (if you want video)
- A **microphone** (required for talking to the AI)
- **Speakers or headphones** (to hear the AI)
- **Internet connection** (to connect to Google's AI)
- **Python 3.10 or newer** installed

### Installation Steps

**Step 1: Open a Terminal or Command Prompt**

**Step 2: Install Required Packages**

```bash
pip install google-genai opencv-python pyaudio pillow
```

These packages are:

- `google-genai` - Connects to Google's AI
- `opencv-python` - Captures video from your camera
- `pyaudio` - Records and plays audio
- `pillow` - Processes images

**Step 3: Get a Google API Key**

1. Go to [Google AI Studio](https://aistudio.google.com/)
2. Create a new API key
3. **Replace the API key in the code** (line 109) with your own key

⚠️ **Important**: The API key in the code should be kept private! Don't share it with others.

---

## How to Use It

### Basic Usage

**Start the program with camera:**

```bash
python main.py
```

**Start with audio only (no video):**

```bash
python main.py --mode none
```

### Custom Settings

**Change how often pictures are sent** (in seconds):

```bash
python main.py --interval 2.0
```

- Lower number (like `0.5`) = more pictures = AI sees more, but uses more internet
- Higher number (like `2.0`) = fewer pictures = AI sees less, but saves internet

### While Running

- **Talk naturally** - Just speak into your microphone. The AI will hear you.
- **Type messages** - You can also type at the `message >` prompt and press Enter
- **Quit** - Type `q` and press Enter to exit

---

## Understanding the Code

### Main Parts of the Program

The code is organized into clear sections:

#### 1. **Imports** (Lines 35-50)

These are the tools the program needs to work:

- `asyncio` - Runs many tasks at the same time
- `cv2` - Captures video from camera
- `pyaudio` - Records and plays audio
- `PIL.Image` - Processes pictures
- `google.genai` - Connects to Google's AI

#### 2. **Settings** (Lines 52-145)

Configuration values that control how the program works:

**Audio Settings:**

- `SEND_SAMPLE_RATE = 16000` - Record voice at 16,000 samples per second (good quality for speech)
- `RECEIVE_SAMPLE_RATE = 24000` - Play AI voice at 24,000 samples per second (higher quality)
- `CHUNK_SIZE = 512` - Process audio in small chunks for fast response

**Video Settings:**

- `DEFAULT_MODE = "camera"` - Use webcam by default
- `FRAME_INTERVAL = 0.8` - Send a picture every 0.8 seconds

**AI Configuration:**

- `MODEL` - Which AI model to use (Gemini 2.5 Flash)
- `CONFIG` - How the AI should behave (use audio responses, voice "Zephyr", etc.)

#### 3. **AudioLoop Class** (Lines 147-550)

This is the main "brain" of the program. It's a class that manages everything.

**Key Methods:**

| Method            | What It Does                                      |
| ----------------- | ------------------------------------------------- |
| `__init__()`      | Sets up all the variables when the program starts |
| `send_text()`     | Lets you type messages to the AI                  |
| `_get_frame()`    | Captures one picture from the camera              |
| `get_frames()`    | Continuously captures pictures from the camera    |
| `send_audio()`    | Sends your voice to the AI                        |
| `send_video()`    | Sends pictures to the AI                          |
| `listen_audio()`  | Records from your microphone                      |
| `receive_audio()` | Gets the AI's response                            |
| `play_audio()`    | Plays the AI's voice through speakers             |
| `run()`           | Starts everything and keeps it running            |

#### 4. **Program Entry Point** (Lines 552-600)

This is where the program actually starts when you run it. It:

- Reads command-line arguments (`--mode`, `--interval`)
- Creates an `AudioLoop` object
- Starts the main loop

---

## Key Concepts Explained

### What is "Async" and "Await"?

You'll see `async` and `await` throughout the code. Here's what they mean:

**Without Async (Normal Code):**

```
Task 1: Start → Wait → Finish
                ↓
Task 2:     Start → Wait → Finish
```

Tasks run one at a time. If Task 1 is waiting, everything stops.

**With Async:**

```
Task 1: Start → Wait → Finish
         ↓
Task 2: Start → Wait → Finish
         ↓
Task 3: Start → Wait → Finish
```

Many tasks run "at the same time". While one waits, others keep working.

**Why This Matters:**
Our program does many things at once:

- Recording your voice
- Sending audio to AI
- Capturing pictures
- Sending pictures to AI
- Receiving AI's response
- Playing AI's voice

Without async, the program would freeze. With async, everything flows smoothly.

### What are "Queues"?

A queue is like a line at a store. Data goes in one end and comes out the other, in order.

```
IN →  [1] [2] [3] [4]  → OUT
      ↑              ↑
     Put            Get
```

**The Program Uses 3 Queues:**

1. **audio_out_queue**: Your voice waiting to be sent to AI
2. **video_out_queue**: Pictures waiting to be sent to AI
3. **audio_in_queue**: AI's voice waiting to be played

**Why Queues?**

- They handle timing differences (recording happens faster than sending)
- They prevent data loss
- They keep everything organized

### What is Base64 Encoding?

Pictures are made of pixels (dots of color). But we need to send them over the internet as text.

**Base64** converts binary data (pictures) into text:

```
Picture (binary) → Base64 → Text string
                            ↓
                   Can be sent over internet
```

**Example:**

- Original: A red pixel (binary: `11111111 00000000 00000000`)
- Base64: `/wAA` (text that represents the same data)

The AI receives the text and converts it back to a picture.

### What is a "Session"?

A **session** is an active connection to the AI. Think of it like a phone call:

- You dial → Connection opens (session starts)
- You talk back and forth
- You hang up → Connection closes (session ends)

In the code:

```python
async with client.aio.live.connect(model=MODEL, config=CONFIG) as session:
```

This line creates the connection (dials the AI). The `session` variable represents this active connection.

### What is PCM Audio?

**PCM** (Pulse Code Modulation) is the simplest form of digital audio - just raw sound data.

Think of it like this:

- **Analog sound** (real world): A continuous wave of air pressure
- **Digital PCM**: Thousands of measurements of that wave per second

When we record at 16,000 Hz, we take 16,000 measurements every second. Each measurement is a number representing how loud the sound is at that exact moment.

### What is MIME Type?

**MIME type** is like a label that says "what kind of data this is."

Examples:

- `image/jpeg` - "This is a JPEG picture"
- `audio/pcm` - "This is raw audio data"
- `text/plain` - "This is plain text"

The AI needs to know the MIME type so it knows how to process the data.

---

## Troubleshooting

### Common Problems and Solutions

#### Problem: "No module named 'google'"

**Solution:** Install the required packages:

```bash
pip install google-genai
```

#### Problem: "Could not open audio device"

**Solution:**

- Make sure your microphone is connected
- On Windows: Check Settings → Privacy → Microphone permissions
- On Mac: Check System Preferences → Security & Privacy → Microphone
- Try closing other programs that might be using the microphone

#### Problem: "Camera not found" or black screen

**Solution:**

- Make sure your camera is connected
- Close other programs using the camera (Zoom, Skype, etc.)
- Try using audio-only mode: `python main.py --mode none`

#### Problem: "Connection issue" messages keep appearing

**Solution:**

- Check your internet connection
- The API key might be invalid - get a new one from Google AI Studio
- Google's servers might be temporarily down - wait a few minutes

#### Problem: AI responds very slowly

**Solution:**

- Increase the frame interval: `--interval 2.0` (sends fewer pictures)
- Use `--mode none` for audio-only (faster)
- Check your internet speed - slow connections cause delays

#### Problem: Audio is choppy or breaking up

**Solution:**

- Close other programs using lots of internet
- The AI might be processing - wait a moment
- Try increasing CHUNK_SIZE in the code (line 69) to 1024

#### Problem: Program crashes with "QueueFull" error

**Solution:** This shouldn't happen (the code handles it), but if it does:

- Restart the program
- Use a slower frame interval: `--interval 1.5`

### How to Report Issues

If you encounter problems:

1. Note what you were doing when it happened
2. Copy any error messages shown
3. Check if the problem happens every time or just sometimes
4. Try the solutions above first

---

## Technical Details (For Advanced Users)

### Data Flow Diagram

```
┌─────────────────────────────────────────────────────────────┐
│                      AudioLoop Class                        │
├─────────────────────────────────────────────────────────────┤
│                                                             │
│  ┌──────────────┐      ┌──────────────┐                   │
│  │ listen_audio │─────▶│audio_out_queue│─────┐            │
│  └──────────────┘      └──────────────┘      │            │
│                                                ▼            │
│  ┌──────────────┐      ┌──────────────┐  ┌─────────────┐ │
│  │  get_frames  │─────▶│video_out_queue│─▶│ send_audio  │─┼──▶ Gemini AI
│  │      or      │      └──────────────┘  │ send_video  │ │
│  │  get_screen  │                         └─────────────┘ │
│  └──────────────┘                                ▲         │
│                                                   │         │
│  ┌──────────────┐      ┌──────────────┐         │         │
│  │ receive_audio│◀─────│audio_in_queue │◀────────┘         │
│  └──────┬───────┘      └──────────────┘                    │
│         │                                                   │
│         ▼                                                   │
│  ┌──────────────┐                                          │
│  │  play_audio  │                                          │
│  └──────────────┘                                          │
│                                                             │
└─────────────────────────────────────────────────────────────┘
```

### Performance Considerations

**CPU Usage:**

- Video capture: ~5-15% CPU
- Audio processing: ~1-5% CPU
- Image encoding: ~5-10% CPU per frame

**Memory Usage:**

- Base program: ~50-100 MB
- With video: +20-50 MB (depends on resolution)
- Queue buffers: ~5-10 MB

**Network Bandwidth:**

- Audio: ~32 KB/s (constant)
- Video (0.8s interval): ~20-50 KB/s average
- Total: ~50-100 KB/s typical

**Latency (Response Time):**

- Microphone → AI: ~50-100ms
- AI processing: ~500-1500ms (depends on complexity)
- AI → Speakers: ~50-100ms
- **Total: 1-2 seconds** typical

### Security Notes

⚠️ **API Key Security:**
The API key in the code (line 109) should be kept secret:

- Don't share your code with the API key in it
- Don't commit it to public GitHub repositories
- Consider using environment variables instead:

```python
import os
api_key = os.environ.get('GEMINI_API_KEY')
client = genai.Client(api_key=api_key)
```

⚠️ **Privacy:**

- All audio and video is sent to Google's servers
- Conversations may be logged by Google for service improvement
- Don't share sensitive or private information

---

## Additional Resources

### Learning More

**About Async Programming in Python:**

- Python's official asyncio documentation
- Real Python's asyncio tutorial

**About Audio Processing:**

- PyAudio documentation
- Understanding PCM audio format

**About Google's Gemini AI:**

- Google AI Studio documentation
- Gemini API reference

### Project Ideas

Once you understand the code, try these modifications:

1. **Add a wake word** - Only start listening when you say "Hey Gemini"
2. **Save conversations** - Write what you say and what the AI says to a file
3. **Add subtitles** - Show what the AI says as text on screen
4. **Multiple languages** - Add translation features
5. **Custom voice** - Change which AI voice is used
6. **Background noise reduction** - Improve audio quality

---

## Summary

**Blind Spectacles** is a powerful tool that combines:

- Real-time video/screen capture
- Continuous audio recording
- Google's advanced AI
- Natural speech output

The code is organized, well-documented, and uses modern Python features like async/await for smooth performance. With this documentation, you should be able to understand how every part works and even modify it for your own projects!

---

**Last Updated:** January 22, 2026  
**Version:** 1.0  
**Author:** Science Quest Project
