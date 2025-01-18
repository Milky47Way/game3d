class Mapmanager():
    import pickle


""" Керування мапою """


# Оголошуємо клас `Mapmanager`, який відповідає за створення і керування мапою у грі.

def __init__(self):
    # Конструктор класу `Mapmanager`. Виконується під час створення об'єкта цього класу.

    self.model = 'block'

    # self.textures = ["textures/block.png","textures/grass.jpg"]

    self.colors = [
        (0.2, 0.2, 0.35, 1),
        (0.2, 0.8, 0.35, 1)
    ]
    self.texture = "grass.jpg"
    # Визначаємо колір RGBA (червоний, зелений, синій, прозорість) для блоку.
    # Це використовується для задання кольору поверх текстури.

    # створюємо основний вузол мапи:
    self.startNew()
    # Викликаємо метод `startNew`, який створює базовий вузол для всієї мапи.

    # створюємо будівельні блоки
    self.addBlock((0, 10, 0))
    # Додаємо один блок на мапу у позицію (x=0, y=10, z=0).
    # Це координати у тривимірному просторі.


def startNew(self):
    """створює основу для нової мапи"""
    # Метод для створення основного вузла, до якого будуть прив'язані всі блоки мапи.

    self.land = render.attachNewNode("Land")
    # Створюємо вузол "Land" у сцені за допомогою `render.attachNewNode`.
    # Усі блоки мапи будуть дочірніми до цього вузла.


def getColor(self, z):
    """Повертає колір для заданого рівня висоти"""
    if z < len(self.colors):
        return self.colors[z]
    else:
        return self.colors[len(self.colors) - 1]


def addBlock(self, position):
    # Метод для додавання блоку до мапи.

    self.block = loader.loadModel(self.model)
    # Завантажуємо модель блоку (файл block.egg).
    # Цей метод шукає файл у папці ресурсів.

    self.block.setTexture(loader.loadTexture(self.texture))
    # Задаємо текстуру для моделі блоку (завантажуємо файл block.png).

    self.block.setPos(position)
    # Встановлюємо позицію блоку у просторі (x, y, z), передану через аргумент `position`.
    # self.color = self.getColor(int(position[2]))

    # self.block.setColor(self.color)
    # Цей рядок відповідає за зміну кольору блоку поверх текстури,
    # але його виконання зараз вимкнене.

    self.block.reparentTo(self.land)
    # Додаємо блок до вузла "Land", щоб він був частиною мапи.


def clear(self):
    """Обнуляє карту"""
    self.land.removeNode()
    self.startNew()


def loadLand(self, filename):
    """Створює карту землі з текстового файлу, повертає її розміри"""
    self.clear()
    with open(filename) as file:
        y = 0
        for line in file:
            x = 0
            line = line.split(' ')
            for z in line:
                for z0 in range(int(z) + 1):
                    self.addBlock((x, y, z0))
                x += 1
            y += 1
    return x, y


def isBlockAt(self, position):
    """Перевіряє, чи є блок у заданій позиції"""
    return position in self.blocks


def findBlocks(self, pos):
    return self.land.findAllMatches('=at' + str(pos))


def findHighesEmpty(self, pos):
    x, y, z = pos
    z = 1
    while self.isBlockAt((round(x), round(y), round(z))):
        z += 1

    return (round(x), round(y), z)


def buildBlock(self, pos):  # гравітація
    x, y, z = pos
    new = self.findHighestEmpty(pos)
    if new[2] <= round(z) + 1:
        self.addBlock(new)


def delBlock(self, position):
    blocks = self.findBlocks(position)
    for block in blocks:
        block.removeNode()


def delBlockFrom(self, position):
    x, y, z = self.findHighestEmpty(position)
    pos = round(x), round(y), round(z) - 1
    for block in self.findBlocks(pos):
        block.removeNode()


defsaveMap(self):
blocks = self.land.getChildren()
wiht
open('my_map.dat', 'wb') as file:
pickle.dump(len(blocks), file)

for block in blocks:
    x, y, z = block.getPos()
    pos = int(x), int(y), int(z))
    pickle.dump(pos, file)


def loadMap(self):
    self.clear()


with open('my_map.dat', 'rb') as file:
    length = pickle.load(file)
    for i in range(length):
        pos = pickle.load(file)
        self.addBlock(pos)