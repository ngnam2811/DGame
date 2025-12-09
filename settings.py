#Lưu trữ các cài đặt của trò chơi

import math

RES = WIDTH, HEIGHT = 1400, 760
HALF_WIDTH = WIDTH // 2
HALF_HEIGHT = HEIGHT // 2
FPS = 0

#Setting khởi tạo cho player

PLAYER_POS = 1.5, 5  # mini_map lần đầu xuất hiện
PLAYER_ANGLE = 0 #góc nhìn nhân vật
PLAYER_SPEED = 0.004 #tốc độ di chuyển
PLAYER_ROT_SPEED = 0.002 #tốc độ quay rotation
PLAYER_SIZE_SCALE = 60
PLAYER_MAX_HEALTH = 100

#Xác định hướng nhìn của nhân vật

FOV = math.pi / 3
HALF_FOV = FOV / 2
NUM_RAYS = WIDTH // 2
HALF_NUM_RAYS = NUM_RAYS // 2
DELTA_ANGLE = FOV / NUM_RAYS
MAX_DEPTH = 20

SCREEN_DIST = HALF_WIDTH / math.tan(HALF_FOV)
SCALE = WIDTH // NUM_RAYS

TEXTURE_SIZE = 256
HALF_TEXTURE_SIZE = TEXTURE_SIZE // 2

#Thêm tốc độ chuột
MOUSE_SENSITIVITY = 0.0002
MOUSE_MAX_REL = 40
MOUSE_BORDER_LEFT = 100
MOUSE_BORDER_RIGHT = WIDTH - MOUSE_BORDER_LEFT


#Màu sàn nhà
FLOOR_COLOR = (30, 30, 30)