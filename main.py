# Panda3D imports _____________________________________
from pandac.PandaModules import *
from direct.actor.Actor import Actor
from direct.showbase.DirectObject import DirectObject
from direct.gui.DirectGui import *
from direct.gui.OnscreenText import OnscreenText
from direct.gui.OnscreenImage import OnscreenImage
from direct.interval.IntervalGlobal import *
from direct.task import Task
from direct.showbase import PythonUtil as PU

from pandac.PandaModules import loadPrcFileData

loadPrcFileData("", "sync-video #f")
loadPrcFileData("", "show-frame-rate-meter #t")
#loadPrcFileData('', 'bullet-enable-contact-events true') 
from direct.showbase.ShowBase import ShowBase


from panda3d.bullet import *

from gamecode.World import *
from gamecode.Player import Player
from gamecode.GUI.SplashGui import *

# Python imports ______________________________________
import imp, glob
import os, sys
import string, re
import cPickle
import random
import math
import time
import types
import traceback


class Game(ShowBase):

    def __init__(self):
        ShowBase.__init__(self)
        self.splash = SplashGui()
        
        self.world = World()
        self.player = Player()
        self.player.setWorld(self.world)
        self.player.init()
        taskMgr.add(self.update, 'update')
        
        
    def update(self,task):
        dt = globalClock.getDt()
        self.world.NP.doPhysics(dt)
        return task.cont

if __name__=='__main__':
    winst = Game()
    run()
