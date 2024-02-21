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
        self.width = 500
        self.height = 460
        self.frame_height1 = 50
        self.frame_height2 = 200
        self.frame_height3 = 100
        self.button_width = 7
        self.dimensions = f"{self.width}x{self.height}"

        # Instantiating window/screen/display
        self.window = Tk()
        self.window.title("Phone Book")
        self.window.geometry(self.dimensions)
        self.window.configure(background=self.WHITE)
        self.window.resizable(width=FALSE, height=FALSE)
        
    def main(self):
        # Frames
        frame_up = Frame(self.window, width=self.width, height=self.frame_height1, bg=self.PRIMARY)
        frame_up.grid(row=0, column=0, padx=0, pady=1)

        frame_down = Frame(self.window, width=self.width, height=self.frame_height2, bg=self.WHITE)
        frame_down.grid(row=1, column=0, padx=0, pady=1)
        
        # table frame
        frame_table = Frame(self.window, width=self.width, height=self.frame_height3, bg=self.DARK_BG)
        frame_table.grid(row=2, column=0, columnspan=2, padx=10, pady=2, sticky=NW)
        
        # function
        def show():
            global tree
            
            list_header = ['Name', 'Gender', 'Telephone', 'Email']
            demo_list = [['Hlomla', "Female", '0693525256', 'hlomla@gmail.com']]
            
            tree = ttk.Treeview(frame_table, selectmode="extended", columns=list_header, show="headings")
            
            vsb = ttk.Scrollbar(frame_table, orient="vertical", command=tree.yview)
            hsb = ttk.Scrollbar(frame_table, orient="horizontal", command=tree.xview)
            
            tree.configure(yscrollcommand=vsb.set, xscrollcommand=hsb.set)
            
            
            tree.grid(column=0, row=0, sticky='nsew')
            vsb.grid(column=1, row=0, sticky='ns')
            hsb.grid(column=0, row=1, sticky='ew')
            
            # tree head
            tree.heading(0, text="Name", anchor=NW)
            tree.heading(1, text="Gender", anchor=NW)
            tree.heading(2, text="Telephone", anchor=NW)
            tree.heading(3, text="Email", anchor=NW)
            
            # tree colums
            tree.column(0, width=120, anchor='nw')
            tree.column(1, width=50, anchor='nw')
            tree.column(2, width=100, anchor='nw')
            tree.column(3, width=180, anchor='nw')
            
            for item in demo_list:
                tree.insert('', 'end', values=item)
       
        show()
        
        
        # frame up widgets
        app_name = Label(frame_up, text="Phonebook", height=1, font=('Arial 16 bold'), bg=self.WHITE, anchor=NW)
        app_name.place(x=5, y=5)
        
        # search input
        search_entry = Entry(frame_up, width=25, justify='left', highlightthickness=1, relief='solid')
        search_entry.place(x=285, y=6)
        # search button
        search_button = Button(frame_up, text="Search", height=1, font=('Ivy 8 bold'), bg=self.SECONDARY)
        search_button.place(x=445, y=6)
        
        # frame down 
        name_label = Label(frame_down, text="Name *", width=15, height=1, font=('Ivy 10'), bg=self.WHITE, anchor=NW)
        name_label.place(x=10, y=20)
        entry_name = Entry(frame_down, width=25, justify='left', highlightthickness=1, relief='solid')
        entry_name.place(x=80, y=20)
        
        gender_label = Label(frame_down, text="Gender *", width=15, height=1, font=('Ivy 10'), bg=self.WHITE, anchor=NW)
        gender_label.place(x=10, y=50)
        combo_gender = ttk.Combobox(frame_down, width=22)
        combo_gender['values'] = [ 'Male', 'Female']
        combo_gender.place(x=80, y=50)
        
        telephone_lable = Label(frame_down, text="Telephone *", width=15, height=1, font=('Ivy 10'), bg=self.WHITE, anchor=NW)
        telephone_lable.place(x=10, y=80)
        entry_telephone = Entry(frame_down, width=25, justify='left', highlightthickness=1, relief='solid')
        entry_telephone.place(x=80, y=80)
        
        email_label = Label(frame_down, text="Email *", width=15, height=1, font=('Ivy 10'), bg=self.WHITE, anchor=NW)
        email_label.place(x=10, y=110)
        entry_email = Entry(frame_down, width=25, justify='left', highlightthickness=1, relief='solid')
        entry_email.place(x=80, y=110)
        
        # view button
        view_button = Button(frame_down, text="View", width=self.button_width, height=1, font=('Ivy 8 bold'), bg=self.SECONDARY)
        view_button.place(x=12, y=160)
        
        # add button
        add_button = Button(frame_down, text="Add", width=self.button_width, height=1, font=('Ivy 8 bold'), bg=self.SECONDARY)
        add_button.place(x=80, y=160)
        
        # update button
        update_button = Button(frame_down, text="Update", width=self.button_width, height=1, font=('Ivy 8 bold'), bg=self.SECONDARY)
        update_button.place(x=148, y=160)
        
        # delete button
        delete_button = Button(frame_down, text="Delete", width=self.button_width, height=1, font=('Ivy 8 bold'), bg=self.SECONDARY)
        delete_button.place(x=216, y=160)
        
        self.window.mainloop()

if __name__ == '__main__':
    PhoneBook().main().run()