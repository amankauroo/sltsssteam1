"""
#############################################################################
#                                                                           #
#             TALKING SPECTACLES - Navigation Aid for the Blind            #
#                  (Raspberry Pi version with PiCamera2)                   #
#                                                                           #
#############################################################################

WHAT DOES THIS PROGRAM DO?
--------------------------
This program turns a Raspberry Pi with a camera into a real-time navigation
assistant for blind or visually impaired users. It:
    1. SEES  - Continuously watches the path ahead via the Pi camera
    2. HEARS - Listens to the user's voice for questions or commands
    3. GUIDES - Proactively speaks out loud to describe surroundings,
               warn about dangers, and help the user navigate safely

Think of it like having a sighted guide walking beside you, constantly
telling you what's ahead and alerting you to hazards!


HOW DOES IT WORK? (Step by Step)
--------------------------------
    Step 1: The Pi camera continuously captures the scene ahead
    Step 2: The microphone picks up the user's voice
    Step 3: Images and voice are streamed to Google's AI (Gemini)
    Step 4: The AI analyzes the scene for obstacles, hazards, and context
    Step 5: The AI speaks navigation guidance through the speakers


BEFORE YOU RUN THIS PROGRAM:
----------------------------
You need to install some helper tools. Open your terminal and type:
    pip install google-genai pyaudio pillow picamera2


HOW TO RUN THIS PROGRAM:
------------------------
Open your terminal and type one of these:

    python talking_spectacles.py                (uses Pi camera - default)
    python talking_spectacles.py --mode none    (voice only, no camera)

#############################################################################
"""


# =============================================================================
# PART 1: IMPORTING LIBRARIES (Loading the tools we need)
# =============================================================================
# Think of libraries like toolboxes. Each one gives us special abilities.
# We need to import them before we can use them.
# =============================================================================

# asyncio: Lets our program do many things at once
# (like record audio AND capture video at the same time)
import asyncio

# base64: Converts images into text so we can send them over the internet
import base64

# io: Helps us work with data in memory (like holding an image temporarily)
import io

# time: Used for tracking when the AI last spoke
import time

# traceback: Shows us detailed error messages when something goes wrong
import traceback

# argparse: Lets users type options when running the program (like --mode none)
import argparse

# picamera2: Raspberry Pi camera library (replaces OpenCV for Pi)
from picamera2 import Picamera2

# pyaudio: Records sound from microphone and plays sound through speakers
import pyaudio

# PIL (Pillow): Helps us resize and convert images
import PIL.Image

# google.genai: Google's AI library - this is what connects us to Gemini AI
from google import genai

# types: Special data types that Google's AI library needs
from google.genai import types


# =============================================================================
# PART 2: SETTINGS (Numbers we can change to customize the program)
# =============================================================================
# These are like the "dials and knobs" of our program.
# You can change these numbers to make the program work differently.
# =============================================================================

# -----------------------------------------------------------------------------
# AUDIO SETTINGS (How we record and play sound)
# -----------------------------------------------------------------------------

# FORMAT: The quality of audio recording (16-bit is standard, like a phone call)
AUDIO_FORMAT = pyaudio.paInt16

# CHANNELS: How many audio channels (1 = mono, 2 = stereo)
# We use 1 (mono) because we only need one microphone
NUMBER_OF_CHANNELS = 1

# SEND_SAMPLE_RATE: How many sound samples per second when recording
# 16000 is good quality for voice (higher = better but uses more data)
RECORDING_QUALITY = 16000

# RECEIVE_SAMPLE_RATE: Quality of the AI's voice when it speaks back
PLAYBACK_QUALITY = 24000

# CHUNK_SIZE: How many audio samples to process at once
# Smaller = faster response, but uses more processing power
AUDIO_CHUNK_SIZE = 512

# -----------------------------------------------------------------------------
# AI MODEL SETTINGS (Which AI to use)
# -----------------------------------------------------------------------------

# This is the name of Google's AI model that can understand audio and video
AI_MODEL_NAME = "models/gemini-2.5-flash-native-audio-preview-12-2025"

# -----------------------------------------------------------------------------
# VIDEO SETTINGS (How we capture pictures)
# -----------------------------------------------------------------------------

# DEFAULT_MODE: What to capture by default
# Options: "camera" (Pi camera), "none" (no video)
DEFAULT_VIDEO_MODE = "camera"

