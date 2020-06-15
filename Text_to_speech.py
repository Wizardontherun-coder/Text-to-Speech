from gtts import gTTS

from pathlib import Path

import os

Automation = Path("C:\\Users\\WIZARD\\Desktop\\")

file_to_open = Automation / "new.txt"

f = open(file_to_open, encoding='utf-8')

myText =(f.read())

language = 'en'

out = gTTS(text=myText, lang= language, slow=False)

out.save("audio.mp3")

os.system("start audio.mp3")