from kivymd.uix.screen import MDScreen
from kivymd.uix.floatlayout import MDFloatLayout
from kivy.uix.image import Image
from kivy.metrics import dp
from kivy.clock import Clock
from kivy.uix.behaviors import ButtonBehavior
from functools import partial
from kivy.animation import Animation
from kivy.properties import ListProperty
from kivy.properties import StringProperty

class ImageButton(ButtonBehavior, Image):

    hex_status = StringProperty('undiscovered', Options=('undiscovered', 'discovered', 'discoverable'))
    hex_position = ListProperty(None)
    hex_tile = StringProperty(None)

    def __init__(self, **kwargs):
        super(ImageButton, self).__init__(**kwargs)
        self.source = 'images/tiles/emptytile.png'
        self.size_hint = (None, None)
        self.size = (dp(200), dp(200))
        self.opacity = 0.1

    def on_hex_status(self, obj, value):

        if self.hex_status == "discovered":

            self.opacity = 1
            self.source = f"images/tiles/{self.hex_tile}.png"

            if self.hex_position != [0, 4]:
                anim_sequence = Animation(size=(dp(250), dp(250)), duration=0.3) +\
                                Animation(size=(dp(200), dp(200)), duration=0.3)
                anim_sequence.start(self)

        if self.hex_status == "discoverable":
            self.opacity = 0.5
            self.disabled = False

    def collide_point(self, x, y):
        # return (self.x + dp(30)) <= x <= (self.right - dp(30)) and (
        #         self.y + dp(30)) <= y <= (self.top - dp(30))
        return (x - self.center_x)**2 + (y - self.center_y)**2 < (self.width/2.2)**2

class DiscoverScreen(MDScreen):

    hex_id = dict()

    def __init__(self, **kwargs):
        super(DiscoverScreen, self).__init__(**kwargs)
        Clock.schedule_once(self.create_map, 0.1)

    def create_map(self, *args):
        from systems.generatetiles import tile_generation

        for num in range(0, 25):
            temp_layout = MDFloatLayout()
            self.ids.discover_tiles.add_widget(temp_layout)

            if num < 5:
                temp_widget = ImageButton(
                    pos=(num * (dp(200) * 0.98), self.y),
                    hex_position=[num, 4],
                    on_release=partial(self.reveal_tile, num + 1),
                )

                temp_layout.add_widget(temp_widget)
                self.hex_id[num + 1] = temp_widget

            elif num < 10:
                temp_widget = ImageButton(
                    pos=((num - 4.5) * (dp(200) * 0.98), dp(200) * (-0.74 * 1)),
                    hex_position=[num - 5, 3],
                    on_release=partial(self.reveal_tile, num + 1),
                )

                temp_layout.add_widget(temp_widget)
                self.hex_id[num + 1] = temp_widget

            elif num < 15:
                temp_widget = ImageButton(
                    pos=((num - 10) * (dp(200) * 0.98), dp(200) * (-0.74 * 2)),
                    hex_position=[num - 10, 2],
                    on_release=partial(self.reveal_tile, num + 1),
                )
                temp_layout.add_widget(temp_widget)
                self.hex_id[num + 1] = temp_widget

            elif num < 20:
                temp_widget = ImageButton(
                    pos=((num - 14.5) * (dp(200) * 0.98), dp(200) * (-0.74 * 3)),
                    hex_position=[num - 15, 1],
                    on_release=partial(self.reveal_tile, num + 1),
                )

                temp_layout.add_widget(temp_widget)
                self.hex_id[num + 1] = temp_widget

            else:
                temp_widget = ImageButton(
                    pos=(dp(num - 20) * (dp(200) * 0.98), dp(200) * (-0.74 * 4)),
                    hex_position=[num - 20, 0],
                    on_release=partial(self.reveal_tile, num + 1),
                )

                temp_layout.add_widget(temp_widget)
                self.hex_id[num + 1] = temp_widget

        river_position, remaining_tiles = tile_generation()

        # Filter out hexs that will contain rivers and set information.
        for item in filter(lambda x: x if self.hex_id[x].hex_position in river_position else None, self.hex_id):
            self.hex_id[item].hex_tile = "river"

        # Filter out hexes with empty tiles and set them information.
        none_tile_list = list(filter(lambda x: self.hex_id[x].hex_tile == None, self.hex_id))
        for num in range(0, len(remaining_tiles)):
            self.hex_id[none_tile_list[num]].hex_tile = remaining_tiles[num]

        # Startup Tile Generation
        self.hex_id[13].hex_status = 'discovered'

        tup = [0, 1]



        self.hex_id[13 - 5].hex_status = 'discoverable'
        self.hex_id[13 - 6].hex_status = 'discoverable'
        self.hex_id[13 - 1].hex_status = 'discoverable'
        self.hex_id[13 + 1].hex_status = 'discoverable'
        self.hex_id[13 + 4].hex_status = 'discoverable'
        self.hex_id[13 + 5].hex_status = 'discoverable'

    def reveal_tile(self, tile_num, button):
        if self.hex_id[tile_num].hex_status == 'discoverable':
            self.hex_id[tile_num].hex_status = 'discovered'

            for item in filter(
                    lambda x: x if self.hex_id[x].collide_widget(
                        self.hex_id[tile_num]
                    ) and self.hex_id[x].hex_status != 'discovered' else None, self.hex_id
            ):

                self.hex_id[item].hex_status = 'discoverable'

            # self.hex_id[tile_num - 5].hex_status = 'discoverable'
            # self.hex_id[tile_num - 6].hex_status = 'discoverable'
            # self.hex_id[tile_num - 1].hex_status = 'discoverable'
            # self.hex_id[tile_num + 1].hex_status = 'discoverable'
            # self.hex_id[tile_num + 4].hex_status = 'discoverable'
            # self.hex_id[tile_num + 5].hex_status = 'discoverable'