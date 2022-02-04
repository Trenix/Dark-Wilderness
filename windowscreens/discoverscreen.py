from kivymd.uix.screen import MDScreen
from kivymd.uix.floatlayout import MDFloatLayout
from kivy.uix.image import Image
from kivy.metrics import dp
from kivy.clock import Clock

class DiscoverScreen(MDScreen):

    def __init__(self, **kwargs):
        super(DiscoverScreen, self).__init__(**kwargs)
        Clock.schedule_once(self.create_map, 0.1)

    def create_map(self, *args):
        hex_id = dict()

        for num in range(0, 25):
            temp_layout = MDFloatLayout()
            self.ids.discover_tiles.add_widget(temp_layout)

            if num < 5:
                temp_widget = Image(
                    pos=(self.x + (num * dp(152)), self.y),
                    size_hint=(None, None),
                    size=(dp(155), dp(180)),
                    source='image/pixelhex.png',
                )

                temp_layout.add_widget(temp_widget)
                hex_id[num + 1] = {'position': (0, num), 'widget': temp_widget}

            elif num < 10:
                temp_widget = Image(
                    pos=(dp(num - 4.5) * dp(152), self.y - dp(112 * 1)),

                    size_hint=(None, None),
                    size=(dp(155), dp(180)),
                    source='image/pixelhex.png'
                )

                temp_layout.add_widget(temp_widget)
                hex_id[num + 1] = {'position': (1, num - 5), 'widget': temp_widget}

            elif num < 15:
                temp_widget = Image(
                    pos=(dp(num - 10) * dp(152), self.y - dp(112 * 2)),
                    size_hint=(None, None),
                    size=(dp(155), dp(180)),
                    source='image/pixelhex.png'
                )
                temp_layout.add_widget(temp_widget)
                hex_id[num + 1] = {'position': (2, num - 10), 'widget': temp_widget}

            elif num < 20:
                temp_widget = Image(
                    pos=(dp(num - 14.5) * dp(152), self.y - dp(112 * 3)),
                    size_hint=(None, None),
                    size=(dp(155), dp(180)),
                    source='image/pixelhex.png'
                )

                temp_layout.add_widget(temp_widget)

                hex_id[num + 1] = {'position': (3, num - 15), 'widget': temp_widget}

            else:
                temp_widget = Image(
                    pos=(dp(num - 20) * dp(152), self.y - dp(112 * 4)),
                    size_hint=(None, None),
                    size=(dp(155), dp(180)),
                    source='image/pixelhex.png'
                )

                temp_layout.add_widget(temp_widget)

                hex_id[num + 1] = {'position': (4, num - 20), 'widget': temp_widget}

        # test = list(filter(lambda x: hex_id[x]['position'] == (4, 4), hex_id))
        # print(test)
        #
        # for x in test:
        #     hex_id[x]['widget'].color = 0, 0, 0, 1
        #     print(hex_id[x]['position'])