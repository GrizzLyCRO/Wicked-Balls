from panda3d.bullet import *
from panda3d.core import *
import types

def addBulletObject(caller,name,shape,size,nodeType="RigidBody"):
    
    #Small hack, we need to send tuple to shape constructor
    if type(size) != tuple:
        size = (size,)
    shapeString = "Bullet%sShape%s" % (shape,size)
    shape = eval(shapeString)
    node = eval("Bullet%sNode(name)" % nodeType)
    node.addShape(shape)
    #Ghost nodes dont have mass
    try:
        node.setMass(1)
    except:
        pass
    
    node.setPythonTag("pyParent",caller)
    exec "caller.world.btWorld.attach%s(node)" % nodeType
    
    return node

def addModelToBulletNode(btNode,modelPath):
    model = loader.loadModel(modelPath)
    NP = render.attachNewNode(btNode)
    model.reparentTo(NP)
    return NP

    
