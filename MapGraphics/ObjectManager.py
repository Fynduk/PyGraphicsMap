from PySide2.QtCore import QObject, QPointF, Signal
from MapGraphics.Objects.MarkObject import MarkObject
import random


class ObjectManager(QObject):
    deleteFromScene = Signal(object)

    def __init__(self, scene):
        super().__init__()
        self.__scene = scene
        self.__objectsDict = {}

    def addObject(self, object, type: str):
        if type in self.__objectsDict.keys():
            self.__objectsDict[type].append(object)
        else:
            self.__objectsDict[type] = [object]

    def delObject(self, object):
        # TODO maybe do type
        print(self.__objectsDict)
        deleteFlag = False
        for key in self.__objectsDict.keys():
            for obj in self.__objectsDict[key]:
                if obj == object:
                    self.__objectsDict[key].remove(obj)
                    deleteFlag = True
                    break
            if deleteFlag:
                break
        self.deleteFromScene.emit(object)

    def createObject(self, point:QPointF):
        rand = random.randint(0, 2)
        mark = MarkObject(point, rand)
        self.addObject(mark, 'Mark')
        self.__scene.addObject(mark)

