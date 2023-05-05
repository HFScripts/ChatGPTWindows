## AIvoice.py

This Python script uses the speech_recognition library to record audio from a microphone, uses the OpenAI API to generate a response, and uses the Eleven Labs API to convert the response to an MP3 file and play it through VLC media player.


[![Watch the video](https://img.youtube.com/vi/bkOeh8xIMF4/maxresdefault.jpg)](https://www.youtube.com/watch?v=bkOeh8xIMF4)


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
