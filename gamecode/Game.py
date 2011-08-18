from panda3d.bullet import *

from World import *
from Player import Player


class Game(ShowBase):

    def __init__(self):
        ShowBase.__init__(self)
        self.world = World()
        self.player = Player()
        self.player.init()
        
        taskMgr.add(self.update, 'update')


    def update(self,task):
        dt = globalClock.getDt()
        self.world.NP.doPhysics(dt)
        return task.cont