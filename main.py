from kivymd.app import MDApp
from kivy.uix.screenmanager import ScreenManager
from kivy.core.window import Window

KIVY_DPI = 320
KIVY_METRICS_DENSITY = 2

Window.size = (720, 1280)

class darkwildernessApp(MDApp):

    def build(self):
        pass

class WindowManager(ScreenManager):
    pass

if __name__ == "__main__":
    darkwildernessApp().run()