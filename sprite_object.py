import pygame as pg
from settings import *
import os #thư viện os để thao tác các tệp và thư mục
from collections import deque #hàng đợi hai đầu cho phép chúng ta thêm và xóa các phần tử ở cả hai đầu

#Class cho các chi tiết tĩnh trong trò chơi, ví dụ đây là cây đuốc, bên dưới sẽ làm animated sprites cho 
#sprites có thể chuyển động được
class SpriteObject:
    def __init__(self, game, path='resources/sprites/static_sprites/candlebra.png', pos=(10.5, 3.5), scale=0.5, shift=0.5):
        #scale: Hệ số tỉ lệ cho việc thay đổi kích thước hình ảnh.
        #shift: Độ dịch chuyển chiều cao của sprite trên màn hình.
        #Thay đổi thông số scale và shift để thay đổi độ cao cho vật thể
        self.game = game
        self.player = game.player
        self.x, self.y = pos
        self.image = pg.image.load(path).convert_alpha()
        self.IMAGE_WIDTH = self.image.get_width()
        self.IMAGE_HALF_WIDTH = self.image.get_width() // 2
        self.IMAGE_RATIO = self.IMAGE_WIDTH / self.image.get_height()
        self.dx, self.dy, self.theta, self.screen_x, self.dist, self.norm_dist = 0, 0, 0, 0, 1, 1
        self.sprite_half_width = 0
        self.SPRITE_SCALE = scale
        self.SPRITE_HEIGHT_SHIFT = shift

    def get_sprite_projection(self):  #Thêm sprite được chia tỷ lệ và định vị vào danh sách các đối tượng sẽ được hiển thị.
            proj = SCREEN_DIST / self.norm_dist * self.SPRITE_SCALE
            proj_width, proj_height = proj * self.IMAGE_RATIO, proj

            image = pg.transform.scale(self.image, (proj_width, proj_height))

            self.sprite_half_width = proj_width // 2
            height_shift = proj_height * self.SPRITE_HEIGHT_SHIFT
            pos = self.screen_x - self.sprite_half_width, HALF_HEIGHT - proj_height // 2 + height_shift

            self.game.raycasting.objects_to_render.append((self.norm_dist, image, pos))

    def get_sprite(self): #Hàm xử lí hình ảnh họa tiết khi người chơi nhìn vào 
        dx = self.x - self.player.x
        dy = self.y - self.player.y
        self.dx, self.dy = dx, dy
        self.theta = math.atan2(dy, dx)

        #Xử lí khi nhân vật đi gần vào họa tiết thì chiều cao sẽ được tăng lên
        delta = self.theta - self.player.angle
        if (dx > 0 and self.player.angle > math.pi) or (dx < 0 and dy < 0):
            delta += math.tau

        delta_rays = delta / DELTA_ANGLE
        self.screen_x = (HALF_NUM_RAYS + delta_rays) * SCALE

        self.dist = math.hypot(dx, dy)
        self.norm_dist = self.dist * math.cos(delta)
        if -self.IMAGE_HALF_WIDTH < self.screen_x < (WIDTH + self.IMAGE_HALF_WIDTH) and self.norm_dist > 0.5:
            self.get_sprite_projection()

    def update(self):
        self.get_sprite()


class AnimatedSprite(SpriteObject): #Lớp để tạo chi tiết động cho trò chơi
    def __init__(self, game, path='resources/sprites/animated_sprites/green_light/0.png',
                 pos=(11.5, 3.5), scale=0.8, shift=0.16, animation_time=120):
        super().__init__(game, path, pos, scale, shift)
        self.animation_time = animation_time
        self.path = path.rsplit('/', 1)[0] #Lặp qua các ảnh để lưu vào biến
        self.images = self.get_images(self.path) #Chạy biến đó để hiện thị hình ảnh 
        self.animation_time_prev = pg.time.get_ticks()
        self.animation_trigger = False

    def update(self): #Cập nhật lên màn hình
        super().update()
        self.check_animation_time()
        self.animate(self.images)

    def animate(self, images): #Hàm animate hoạt động cùng với hàm check_animation_time để cập nhật khung hình động theo định kỳ.
        if self.animation_trigger:
            images.rotate(-1)
            self.image = images[0]

    def check_animation_time(self): #Hàm xử lí cho các ảnh chạy ổn định bất kể khung hình của trò chơi
        self.animation_trigger = False
        time_now = pg.time.get_ticks()
        if time_now - self.animation_time_prev > self.animation_time:
            self.animation_time_prev = time_now
            self.animation_trigger = True

    def get_images(self, path): #Lấy hình ảnh từ folder 
        images = deque()
        for file_name in os.listdir(path):
            if os.path.isfile(os.path.join(path, file_name)):
                img = pg.image.load(path + '/' + file_name).convert_alpha()
                images.append(img)
        return images
 