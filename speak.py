#!/usr/bin/env python3

import os
from gtts import gTTS


def tts(text,lang):
    tts = gTTS(text=text,lang=lang)
    tts.save("current_audio.mp3")
    os.system("mpg321 current_audio.mp3")
