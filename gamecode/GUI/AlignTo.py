from pandac.PandaModules import NodePath, PGItem, Vec4 
from direct.gui.DirectGui import DGG 
from direct.gui.DirectGuiBase import DirectGuiWidget 

def alignTo(obj, other, selfPos, otherPos=None, gap=(0,0)): 
    ''' 
       Usage : 
         myGui.alignTo( other, selfPos, otherPos, gap=(x,z) ) 
           OR 
         alignTo( nodepath, other, selfPos, otherPos, gap=(x,z) ) 

         [+] selfPos is a position in myGui's coordinate space 
         [+] otherPos is a position in other's coordinate space 
         [x] if otherPos is missing, the same position will be used 
         [+] they could be any of : 
             LL (lower left) 
             UL (upper left) 
             LR (lower right) 
             UR (upper right) 
             C (center) 
             CL (center left) 
             CR (center right) 
             CB (center bottom) 
             CT (center top) 
             O (origin) 
         [+] gap is in the myGui/nodepath's coordinate space 
    ''' 
    objNode = obj.node() 
    otherNode = other.node() 
    if otherPos is None: 
       otherPos = selfPos 
    if isinstance(objNode,PGItem): 
       wB = Vec4(objNode.getFrame()) 
    else: 
       isOrigin = selfPos==0 
       if not NodePath(obj).getBounds().isEmpty() and not isOrigin: 
          minb,maxb = obj.getTightBounds() 
       else: 
          minb = maxb = obj.getPos() 
          if isOrigin: 
             selfPos = (0,)*2 # any point is OK 
       minb = obj.getRelativePoint(obj.getParent(),minb) 
       maxb = obj.getRelativePoint(obj.getParent(),maxb) 
       wB = Vec4(minb[0],maxb[0],minb[2],maxb[2]) 
    if isinstance(otherNode,PGItem): 
       oB = Vec4(otherNode.getFrame()) 
    else: 
       isOrigin = otherPos==0 
       if not NodePath(other).getBounds().isEmpty() and not isOrigin: 
          minb,maxb = other.getTightBounds() 
       else: 
          minb = maxb = other.getPos() 
          if isOrigin: 
             otherPos = (0,)*2 # any point is OK 
       minb = other.getRelativePoint(other.getParent(),minb) 
       maxb = other.getRelativePoint(other.getParent(),maxb) 
       oB = Vec4(minb[0],maxb[0],minb[2],maxb[2]) 
    if selfPos[0]<0: # center 
       selfPos=(0,selfPos[1]) 
       wB.setX(.5*(wB[0]+wB[1])) 
    if selfPos[1]<0: # center 
       selfPos=(selfPos[0],2) 
       wB.setZ(.5*(wB[2]+wB[3])) 
    if otherPos[0]<0: # center 
       otherPos=(0,otherPos[1]) 
       oB.setX(.5*(oB[0]+oB[1])) 
    if otherPos[1]<0: # center 
       otherPos=(otherPos[0],2) 
       oB.setZ(.5*(oB[2]+oB[3])) 
    Xsign = 1-2*(selfPos[0]==otherPos[0]) 
    if ( (Xsign==-1 and selfPos[0]==1) or (Xsign==1 and selfPos[0]==0) ): 
       Xsign*=-1 
    Zsign = 1-2*(selfPos[1]==otherPos[1]) 
    if ( (Zsign==-1 and selfPos[1]==3) or  (Zsign==1 and selfPos[1]==2) ): 
       Zsign*=-1 
    obj.setX( other, oB[otherPos[0]]-(wB[selfPos[0]]+gap[0]*Xsign)*obj.getSx(other) ) 
    obj.setZ( other, oB[otherPos[1]]-(wB[selfPos[1]]+gap[1]*Zsign)*obj.getSz(other) ) 
DirectGuiWidget.alignTo = alignTo 
LL = DGG.LL = (0,2) #LOWER LEFT 
UL = DGG.UL = (0,3) #UPPER LEFT 
LR = DGG.LR = (1,2) #LOWER RIGHT 
UR = DGG.UR = (1,3) #UPPER RIGHT 
C = DGG.C = (-1,)*2 #CENTER 
CL = DGG.CL = (0,-1) #CENTER LEFT 
CR = DGG.CR = (1,-1) #CENTER RIGHT 
CB = DGG.CB = (-1,2) #CENTER BOTTOM 
CT = DGG.CT = (-1,3) #CENTER TOP 
O = DGG.O = 0 #ORIGIN 

"""
if __name__ == '__main__': 
   from direct.interval.IntervalGlobal import * 
   from direct.gui.DirectGui import DirectButton 
   from pandac.PandaModules import PandaNode 
   import direct.directbase.DirectStart 
   from random import random 
   import sys 



   ULcorner = DirectButton(parent=base.a2dTopLeft, text='RIGHT\nTO THE\nCORNER',scale=.05) 
   ULcorner.alignTo(base.a2dTopRight,UR) 


   dummy = DirectButton(text='dummy button\nto align\n4 empty nodes',scale=.05,pos=(-.8,0,.2)) 
   dummy.setR(-45) 

   s2 = loader.loadModel('misc/sphere') 
   s2.setScale(.015) 
   s2.setColor(1,1,0,1) 
   pos4 = (UL,UR,LR,LL) 
   for i in range(4): 
       emptyNP = aspect2d.attachNewNode(PandaNode('')) 
       alignTo(emptyNP, dummy, pos4[i]) 
       s2.copyTo(emptyNP) 

   run()
   
"""