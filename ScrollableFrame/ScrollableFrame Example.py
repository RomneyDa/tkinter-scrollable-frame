# -*- coding: utf-8 -*-
"""
Created on Sun Apr 12 19:16:07 2020

@author: Dallin Romney
"""

import tkinter as tk
from ScrollableFrame import ScrollableFrame

class MainGUI:
    def __init__(self, parent):
        self.container = tk.Frame(parent)
        
        # Create four scrollable frames and add them to the container
        self.SF1 = ScrollableFrame(self.container)
        self.SF1.grid(row = 0, column = 0, sticky = tk.N+tk.E+tk.S+tk.W)
        
        self.SF2 = ScrollableFrame(self.container, direction = 'both', scroll_sensitivity = 8, bg = 'green', cursor = 'heart')
        self.SF2.grid(row = 1, column = 0, sticky = tk.N+tk.E+tk.S+tk.W)

        self.SF3 = ScrollableFrame(self.container, direction = 'vertical', bg = 'red', cursor = 'circle')
        self.SF3.grid(row = 0, column = 1, sticky = tk.N+tk.E+tk.S+tk.W)
        
        self.SF4 = ScrollableFrame(self.container, direction = 'horizontal', bg = 'blue', cursor = 'cross')
        self.SF4.grid(row = 1, column = 1, sticky = tk.N+tk.E+tk.S+tk.W)

        # Configure all rows and columns present to have the same weight (so they expand with the window)
        tk.Grid.columnconfigure(parent, 0, weight = 1)
        tk.Grid.rowconfigure(parent, 0, weight = 1)
        tk.Grid.columnconfigure(self.container, 0, weight = 1)
        tk.Grid.columnconfigure(self.container, 1, weight = 1)
        tk.Grid.rowconfigure(self.container, 0, weight = 1)
        tk.Grid.rowconfigure(self.container, 1, weight = 1)
        
        # Fill each frame with a grid of labels
        self.lots_of_labels(self.SF1.frame, 'default SF', (20, 20))
        self.lots_of_labels(self.SF2.frame, 'green, fast scroll', (40, 10))
        self.lots_of_labels(self.SF3.frame, 'red vertical', (20, 4))
        self.lots_of_labels(self.SF4.frame, 'blue horizontal', (4, 20))
        
        # Add the frame
        self.container.grid(row = 0, column = 0, sticky = tk.N+tk.E+tk.S+tk.W)
        
        
        # Add a button to demonstrate the set_direction method and direction attribute of SF
        tk.Button(text = 'change directions', font = ('Times', 15, 'bold'), command = self.change_dir).grid(row = 2, column = 0)
    
    # Rotate through all the possibilities of scroll direction setups
    def change_dir(self):
        if self.SF2.direction == 'both':
            self.SF2.set_direction('horizontal')
        elif self.SF2.direction == 'horizontal':
            self.SF2.set_direction('vertical')
        elif self.SF2.direction == 'vertical':
            self.SF2.set_direction('both')
        
    # Populates a frame with a grid of labes of given text and same bg as frame
    def lots_of_labels(self, parent, text, dim):
        for row in range(dim[0]):
            for col in range(dim[1]):
                tk.Grid.columnconfigure(parent, col, weight = 1)
                tk.Grid.rowconfigure(parent, row, weight = 1)
                tk.Label(parent, fg = 'black', text = text, bg = parent.cget('bg')).grid(row = row, column = col)
    
# Create and start app
root = tk.Tk()
app = MainGUI(root)
root.mainloop()
