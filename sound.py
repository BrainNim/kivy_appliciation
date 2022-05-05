from kivy.app import App
from kivy.core.audio import SoundLoader

class Play(App):

    def beep(self):
        sound = SoundLoader.load('Digital Watch Alarm Long.mp3')
        sound.play()