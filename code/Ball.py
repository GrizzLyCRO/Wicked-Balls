from direct.showbase.ShowBase import ShowBase
from panda3d.bullet import *

from panda3d.core import *

class Ball():
    def __init__(self,parent):
        self.parent = parent
        self.worldNP = parent.NP
        shape = BulletSphereShape(1)
        self.node = BulletRigidBodyNode('Sphere')
        self.node.addShape(shape)
        self.node.setMass(1)
        self.node.setRestitution(1)
        self.node.setFriction(0.6)
        self.np = render.attachNewNode(self.node)
        self.np.setPos(5, 0, 3)
        self.worldNP.attachRigidBody(self.node)