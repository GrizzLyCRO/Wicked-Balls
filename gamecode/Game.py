from panda3d.bullet import *

from World import *
from Player import Player



class Game(ShowBase):

    def __init__(self):
        ShowBase.__init__(self)
        self.world = World()
        self.players = {}
        #self.world.totalPlayers = 3
        #self.world.distance = 20
        self.world.init()
        for i in range(self.world.totalPlayers):
            self.players[i] = Player(self.world, i)
        
        taskMgr.add(self.update, 'update')


    def update(self,task):
        dt = globalClock.getDt()
        self.world.btWorld.doPhysics(dt)
        return task.cont