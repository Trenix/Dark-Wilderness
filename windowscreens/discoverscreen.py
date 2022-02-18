from kivymd.uix.screen import MDScreen
from kivymd.uix.floatlayout import MDFloatLayout
from kivy.uix.image import Image
from kivy.metrics import dp
from kivy.clock import Clock
from kivy.uix.behaviors import ButtonBehavior
from kivy.graphics import Rectangle
from kivy.uix.button import Button
from kivymd.app import MDApp
import random

class ImageButton(ButtonBehavior, Image):
    def collide_point(self, x, y):
        # return (self.x + dp(30)) <= x <= (self.right - dp(30)) and (
        #         self.y + dp(30)) <= y <= (self.top - dp(30))
        return (x - self.center_x)**2 + (y - self.center_y)**2 < (self.width/2.2)**2

class DiscoverScreen(MDScreen):

    def __init__(self, **kwargs):
        super(DiscoverScreen, self).__init__(**kwargs)
        Clock.schedule_once(self.create_map, 0.1)


    def create_map(self, *args):

        tiles = ['EmptyTile.png', 'Forest.png', 'Grassland.png', 'Hills.png', 'Lake.png',
                 'Marsh.png', 'Mountain.png', 'River.png', 'Swamp.png']


        hex_id = dict()

        for num in range(0, 25):
            temp_layout = MDFloatLayout()
            self.ids.discover_tiles.add_widget(temp_layout)

            if num < 5:
                temp_widget = ImageButton(
                    source=f'images/tiles/{tiles[random.randrange(1,9)]}',
                    size_hint=(None, None),
                    size=(dp(200), dp(200)),
                    pos=(num * (dp(200) * 0.98), self.y),
                    on_release=self.test,
                )

                temp_layout.add_widget(temp_widget)
                hex_id[num + 1] = {'position': (0, num), 'widget': temp_widget}

            elif num < 10:
                temp_widget = ImageButton(
                    pos=((num - 4.5) * (dp(200) * 0.98), dp(200) * (-0.74 * 1)),
                    size_hint=(None, None),
                    size=(dp(200), dp(200)),
                    source=f'images/tiles/{tiles[random.randrange(1,9)]}',
                    on_release=self.test2,
                )

                temp_layout.add_widget(temp_widget)
                hex_id[num + 1] = {'position': (1, num - 5), 'widget': temp_widget}

            elif num < 15:
                temp_widget = ImageButton(
                    pos=((num - 10) * (dp(200) * 0.98), dp(200) * (-0.74 * 2)),
                    size_hint=(None, None),
                    size=(dp(200), dp(200)),
                    source=f'images/tiles/{tiles[random.randrange(1,9)]}',
                )
                temp_layout.add_widget(temp_widget)
                hex_id[num + 1] = {'position': (2, num - 10), 'widget': temp_widget}

            elif num < 20:
                temp_widget = ImageButton(
                    pos=((num - 14.5) * (dp(200) * 0.98), dp(200) * (-0.74 * 3)),
                    size_hint=(None, None),
                    size=(dp(200), dp(200)),
                    source=f'images/tiles/{tiles[random.randrange(1,9)]}',
                )

                temp_layout.add_widget(temp_widget)

                hex_id[num + 1] = {'position': (3, num - 15), 'widget': temp_widget}

            else:
                temp_widget = ImageButton(
                    pos=(dp(num - 20) * (dp(200) * 0.98), dp(200) * (-0.74 * 4)),
                    size_hint=(None, None),
                    size=(dp(200), dp(200)),
                    source=f'images/tiles/{tiles[random.randrange(1,9)]}',
                )

                temp_layout.add_widget(temp_widget)

                hex_id[num + 1] = {'position': (4, num - 20), 'widget': temp_widget}

    def test(self, button):
        print('works')
        print('images/tiles/*.png')

    def test2(self, button):
        print('works2')

        # test = list(filter(lambda x: hex_id[x]['position'] == (4, 4), hex_id))
        # print(test)
        #
        # for x in test:
        #     hex_id[x]['widget'].color = 0, 0, 0, 1
        #     print(hex_id[x]['position'])