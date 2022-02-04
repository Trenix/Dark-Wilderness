from kivymd.app import MDApp
from kivy.uix.screenmanager import ScreenManager
from kivy.core.window import Window
from kivymd.uix.screen import MDScreen
from kivy.clock import Clock
from kivy.metrics import dp
from kivymd.uix.floatlayout import MDFloatLayout
from kivy.core.text import LabelBase
from kivymd.font_definitions import theme_font_styles
from kivy.uix.image import Image

KIVY_DPI = 320
KIVY_METRICS_DENSITY = 2

Window.size = (720, 1280)

class DarkWildernessApp(MDApp):
    def build(self):
        pass

class MainScreen(MDScreen):
    def __init__(self, **kwargs):
        super(MDScreen, self).__init__(**kwargs)

        # Future Use
        MDApp.get_running_app().theme_cls.material_style = "M3"

        # Set colors to use throughout app
        MDApp.get_running_app().theme_cls.set_colors("Green", "800", "600", "900", "Lime", "600", "100", "900")

        # Set Fonts
        # LabelBase.register(name="H1", fn_regular="font/JetBrainsMono-Light.ttf")
        # theme_font_styles.append('H1')
        # MDApp.get_running_app().theme_cls.font_styles["H1"] = ["H1", 96, False, -1.5]
        #
        # LabelBase.register(name="H2", fn_regular="font/JetBrainsMono-Light.ttf")
        # theme_font_styles.append('H2')
        # MDApp.get_running_app().theme_cls.font_styles["H2"] = ["H2", 60, False, -0.5]
        #
        # LabelBase.register(name="H3", fn_regular="font/JetBrainsMono-Regular.ttf")
        # theme_font_styles.append('H3')
        # MDApp.get_running_app().theme_cls.font_styles["H3"] = ["H3", 48, False, 0]
        #
        # LabelBase.register(name="H4", fn_regular="font/JetBrainsMono-Regular.ttf")
        # theme_font_styles.append('H4')
        # MDApp.get_running_app().theme_cls.font_styles["H4"] = ["H4", 34, False, 0.25]
        #
        # LabelBase.register(name="H5", fn_regular="font/JetBrainsMono-Regular.ttf")
        # theme_font_styles.append('H5')
        # MDApp.get_running_app().theme_cls.font_styles["H5"] = ["H5", 24, False, 0]
        #
        # LabelBase.register(name="H6", fn_regular="font/JetBrainsMono-Medium.ttf")
        # theme_font_styles.append('H6')
        # MDApp.get_running_app().theme_cls.font_styles["H6"] = ["H6", 20, False, 0.15]
        #
        # LabelBase.register(name="Subtitle1", fn_regular="font/JetBrainsMono-Regular.ttf")
        # theme_font_styles.append('Subtitle1')
        # MDApp.get_running_app().theme_cls.font_styles["Subtitle1"] = ["Subtitle1", 16, False, 0.15]
        #
        # LabelBase.register(name="Subtitle2", fn_regular="font/JetBrainsMono-Medium.ttf")
        # theme_font_styles.append('Subtitle2')
        # MDApp.get_running_app().theme_cls.font_styles["Subtitle2"] = ["Subtitle2", 14, False, 0.1]
        #
        # LabelBase.register(name="Body1", fn_regular="font/JetBrainsMono-Regular.ttf")
        # theme_font_styles.append('Body1')
        # MDApp.get_running_app().theme_cls.font_styles["Body1"] = ["Body1", 16, False, 0.5]
        #
        # LabelBase.register(name="Body2", fn_regular="font/JetBrainsMono-Regular.ttf")
        # theme_font_styles.append('Body2')
        # MDApp.get_running_app().theme_cls.font_styles["Body2"] = ["Body2", 14, False, 0.25]
        #
        # LabelBase.register(name="Button", fn_regular="font/JetBrainsMono-Medium.ttf")
        # theme_font_styles.append('Button')
        # MDApp.get_running_app().theme_cls.font_styles["Button"] = ["Button", 14, True, 1.25]
        #
        # LabelBase.register(name="Caption", fn_regular="font/JetBrainsMono-Regular.ttf")
        # theme_font_styles.append('Caption')
        # MDApp.get_running_app().theme_cls.font_styles["Caption"] = ["Caption", 12, False, 0.4]
        #
        # LabelBase.register(name="Overline", fn_regular="font/JetBrainsMono-Regular.ttf")
        # theme_font_styles.append('Overline')
        # MDApp.get_running_app().theme_cls.font_styles["Overline"] = ["Overline", 10, True, 1.5]


    def on_pre_enter(self, *args):
        MDApp.get_running_app().theme_cls.material_style = "M3"

        # Set colors to use throughout app
        MDApp.get_running_app().theme_cls.set_colors("Brown", "400", "200", "800", "Lime", "600", "100", "900")

    def prevent_break_timer(self):
        Clock.schedule_once(self.disable_rail, 0.3)

    def disable_rail(self, td):
        self.ids.rail.disabled = False

    # def on_enter(self):
    #     Clock.schedule_once(self.create_map)

    # def create_map(self, *args):
    #
    #     hex_id = dict()
    #
    #     for num in range(0, 25):
    #         temp_layout = MDFloatLayout()
    #         self.ids.discovery_tiles.add_widget(temp_layout)
    #
    #         if num < 5:
    #             temp_widget = Image(
    #                     pos=(self.x + (num * dp(150)), self.y),
    #                     size_hint=(None, None),
    #                     size=(dp(155), dp(180)),
    #                     source='image/Hexagon.png',
    #                 )
    #
    #             temp_layout.add_widget(temp_widget)
    #             hex_id[num + 1] = {'position': (0, num), 'widget': temp_widget}
    #
    #         elif num < 10:
    #             temp_widget = Image(
    #                     pos=((num - 4.5) * dp(150), self.y - (130 * 1)),
    #
    #
    #                     size_hint=(None, None),
    #                     size=(dp(155), dp(180)),
    #                     source='image/Hexagon.png'
    #                 )
    #
    #             temp_layout.add_widget(temp_widget)
    #             hex_id[num + 1] = {'position': (1, num - 5), 'widget': temp_widget}
    #
    #         elif num < 15:
    #             temp_widget = Image(
    #                     pos=((num - 10) * dp(150), self.y - (130 * 2)),
    #                     size_hint=(None, None),
    #                     size=(dp(155), dp(180)),
    #                     source='image/Hexagon.png'
    #                 )
    #             temp_layout.add_widget(temp_widget)
    #             hex_id[num + 1] = {'position': (2, num - 10), 'widget': temp_widget}
    #
    #         elif num < 20:
    #             temp_widget = Image(
    #                     pos=((num - 14.5) * dp(150), self.y - (130 * 3)),
    #                     size_hint=(None, None),
    #                     size=(dp(155), dp(180)),
    #                     source='image/Hexagon.png'
    #                 )
    #
    #             temp_layout.add_widget(temp_widget)
    #
    #             hex_id[num + 1] = {'position': (3, num - 15), 'widget': temp_widget}
    #
    #         else:
    #             temp_widget = Image(
    #                     pos=((num - 20) * dp(150), self.y - (130 * 4)),
    #                     size_hint=(None, None),
    #                     size=(dp(155), dp(180)),
    #                     source='image/Hexagon.png'
    #                 )
    #
    #             temp_layout.add_widget(temp_widget)
    #
    #             hex_id[num + 1] = {'position': (4, num - 20), 'widget': temp_widget}



# -----

        # test = list(filter(lambda x: hex_id[x]['position'] == (4, 4), hex_id))
        # print(test)
        #
        # for x in test:
        #     hex_id[x]['widget'].color = 0, 0, 0, 1
        #     print(hex_id[x]['position'])


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