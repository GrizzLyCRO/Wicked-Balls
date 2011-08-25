from direct.showbase.ShowBase import ShowBase
from panda3d.bullet import *
from panda3d.core import *
from wrappers import *

class Ball():
    def __init__(self,world):
        self.world = world
        
        self.btNode = addBulletObject(self,"WickedBall","Sphere",0.4)
        self.btNode.setRestitution(1.00)
        self.btNode.setFriction(0.0)
        self.btNode.setMass(0.08)
        #self.btNode.setAngularFactor((10,10,10))
        self.NP = addModelToBulletNode(self.btNode,"models/Ball/zero")
        self.NP.setZ(0.5)

    def destroyMe(self):
        print "deleting"
        self.btNode.clearPythonTag("pyClass")
        self.world.btWorld.removeRigidBody(self.btNode)
        self.NP.removeNode()