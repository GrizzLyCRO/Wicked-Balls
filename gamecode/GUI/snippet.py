# -*- coding: utf-8 -*- 
"""Panda/PyCEGUI Integration Module 

Copyright (c) 2011 Christopher S. Case 
Licensed under the MIT license; see the LICENSE file for details. 

""" 
from direct.showbase.ShowBase import ShowBase 

# PandaCEGUI import 
from pcegui import PandaCEGUI 

class MyApp(ShowBase): 
  
    def __init__(self): 
        ShowBase.__init__(self) 

        # Instantiate CEGUI helper class 
        self.CEGUI = PandaCEGUI() 

        # Setup CEGUI resources 
        self.CEGUI.initializeResources('./datafiles') 

        # Setup our CEGUI layout 
        self.setupUI() 

        # Enable CEGUI Rendering/Input Handling 
        self.CEGUI.enable() 

    def setupUI(self): 
        self.CEGUI.SchemeManager.create("VanillaSkin.scheme") 
        self.CEGUI.SchemeManager.create("TaharezLook.scheme") 
        self.CEGUI.System.setDefaultMouseCursor("Vanilla-Images", "MouseArrow") 

        root = self.CEGUI.WindowManager.loadWindowLayout("VanillaWindows.layout") 
        self.CEGUI.System.setGUISheet(root) 
        
        self.wnd = self.CEGUI.WindowManager.createWindow("TaharezLook/FrameWindow", "Demo Window") 
        root.addChildWindow(self.wnd) 

app = MyApp() 
app.run() 