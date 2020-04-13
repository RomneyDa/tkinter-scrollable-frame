# -*- coding: utf-8 -*-
"""
Created on Fri Apr 10 23:54:11 2020

@author: Dallin Romney
"""

import tkinter as tk

class ScrollableFrame(tk.Frame):
    
    def __init__(self, parent, **kwargs):
        self.parent = parent
        
        # Initiate container frame
        tk.Frame.__init__(self, self.parent)

        # Create a frame within a scrollable canvas within the container
        self.canvas = tk.Canvas(self)
        self.frame = tk.Frame(self.canvas)
        
        # (CUSTOM OPTION) Sets scroll sensitivity on a scale of 1 to 10
        if 'scroll_sensitivity' in kwargs and kwargs['scroll_sensitivity'] >= 1 and kwargs['scroll_sensitivity'] <= 10:
            self.scroll_sensitivity = kwargs['scroll_sensitivity']
            kwargs.pop('scroll_sensitivity')
        else:
            self.scroll_sensitivity = 3 # default scroll sensitivity is 3/10
        
        # (CUSTOM OPTION) Determines if there will be just a horizontal, just a vertical, or both scroll bars on the frame
        if 'direction' in kwargs and kwargs['direction'] in ['both', 'horizontal', 'vertical']:
            self.direction = kwargs['direction']
            kwargs.pop('direction')
        else:
            self.direction = 'both'
        
        # config_sf function applies any remaining keyword properties
        self.config_sf(**kwargs)
        
        self.frame.bind("<Configure>", lambda e: self.canvas.configure(scrollregion = self.canvas.bbox('all')))
        self.canvas.create_window((0, 0), window = self.frame, anchor = "nw")
        
        self.xscrollbar = tk.Scrollbar(self, orient = 'horizontal', command = self.canvas.xview)
        self.canvas.configure(xscrollcommand = self.xscrollbar.set)
        self.yscrollbar = tk.Scrollbar(self, orient = 'vertical', command = self.canvas.yview)
        self.canvas.configure(yscrollcommand = self.yscrollbar.set)
        
        # These functions prevent the canvas from scrolling unless the cursor is in it
        self.canvas.bind('<Enter>', self._enter_frame)
        self.canvas.bind('<Leave>', self._leave_frame)
        
        # This method places the scrollbars onto the containing frame
        self.set_direction(self.direction)

        # Place the canvas onto the container and weigh relevant rows/cols for proper expansion
        self.canvas.grid(row = 0, column = 0, sticky = tk.S+tk.E+tk.N+tk.W)
        tk.Grid.rowconfigure(self, 0, weight = 1)
        tk.Grid.columnconfigure(self, 0, weight = 1)
        tk.Grid.rowconfigure(self, 1, weight = 0)
        tk.Grid.columnconfigure(self, 1, weight = 0)

    def _on_mouse_wheel(self, event):
        self.canvas.yview_scroll(-1*int(event.delta*self.scroll_sensitivity/360), "units")
    
    def _on_shift_mouse_wheel(self, event):
        self.canvas.xview_scroll(-1*int(event.delta*self.scroll_sensitivity/360), "units")

    def _enter_frame(self, event):
        if self.direction != 'horizontal': self.frame.bind_all("<MouseWheel>",       self._on_mouse_wheel)
        if self.direction != 'vertical':   self.frame.bind_all("<Shift-MouseWheel>", self._on_shift_mouse_wheel)

    def _leave_frame(self, event):
        if self.direction != 'horizontal': self.frame.unbind_all("<MouseWheel>")
        if self.direction != 'vertical':   self.frame.unbind_all("<Shift-MouseWheel>")
    
    def set_direction(self, direction):
        if direction in ['both', 'horizontal', 'vertical']:
            self.direction = direction
            self.xscrollbar.grid_forget()
            self.yscrollbar.grid_forget()
            if self.direction != 'horizontal':
                self.yscrollbar.grid(row = 0, column = 1, sticky = tk.S+tk.E+tk.N+tk.W)
            if self.direction != 'vertical':
                self.xscrollbar.grid(row = 1, column = 0, sticky = tk.S+tk.E+tk.N+tk.W)
        else:
            raise ValueError("Direction must be 'horizontal', 'vertical', or 'both'")
            
    # This overwrites the config for the containing frame and sends options to the scrollable frame            
    def config_sf(self, **options):
        
        # Some options will only apply to the canvas
        if 'highlightbackground' in options:
            self.canvas.configure(highlightbackground = options.get('highlightbackground'))
            options.pop('highlightbackground')
        
        if 'highlightcolor' in options:
            self.canvas.configure(highlightcolor = options.get('highlightcolor'))
            options.pop('highlightcolor')
        
        if 'highlightthickness' in options:
            self.canvas.configure(highlightthickness = options.get('highlightthickness'))
            options.pop('highlightthickness')
            
        # Some options will apply to both the frame and canvas
        if 'bg' in options and 'background' in options:
            raise KeyError("Can't use both bg and background options")
        elif 'bg' in options: self.canvas.configure(bg = options.get('bg'))
        elif 'background' in options: self.canvas.configure(bg = options.get('background'))
        
        if 'bd' in options and 'borderwidth' in options:
            raise KeyError("Can't use both bd and borderwidth options")
        elif 'bd' in options: 
            self.canvas.configure(bd = options.get('bd'))
            options.pop('bd')
        elif 'borderwidth' in options: 
            self.canvas.configure(bd = options.get('borderwidth'))
            options.pop('borderwidth')
                
        self.canvas.configure(height = options.get('height'))
        self.canvas.configure(width = options.get('width'))
        self.canvas.configure(cursor = options.get('cursor'))
        
        # Apply all non-popped options to frame
        self.frame.configure(**options)

        