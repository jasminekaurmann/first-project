import tkinter
# init tk
root = tkinter.Tk()

# create canvas
myCanvas = tkinter.Canvas(root, bg="white", height=700, width=700)

# draw arcs
coord = 10, 10, 300, 300
arc = myCanvas.create_arc(coord, start=0, extent=160, fill="pink")
arv2 = myCanvas.create_arc(coord, start=160, extent=215, fill="lightblue")

# add to window and show
myCanvas.pack()
root.mainloop()
