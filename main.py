from pandac.PandaModules import loadPrcFileData

loadPrcFileData("", "sync-video #f")
loadPrcFileData("", "show-frame-rate-meter #t")
loadPrcFileData('', 'bullet-enable-contact-events true') 
from direct.showbase.ShowBase import ShowBase

from panda3d.core import Vec3

from panda3d.bullet import *

from code.World import *
from code.Player import Player



class Game(ShowBase):

    def __init__(self):
        ShowBase.__init__(self) 
        self.world = World()
        self.player = Player()
        self.player.setWorld(self.world)
        self.player.init()
        taskMgr.add(self.update, 'update')
        
    def update(self,task):
        dt = globalClock.getDt()
        self.world.NP.doPhysics(dt)
        return task.cont
    
if __name__ == '__main__':      
    winst = Game()
    winst.run()         
