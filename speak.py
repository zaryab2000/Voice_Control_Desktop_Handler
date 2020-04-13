#!/usr/bin/env python3

import os
from gtts import gTTS

<<<<<<< HEAD
=======

>>>>>>> 82ddc88493813f4e7c4fb8438977732b79641c41
def tts(text,lang):
    tts = gTTS(text=text,lang=lang)
    tts.save("current_audio.mp3")
    os.system("mpg321 current_audio.mp3")
