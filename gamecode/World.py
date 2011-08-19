from direct.showbase.DirectObject import DirectObject

from direct.showbase.ShowBase import ShowBase
from panda3d.bullet import *

from panda3d.core import *

class World(DirectObject):
    _self = None
    def __new__(cls):
        if cls._self is None:
            cls._self = super(World, cls).__new__(cls)
        return cls._self

    def __init__(self):
        self.keyBinds()
        self.balls = []
        self.createBulletWorld()
        self.makeDebugNode()
        self.createFloor()

    def makeDebugNode(self):
        self.debugNode = BulletDebugNode('Debug')
        self.debugNode.setVerbose(True)
        self.debugNP = render.attachNewNode(self.debugNode)
        self.debugNP.show()
        self.btWorld.setDebugNode(self.debugNP.node())
        
    def keyBinds(self):
        self.accept("f1",self.toggleDebug)
        # listen for events 
        self.accept('bullet-contact-added', self.handleCollisions) 
        
    def toggleDebug(self):
            if self.debugNP.isHidden():
                self.debugNP.show()
            else:
                self.debugNP.hide()
                
    def createBulletWorld(self):
        self.btWorld = BulletWorld()
        self.btWorld.setGravity(Vec3(0, 0, -9.81))


    def createFloor(self):
        shape = BulletPlaneShape(Vec3(0, 0, 1), 0)
        node = BulletRigidBodyNode('Ground')
        node.addShape(shape)
        node.setRestitution(0)
        node.setFriction(1)
        self.floor = node
        NP = render.attachNewNode(node)
        NP.setPos(0, 0, 0)
        self.btWorld.attachRigidBody(node)

    # finally the event handlers 
    def handleCollisions(self, node1, node2):
        if node1.getName() == "WickedBall" and  node2.getName() == "Wall":
            x = node1.getPythonTag("pyClass")
            x.destroyMe()
            playerNum = node2.getTag("playerNum")
            print "player "+playerNum + " just had an utjerani!"