# MICROPHONE_DEVICE: Which microphone to use
# Use None to auto-detect USB mic, or a number (0, 1, 2...) from check_audio.py
MICROPHONE_DEVICE = None

# FRAME_INTERVAL: How many seconds to wait between taking pictures
# 0.5 seconds = 2 frames per second - fast enough to catch hazards
# Lower number = more pictures = more data used
SECONDS_BETWEEN_FRAMES = 0.5

# NUDGE_INTERVAL: How often (seconds) to prompt the AI to describe the scene
# This forces the AI to speak even when the user hasn't said anything
# 3 seconds gives frequent updates without overwhelming the user
NUDGE_INTERVAL = 3

# -----------------------------------------------------------------------------
# API KEY (Your password to use Google's AI)
# -----------------------------------------------------------------------------
# IMPORTANT: Keep this secret! Don't share it with anyone.
# If someone gets your API key, they can use your Google AI account.

MY_API_KEY = "AIzaSyAsMCiS-q6qWFPC_PhqlahkrdNglhWmIz8"


# =============================================================================
# PART 3: CONNECTING TO GOOGLE'S AI
# =============================================================================
# This section creates a connection to Google's AI service.
# Think of it like dialing a phone number to call a friend.
# =============================================================================

# Create a connection to Google's AI service
# The API key is like a password that lets us use the service
google_ai_client = genai.Client(
    # Use the beta version of the API (newer features)
    http_options={"api_version": "v1beta"},
    # Our API key (password)
    api_key=MY_API_KEY,
)


# =============================================================================
# PART 4: AI CONFIGURATION (How the AI should behave)
# =============================================================================
# This tells the AI what we want it to do and how to respond.
# =============================================================================

# =============================================================================
# SYSTEM INSTRUCTION (Tells the AI how to behave as a navigation guide)
# =============================================================================
# This is the most important part - it turns a general AI into a
# specialized blind navigation assistant.
# =============================================================================

SYSTEM_INSTRUCTION = """
You are a real-time navigation assistant mounted on spectacles worn by a blind 
or visually impaired person. Your primary job is to keep them SAFE and informed.

YOU MUST SPEAK CONSTANTLY. Every time you receive a prompt or see an updated 
image, you MUST respond with a spoken update. Never stay silent.

CORE RULES:
1. DANGERS FIRST - Always announce hazards IMMEDIATELY and URGENTLY:
   - "Stop! Stairs going down, 3 steps ahead."
   - "Careful, car approaching from your right."
   - "Low branch at head height, duck slightly."
   - "Uneven pavement ahead, step carefully."
   - "Obstacle on your left, move right."
   - "Wet floor, walk slowly."

2. DESCRIBE WHAT THE USER IS HOLDING OR TOUCHING:
   - If the user's hands are visible holding something, always say what it is.
   - "You're holding a water bottle." / "You have your phone in your right hand."
   - "You're holding a white cane." / "You picked up a bag."
   - If what they're holding changes, announce it immediately.

3. CONTINUOUS SCENE UPDATES - Every time you get a prompt, describe what changed:
   - Path conditions (clear path, narrow sidewalk, rough terrain)
   - Upcoming changes (intersection, doorway, ramp, curb, steps)
   - Moving objects (people, vehicles, animals, cyclists) with direction
   - Landmarks and orientation cues (shop entrance, traffic light, sign)
   - Indoor details (furniture, doors, counters, walls)
   - What the user is facing or approaching

4. KEEP IT SHORT - 5-15 words per update. Be concise and direct.
   Speak naturally. Do not list things mechanically.

5. USE CLOCK DIRECTIONS for positions:
   - "Person at your 2 o'clock" (front-right)
   - "Bench on your left" / "Pole directly ahead"

6. HIGHLIGHT CHANGES - When the scene changes from the last update, focus on 
   what's NEW or DIFFERENT:
   - "Now entering a room. Table ahead, chairs on your right."
   - "Person walked past you on the left."
   - "You've stopped. Door handle at your right hand."

7. PRIORITIZE by urgency:
   - URGENT: Immediate dangers (vehicles, drop-offs, collisions)
   - HIGH: Obstacles in path, what user is holding/doing
   - MEDIUM: Navigation context (turns, intersections, crosswalks)
   - LOW: General scene (only when safe and nothing else to report)

8. ANSWER QUESTIONS immediately if the user speaks.

9. STAY CALM but FIRM for dangers. Be reassuring when safe:
   "Clear path ahead, you're doing great."

10. NEVER say "I see an image" or "Based on the image". Speak as if you 
    ARE their eyes. Say what's there directly.
"""

