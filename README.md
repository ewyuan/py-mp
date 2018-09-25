# py-mp
py-mp uses command-line to take in inputs from the user and makes a search query on Youtube. py-mp will pull the most relevant video and will stream the audio to the computer.

## Prerequisites
* Python 3 https://www.python.org/downloads/
* VLC https://www.videolan.org/vlc/

## How to install
```
>> pip3 install py-mp
```

## How to run
```
>> py-mp       # this can be done from any directory
```

## 'help' page
```
add [song]       # Adds [song] to the queue
clear            # Clears the queue
pause            # Pause the current song
resume           # Resumes the current song
queue            # Prints the current queue
skip             # Plays the next song in queue
cur              # Get the title of the current song
time             # Get the time of the current song
prev             # Get the title of the previous song
rewind           # Restart the current song
remove [pos]     # Removes the song in position [pos] from the queue
exit             # Exits the program
```
