from wrappers import *
import math
class Pillar():
    def __init__(self,world,myAngle):
        self.world = world
        self.setupBulletObject(myAngle)
    
    def setupBulletObject(self,myAngle):
        print myAngle
        self.btNode = addBulletObject(self,"Pillar","Sphere",2.5)
        self.btNode.setMass(0)
        self.btNode.setRestitution(1.0)
        self.btNode.setFriction(0)
        self.btNode.setDeactivationEnabled(False)
        self.NP = render.attachNewNode(self.btNode)
        self.NP.setHpr(myAngle,0,0)
        dist = self.world.distance*-1
        n = self.world.totalPlayers
        dist = dist/math.cos(math.pi/n)
        self.NP.setPos(self.NP,0,dist+1,0.4)