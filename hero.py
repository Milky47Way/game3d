key_switch_camera = 'f'  # від якого обличчя
key_switch_mode = 'z'  # проходить через перешкоди чи ні
key_forward = 'arrow_up' # вперед
key_back = 'arrow_down'  # назад
key_left = 'arrow_left'  # вліво
key_right = 'arrow_right'  # вправо

key_up = 'u'  # вгору
key_down = 'd'  # вниз

key_turn_left = 'q'
key_turn_right = 'r'

key_build = 'mouse1'
key_destroy = 'mouse3'

step = 1


class Hero():
    def __init__(self, pos, land):
        self.land = land
        self.mode = True  # крізь усе
        self.hero = loader.loadModel('panda')  # hero.egg + texture

        model.reparentTo(self.render)
        base_texture = loader.loadTexture('models/backgrounds/

        model.setTexture(base_texture)
        #self.hero.setScale(1.0)
        self.hero.setColor(1, 0.5, 0)
        self.hero.setColor(0.3)
        self.hero.setPos(pos)
        self.hero.reparentTo(render)
        self.cameraBind()
        self.accept_events()

    def cameraBind(self):
        base.disableMouse()
        base.camera.setH(180)
        base.camera.reparentTo(self.hero)
        base.camera.setPos(0, 0, 1.5)
        self.cameraOn = True

    def cameraUp(self):
        x, y, z = self.hero.getPos()
        base.mouseInterfaceNode.setPos(-x, -y, -z - 3)
        base.camera.reparentTo(render)
        base.enableMouse()
        self.cameraOn = False

    def changeView(self):
        if self.cameraOn:
            self.cameraUp()
        else:
            self.cameraBind()

    def turn_left(self):
        self.hero.setH((self.hero.getH() + 5) % 360)

    def turn_right(self):
        """Поворот героя вправо (зміна кута погляду проти годинникової стрілки)."""
        self.hero.setH((self.hero.getH() - 5) % 360)

    def look_at(self, angle):  # розраховує в який напрямок треба рухатись, координати
        x_from = self.hero.getX()
        y_from = self.hero.getY()
        z_from = self.hero.getZ()
        dx, dy = self.check_dir(angle)
        x_to = x_from + dx
        y_to = y_from + dy
        return x_to, y_to, z_from

    def just_move(self, angle):
        x, y, z = self.look_at(angle)
        if not self.land.isBlockAt((round(x), round(y), round(z))):
            self.hero.setPos((x, y, z))
            print(f"Герой переміщений на {(x, y, z)}")
        else:
            print(f"Неможливо рухатись, є блок на {(x, y, z)}")

    def look_at(self, angle):

        x_from = self.hero.getX()
        y_from = self.hero.getY()
        z_from = self.hero.getZ()
        dx, dy = self.check_dir(angle)
        x_to = x_from + dx
        y_to = y_from + dy
        return x_to, y_to, z_from

    def just_move(self, angle):
        x, y, z = self.look_at(angle)
        if not self.land.isBlockAt((round(x), round(y), round(z))):
            self.hero.setPos((x, y, z))
            print(f"Герой переміщений на {(x, y, z)}")
        else:
            print(f"Неможливо рухатись, є блок на {(x, y, z)}")

    def move_to(self, angle):
        if self.mode:
            self.just_move(angle)

    def check_dir(self, angle):
        if angle >= 0 and angle <= 20:
            return (0, -step)
        elif angle <= 65:
            return (step, -step)
        elif angle <= 110:
            return (step, 0)
        elif angle <= 155:
            return (step, step)
        elif angle <= 200:
            return (0, step)
        elif angle <= 245:
            return (-step, step)
        elif angle <= 290:
            return (-step, 0)
        elif angle <= 335:
            return (-step, -step)
        else:
            return (0, -step)

    def forward(self):
        angle = (self.hero.getH()) % 360
        self.move_to(angle)

    def back(self):
        angle = (self.hero.getH() + 180) % 360
        self.move_to(angle)

    def left(self):
        angle = (self.hero.getH() + 90) % 360
        self.move_to(angle)

    def right(self):
        angle = (self.hero.getH() + 270) % 360
        self.move_to(angle)

    def move_up(self):
        x, y, z = self.hero.getPos()
        if not z == 8:
            new_pos = (x, y, z + step)
            self.hero.setPos(new_pos)

    def move_down(self):
        x, y, z = self.hero.getPos()
        if not z == 0 and not self.land.isBlockAt((round(x), round(y), round(z - step))):
            new_pos = (x, y, z - step)
            self.hero.setPos(new_pos)

    def switch_mode(self):
        if self.mode:
            self.mode = False
            print("Тепер неможна проходити крізь перешкоди")
        else:
            self.mode = True
            print("Тепер можна проходити крізь перешкоди")

    def build(self):
        angle = self.hero.getH() % 360
        pos = self.look_at(angle)
        if self.mode:
            self.land.addBlock(pos)
        else:
            self.land.buildBlock(pos)

    def destroy(self):
        angle = self.hero.getH() % 360
        pos = self.look_at(angle)
        if self.mode:
            self.land.delBlock(pos)
        else:
            self.land.delBlockFrom(pos)

    def accept_events(self):
        base.accept(key_turn_left, self.turn_left)
        base.accept(key_turn_left + '-repeat', self.turn_left)
        base.accept(key_turn_right, self.turn_right)
        base.accept(key_turn_right + '-repeat', self.turn_right)

        base.accept(key_forward, self.forward)
        base.accept(key_forward + '-repeat', self.forward)
        base.accept(key_back, self.back)
        base.accept(key_back + '-repeat', self.back)
        base.accept(key_left, self.left)
        base.accept(key_left + '-repeat', self.left)
        base.accept(key_right, self.right)
        base.accept(key_right + '-repeat', self.right)

        base.accept(key_down, self.move_down)
        base.accept(key_up, self.move_up)

        base.accept(key_switch_camera, self.changeView)

        base.accept(key_switch_mode, self.switch_mode)
        base.accept(key_build, self.build)
        base.accept(key_destroy, self.destroy)

        base.accept('k', self.land.saveMap)
        base.accept('l', self.land.loadMap)
