from direct.showbase.DirectObject import DirectObject

from direct.showbase.ShowBase import ShowBase
from panda3d.bullet import *

from panda3d.core import *

from Player import Player
from Ball import Ball

class World(DirectObject):
    def __init__(self):
        self.keyBinds()
        
        self.balls = []
        self.goals = []
        
        self.createWorld()
        self.createBall()
        
        self.makeDebugNode()
        
    def createBall(self):
        ball = Ball(self)
        self.balls.append(ball)

    def makeDebugNode(self):
        self.debugNode = BulletDebugNode('Debug')
        self.debugNode.setVerbose(True)
        self.debugNP = render.attachNewNode(self.debugNode)
        self.debugNP.show()
        self.NP.setDebugNode(self.debugNP.node())
        
    def keyBinds(self):
        self.accept("f1",self.toggleDebug)
        self.accept("f2",self.createBall)
        
    def toggleDebug(self):
            if self.debugNP.isHidden():
                self.debugNP.show()
            else:
                self.debugNP.hide()
                
    def createWorld(self):
        self.NP = BulletWorld()
        self.NP.setGravity(Vec3(0, 0, -9.81))
        self.createWalls()
        self.createFloor()
    
    def createWalls(self):
        distance = 20 #distance of walls from coordinate system center
        walls = ((1,0,0),(-1,0,0),(0,1,0),(0,-1,0))
        for wall in walls:
            shape = BulletPlaneShape(Vec3(wall), 0)
            node = BulletGhostNode('Wall')
            node.setRestitution(1.0)
            node.setFriction(0)
            node.addShape(shape)
            self.goals.append(node)
            np = render.attachNewNode(node)
            np.setCollideMask(BitMask32(0x0f))
            np.setPos(wall[0]*distance*-1, wall[1]*distance*-1, 0)
            #self.NP.attachRigidBody(node)
            taskMgr.add(self.checkGhost, 'checkGhost')
            self.NP.attachGhost(node)

    def checkGhost(self, task):
        print "check"
        for goal in self.goals:
            print goal.getNumOverlappingNodes()
            for node in goal.getOverlappingNodes():
                print node
        
        return task.cont

    def createFloor(self):
        shape = BulletPlaneShape(Vec3(0, 0, 1), 0)
        node = BulletRigidBodyNode('Ground')
        node.addShape(shape)
        node.setRestitution(0)
        node.setFriction(1)
        np = render.attachNewNode(node)
        np.setPos(0, 0, 0)
        self.NP.attachRigidBody(node)