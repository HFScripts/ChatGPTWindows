# Check if Python is installed
if (-not (Test-Path "C:\Program Files\Python39\python.exe")) {
    # Download the Python 3.9 installer
    Invoke-WebRequest "https://www.python.org/ftp/python/3.9.5/python-3.9.5-amd64.exe" -OutFile "python-3.9.5-amd64.exe"

    # Install Python 3.9
    Start-Process -FilePath "python-3.9.5-amd64.exe" -ArgumentList "/quiet InstallAllUsers=1 PrependPath=1" -Wait

    # Remove the installer file
    Remove-Item "python-3.9.5-amd64.exe"
}

# Add Python and pip to the PATH environment variable
$env:Path += ";C:\Program Files\Python39;C:\Program Files\Python39\Scripts"

# Check if pip is installed
if (-not (Get-Command pip.exe -ErrorAction SilentlyContinue)) {
    # Install pip
    python -m ensurepip --default-pip
}

# Install required packages if they are not already installed

& "C:\Program Files\Python39\python.exe" -m pip install --upgrade pip

if (-not (Get-Module SpeechRecognition -ErrorAction SilentlyContinue)) {
    & "C:\Program Files\Python39\python.exe" -m pip install SpeechRecognition | Out-Null
}

if (-not (Get-Module openai -ErrorAction SilentlyContinue)) {
    & "C:\Program Files\Python39\python.exe" -m pip install openai | Out-Null
}

if (-not (Get-Module requests -ErrorAction SilentlyContinue)) {
    & "C:\Program Files\Python39\python.exe" -m pip install requests | Out-Null
}

if (-not (Get-Module configparser -ErrorAction SilentlyContinue)) {
    & "C:\Program Files\Python39\python.exe" -m pip install configparser | Out-Null
}

if (-not (Get-Module pyaudio -ErrorAction SilentlyContinue)) {
    & "C:\Program Files\Python39\python.exe" -m pip install pyaudio | Out-Null
}


# Set the path where AIvoice.py should be downloaded
$scriptPath = Join-Path $PWD.Path "AIvoice.py"

# Check if AIvoice.py script exists
if (!(Test-Path $scriptPath)) {
    # Download AIvoice.py script
    Invoke-WebRequest "https://raw.githubusercontent.com/HFScripts/ChatGPTWindows/main/AIVoice.py" -OutFile $scriptPath
}

# Clear the PowerShell console
Clear-Host

# Run AIvoice.py script
& "C:\Program Files\Python39\python.exe" $scriptPath --no-warn-script-location
