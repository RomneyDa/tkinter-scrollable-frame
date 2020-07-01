"""
Created on Sun Apr 12 19:16:07 2020
Copyright 2020 Dallin Romney
License: CC BY 4.0
"""

import tkinter as tk

class SimpleScrollableFrame(tk.Frame):
    
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
        else:
            self.scroll_sensitivity = 3 # default scroll sensitivity is 3/10
        
        self.frame.bind("<Configure>",  self._frame_changed)
        self.canvas.bind("<Configure>", self._frame_changed)
        self.canvas.create_window((0, 0), window = self.frame, anchor = "nw")
        
        self.xscrollbar = tk.Scrollbar(self, orient = 'horizontal', command = self.canvas.xview)
        self.canvas.configure(xscrollcommand = self.xscrollbar.set)
        self.yscrollbar = tk.Scrollbar(self, orient = 'vertical', command = self.canvas.yview)
        self.canvas.configure(yscrollcommand = self.yscrollbar.set)
        
        # These functions prevent the canvas from scrolling unless the cursor is in it
        self.canvas.bind('<Enter>', self._enter_frame)
        self.canvas.bind('<Leave>', self._leave_frame)

        # Place the canvas onto the container and weigh relevant rows/cols for proper expansion
        self.canvas.grid(row = 0, column = 0, sticky = tk.S+tk.E+tk.N+tk.W)
        tk.Grid.rowconfigure(self, 0, weight = 1)
        tk.Grid.columnconfigure(self, 0, weight = 1)
        tk.Grid.rowconfigure(self, 1, weight = 0)
        tk.Grid.columnconfigure(self, 1, weight = 0)
    
    def _frame_changed(self, event):
        self.canvas.configure(scrollregion = self.canvas.bbox('all'))
        
        if self.frame.winfo_width() > self.canvas.winfo_width():
            self.showX = True
            self.xscrollbar.grid(row = 1, column = 0, sticky = tk.S+tk.E+tk.N+tk.W)
        else:
            self.showX = False
            self.xscrollbar.grid_forget()
            
        if self.frame.winfo_height() > self.canvas.winfo_height():
            self.showY = True
            self.yscrollbar.grid(row = 0, column = 1, sticky = tk.S+tk.E+tk.N+tk.W)
        else:
            self.showY = False
            self.yscrollbar.grid_forget()

    # Scroll in the Y direction on mouse wheel movement
    def _on_mouse_wheel(self, event):
        self.canvas.yview_scroll(-1*int(event.delta*self.scroll_sensitivity/360), "units")
    
    # Scroll in the X direction on shift + mouse wheel movement
    def _on_shift_mouse_wheel(self, event):
        self.canvas.xview_scroll(-1*int(event.delta*self.scroll_sensitivity/360), "units")

    # These two fucntions simply prevent scrolling unless the cursor is in the frame
    def _enter_frame(self, event):
        if self.showY: self.frame.bind_all("<MouseWheel>", self._on_mouse_wheel)
        if self.showX: self.frame.bind_all("<Shift-MouseWheel>", self._on_shift_mouse_wheel)

    def _leave_frame(self, event):
        if self.showY: self.frame.unbind_all("<MouseWheel>")
        if self.showX: self.frame.unbind_all("<Shift-MouseWheel>")

