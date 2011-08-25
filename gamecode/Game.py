from panda3d.bullet import *

from World import *
from Player import Player
from config.controls import profiles


class Game(ShowBase):

    def __init__(self):
        ShowBase.__init__(self)
        self.world = World()
        self.players = []
        self.world.totalPlayers = 4
        self.world.distance = 15
        self.world.init()
        for i in range(self.world.totalPlayers):
            player = Player(self.world, i)
            player.setupControls(profiles[i])
            self.players.append(player)
        
        taskMgr.add(self.update, 'update')


    def update(self,task):
        dt = globalClock.getDt()
        self.world.btWorld.doPhysics(dt,10,1.0/180.0)
        return task.cont