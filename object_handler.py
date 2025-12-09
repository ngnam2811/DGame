from sprite_object import *
from npc import *
from random import choices, randrange

class ObjectHandler: #chịu trách nhiệm quản lý các đối tượng trong trò chơi,
    #bao gồm việc tạo, cập nhật và kiểm tra trạng thái của các sprite và NPC 
    def __init__(self, game):
        self.game = game
        self.sprite_list = []
        self.npc_list = []
        self.npc_sprite_path = 'resources/sprites/npc/'
        self.static_sprite_path = 'resources/sprites/static_sprites/'
        self.anim_sprite_path = 'resources/sprites/animated_sprites/'
        add_sprite = self.add_sprite
        add_npc = self.add_npc
        self.npc_positions = {}


        self.enemies = 20  # npc count
        self.npc_types = [SoldierNPC, CacoDemonNPC, CyberDemonNPC]
        self.weights = [50, 30, 20]
        self.restricted_area = {(i, j) for i in range(10) for j in range(10)}
        self.spawn_npc()

        # sprite map
        add_sprite(AnimatedSprite(game))
        add_sprite(AnimatedSprite(game, pos=(1.5, 1.5)))
        add_sprite(AnimatedSprite(game, pos=(1.5, 7.5)))
        add_sprite(AnimatedSprite(game, pos=(5.5, 3.25)))
        add_sprite(AnimatedSprite(game, pos=(5.5, 4.75)))
        add_sprite(AnimatedSprite(game, pos=(7.5, 2.5)))
        add_sprite(AnimatedSprite(game, pos=(7.5, 5.5)))
        add_sprite(AnimatedSprite(game, pos=(14.5, 1.5)))
        add_sprite(AnimatedSprite(game, path=self.anim_sprite_path + 'red_light/0.png', pos=(14.5, 7.5)))
        add_sprite(AnimatedSprite(game, path=self.anim_sprite_path + 'red_light/0.png', pos=(12.5, 7.5)))
        add_sprite(AnimatedSprite(game, path=self.anim_sprite_path + 'red_light/0.png', pos=(9.5, 7.5)))


        # npc map
        # add_npc(NPC(game))
        # add_npc(NPC(game))

    def spawn_npc(self): #Tạo và thêm các NPC vào trò chơi.
        #Chọn ngẫu nhiên một loại NPC dựa trên trọng số.
        #Chọn vị trí ngẫu nhiên cho NPC, đảm bảo vị trí không nằm trong khu vực hạn chế hoặc trên bản đồ thế giới.
        #Thêm NPC vào danh sách NPC. 
        for i in range(self.enemies):
                npc = choices(self.npc_types, self.weights)[0]
                pos = x, y = randrange(self.game.map.cols), randrange(self.game.map.rows)
                while (pos in self.game.map.world_map) or (pos in self.restricted_area):
                    pos = x, y = randrange(self.game.map.cols), randrange(self.game.map.rows)
                self.add_npc(npc(self.game, pos=(x + 0.5, y + 0.5)))

    def check_win(self): #Kiểm tra xem người chơi đã thắng chưa.
        #Nếu danh sách vị trí NPC trống (tức là không còn NPC sống sót), người chơi thắng.
        #Hiển thị thông báo thắng, tạm dừng và bắt đầu trò chơi mới.
        if not len(self.npc_positions):
            self.game.object_render.win()
            pg.display.flip()
            pg.time.delay(1500)
            self.game.new_game()

    def update(self):
        #Cập nhật trạng thái của tất cả các sprite và NPC.
        #Cập nhật danh sách vị trí NPC dựa trên các NPC còn sống.
        #Gọi phương thức update cho mỗi sprite và NPC trong danh sách.

        self.npc_positions = {npc.map_pos for npc in self.npc_list if npc.alive} #Phòng tránh việc có nhiều hơn 1
        #ncp thì tọa tộ của 2 npc có thể trùng nhau nên vô lí
        [sprite.update() for sprite in self.sprite_list]
        [npc.update() for npc in self.npc_list]
        self.check_win()

    def add_npc(self, npc):
        self.npc_list.append(npc)

    def add_sprite(self, sprite):
        self.sprite_list.append(sprite)


    #Thêm một NPC hoặc một sprite vào danh sách tương ứng.
    #add_npc: Thêm NPC vào danh sách NPC.
    #add_sprite: Thêm sprite vào danh sách sprite.