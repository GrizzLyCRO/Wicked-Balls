from direct.gui.DirectGui import *
from gamecode.GUI.AlignTo import *

class SplashGui():
    def __init__(self):
        self.frame = DirectFrame(frameColor=(0, 0, 0, 1),
                      frameSize=(0, 1, 0, 1))
        
        self.frame.alignTo(base.a2dTopLeft,UL,gap=(0.1,0.1))
        
        self.NewGame = DirectButton(text = ("New Game"), scale = 0.07)
        self.NewGame.reparentTo(self.frame)
        self.NewGame.alignTo(self.frame,UL,gap=(2,1))
        
        
        self.About = DirectButton(text = ("About"), scale = 0.07)
        self.About.reparentTo(self.frame)
        self.About.alignTo(self.NewGame,UL,LL,gap=(0,0.6))
        
        self.Config = DirectButton(text = ("Config"), scale = 0.07)
        self.Config.reparentTo(self.frame)
        self.Config.alignTo(self.About,UL,LL,gap=(0,0.6))