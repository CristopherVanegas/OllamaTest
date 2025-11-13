import pygame
from gtts import gTTS

def speech(response):
    audio_file = "audios/audio.mp3"
    tts = gTTS(text=str(response), lang="en")
    tts.save(audio_file)
    pygame.mixer.init()
    pygame.mixer.music.load(audio_file)
    pygame.mixer.music.play()
    while pygame.mixer.music.get_busy():
        pygame.time.Clock().tick(10)

speech("Hello, this is a test.")
