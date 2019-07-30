from gtts import gTTS
mp3='off.mp3'

tts = gTTS(text='выключаю', lang='ru')
tts.save(mp3)
mixer.music.load(mp3)
mixer.music.play()
