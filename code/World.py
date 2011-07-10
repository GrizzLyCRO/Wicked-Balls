from direct.showbase.DirectObject import DirectObject

from direct.showbase.ShowBase import ShowBase
from panda3d.bullet import *

from panda3d.core import *

from Player import Player

class World(DirectObject):
    def __init__(self):
        self.createWorld()
        self.makeDebugNode()
        self.keyBinds()
        self.createBall()
        
    def createBall(self):
        shape = BulletSphereShape(1)
        self.ball = BulletRigidBodyNode('Sphere')
        self.ball.addShape(shape)
        self.ball.setMass(1)
        self.ball.setRestitution(1)
        self.ball.setFriction(0)
        
        np = render.attachNewNode(self.ball)
        np.setPos(5, 0, 3)
        self.world.attachRigidBody(self.ball)
        
    def makeDebugNode(self):
        self.debugNode = BulletDebugNode('Debug')
        self.debugNode.setVerbose(True)
        self.debugNP = render.attachNewNode(self.debugNode)
        self.debugNP.show()
        self.world.setDebugNode(self.debugNP.node())
        
    def keyBinds(self):
        self.accept("f1",self.toggleDebug)
        
    def toggleDebug(self):
            if self.debugNP.isHidden():
                self.debugNP.show()
            else:
                self.debugNP.hide()
                
    def createWorld(self):
        self.world = BulletWorld()
        self.world.setGravity(Vec3(0, 0, -9.81))
        self.createWalls()
        self.createFloor()
    
    def createWalls(self):
        distance = 20 #distance of walls from coordinate system center
        walls = ((1,0,0),(-1,0,0),(0,1,0),(0,-1,0))
        for wall in walls:
            shape = BulletPlaneShape(Vec3(wall), 0)
            node = BulletRigidBodyNode('Ground')
            node.setRestitution(1.0)
            node.setFriction(0)
            node.addShape(shape)
            np = render.attachNewNode(node)
            np.setPos(wall[0]*distance*-1, wall[1]*distance*-1, 0)
            self.world.attachRigidBody(node)
            node.setAngularDamping(1)
            node.setLinearDamping(1)

    
    def createFloor(self):
        shape = BulletPlaneShape(Vec3(0, 0, 1), 0)
        node = BulletRigidBodyNode('Ground')
        node.addShape(shape)
        node.setRestitution(0)
        node.setFriction(1)
        #node.setAngularDamping(1)
        #node.setLinearDamping(1)
        np = render.attachNewNode(node)
        np.setPos(0, 0, 0)
        self.world.attachRigidBody(node)