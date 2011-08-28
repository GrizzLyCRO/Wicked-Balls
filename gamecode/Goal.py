from wrappers import *

class Goal():
    def __init__(self,player):
        self.player = player
        self.world = self.player.world
        self.setupBulletObject()
        
    def setupBulletObject(self):
        
        coords = self.player.NP.getPos()
        dist = self.player.world.distance*-1
        coords[0] = coords[0]*-1
        coords[1] = coords[1]*-1
        coords[2] = 0
        
        self.btNode = addBulletObject(self,"Goal","Plane",(Vec3(coords), dist-1),"Ghost")
        self.btNode.notifyCollisions(True)
        
        
        self.NP = render.attachNewNode(self.btNode)
        self.NP.setPos(0,0,0)