from direct.showbase.DirectObject import DirectObject
from direct.showbase.InputStateGlobal import inputState
from panda3d.bullet import *
from panda3d.core import *
from direct.showbase.ShowBase import ShowBase


class Player(DirectObject):
    
    def setWorld(self, parent):
        self.worldNP = parent.NP
        self.world = parent
    
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
        self.worldNP.attachRigidBody(self.node)
        self.node.setRestitution(1.0)
        self.node.setFriction(0)

        
    def setupControls(self):
        #handle input
        taskMgr.add(self.processInput, "process input")
        
        #keyboard shortcuts
        inputState.watchWithModifiers('forward', 'w')
        inputState.watchWithModifiers('left', 'a')
        inputState.watchWithModifiers('right', 'd')
        inputState.watchWithModifiers('back', 's')
        inputState.watchWithModifiers('turbo', 'k')

        
    def processInput(self, task):
        self.dt = globalClock.getDt()
        speed = 40
        turboModifier = 3
        
        if inputState.isSet('turbo'):
            speed = speed*turboModifier
        
        if inputState.isSet('left'):
            self.NP.setX(self.NP, -self.dt * speed)
        if inputState.isSet('right'):
            self.NP.setX(self.NP, self.dt * speed)
        if inputState.isSet('forward'):
            self.NP.setY(self.NP, self.dt * speed)
        if inputState.isSet('back'):
            self.NP.setY(self.NP, -self.dt * speed)
            
        return task.cont
        
        