AI_SETTINGS = types.LiveConnectConfig(

    # The system instruction that makes the AI act as a navigation guide
    system_instruction=SYSTEM_INSTRUCTION,

    # Tell the AI to respond with audio (spoken words, not text)
    response_modalities=["AUDIO"],

    # Medium quality for video/images (balances quality vs speed)
    media_resolution="MEDIA_RESOLUTION_MEDIUM",

    # Voice settings - which voice the AI should use when speaking
    # "Zephyr" is one of Google's AI voices (there are others too)
    speech_config=types.SpeechConfig(
        voice_config=types.VoiceConfig(
            prebuilt_voice_config=types.PrebuiltVoiceConfig(
                voice_name="Zephyr"
            )
        )
    ),

    # Memory management - prevents the AI from running out of memory
    # When the conversation gets too long, older parts are removed
    context_window_compression=types.ContextWindowCompressionConfig(
        trigger_tokens=25600,  # Start removing old stuff at this point
        sliding_window=types.SlidingWindow(
            target_tokens=12800  # Keep this much of the conversation
        ),
    ),
)


# =============================================================================
# PART 5: INITIALIZE AUDIO SYSTEM
# =============================================================================
# This creates the audio system that handles microphone and speakers.
# =============================================================================

# Create the PyAudio object - this manages all audio input/output
# We only need to create this once at the start
audio_system = pyaudio.PyAudio()


# =============================================================================
# PART 6: THE MAIN PROGRAM CLASS
# =============================================================================
#
# WHAT IS A CLASS?
# ----------------
# A class is like a blueprint for creating something. Think of it like a
# recipe - it describes how to make something, but isn't the thing itself.
#
# This class (called "AIAssistant") is like a recipe for creating an AI
# assistant that can see, hear, and speak.
#
# WHAT DOES THIS CLASS DO?
# ------------------------
# It coordinates everything:
#   - Recording from the microphone
#   - Capturing from the Pi camera
#   - Sending data to Google's AI
#   - Receiving responses from the AI
#   - Playing the AI's voice through speakers
#
# =============================================================================

