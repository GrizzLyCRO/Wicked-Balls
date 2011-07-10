from direct.showbase.DirectObject import DirectObject
from panda3d.bullet import *
from panda3d.core import *


class Player(DirectObject):
    
    def setWorld(self,world):
        self.world = world.world
        self.parent = world
    
    def init(self):
        self.setupBody()
        self.setupControls()

    def setupBody(self):
        radius = 2
        shape = BulletSphereShape(radius)
        
        self.node = BulletRigidBodyNode('Player')
        self.node.addShape(shape)
        self.node.setKinematic(1)
        self.node.setDisableDeactivation(1)
        self.node.setMass(100)
        self.NP = render.attachNewNode(self.node)
        self.NP.setPos(0, 0, 1.01)
        self.world.attachRigidBody(self.node)
        self.node.setRestitution(1.0)
        self.node.setFriction(0)

        
    def setupControls(self):
        self.accept("a",self.moveLeft)
        self.accept("w",self.moveForward)
        self.accept("s",self.moveBackward)
        self.accept("d",self.moveRight)
        
    def moveLeft(self):
        self.NP.setX(self.NP,-1)
    def moveRight(self):
        self.NP.setX(self.NP,1)
    def moveForward(self):
        self.NP.setY(self.NP,1)
    def moveBackward(self):
        self.NP.setY(self.NP,-1)
        
        