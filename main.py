from kivy.app import App
from kivy.uix.button import Button
class TestApp(App):
    def build(self):
        return Button(text='Welcome to VIP Casino')
TestApp().run()
