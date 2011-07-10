import direct.directbase.DirectStart
from panda3d.core import Vec3


from panda3d.bullet import *

from code.World import *
from code.Player import Player


base.cam.setPos(0, -10, 0)
base.cam.lookAt(0, 0, 0)

w = World()
p = Player()
p.setWorld(w)
p.init()
 
# Update
def update(task):
    dt = globalClock.getDt()
    w.world.doPhysics(dt)
    return task.cont
 
taskMgr.add(update, 'update')
run()