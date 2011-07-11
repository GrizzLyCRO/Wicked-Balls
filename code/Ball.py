from direct.showbase.ShowBase import ShowBase
from panda3d.bullet import *
import math
from panda3d.core import *

class Ball():
    def __init__(self,parent):
        self.parent = parent
        self.worldNP = parent.NP
        self.birth = globalClock.getFrameTime()
        shape = BulletSphereShape(1)
        
        self.node = BulletRigidBodyNode('Sphere')
        self.node.addShape(shape)
        
        self.node.setMass(1)
        self.node.setRestitution(1.02)
        self.node.setFriction(0)
        self.worldNP.attachRigidBody(self.node)
        
        self.model = loader.loadModel("smiley")
        
        self.NP = render.attachNewNode(self.node)
        self.NP.setPos(5, 0, 1.5)
        self.model.reparentTo(self.NP)
        
        taskMgr.add(self.updateVelocity, "updateVelocity")
    
    def updateVelocity(self, task):
        #we do this to prevent ball from goign in straight line
        velocity = self.node.getLinearVelocity()
        #print velocity
        x = velocity[0]+1.0
        y = velocity[1]+1.0
        factor = 10
        angle = math.fabs(x/y)
        if angle < 1:
            angle = 1/angle
        if angle > factor:
            if x < y:
                x = y
            else:
                y = x
            print "update"
            newVelocity = Vec3(x,y,0) 
            
            self.node.setLinearVelocity(velocity)
            
        
        return task.cont