from direct.showbase.ShowBase import ShowBase
from panda3d.core import DirectionalLight, PointLight, AmbientLight
from mapmanageеr import Mapmanager
from hero import Hero

class Game(ShowBase):
   def __init__(self):
       ShowBase.__init__(self)
       self.land = Mapmanager()
       self.land.loadLand("land.txt")

       x, y = self.land.loadLand("land.txt")
       self.hero = Hero((x // 2, y // 2, 2), self.land)

       base.camLens.setFov(90)

       # небо
       model = self.loader.loadModel('models/backgrounds/sky_sphere')
       model.reparentTo(self.render)
       base_texture = loader.loadTexture('models/backgrounds/skyy.jpg')
       model.setTexture(base_texture)

       model.setPos(24, 0, 0)
       model.setScale(65, 65, 65)
       model.setHpr(90, 0, 0)

       # пташка
       model1 = self.loader.loadModel('models/bird/bird1')
       model1.reparentTo(self.render)
       base_texture = loader.loadTexture('models/bird/BirdyTexture.tif')
       model1.setTexture(base_texture)

       model1.setColor((0, 0, 0.6, 0))
       model1.setPos(5, 0, 8)
       model1.setScale(4, 4, 4)
       model1.setHpr(0, 0, 0)

       #планети
       model0 = self.loader.loadModel('models/planets/planet_sphere')
       model0.reparentTo(self.render)
       base_texture = loader.loadTexture('models/planets/bb.jpg')
       model0.setTexture(base_texture)

       # model1.setColor((0, 0, 0.6, 0))
       model0.setPos(9, 0, 30)
       model0.setScale(7, 7, 7)
       model0.setHpr(0, 0, 0)

       self.setupLighting()

       model2 = self.loader.loadModel('models/planets/planet_sphere')
       model2.reparentTo(self.render)
       base_texture = loader.loadTexture('models/planets/moon.png')
       model2.setTexture(base_texture)

       model2.setPos(12, 0, -14)
       model2.setScale(4, 4, 4)
       model2.setHpr(0, 0, 0)

       model3 = self.loader.loadModel('models/planets/planet_sphere')
       model3.reparentTo(self.render)
       base_texture = loader.loadTexture('models/planets/v.jpg')
       model3.setTexture(base_texture)

       # model1.setColor((0, 0, 0.6, 0))
       model3.setPos(56, 0, 20)
       model3.setScale(4, 4, 4)
       model3.setHpr(0, 0, 0)



   def setupLighting(self):
       directionalLight = DirectionalLight("directionalLight")
       directionalLight.setColor((1, 1, 1, 1))  # Біле світло
       directionalLightNP = self.render.attachNewNode(directionalLight)
       directionalLightNP.setHpr(-45, -45, 0)  # Кут освітлення
       self.render.setLight(directionalLightNP)

           # Додати розсіяне світло
       ambientLight = AmbientLight("ambientLight")
       ambientLight.setColor((0.6, 0.6, 0.6, 1))  # М'яке, тьмяне світло
       ambientLightNP = self.render.attachNewNode(ambientLight)
       self.render.setLight(ambientLightNP)

           # Додати точкове світло (опціонально)
       pointLight = PointLight("pointLight")
       pointLight.setColor((1, 1, 1, 1))  # Біле світло
       pointLightNP = self.render.attachNewNode(pointLight)
       pointLightNP.setPos(10, 10, 15)  # Позиція світла
       self.render.setLight(pointLightNP)


game = Game()
game.run()