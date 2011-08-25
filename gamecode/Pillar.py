from wrappers import *

class Pillar():
    def __init__(self,world,myAngle):
        self.world = world
        self.setupBulletObject(myAngle)
    
    def setupBulletObject(self,myAngle):
        self.btNode = addBulletObject(self,"Pillar","Sphere",4)
        self.NP = render.attachNewNode(self.btNode)
        self.NP.setHpr(myAngle,0,0)
        dist = self.world.distance*-1
        self.NP.setY(self.NP,dist)
        self.NP.setX(self.NP,dist)