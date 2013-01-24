import Tkinter
import turtle
import sys

def main():

	root = Tkinter.Tk()
	
	cv = Tkinter.Canvas(root, width=600, height=600)
	cv.pack(side = Tkinter.LEFT)
	
	

	root.title("Draw something")
	
	t = turtle.RawTurtle(cv)
	
	screen = t.getscreen()
	screen.setworldcoordinates(0,0,600,600)
	
	frame = Tkinter.Frame(root)
	frame.pack(side = Tkinter.RIGHT, fill=Tkinter.BOTH)
	
	def quitHandler():
		print("Goodbye")
		sys.exit(0)
		
	quitButton = Tkinter.Button(frame, text="Quit", command=quitHandler)
	quitButton.pack()
	
	def clickHandler(x,y):
		t.goto(x,y)
		
	screen.onclick(clickHandler)
	
	
	Tkinter.mainloop()
	
if __name__ == "__main__":main()
	
	
	