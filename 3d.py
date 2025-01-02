#pip install panda3d

from direct.showbase.ShowBase import ShowBase #сцена
#base = ShowBase() 
# ↑ об'єкт від класу
#base.run() 
# ↑ викл. метод run

#сцена, висота персонажа..
class Game(ShowBase):
    def __init__(self):
        ShowBase.__init__(self)
        #self.model = loader.loadModel('models/enviroment')
        self.model = loader.loadModel('models/Fighter.egg')
        self.model.reparentTo(render)
        self.model.setScale(0.1)#self.model
        self.model.setPos(-2, 25, -3)
        base.camLens.setFov(90) #189 max

game = Game()
game.run()
