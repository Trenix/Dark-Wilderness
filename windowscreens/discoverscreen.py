from kivymd.uix.screen import MDScreen
from kivymd.uix.floatlayout import MDFloatLayout
from kivy.uix.image import Image
from kivy.metrics import dp
from kivy.clock import Clock
from kivy.uix.behaviors import ButtonBehavior
from functools import partial

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
        from systems.generatetiles import tile_generation
        global hex_id

        hex_id = dict()

        for num in range(0, 25):
            temp_layout = MDFloatLayout()
            self.ids.discover_tiles.add_widget(temp_layout)

            if num < 5:
                temp_widget = ImageButton(
                    source='images/tiles/emptytile.png',
                    size_hint=(None, None),
                    size=(dp(200), dp(200)),
                    pos=(num * (dp(200) * 0.98), self.y),
                    disabled=True,
                    opacity=0.1,
                    on_release=partial(self.reveal_tile, num + 1),
                )

                temp_layout.add_widget(temp_widget)
                hex_id[num + 1] = {'position': (num, 4), 'widget': temp_widget, 'tile': None, 'discovered': False}

            elif num < 10:
                temp_widget = ImageButton(
                    pos=((num - 4.5) * (dp(200) * 0.98), dp(200) * (-0.74 * 1)),
                    size_hint=(None, None),
                    size=(dp(200), dp(200)),
                    source='images/tiles/emptytile.png',
                    disabled=True,
                    opacity=0.1,
                    on_release=partial(self.reveal_tile, num + 1),
                )

                temp_layout.add_widget(temp_widget)
                hex_id[num + 1] = {'position': (num - 5, 3), 'widget': temp_widget, 'tile': None, 'discovered': False}

            elif num < 15:
                temp_widget = ImageButton(
                    pos=((num - 10) * (dp(200) * 0.98), dp(200) * (-0.74 * 2)),
                    size_hint=(None, None),
                    size=(dp(200), dp(200)),
                    opacity=0.1,
                    disabled=True,
                    source='images/tiles/emptytile.png',
                    on_release=self.reveal_tile,
                )
                temp_layout.add_widget(temp_widget)
                hex_id[num + 1] = {'position': (num - 10, 2), 'widget': temp_widget, 'tile': None, 'discovered': False}

            elif num < 20:
                temp_widget = ImageButton(
                    pos=((num - 14.5) * (dp(200) * 0.98), dp(200) * (-0.74 * 3)),
                    size_hint=(None, None),
                    size=(dp(200), dp(200)),
                    opacity=0.1,
                    disabled=True,
                    source='images/tiles/emptytile.png',
                    on_release=self.reveal_tile,
                )

                temp_layout.add_widget(temp_widget)
                hex_id[num + 1] = {'position': (num - 15, 1), 'widget': temp_widget, 'tile': None, 'discovered': False}

            else:
                temp_widget = ImageButton(
                    pos=(dp(num - 20) * (dp(200) * 0.98), dp(200) * (-0.74 * 4)),
                    size_hint=(None, None),
                    size=(dp(200), dp(200)),
                    opacity=0.1,
                    disabled=True,
                    source='images/tiles/emptytile.png',
                    on_release=self.reveal_tile,
                )

                temp_layout.add_widget(temp_widget)
                hex_id[num + 1] = {'position': (num - 20, 0), 'widget': temp_widget, 'tile': None, 'discovered': False}

        # Startup Tile Generation
        hex_id[1]['widget'].opacity = 1
        hex_id[1]['discovered'] = True
        hex_id[2]['widget'].opacity = 0.5
        hex_id[6]['widget'].opacity = 0.5
        hex_id[2]['widget'].disabled = False
        hex_id[6]['widget'].disabled = False

        river_position, remaining_tiles = tile_generation()

        # Filter out hexs that will contain rivers and set information.
        for item in filter(lambda x: x if hex_id[x]['position'] in river_position else None, hex_id):
            hex_id[item]['tile'] = "river"
            # hex_id[item]['widget'].source = 'images/tiles/river.png'

        # Filter out hexes with empty tiles and set them information.
        none_tile_list = list(filter(lambda x: hex_id[x]['tile'] == None, hex_id))

        for num in range(0, len(remaining_tiles)):
            hex_id[none_tile_list[num]]['tile'] = remaining_tiles[num]
            # hex_id[none_tile_list[num]]['widget'].source = f'images/tiles/{remaining_tiles[num]}'


        # list(filter(lambda x, y: hex_id+river_tiles, hex_id, river_tiles))

        # test = list(filter(lambda x: hex_id[x]['position'] == (1, 0), hex_id))
        # # print(test)
        # #
        # for x in test:
        #     hex_id[x]['widget'].color = 0, 0, 0, 1
        #     print(hex_id[x]['position'])


    def reveal_tile(self, tile, button):
        button.opacity = 1
        print(hex_id[tile]['position'])



    def test2(self, button):
        print('works2')

        # test = list(filter(lambda x: hex_id[x]['position'] == (4, 4), hex_id))
        # print(test)
        #
        # for x in test:
        #     hex_id[x]['widget'].color = 0, 0, 0, 1
        #     print(hex_id[x]['position'])