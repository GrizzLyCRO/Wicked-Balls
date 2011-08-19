from direct.showbase.DirectObject import DirectObject
from direct.showbase.InputStateGlobal import inputState
from panda3d.bullet import *
from panda3d.core import *
from direct.showbase.ShowBase import ShowBase
from World import World


class Player(DirectObject):
    
    
    def __init__(self,world,id):
        self.world = world
        self.playerId = id
        self.setupBody()
        self.setupGoal()
        self.setupControls()
        self.lives = 15
        

    def setupBody(self):
        radius = 2
        shape = BulletSphereShape(radius)
        
        self.node = BulletRigidBodyNode('Player')
        self.node.addShape(shape)
        self.node.setKinematic(1)
        self.node.setDisableDeactivation(1)
        self.node.setMass(100)
        self.NP = render.attachNewNode(self.node)
        
        angle = 360/self.world.totalPlayers
        myAngle = angle*self.playerId
        self.NP.setHpr(myAngle,0,0)
        dist = self.world.distance*-1
        self.NP.setPos(self.NP,(0, dist, 1.01))
        
        self.world.btWorld.attachRigidBody(self.node)
        self.node.setRestitution(1.0)
        self.node.setFriction(0)

    def ballInGoal(self):
        self.lives -= 1
        print "I am player "+str(self.playerId+1)+", and i just got goal.. Lives left: "+str(self.lives)

    def setupGoal(self):
        coords = self.NP.getPos()
        dist = self.world.distance*-1
        coords[0] = coords[0]*-1
        coords[1] = coords[1]*-1
        coords[2] = 0
        shape = BulletPlaneShape(Vec3(coords), dist-2)
        node = BulletGhostNode('Goal')
        node.setRestitution(1.0)
        node.setFriction(0)
        node.notifyCollisions(True)
        node.addShape(shape)
        node.setPythonTag("player",self)
        self.goal = node
        np = render.attachNewNode(node)
        np.setPos(0,0,0)
        self.world.btWorld.attachGhost(node)
    
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
        
        
