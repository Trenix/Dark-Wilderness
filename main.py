from kivymd.app import MDApp
from kivy.uix.screenmanager import ScreenManager
from kivy.core.window import Window
from kivymd.uix.screen import MDScreen
from kivy.clock import Clock
from kivy.uix.gridlayout import GridLayout
from kivy.metrics import dp
from kivymd.uix.floatlayout import MDFloatLayout
from kivy.uix.image import Image
from kivy.uix.button import Button

KIVY_DPI = 320
KIVY_METRICS_DENSITY = 2

Window.size = (720, 1280)

class DarkWildernessApp(MDApp):
    def build(self):
        pass

class MainScreen(MDScreen):

    def on_enter(self):
        Clock.schedule_once(self.create_map)

    def create_map(self, *args):

        hex_id = dict()

        for num in range(0, 25):
            temp_layout = MDFloatLayout()

            self.ids.discovery_tiles.add_widget(temp_layout)

            if num < 5:
                temp_layout.add_widget(
                    Image(
                        pos=(self.x + (num * dp(150)), self.y),
                        size_hint=(None, None),
                        size=(dp(155), dp(180)),
                        source='image/Hexagon.png',
                    )
                )

                #TODO: Need to store every hex to pull it whenever

                hex_id[num + 1] = {'position': (0, num)}

            elif num < 10:
                temp_layout.add_widget(
                    Image(
                        pos=(self.x + ((9.5 - num) * dp(150)), self.y - (130 * 1)),
                        size_hint=(None, None),
                        size=(dp(155), dp(180)),
                        source='image/Hexagon.png'
                    )
                )

                hex_id[num + 1] = {'position': (1, num - 5)}

            elif num < 15:
                temp_layout.add_widget(
                    Image(
                        pos=(self.x + ((14 - num) * dp(150)), self.y - (130 * 2)),
                        size_hint=(None, None),
                        size=(dp(155), dp(180)),
                        source='image/Hexagon.png'
                    )
                )

                hex_id[num + 1] = {'position': (2, num - 10)}

            elif num < 20:
                temp_layout.add_widget(
                    Image(
                        pos=(self.x + ((19.5 - num) * dp(150)), self.y - (130 * 3)),
                        size_hint=(None, None),
                        size=(dp(155), dp(180)),
                        source='image/Hexagon.png'
                    )
                )

                hex_id[num + 1] = {'position': (3, num - 15)}

            else:
                temp_layout.add_widget(
                    Image(
                        pos=(self.x + ((24 - num) * dp(150)), self.y - (130 * 4)),
                        size_hint=(None, None),
                        size=(dp(155), dp(180)),
                        source='image/Hexagon.png'
                    )
                )

                hex_id[num + 1] = {'position': (4, num - 20)}

        print(hex_id[20])


# kv = '''
# Honeycombed:
#     cols: 5
#     spacing: 30, 25
#     padding: 75
# '''
#
# class Honeycombed(GridLayout):
#     def on_kv_post(self, base_widget):
#         for _ in range(25):
#             self.add_widget(Button())
#
#     def do_layout(self, *largs):
#         children = self.children
#         if not children or not self._init_rows_cols_sizes(len(children)):
#             l, t, r, b = self.padding
#             self.minimum_size = l + r, t + b
#             return
#         self._fill_rows_cols_sizes()
#         self._update_minimum_size()
#         self._finalize_rows_cols_sizes()
#
#         for i, x, y, w, h in self._iterate_layout(len(children)):
#             c = children[i]
#             c.pos = x, y
#             shw, shh = c.size_hint
#             shw_min, shh_min = c.size_hint_min
#             shw_max, shh_max = c.size_hint_max
#
#             if shw_min is not None:
#                 if shw_max is not None:
#                     w = max(min(w, shw_max), shw_min)
#                 else:
#                     w = max(w, shw_min)
#             else:
#                 if shw_max is not None:
#                     w = min(w, shw_max)
#
#             if shh_min is not None:
#                 if shh_max is not None:
#                     h = max(min(h, shh_max), shh_min)
#                 else:
#                     h = max(h, shh_min)
#             else:
#                 if shh_max is not None:
#                     h = min(h, shh_max)
#
#             if shw is None:
#                 if shh is not None:
#                     c.height = h
#             else:
#                 if shh is None:
#                     c.width = w
#                 else:
#                     c.size = (w, h)
#             # just these
#             c.y -= ((h + self.spacing[1]) // 2) * (i // self.cols)
#             if i//self.cols % 2:
#                 c.x -= (w + self.spacing[0]) // 2



class WindowManager(ScreenManager):
    pass

if __name__ == "__main__":
    DarkWildernessApp().run()