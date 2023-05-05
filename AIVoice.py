import os
import speech_recognition as sr
import openai
import requests
import json
import subprocess
import sys
import configparser

# Construct the path to the VLC executable in "Program Files"
vlc_path_64 = os.path.join("C:", os.sep, "Program Files", "VideoLAN", "VLC", "vlc.exe")

# Construct the path to the VLC executable in "Program Files (x86)"
vlc_path_32 = os.path.join("C:", os.sep, "Program Files (x86)", "VideoLAN", "VLC", "vlc.exe")

# Check if VLC is installed in either folder
if not os.path.exists(vlc_path_64) and not os.path.exists(vlc_path_32):
    print("VLC is not installed on this computer.")
    sys.exit()

# Load API keys from file
config = configparser.ConfigParser()
config.read("apikeys.txt")

# Check that chatgpt API key is present and not default
if not config.has_section('chatgpt') or config.get('chatgpt', 'key') == 'APIKEYGOESHERE':
    print("Please set the chatgpt API key in apikeys.txt file.")
    sys.exit()

# Check that elvenlabs API key is present
if not config.has_section('elvenlabs'):
    print("elvenlabs API key not found in file.")
    sys.exit()

# Set up OpenAI credentials
openai.api_key = config.get('chatgpt', 'key')
elvenlabsapikey = config.get('elvenlabs', 'key')

# Define the function to get audio and send to OpenAI
def get_audio():
    # Record audio from microphone
    r = sr.Recognizer()
    with sr.Microphone() as source:
        print("Say something! (Prompt is: Ask AI)")
        audio = r.listen(source)

    # Convert audio to text using speech recognition library
    try:
        text = r.recognize_google(audio)
        print("You said: " + text)
    except sr.UnknownValueError:
        print("Could not understand audio")
        return
    except sr.RequestError as e:
        print("Could not request results from Google Speech Recognition service; {0}".format(e))
        return

    # Check if the user said "ask AI" and send the rest of the text to OpenAI
    if "ask AI" in text:
        said = text.split("ask AI", 1)[1].strip()
        tosend = "respond in a flirtatious fantasy female character accent, never say emotions like giggles." + said
        print("Sending to OpenAI: " + said)
        try:
            completion = openai.ChatCompletion.create(model="gpt-3.5-turbo", messages=[{"role": "user", "content": tosend}])
            response = completion.choices[0].message.content
            print("OpenAI response: " + response)

            # Download MP3 file from Eleven Labs API
            url = 'https://api.elevenlabs.io/v1/text-to-speech/EXAVITQu4vr4xnSDxMaL/stream?optimize_streaming_latency=0'
            headers = {
                'accept': '*/*',
                'xi-api-key': f'{elvenlabsapikey}',
                'Content-Type': 'application/json'
            }
            data = {
                "text": f"{response}",
                "model_id": "eleven_monolingual_v1",
                "voice_settings": {
                    "stability": 0,
                    "similarity_boost": 0
                }
            }
            response = requests.post(url, headers=headers, data=json.dumps(data))

            if response.status_code == 200:
                # Save the MP3 file to the current directory as output.mp3
                mp3_file = os.path.join(os.getcwd(), 'output.mp3')
                with open(mp3_file, 'wb') as f:
                    f.write(response.content)
                    print("MP3 file saved to:", mp3_file)
                    # Construct the path to the VLC executable
                    vlc_path = os.path.join("C:", os.sep, "Program Files (x86)", "VideoLAN", "VLC", "vlc.exe")
                    
                    # Check if VLC is installed in "Program Files (x86)"
                    if os.path.exists(vlc_path):
                        # Run VLC with the specified arguments
                        subprocess.call([vlc_path, "-Idummy", "--play-and-exit", "output.mp3"])
                        print("VLC has been run with the specified arguments.")
                    else:
                        # Check if VLC is installed in "Program Files"
                        vlc_path = os.path.join("C:", os.sep, "Program Files", "VideoLAN", "VLC", "vlc.exe")
                        if os.path.exists(vlc_path):
                            # Run VLC with the specified arguments
                            subprocess.call([vlc_path, "-Idummy", "--play-and-exit", "output.mp3"])
                            print("VLC has been run with the specified arguments.")
                        else:
                            print("VLC is not installed on this computer.")
                            sys.exit()
                # Delete the MP3 file
                os.remove(mp3_file)
            else:
                print("Error:", response.status_code, response.text)
        except openai.OpenAIError as e:
            print("OpenAI error: {0}".format(e))
            return

# Continuously listen for audio and send to OpenAI
while True:
    get_audio()
