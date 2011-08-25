from direct.showbase.ShowBase import ShowBase
from panda3d.bullet import *
from panda3d.core import *
from wrappers import *

class Ball():
    def __init__(self,world):
        self.world = world
        
        self.btNode = addBulletObject(self,"WickedBall","Sphere",0.4)
        self.btNode.setRestitution(1.00)
        self.NP = addModelToBulletNode(self.btNode,"models/Ball/zero")

    def destroyMe(self):
        print "deleting"
        self.btNode.clearPythonTag("pyClass")
        self.world.btWorld.removeRigidBody(self.btNode)
        self.NP.removeNode()