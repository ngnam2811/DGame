from settings import *
import pygame as pg
import math

class Player:
    def __init__(self, game):
        self.game = game
        self.x, self.y = PLAYER_POS
        self.angle = PLAYER_ANGLE
        self.shot = False
        self.health = PLAYER_MAX_HEALTH
        self.rel = 0
        self.health_recovery_delay = 700
        self.time_prev = pg.time.get_ticks()

    def recover_health(self):
        if self.check_health_recovery_delay() and self.health < PLAYER_MAX_HEALTH:
            self.health += 1

    def check_health_recovery_delay(self):
        time_now = pg.time.get_ticks()
        if time_now - self.time_prev > self.health_recovery_delay:
            self.time_prev = time_now
            return True
        
    def check_game_over(self):
        if self.health < 1:
            self.game.object_render.game_over()
            pg.display.flip()
            pg.time.delay(1500)
            self.game.new_game()

    def get_damage(self, damage):
        self.health -= damage
        self.game.object_render.player_damage()
        self.game.sound.player_pain.play()
        self.check_game_over()


    def single_fire_event(self, event):
        if event.type == pg.MOUSEBUTTONDOWN:
            if event.button == 1 and not self.shot and not self.game.weapon.reloading:
                self.game.sound.shotgun.play()
                self.shot = True
                self.game.weapon.reloading = True

    def movement(self):
        sin_a = math.sin(self.angle)
        cos_a = math.cos(self.angle)
        dx, dy = 0, 0

        #Important
        #Nếu muốn tốc độ di chuyển của người chơi độc lập với 
        #tốc độ khung hình thì cần sử dụng delta time để lấy cho mỗi khung hình

        #delta time là khoảng thời gian giữa khung hình cuối cùng và khung hình hiện tại

        speed = PLAYER_SPEED * self.game.delta_time
        speed_sin = speed * sin_a
        speed_cos = speed * cos_a


        #Tạo cái phím di chuyển
        keys = pg.key.get_pressed()
        if keys[pg.K_w]:
            dx += speed_cos
            dy += speed_sin
        if keys[pg.K_s]:
            dx += -speed_cos
            dy += -speed_sin
        if keys[pg.K_a]:
            dx += speed_sin
            dy += -speed_cos
        if keys[pg.K_d]:
            dx += -speed_sin
            dy += speed_cos

        self.check_wall_collision(dx, dy)

        #Áp dụng để quay bằng phím left và right
        # if keys[pg.K_LEFT]:
        #     self.angle -= PLAYER_ROT_SPEED * self.game.delta_time
        # if keys[pg.K_RIGHT]:
        #     self.angle += PLAYER_ROT_SPEED * self.game.delta_time
        self.angle %= math.tau

        #tau = 2pi 
        # Đây thường được sử dụng để đảm bảo rằng góc hướng được biểu diễn trong khoảng từ 0 đến 2π

    def check_wall(self, x, y): #kiểm tra tọa độ nếu chạm vào tường
        return (x, y) not in self.game.map.world_map

    def check_wall_collision(self, dx, dy): #Kiểm tra va chạm
        scale = PLAYER_SIZE_SCALE / self.game.delta_time
        if self.check_wall(int(self.x + dx * scale), int(self.y)):
            self.x += dx
        if self.check_wall(int(self.x), int(self.y + dy * scale)):
            self.y += dy
        #chỉ cho phép di chuyển khi không có tường

    #Hàm draw được sử dụng để vẽ người chơi lên màn hình của trò chơi
    def draw(self):
        #Hàm line để vẽ đường thẳng đại diện cho hướng nhìn của người chơi
        # pg.draw.line(self.game.screen, 
        #             'yellow',
        #             (self.x * 50, self.y * 50),
        #             (self.x * 50 + WIDTH * math.cos(self.angle), self.y * 50 + WIDTH * math. sin(self.angle)),
        #             2)

        pg.draw.circle(self.game.screen, 'green', (self.x * 100, self.y * 100), 15)
    
    def mouse_control(self):
        mx, my = pg.mouse.get_pos()
        if mx < MOUSE_BORDER_LEFT or mx > MOUSE_BORDER_RIGHT:
            pg.mouse.set_pos([HALF_WIDTH, HALF_HEIGHT])
        self.rel = pg.mouse.get_rel()[0]
        self.rel = max(-MOUSE_MAX_REL, min(MOUSE_MAX_REL, self.rel))
        self.angle += self.rel * MOUSE_SENSITIVITY * self.game.delta_time



    def update(self):
        self.movement()
        self.mouse_control()
        self.recover_health()


    #Tạo 2 thuộc tính cho player 
    #pos:
    #Phương thức này trả về một bộ (tuple) chứa tọa độ x và y của người chơi
    @property
    def pos(self):
        return self.x, self.y

    @property
    def map_pos(self):
        return int(self.x), int(self.y)