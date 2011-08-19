from direct.showbase.ShowBase import ShowBase
from panda3d.bullet import *
from panda3d.core import *

class Ball():
    def __init__(self,parent):
        self.parent = parent
        self.birth = globalClock.getFrameTime()
        shape = BulletSphereShape(1)
        
        self.node = BulletRigidBodyNode('WickedBall')
        self.node.addShape(shape)
        
        self.node.setMass(1)
        self.node.setRestitution(1.00)
        self.node.setFriction(0.25)
        self.node.setAngularFactor(Vec3(4,4,4))
        self.world = World()
        self.world.btWorld.attachRigidBody(self.node)
        
        self.model = loader.loadModel("smiley")
        
        self.NP = render.attachNewNode(self.node)
        self.NP.setPos(5, 0, 1.5)
        self.model.reparentTo(self.NP)
        self.NP.setPythonTag("pyClass",self)
        
    def destroyMe(self):
        print "deleting"
        self.NP.clearPythonTag("pyClass")
        self.worldNP.removeRigidBody(self.node)
        self.NP.removeNode()