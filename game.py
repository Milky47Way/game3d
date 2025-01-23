from direct.showbase.ShowBase import ShowBase
from panda3d.core import DirectionalLight, PointLight, AmbientLight
from mapmanagеr import Mapmanager
from hero import Hero

class Game(ShowBase):
   def __init__(self):
       ShowBase.__init__(self)
       self.land = Mapmanager()
       self.land.loadLand("land.txt")

       x, y = self.land.loadLand("land.txt")
       self.hero = Hero((x // 2, y // 2, 2), self.land)

       base.camLens.setFov(90)

       #небо
       model = self.loader.loadModel('models/backgrounds/sky_sphere')
       model.reparentTo(self.render)
       base_texture = loader.loadTexture('models/backgrounds/skyy.jpg')
       model.setTexture(base_texture)

       model.setPos(24, 0, 0)
       model.setScale(65, 65, 65)
       model.setHpr(90, 0, 0)

       #пташки
       model1 = self.loader.loadModel('models/bird/bird1')
       model1.reparentTo(self.render)
       base_texture = loader.loadTexture('models/bird/BirdyTexture.tif')
       model1.setTexture(base_texture)

       model1.setColor((0, 0, 0.6, 0))
       model1.setPos(5, 0, 8)
       model1.setScale(4, 4, 4)
       model1.setHpr(0, 0, 0)

       model4 = self.loader.loadModel('models/bird/Chicken2')
       model4.reparentTo(self.render)
       base_texture = loader.loadTexture('models/bird/chicken.tif')
       model4.setTexture(base_texture)
       model4.setPos(3, 22, 1.6)
       model4.setScale(0.8, 0.8, 0.8)
       model4.setHpr(-165, 0, 0)

       model5 = self.loader.loadModel('models/bird/Chicken2')
       model5.reparentTo(self.render)
       base_texture = loader.loadTexture('models/bird/chicken.tif')
       model5.setTexture(base_texture)
       model5.setPos(1, 20, 1.6)
       model5.setScale(0.8, 0.8, 0.8)
       model5.setHpr(-90, 0, 0)

       #планети
       model0 = self.loader.loadModel('models/planets/planet_sphere')
       model0.reparentTo(self.render)
       base_texture = loader.loadTexture('models/planets/bb.jpg')
       model0.setTexture(base_texture)

       model0.setPos(9, 0, 30)
       model0.setScale(7, 7, 7)
       model0.setHpr(0, 0, 0)

       self.setupLighting()

       model2 = self.loader.loadModel('models/planets/planet_sphere')
       model2.reparentTo(self.render)
       base_texture = loader.loadTexture('models/planets/moon.png')
       model2.setTexture(base_texture)

       model2.setPos(12, 15, -14)
       model2.setScale(4, 4, 4)
       model2.setHpr(0, 0, 0)

       model3 = self.loader.loadModel('models/planets/planet_sphere')
       model3.reparentTo(self.render)
       base_texture = loader.loadTexture('models/planets/v.jpg')
       model3.setTexture(base_texture)

       model3.setPos(56, 0, 20)
       model3.setScale(4, 4, 4)
       model3.setHpr(0, 0, 0)

       #трава
       fern = self.loader.loadModel('models/tree/Fern.egg')
       fern.setPos(17,1,2)
       fern.reparentTo(self.render)
       base_texture = loader.loadTexture('models/tree/Material_#2_CL.tif')
       fern.setTexture(base_texture)
       fern.setScale(0.015, 0.015, 0.015)
       positions = [
           (2, 2, 2),
           (5, 12, 1),
           (27, 23, 1),
           (42, 19, 1),
           (29, 29, 1),
           (18, 22, 1),
       ]
       for pos in positions:
           new_fern = fern.copyTo(self.render)
           new_fern.setPos(*pos)
           new_fern.setHpr(0, 0, 0)

           flo = self.loader.loadModel('models/tree/PurpleFlower.egg')
           flo.setPos(16, 1, 2)
           flo.reparentTo(self.render)
           base_texture = loader.loadTexture('models/tree/impatientsHi_Material_#2_CL.tif')
           flo.setTexture(base_texture)
           flo.setScale(1, 1, 1)
           positions = [
               (3, 2, 1),
               (8, 2, 1),
               (11, 2, 1),
               (15, 2, 2),
               (30, 1, 1),
               (34, 1, 1),
               (3, 20, 1),
               (8, 25, 1),
               (11, 27, 1),
               (15, 26, 2),
               (30, 19, 1),
               (34, 17, 1),
               (18, 25, 1),
               (19, 27, 1),
               (24, 29, 2),
               (32, 21, 1),
               (37, 18, 1),
           ]
           for pos in positions:
               new_fern = flo.copyTo(self.render)
               new_fern.setPos(*pos)
               new_fern.setHpr(0, 0, 0)

       #міст
       model9 = self.loader.loadModel('models/tree/bridge.egg')
       model9.reparentTo(self.render)
       base_texture = loader.loadTexture('models/tree/Material_#20_CL.tif')
       model9.setTexture(base_texture)

       model9.setPos(8,24,3)
       model9.setScale(0.006, 0.006, 0.006)
       model9.setHpr(-90,0,0)


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