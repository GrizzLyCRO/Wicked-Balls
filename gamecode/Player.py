from direct.showbase.DirectObject import DirectObject
from direct.showbase.InputStateGlobal import inputState
from panda3d.bullet import *
from panda3d.core import *
from direct.showbase.ShowBase import ShowBase
from World import World
from Goal import Goal
from wrappers import *
import types

class Player(DirectObject):
    
    
    def __init__(self,world,id):
        self.world = world
        self.playerId = id
        self.setupBody()
        self.goal = Goal(self)
        #self.setupControls()
        self.lives = 15
        self.inputStates = set()

    def setupBody(self):
        
        self.btNode = addBulletObject(self,"Player","Sphere",1.25)
        self.btNode.setKinematic(1)
        self.btNode.setDisableDeactivation(1)
        self.btNode.setMass(100)
        self.NP = addModelToBulletNode(self.btNode,"models/Player/untitled")
        angle = 360/self.world.totalPlayers
        myAngle = angle*self.playerId
        self.NP.setHpr(myAngle,0,0)
        dist = self.world.distance*-1
        self.NP.setPos(self.NP,(0, dist, 0.4))

        self.btNode.setRestitution(1.0)
        self.btNode.setFriction(0)

    def ballInGoal(self):
        self.lives -= 1
        print "I am player "+str(self.playerId+1)+", and i just got goal.. Lives left: "+str(self.lives)

    
    def setupControls(self,controls):
        taskMgr.add(self.processInput, "Process Input")
        #keyboard shortcuts
        for action,bind in controls["keyboard"].items():
            self.accept(bind,self.setInputState,[action])
            self.accept(bind+"-up",self.removeInputState,[action])

    def setInputState(self, action):
        print "Player %s setting state %s" % (self.playerId, action)
        self.inputStates.add(action)
        
    def removeInputState(self, action):
        self.inputStates.remove(action)
  
    
    def state(self,state):
        return state in self.inputStates
    
    def processInput(self, task):
        self.dt = globalClock.getDt()
        speed = 40
        turboModifier = 4

        if self.state('turbo'):
            speed = speed*turboModifier
        
        if self.state('left'):
            self.NP.setX(self.NP, -self.dt * speed)
        if self.state('right'):
            self.NP.setX(self.NP, self.dt * speed)
        if self.state('forward'):
            self.NP.setY(self.NP, self.dt * speed)
        if self.state('back'):
            self.NP.setY(self.NP, -self.dt * speed)
            
        return task.cont
        
        
