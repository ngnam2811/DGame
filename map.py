#Tạo ra thế giới cho trò chơi

import pygame as pg

_ = False

mini_map = [
    [1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1],
    [1, _, _, _, _, _, _, _, _, _, _, _, _, _, _, 1],
    [1, _, _, 5, 3, 3, 3, _, _, _, 2, 2, 2, _, _, 1],
    [1, _, _, _, _, _, 4, _, _, _, _, _, 2, _, _, 1],
    [1, _, _, _, _, _, 4, _, _, _, _, _, 2, _, _, 1],
    [1, _, _, 5, 3, 3, 3, _, _, _, _, _, _, _, _, 1],
    [1, _, _, _, _, _, _, _, _, _, _, _, _, _, _, 1],
    [1, _, _, _, 4, _, _, _, 4, _, _, _, _, _, _, 1],
    [1, 1, 1, 3, 1, 3, 1, 1, 1, 3, _, _, 3, 1, 1, 1],
    [1, 1, 1, 1, 1, 1, 1, 1, 1, 3, _, _, 3, 1, 1, 1],
    [1, 1, 1, 1, 1, 1, 1, 1, 1, 3, _, _, 3, 1, 1, 1],
    [1, 1, 3, 1, 1, 1, 1, 1, 1, 3, _, _, 3, 1, 1, 1],
    [1, 4, _, _, _, _, _, _, _, _, _, _, _, _, _, 1],
    [3, _, _, _, _, _, _, _, _, _, _, _, _, _, _, 1],
    [1, _, _, _, _, _, _, _, _, _, _, _, _, _, _, 1],
    [1, _, _, 2, _, _, _, _, _, 3, 4, _, 4, 3, _, 1],
    [1, _, _, 5, _, _, _, _, _, _, 3, _, 3, _, _, 1],
    [1, _, _, 2, _, _, _, _, _, _, _, _, _, _, _, 1],
    [1, _, _, _, _, _, _, _, _, _, _, _, _, _, _, 1],
    [3, _, _, _, _, _, _, _, _, _, _, _, _, _, _, 1],
    [1, 4, _, _, _, _, _, _, 4, _, _, 4, _, _, _, 1],
    [1, 1, 3, 3, _, _, 3, 3, 1, 3, 3, 1, 3, 1, 1, 1],
    [1, 1, 1, 3, _, _, 3, 1, 1, 1, 1, 1, 1, 1, 1, 1],
    [1, 3, 3, 4, _, _, 4, 3, 3, 3, 3, 3, 3, 3, 3, 1],
    [3, _, _, _, _, _, _, _, _, _, _, _, _, _, _, 3],
    [3, _, _, _, _, _, _, _, _, _, _, _, _, _, _, 3],
    [3, _, _, _, _, _, _, _, _, _, _, _, _, _, _, 3],
    [3, _, _, 5, _, _, _, 5, _, _, _, 5, _, _, _, 3],
    [3, _, _, _, _, _, _, _, _, _, _, _, _, _, _, 3],
    [3, _, _, _, _, _, _, _, _, _, _, _, _, _, _, 3],
    [3, _, _, _, _, _, _, _, _, _, _, _, _, _, _, 3],
    [3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3],
]


class Map:
    def __init__(self, game):
        self.game = game
        self.mini_map = mini_map #Lưu trữ bản mini_map của trò chơi.
        self.world_map = {} #Một dictionary để lưu trữ tọa độ và giá trị của các ô trên bản đồ.
        self.rows = len(self.mini_map)
        self.cols = len(self.mini_map[0])
        self.get_map() #để tạo world_map từ mini_map

    def get_map(self):
        for j, row in enumerate(self.mini_map): #Vòng lặp này duyệt qua từng hàng (row) trong mini_map.
            # enumerate(self.mini_map) trả về cặp giá trị (j, row) trong đó j là chỉ số của hàng và row là nội dung của hàng đó.
            for i, value in enumerate(row): #Vòng lặp này duyệt qua từng giá trị (value) trong hàng hiện tại (row).
                if value: #Nếu value không phải là giá trị False (trong trường hợp này là _), tức là ô có nội dung, thì thực hiện
                    self.world_map[(i, j)] = value #Sử dụng cặp tọa độ (i, j) làm khóa trong từ điển world_map,
                    #trong đó i là chỉ số cột và j là chỉ số hàng.
                    #giá trị của 1 ô là value

    def draw(self):
        [pg.draw.rect(self.game.screen, 'darkgray', (pos[0] * 100, pos[1] * 100, 100, 100), 2)    
        for pos in self.world_map]

        #Duyệt qua các phần tử trong từ điển world_map:
        #self.world_map chứa các cặp tọa độ và giá trị của các ô trên bản đồ thế giới đã được lưu ở trên.
        #Mỗi pos trong vòng lặp này là một cặp tọa độ (i, j) của một ô trên bản đồ thế giới.


        #pg.draw.rect() được sử dụng để vẽ hình chữ nhật.
        #(pos[0] * 100, pos[1] * 100, 100, 100) là tuple chứa thông tin về vị trí và kích thước của hình chữ nhật:

        #pos[0] * 100 là tọa độ x của góc trái trên của hình chữ nhật.
        #pos[1] * 100 là tọa độ y của góc trái trên của hình chữ nhật.
        #100, 100 là chiều rộng và chiều cao của hình chữ nhật, ở đây là 100 pixel.
        #2 là độ dày của viền của hình chữ nhật.