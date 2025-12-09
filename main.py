import pygame as pg
import sys #thu vien builtin cua python
from settings import *
from map import *
from player import *
from raycasting import *
from object_render import *
from sprite_object import *
from object_handler import *
from weapon import *
from sound import *
from pathfinding import *

class Game:
    def __init__(self):
        pg.init() #Khởi tạo game
        pg.mouse.set_visible(False) #Cho con trỏ chuột biến mất trên màn hình game
        self.screen = pg.display.set_mode(RES) #Tạo một cửa sổ trò chơi với kích thước được định nghĩa ở setting
        self.clock = pg.time.Clock() #Khởi tạo một đối tượng clock để theo dõi thời gian trong trò chơi
        self.delta_time = 1
        self.global_trigger = False #Tạo 1 biến chung để set thời gian animated die cho npc 
        self.global_event = pg.USEREVENT + 0
        pg.time.set_timer(self.global_event, 40)
        self.new_game()

    def new_game(self):
        self.map = Map(self)
        self.player = Player(self)
        self.object_render = ObjectRenderer(self)
        self.raycasting = RayCasting(self)
        self.object_handler = ObjectHandler(self)
        self.weapon = Weapon(self)
        self.sound = Sound(self)
        self.pathfinding = PathFinding(self)
        # pg.mixer.music.play(-1) #Play theme song

    def update(self):
        self.player.update()
        self.raycasting.update()
        self.object_handler.update()
        self.weapon.update()
        pg.display.flip() #Cập nhật màn hình với những thay đổi đã được vẽ.
        self.delta_time = self.clock.tick(FPS) # Điều chỉnh tốc độ của trò chơi để đảm bảo rằng nó chạy với FPS mong muốn.
        pg.display.set_caption(f'{self.clock.get_fps() :.1f}')

    def draw(self):
        # self.screen.fill('black')
        self.object_render.draw()
        self.weapon.draw()
        # self.map.draw()
        # self.player.draw()

    def check_events(self):
        self.global_trigger = False
        for event in pg.event.get():
            if event.type == pg.QUIT or (event.type == pg.KEYDOWN and event.key == pg.K_ESCAPE):
                pg.quit()
                sys.exit()
            elif event.type == self.global_event:
                self.global_trigger = True
            self.player.single_fire_event(event)

    def run(self):
        while True:
            self.check_events()
            self.update()
            self.draw()

if __name__ == '__main__':
    game = Game()
    game.run()