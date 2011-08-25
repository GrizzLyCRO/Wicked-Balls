from direct.showbase.DirectObject import DirectObject

from direct.showbase.ShowBase import ShowBase
from panda3d.bullet import *
from panda3d.core import *

from wrappers import *

from Ball import Ball
from Pillar import Pillar

class World(DirectObject):
    
    def __init__(self):
        self.totalPlayers = 4
        self.distance = 15

    def init(self):
        self.keyBinds()
        self.balls = []
        self.createBulletWorld()
        self.makeDebugNode()
        self.createFloor()
        self.createPillars()

    def makeDebugNode(self):
        self.debugNode = BulletDebugNode('Debug')
        self.debugNode.setVerbose(True)
        self.debugNP = render.attachNewNode(self.debugNode)
        self.debugNP.show()
        self.btWorld.setDebugNode(self.debugNP.node())
        
    def keyBinds(self):
        self.accept("f1",self.toggleDebug)
        self.accept("f3",self.listBodies)
        self.accept("f2",self.createBall)
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
        
    def createPillars(self):
        self.pillars = []
        angle = 360/self.totalPlayers
        for i in range(self.totalPlayers):
            myAngle = angle*i
            pillar = Pillar(self,myAngle)
            self.pillars.append(pillar)
        
    def createBall(self):
        ball = Ball(self)
        self.balls.append(ball)

    # finally the event handlers 
    def handleCollisions(self, node1, node2):
        if node1.getName() == "WickedBall" and  node2.getName() == "Goal":
            ball = node1.getPythonTag("pyParent")
            ball.destroyMe()
            goal = node2.getPythonTag("pyParent")
            goal.player.ballInGoal()
            
    def listBodies(self):
        for x in self.btWorld.getRigidBodies():
            print x