class AIAssistant:
    """
    This is the main class that runs the AI assistant.

    It handles:
    - Video capture (from Pi camera)
    - Audio recording (from microphone)
    - Sending data to Google's AI
    - Playing back the AI's voice
    """

    def __init__(self, video_mode):
        """
        CONSTRUCTOR: This runs when we create a new AIAssistant.

        Think of this like setting up your workspace before starting work.
        We're preparing all the variables we'll need later.

        What is 'self'?
        ---------------
        'self' is how we refer to "this specific assistant" we're creating.
        It's like saying "my" - "my video mode", "my audio queue", etc.

        Parameters:
        -----------
        video_mode: What video source to use
            - "camera" = use the Pi camera
            - "none" = no video, just audio
        """

        # Save the video mode (camera or none)
        self.video_mode = video_mode

        # =====================================================================
        # QUEUES (Data waiting lines)
        # =====================================================================
        # A queue is like a line at a store - first person in line gets
        # served first. Data goes in one end and comes out the other.
        #
        # We use queues because different parts of our program run at
        # different speeds. The queue holds data until it's ready to be used.
        # =====================================================================

        # Queue for audio coming FROM the AI (responses to play)
        self.incoming_audio_queue = None

        # Queue for audio going TO the AI (your voice)
        self.outgoing_audio_queue = None

        # (Video frames are sent directly - no queue needed for sync)

        # =====================================================================
        # CONNECTION VARIABLES
        # =====================================================================

        # The active connection to Google's AI (None until we connect)
        self.ai_session = None

        # The microphone input stream (None until we start recording)
        self.microphone_stream = None

        # =====================================================================
        # STATUS FLAGS (True/False variables to track what's happening)
        # =====================================================================

        # Timestamp of the last audio chunk received from the AI
        # Used to mute the mic briefly after AI speaks (avoid echo)
        self.last_ai_audio_time = 0

        # Are we connected to Google's AI? (True = yes, False = no)
        self.is_connected = False

        # Timestamp of the last nudge prompt sent to the AI
        self.last_nudge_time = 0

    # =========================================================================
    # FUNCTION: Auto-detect the best USB microphone
    # =========================================================================
    def get_best_mic_index(self):
        """
        Automatically finds a USB microphone connected to the Raspberry Pi.
        Falls back to the system default if no USB mic is found.
        """
        for i in range(audio_system.get_device_count()):
            info = audio_system.get_device_info_by_index(i)
            name = info["name"].lower()
            if ("usb" in name or "audio" in name) and info["maxInputChannels"] > 0:
                print(f"[AUTO MIC SELECTED]: {info['name']} (index {i})")
                return i

        # No USB mic found, fall back to system default
        default_info = audio_system.get_default_input_device_info()
        print(
            f"[DEFAULT MIC]: {default_info['name']} (index {default_info['index']})")
        return default_info["index"]

    # =========================================================================
    # FUNCTION: Send Text Messages to the AI
    # =========================================================================
    # This lets the user type messages to the AI instead of speaking.
    # It runs in a loop, waiting for the user to type something.
    # =========================================================================

    async def handle_text_input(self):
        """
        Allows you to type messages to the AI.

        How it works:
        1. Shows a prompt "message > " and waits for you to type
        2. When you press Enter, sends your message to the AI
        3. Type 'q' and press Enter to quit the program
        """

        # Keep running forever (until user types 'q')
        while True:

            # Wait for the user to type something
            # asyncio.to_thread runs input() in a separate thread so it
            # doesn't block other tasks (like audio recording)
            text_from_user = await asyncio.to_thread(
                input,
                "message > "  # This is the prompt shown to the user
            )

            # Check if user wants to quit
            # .lower() converts "Q" to "q" so both work
            if text_from_user.lower() == "q":
                # Exit this loop (and eventually the whole program)
                break

            # Only send the message if we're connected to the AI
            if self.is_connected:

                # Send the typed text to the AI
                # turn_complete=True means "I'm done talking, your turn"
                await self.ai_session.send_client_content(
                    turns={"parts": [{"text": text_from_user or "."}]},
                    turn_complete=True
                )

    # =========================================================================
    # FUNCTION: Capture One Picture from the Pi Camera
    # =========================================================================
    # This takes a single photo from the Pi camera and prepares it for sending.
    # =========================================================================

    def capture_camera_frame(self, picam):
        """
        Takes one picture from the Pi camera.

        Parameters:
        -----------
        picam: The Picamera2 camera object

        Returns:
        --------
        A dictionary with the image data, or None if capture failed.

        Steps:
        1. Capture a frame from the Pi camera (already RGB)
        2. Make the image smaller (to save bandwidth)
        3. Convert to JPEG format
        4. Encode as text (base64) so we can send it over the internet
        """

        try:
            # -----------------------------------------------------------------
            # Step 1: Capture a frame from the Pi camera
            # -----------------------------------------------------------------
            # capture_array() returns an RGB numpy array directly
            frame = picam.capture_array()

            # If capture failed, return None (nothing)
            if frame is None:
                return None

            # -----------------------------------------------------------------
            # Step 2: Convert to PIL Image and make it smaller
            # -----------------------------------------------------------------
            # PIL (Pillow) is easier to work with for image processing
            image = PIL.Image.fromarray(frame)

            # thumbnail() shrinks the image to fit within 1024x1024 pixels
            # This makes the file smaller and faster to send
            image.thumbnail([1024, 1024])

            # -----------------------------------------------------------------
            # Step 3: Convert to JPEG format
            # -----------------------------------------------------------------
            # JPEG is a compressed image format (smaller file size)

            # Create a "file" in memory (not on disk)
            image_buffer = io.BytesIO()

            # Save the image as JPEG into this memory buffer
            image.save(image_buffer, format="jpeg")

            # Go back to the start of the buffer to read it
            image_buffer.seek(0)

            # Read the raw bytes (the actual image data)
            image_bytes = image_buffer.read()

            # -----------------------------------------------------------------
            # Step 4: Encode as base64 text
            # -----------------------------------------------------------------
            # base64 converts binary data (like images) into text
            # This is needed because we're sending it over the internet
            encoded_image = base64.b64encode(image_bytes).decode()

            # Return the image data in a dictionary
            return {
                "mime_type": "image/jpeg",  # Tells the AI this is a JPEG image
                "data": encoded_image        # The actual image data (as text)
            }

        except Exception:
            return None

    # =========================================================================
    # FUNCTION: Continuously Capture from Pi Camera
    # =========================================================================
    # This runs forever, taking pictures from the Pi camera and sending them
    # to the AI.
    # =========================================================================

    async def continuous_camera_capture(self):
        """
        Continuously captures pictures from the Pi camera and sends them
        directly to the AI for perfect sync with audio.

        This function:
        1. Opens the Pi camera
        2. Takes a picture
        3. Sends it immediately to the AI (no queue delay)
        4. Waits a bit
        5. Repeats forever (until the program stops)
        """

        # Initialize the Pi camera
        picam = Picamera2()

        # Configure the camera for still image capture
        # Use RGB888 format so frames are already in RGB (no color conversion needed)
        config = picam.create_still_configuration(
            main={"size": (1024, 768), "format": "RGB888"}
        )
        picam.configure(config)
        picam.start()
        print("[Pi Camera started]")

        try:
            # Keep capturing forever
            while True:

                # Skip capture when not connected (nothing to send to)
                if not self.is_connected:
                    await asyncio.sleep(0.2)
                    continue

                # Take a picture
                frame = await asyncio.to_thread(self.capture_camera_frame, picam)

                # If capture failed (camera disconnected?), skip
                if frame is None:
                    await asyncio.sleep(0.2)
                    continue

                # Send the frame directly to the AI - no queue delay!
                # This keeps video perfectly in sync with audio
                try:
                    image_bytes = base64.b64decode(frame["data"])
                    await self.ai_session.send_realtime_input(
                        media=types.Blob(
                            data=image_bytes,
                            mime_type=frame["mime_type"]
                        )
                    )
                except Exception:
                    self.is_connected = False
                    await asyncio.sleep(0.2)
                    continue

                # Wait before taking the next picture
                # This controls how often we send frames to the AI
                await asyncio.sleep(SECONDS_BETWEEN_FRAMES)

        finally:
            # Clean up: stop the camera when done (even if an error occurred)
            picam.stop()
            picam.close()

    # =========================================================================
    # FUNCTION: Periodic Scene Analysis Nudge
    # =========================================================================
    # The AI won't speak on its own just from receiving video frames.
    # This function periodically sends a short text prompt to force the AI
    # to analyze the latest frames and speak an update.
    # =========================================================================

    async def nudge_scene_analysis(self):
        """
        Periodically prompts the AI to describe what it sees.

        Without this, the AI just passively receives frames but doesn't
        speak until the user says something. This nudge forces it to
        constantly analyze and narrate the scene.
        """

        # Rotating prompts to get varied, natural responses
        # Each one focuses on a slightly different aspect
        prompts = [
            "Describe what you see right now. Focus on dangers, obstacles, and what I'm holding.",
            "What's in front of me? Any hazards? What am I holding or touching?",
            "Update me. What changed? Any people, objects, or dangers nearby?",
            "Quick update on my surroundings. Anything I should watch out for?",
            "What's around me right now? Describe the scene and any obstacles.",
        ]

        prompt_index = 0

        # Wait a moment for the first frames to arrive before nudging
        await asyncio.sleep(2)

        while True:

            # Only nudge when connected and AI hasn't spoken recently
            if self.is_connected and (time.monotonic() - self.last_ai_audio_time > 1.0):

                try:
                    # Send a text prompt to trigger the AI to speak
                    await self.ai_session.send_client_content(
                        turns={"parts": [{"text": prompts[prompt_index]}]},
                        turn_complete=True
                    )

                    # Cycle through different prompts for natural variety
                    prompt_index = (prompt_index + 1) % len(prompts)

                    self.last_nudge_time = time.time()

                except Exception:
                    self.is_connected = False

            # Wait before sending the next nudge
            await asyncio.sleep(NUDGE_INTERVAL)

    # =========================================================================
    # FUNCTION: Send Audio to the AI
    # =========================================================================
    # This takes audio data from the queue and sends it to Google's AI.
    # =========================================================================

    async def send_audio_to_ai(self):
        """
        Sends your voice (audio) to the AI.

        This runs in a loop:
        1. Gets audio data from the outgoing audio queue
        2. Sends it to Google's AI
        3. Repeats forever

        Audio is prioritized over video because voice responses
        feel more natural when they're fast.
        """

        # Keep running forever
        while True:

            # Wait until we're connected before consuming from queue
            # Drain stale audio while disconnected to avoid sending old data
            if not self.is_connected:
                while not self.outgoing_audio_queue.empty():
                    try:
                        self.outgoing_audio_queue.get_nowait()
                    except asyncio.QueueEmpty:
                        break
                await asyncio.sleep(0.1)  # Wait a bit and try again
                continue

            # Get the next audio chunk from the queue
            # This waits until there's data available
            audio_chunk = await self.outgoing_audio_queue.get()

            # Try to send the audio to the AI
            try:
                await self.ai_session.send_realtime_input(
                    media=types.Blob(
                        data=audio_chunk["data"],         # The audio bytes
                        mime_type=audio_chunk["mime_type"]  # "audio/pcm"
                    )
                )
            except Exception as error:
                # If sending failed, mark as disconnected
                self.is_connected = False
                await asyncio.sleep(0.1)

    # =========================================================================
    # FUNCTION: Record from Microphone
    # =========================================================================
    # This captures audio from your microphone and adds it to the queue.
    # =========================================================================

    async def record_from_microphone(self):
        """
        Records audio from your microphone.

        This runs continuously:
        1. Opens the microphone
        2. Reads small chunks of audio
        3. Adds each chunk to the queue
        4. Repeats forever
        """

        # Get the microphone device index
        if MICROPHONE_DEVICE is not None:
            mic_index = MICROPHONE_DEVICE
        else:
            mic_index = self.get_best_mic_index()

        mic_info = audio_system.get_device_info_by_index(mic_index)
        print(f"[Mic device info: {mic_info}]")
        print(
            f"[Using microphone: {mic_info['name']} (index {mic_index}, channels 1, rate {RECORDING_QUALITY})]")

        # Open an audio input stream (start recording)
        # Force mono (1 channel) for reliable USB mic compatibility
        self.microphone_stream = await asyncio.to_thread(
            audio_system.open,
            format=AUDIO_FORMAT,                        # 16-bit audio
            channels=1,                                 # Force mono for USB mic
            rate=RECORDING_QUALITY,                     # 16,000 samples per second
            # This is an INPUT (microphone)
            input=True,
            input_device_index=mic_index,               # Use the selected mic
            frames_per_buffer=AUDIO_CHUNK_SIZE,         # Read this many samples at once
        )

        # Settings for reading audio
        read_settings = {"exception_on_overflow": False}

        # Keep recording forever
        while True:

            # Read a chunk of audio from the microphone
            audio_data = await asyncio.to_thread(
                self.microphone_stream.read,
                AUDIO_CHUNK_SIZE,
                **read_settings
            )

            # Don't send mic audio while the AI is speaking (or just finished)
            # This prevents the speakers' sound from being picked up by the mic
            # and causing the AI to cut itself off mid-sentence
            # We mute for 0.5 seconds after the last AI audio chunk
            if time.monotonic() - self.last_ai_audio_time < 0.5:
                continue

            # Try to add the audio to the send queue
            try:
                # put_nowait: Add immediately without waiting
                # If the queue is full, this will raise an error (which we catch)
                self.outgoing_audio_queue.put_nowait({
                    "data": audio_data,
                    "mime_type": "audio/pcm"  # PCM = raw audio format
                })
            except asyncio.QueueFull:
                # If the queue is full, just skip this chunk
                # This prevents lag if the network can't keep up
                pass

    # =========================================================================
    # FUNCTION: Receive Responses from the AI
    # =========================================================================
    # This listens for the AI's response and adds it to the playback queue.
    # =========================================================================

    async def receive_from_ai(self):
        """
        Receives the AI's responses (audio and text).

        This runs continuously:
        1. Waits for a response from the AI
        2. If it's audio, adds it to the playback queue
        3. If it's text, prints it to the console
        """

        # Keep running forever
        while True:

            # Wait if not connected
            if not self.is_connected:
                await asyncio.sleep(0.5)
                continue

            # Try to receive from the AI
            try:
                # Get the response stream from the AI
                response_stream = self.ai_session.receive()

                # Process each piece of the response as it arrives
                # The 'async for' loop handles streaming data piece by piece
                async for response in response_stream:

                    # Check if there's audio data
                    audio_data = response.data
                    if audio_data:
                        # Track when the AI last sent audio
                        self.last_ai_audio_time = time.monotonic()
                        # Add the audio to the playback queue
                        self.incoming_audio_queue.put_nowait(audio_data)
                        continue  # Move to the next piece

                    # Check if there's text
                    text_data = response.text
                    if text_data:
                        # Print the text (without a newline at the end)
                        print(text_data, end="")

            except asyncio.CancelledError:
                # Program is shutting down, exit cleanly
                raise

            except Exception as error:
                # Connection problem - will try to reconnect
                self.is_connected = False
                error_type = type(error).__name__
                print(
                    f"\n[Connection issue: {error_type}, reconnecting...]\n", end="")
                await asyncio.sleep(0.5)

    # =========================================================================
    # FUNCTION: Play Audio Through Speakers
    # =========================================================================
    # This plays the AI's voice through your speakers.
    # =========================================================================

    async def play_audio_through_speakers(self):
        """
        Plays the AI's voice through your speakers.

        This runs continuously:
        1. Gets audio data from the incoming audio queue
        2. Plays it through the speakers
        3. Repeats forever
        """

        # Open an audio output stream (for playing sound)
        # Use a larger output buffer to smooth out delivery jitter
        speaker_stream = await asyncio.to_thread(
            audio_system.open,
            format=AUDIO_FORMAT,      # 16-bit audio
            channels=NUMBER_OF_CHANNELS,  # Mono
            rate=PLAYBACK_QUALITY,    # 24,000 samples per second
            output=True,              # This is an OUTPUT (speakers)
            frames_per_buffer=AUDIO_CHUNK_SIZE * 4,  # Larger buffer for smoother playback
        )

        # Keep playing forever
        while True:

            # Wait for audio data from the AI
            audio_bytes = await self.incoming_audio_queue.get()

            # Batch any additional immediately-available chunks together
            # This smooths out playback and reduces gaps from network jitter
            while not self.incoming_audio_queue.empty():
                try:
                    audio_bytes += self.incoming_audio_queue.get_nowait()
                except asyncio.QueueEmpty:
                    break

            # Play the audio through the speakers
            await asyncio.to_thread(speaker_stream.write, audio_bytes)

    # =========================================================================
    # FUNCTION: Main Run Loop (The Heart of the Program)
    # =========================================================================
    # This is where everything comes together and runs.
    # =========================================================================

    async def run(self):
        """
        The main function that runs the entire AI assistant.

        This function:
        1. Sets up all the data queues
        2. Connects to Google's AI
        3. Starts all the background tasks
        4. Handles reconnection if connection drops
        5. Cleans up when you quit
        """

        # ---------------------------------------------------------------------
        # Print a welcome message
        # ---------------------------------------------------------------------
        print("=" * 50)
        print("TALKING SPECTACLES - Blind Navigation Aid")
        print("=" * 50)

        # Show which video mode is being used
        if self.video_mode == "none":
            print("Video: OFF (audio only)")
        else:
            print("Video: PI CAMERA")

        print("Frame interval: " + str(SECONDS_BETWEEN_FRAMES) + " seconds")
        print("Type 'q' and press Enter to quit")
        print("=" * 50)

        # ---------------------------------------------------------------------
        # Create the data queues
        # ---------------------------------------------------------------------
        # Queues are like waiting lines - data goes in one end and out the other

        # Queue for audio FROM the AI (no size limit - we want all of it)
        self.incoming_audio_queue = asyncio.Queue()

        # Queue for audio TO the AI (max 30 items to prevent buildup)
        self.outgoing_audio_queue = asyncio.Queue(maxsize=30)

        # (Video frames are sent directly from the capture loop - no queue)

        # ---------------------------------------------------------------------
        # Main connection loop
        # ---------------------------------------------------------------------
        # This keeps trying to stay connected to the AI

        try:
            while True:
                try:
                    # ---------------------------------------------------------
                    # Connect to Google's Gemini AI
                    # ---------------------------------------------------------
                    # 'async with' ensures the connection is properly closed
                    # if something goes wrong

                    async with google_ai_client.aio.live.connect(
                        model=AI_MODEL_NAME,
                        config=AI_SETTINGS
                    ) as session:

                        # Save the session and mark as connected
                        self.ai_session = session

                        # Drain any stale data from previous session
                        while not self.incoming_audio_queue.empty():
                            try:
                                self.incoming_audio_queue.get_nowait()
                            except asyncio.QueueEmpty:
                                break

                        self.is_connected = True
                        print("[Connected to AI]")

                        # -----------------------------------------------------
                        # Start all the background tasks
                        # -----------------------------------------------------
                        # TaskGroup runs multiple functions at the same time
                        # Think of it like having multiple workers doing
                        # different jobs simultaneously

                        async with asyncio.TaskGroup() as task_group:

                            # Task 1: Handle text input from user
                            text_input_task = task_group.create_task(
                                self.handle_text_input()
                            )

                            # Task 2: Send audio to the AI
                            task_group.create_task(
                                self.send_audio_to_ai()
                            )

                            # Task 3: Record from microphone
                            task_group.create_task(
                                self.record_from_microphone()
                            )

                            # Task 4: Capture and send video directly (camera only)
                            if self.video_mode == "camera":
                                task_group.create_task(
                                    self.continuous_camera_capture()
                                )

                            # Task 5: Periodically nudge AI to describe scene
                            if self.video_mode == "camera":
                                task_group.create_task(
                                    self.nudge_scene_analysis()
                                )

                            # Task 6: Receive responses from AI
                            task_group.create_task(
                                self.receive_from_ai()
                            )

                            # Task 7: Play AI's audio through speakers
                            task_group.create_task(
                                self.play_audio_through_speakers()
                            )

                            # Wait for user to quit (text input task will end)
                            await text_input_task

                            # User typed 'q', so exit
                            raise asyncio.CancelledError("User requested exit")

                except asyncio.CancelledError:
                    # User wants to quit - exit the loop
                    raise

                except Exception as error:
                    # Connection failed - try to reconnect
                    self.is_connected = False
                    error_type = type(error).__name__
                    print(
                        f"\n[Connection lost: {error_type}, reconnecting in 2 seconds...]")
                    await asyncio.sleep(2)  # Wait 2 seconds before retry

        except asyncio.CancelledError:
            # Clean exit - user quit the program
            print("\n[Goodbye!]")

        except ExceptionGroup as error_group:
            # Multiple errors occurred - clean up and print details
            if self.microphone_stream:
                self.microphone_stream.close()
            traceback.print_exception(error_group)


