## AIvoice.py

This Python script uses the speech_recognition library to record audio from a microphone, uses the OpenAI API to generate a response, and uses the Eleven Labs API to convert the response to an MP3 file and play it through VLC media player.


[![Watch the video](https://img.youtube.com/vi/bkOeh8xIMF4/maxresdefault.jpg)](https://www.youtube.com/watch?v=bkOeh8xIMF4)


## Multiple voices and personalities per voice.
- I have updated the main AIVoice.py file to include personalities and voices for different characters like this
```
# Define the names and corresponding Elven Labs URLs
name_urls = {
    "Josh": "https://api.elevenlabs.io/v1/text-to-speech/TxGEqnHWrfWFTfGW9XjX/stream?optimize_streaming_latency=0",
    "Bella": "https://api.elevenlabs.io/v1/text-to-speech/EXAVITQu4vr4xnSDxMaL/stream?optimize_streaming_latency=0",
    "Rachel": "https://api.elevenlabs.io/v1/text-to-speech/21m00Tcm4TlvDq8ikWAM/stream?optimize_streaming_latency=0"
}

personalities = {
    "Josh": "respond in a professional and responsive manner, try to keep things short and accurate.",
    "Bella": "respond in a flirtatious fantasy female character accent, never say emotions like giggles.",
    "Rachel": "respond as a mature woman."
}
```

- You can freely edit these how you want with different IDs for the voices and personalities to match. 
- You now interact by simply saying:
1. "Ask Bella tell me a short story" 
2. "Ask Josh tell me a short story"
3. "Ask Rachel tell me a short story"

- You can change these names to whatever you would like in the list areas shown above, then those names will be called upon when you speak. Simply changing Josh in both the name_urls and personalities to John for example will let you do:
1. "Ask John tell me a short story"


### Prerequisites

### You MUST install VLC media player 
- https://www.videolan.org/vlc/

### Configuration

Before using the script, you will need to set up API keys for the OpenAI and Eleven Labs APIs. To do this, edit the apikeys.txt file with your keys.
- https://beta.elevenlabs.io/
- https://platform.openai.com/account/api-keys

```
[chatgpt]
key=APIKEYGOESHERE


[elvenlabs]
key=APIKEYGOESHERE
```

Replace "APIKEYGOESHERE" and "APIKEYGOESHERE" with your actual API keys.

### Usage

1. Open a powershell window.
2. Navigate to the directory where you downloaded and extracted the files.
3. Run the following command to execute the script:

```bash
Set-ExecutionPolicy RemoteSigned
```
- This will allow the powershell script to be executed.

Now run:
```bash
.\Run.ps1
```

What will happen on your first run:
It will download and install python3.9 to the correct folder for use. It will also install the pypi packages required:
```
SpeechRecognition
openai
requests
configparser
pyaudio
```

- It will then check for the existence of the AIVoice.py file. If it isn't found it will download a fresh copy from this github.

Finally it will execute the python script to start listening.

- You will need to run the Run.ps1 file every time you wish to start the listener. 


### In the AIvoice.py...
We have something setup that looks like this on line "61":
```
tosend = "respond in a flirtatious fantasy female character accent, never say emotions like giggles." + said
```
- What it does is applies that prefix to everything you ask. Changing it can give you some fun results:

```
tosend = "respond like a barbarian warrior who has just been injured in battle" + said
```

- You can also change the voice by editing this line
```
https://api.elevenlabs.io/v1/text-to-speech/EXAVITQu4vr4xnSDxMaL/stream?optimize_streaming_latency=0
```
Just adjust the token "EXAVITQu4vr4xnSDxMaL" in this case, to a different token from the voice list here:
- https://api.elevenlabs.io/v1/voices
