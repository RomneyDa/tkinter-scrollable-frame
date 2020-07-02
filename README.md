# tkinter Scrollable Frame
ScrollableFrame is a class for tkinter that acts like a frame but has dynamic scrollbars attached to it. The "with example" files demonstrate how to use it, but in summary,

Like a frame, the first input to the constructor should be the tkinter parent. 
It can also accept normal Tk.Frame parameters such as background, bd, highlightcolor, etc.

The scroll sensitivity can be set by passing an optional scroll_sensitivity' parameter into the constructor. It can range from 1 to 10. The default is 3.

For example,

self.SF = SimpleScrollableFrame(self.container, scroll_sensitivity = 7, bg = 'red')

To add things to the frame, make sure to use the frame attribute of the scrollable frame as the parent, not the scrollable frame itself. This is because the scrollable frame is actually a frame within a canvas within a frame. For example,

self.button1 = tk.Button(SF.frame, fg = 'blue')

SimpleScrollableFrame is the same but doesn't take frame parameters such as background color, etc., making for a lot less code. It does still take scroll sensitivity.

The SimpleScrollableFrameClam file contains a (in my opinion) nicer looking version of the SimpleScrollableFrame that uses the clam ttk style. Warning: it might apply clam to your entire project.
