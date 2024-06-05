#importing libraries
from tkinter import Label, Tk
import time

#defining title and size
"""
set both height and width of resizeable function as True(1,1)
if no maximize or minimize- set False(0,0)
"""
app_window= Tk()
app_window.title=("Digital Clock")
app_window.geometry=("420x150")
app_window.resizable(1,1)

#defining font and colour
"""
deine font of time, its colour, border width and background
colour of the digital clock  
"""
text_font=("Boulder", 68, 'bold')
background= "#f2e750"
foreground= "#363529"
border_width= 25

#defining lable of clock application
label= Label(app_window, font=text_font, bg=background, fg= foreground, bd= border_width)
label.grid(row=0, column=1)

#main function of clock
"""
main function of digital clock. 
setting the text of label as the realtime
"""
def digital_clock():
    time_live= time.strftime("%H:%M:%S")
    label.config(text= time_live)
    label.after(200, digital_clock)

#run 
digital_clock()
app_window.mainloop()
    