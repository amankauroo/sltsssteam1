"""
Quick test to check if your Google Gemini API key is working.
Run this BEFORE running talking_spectacles.py to verify connectivity.

Usage:
    python test_api_key.py
"""

from google import genai

# The same API key used in talking_spectacles.py
MY_API_KEY = ""

print("=" * 50)
print("TESTING GEMINI API KEY")
print("=" * 50)

# Test 1: Basic connection
print("\n[Test 1] Connecting to Google AI...")
try:
    client = genai.Client(
        http_options={"api_version": "v1beta"},
        api_key=MY_API_KEY,
    )
    print("  OK - Client created")
except Exception as e:
    print(f"  FAILED - {type(e).__name__}: {e}")
    print("\n>>> Your API key may be invalid. Get a new one at:")
    print(">>> https://aistudio.google.com/apikey")
    exit(1)

# Test 2: List models (quick API call to verify key works)
print("\n[Test 2] Verifying API key with a simple request...")
try:
    # Try a simple text generation to confirm the key works
    response = client.models.generate_content(
        model="gemini-2.5-flash",
        contents="Say hello in exactly 3 words.",
    )
    print(f"  OK - AI responded: {response.text.strip()}")
except Exception as e:
    print(f"  FAILED - {type(e).__name__}: {e}")
    print("\n>>> Your API key is not working. Possible reasons:")
    print(">>>   1. Key is expired or revoked")
    print(">>>   2. Key has no quota left")
    print(">>>   3. No internet connection on the Pi")
    print(">>>   4. Key doesn't have Gemini API enabled")
    print("\n>>> Get a new key at: https://aistudio.google.com/apikey")
    exit(1)

# Test 3: Check if the Live model is accessible
print("\n[Test 3] Checking Live Audio model access...")
LIVE_MODEL = "models/gemini-2.5-flash-native-audio-preview-12-2025"
try:
    model_info = client.models.get(model=LIVE_MODEL)
    print(f"  OK - Model found: {model_info.display_name}")
except Exception as e:
    print(f"  FAILED - {type(e).__name__}: {e}")
    print(f"\n>>> The Live Audio model '{LIVE_MODEL}' is not accessible.")
    print(">>> Your API key may not have access to this preview model.")
    exit(1)

print("\n" + "=" * 50)
print("ALL TESTS PASSED - API key is working!")
print("=" * 50)
print("\nYou can now run: python talking_spectacles.py")