# =============================================================================
# PART 7: PROGRAM ENTRY POINT (Where the program starts)
# =============================================================================
#
# This section runs when you execute the script directly, like:
#     python talking_spectacles.py
#
# It sets up command-line options and starts the AI assistant.
#
# =============================================================================

# The special check below means:
# "Only run this code if this file is being run directly"
# (not if it's being imported by another file)

if __name__ == "__main__":

    # -------------------------------------------------------------------------
    # Step 1: Set up command-line arguments
    # -------------------------------------------------------------------------
    # This lets users customize how the program runs
    # Example: python talking_spectacles.py --mode none

    # Create an argument parser (handles command-line options)
    argument_parser = argparse.ArgumentParser()

    # Add the --mode option
    # This chooses what video source to use
    argument_parser.add_argument(
        "--mode",                    # The option name (use with --)
        type=str,                    # It should be text
        default=DEFAULT_VIDEO_MODE,  # Default is "camera"
        help="Video source to use: camera or none",
        choices=["camera", "none"],  # Only allow these values
    )

    # Add the --interval option
    # This sets how often to send video frames
    argument_parser.add_argument(
        "--interval",                # The option name
        # It should be a number (can have decimals)
        type=float,
        default=SECONDS_BETWEEN_FRAMES,  # Default is 0.5 seconds
        help="Seconds between video frames (lower = more frames)",
    )

    # Parse the arguments (read what the user typed)
    user_arguments = argument_parser.parse_args()

    # -------------------------------------------------------------------------
    # Step 2: Apply the user's settings
    # -------------------------------------------------------------------------

    # Update the frame interval with the user's choice
    SECONDS_BETWEEN_FRAMES = user_arguments.interval

    # -------------------------------------------------------------------------
    # Step 3: Create and run the AI assistant
    # -------------------------------------------------------------------------

    # Create an AIAssistant with the chosen video mode
    assistant = AIAssistant(video_mode=user_arguments.mode)

    # Run the assistant!
    # asyncio.run() starts the async event loop and runs until done
    asyncio.run(assistant.run())
