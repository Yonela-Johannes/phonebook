# Libraries
from tkinter import *
from tkinter import ttk


class PhoneBook:
    def __init__(self):
        # Colors 
        self.WHITE = "#fff"
        self.BLACK = "#000"
        self.DARK_BG = "#242323"
        self.PRIMARY = "#252335"
        self.SECONDARY = "#9B1C1C"

        # Variables
        self.width = 400
        self.height = 380
        self.frame_width1 = 500
        self.frame_height1 = 50
        self.frame_height2 = 150        
        self.dimensions = f"{self.width}x{self.height}"

        # Instantiating window/screen/display
        self.window = Tk()
        self.window.title("Phone Book")
        self.window.geometry(self.dimensions)
        self.window.configure(background=self.WHITE)
        self.window.resizable(width=FALSE, height=FALSE)
        
    def main(self):
        frame_up = Frame(self.window, width=self.frame_width1, height=self.frame_height1, bg=self.PRIMARY)
        frame_up.grid(row=0, column=0, padx=0, pady=1)

        frame_down = Frame(self.window, width=self.frame_width1, height=self.frame_height2, bg=self.DARK_BG)
        frame_down.grid(row=0, column=0, padx=0, pady=1)
        
        self.window.mainloop()

if __name__ == '__main__':
    PhoneBook().main().run()