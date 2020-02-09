#!/usr/bin/env python3

import os
from gtts import gTTS
<<<<<<< HEAD
text="The subject of this article is technology of distributed trustless consensus, for this is the one area in which blockchain systems, like Bitcoin, are indeed a major breakthrough. When it comes to other goals, such as distributed data storage, anonymity, transaction verifiability, data obfuscation, shared ledgers, micropayments, high throughput, digital contracts, and so on, cryptographic blockchain systems are, essentially, incidental. Solutions to these problems are well known outside of the blockchain space and, consequently, I will not focus on them here."
=======

>>>>>>> 4ddc822f75381b2e4ff4b4ab94c20e7aa9eab553
def tts(text,lang):
    tts = gTTS(text=text,lang=lang)
    tts.save("current_audio.mp3")
    os.system("mpg321 current_audio.mp3")
