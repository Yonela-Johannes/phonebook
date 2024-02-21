# Libraries
from tkinter import *
from tkinter import ttk
from tkinter import messagebox
from crud import CRUD

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
        # Init CRUD method
        crud_method = CRUD
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
            demo_list = crud_method.view()
            
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
        
        # Add data
        def insert():
            Name = entry_name.get()
            Gender = combo_gender.get()
            Telephone = entry_telephone.get()
            Email = entry_email.get()
            
            data = [Name, Gender, Telephone, Email]
            
            if Name == None or Gender == None or Telephone == None or Email == None:
                messagebox.showwarning('Data Required', 'Please fill in all fields')
            else:
                CRUD.add(data)
                messagebox.showinfo('Successfully', 'Phone details added successfully')
                entry_name.delete(0, 'end')
                entry_email.delete(0, 'end')
                combo_gender.delete(0, 'end')
                entry_telephone.delete(0, 'end')
                
            show()
            
        # Update data
        def set_update():
            try:
                tree_data = tree.focus()
                tree_dictionary = tree.item(tree_data)
                tree_list = tree_dictionary['values']
                
                Name = str(tree_list[0])
                Gender = str(tree_list[1])
                Telephone = str(tree_list[2])
                Email = str(tree_list[3])
                
                entry_name.insert(0, Name)
                entry_email.insert(0, Gender)
                combo_gender.insert(0, Telephone)
                entry_telephone.insert(0, Email)
                
                def confirm():
                    new_name = entry_name.get()
                    new_gender = combo_gender.get()
                    new_telephone =  entry_telephone.get()
                    new_email = entry_email.get()
                    
                    data = [new_name, new_gender, new_telephone, new_email]
                    
                    crud_method.update(data)
                    
                    messagebox.showinfo('Successs',  "Phone details updated successfully")
                    
                    entry_name.delete(0, 'end')
                    entry_email.delete(0, 'end')
                    combo_gender.delete(0, 'end')
                    entry_telephone.delete(0, 'end')
                    
                    for widget in frame_table.winfo_children():
                        widget.destroy()
                        
                    button_confirm.destroy()
                    
                    show()
                    
                button_confirm = Button(frame_down, text="Confirm", height=1, font=('Ivy 8 bold'), bg=self.SECONDARY, command=confirm)
                button_confirm.place(x=264, y=160)
                
                
            except:
                messagebox.showerror('Error',  "Select phone details from list")
                
        
        def to_remove():
            try:
                tree_data = tree.focus()
                tree_dictionary = tree.item(tree_data)
                tree_list = tree_dictionary['values']
                tree_telephone = str(tree_list[2])
                
                crud_method.remove(tree_telephone)
                
                messagebox.showinfo('Successs',  "Phone details deleted successfully")
                
            except:
                messagebox.showinfo('Error',  "Select number from phone details list")
            
            show()
            
        def to_search():
            telephone = search_entry.get()
            
            data = crud_method.search(telephone)
            
            def delete_command():
                tree.delete(*tree.get_children())
                
            delete_command()
            
            for item in data:
                tree.insert('', 'end', values=item)
                
        # frame up widgets
        app_name = Label(frame_up, text="Phonebook", height=1, font=('Arial 16 bold'), bg=self.WHITE, anchor=NW)
        app_name.place(x=5, y=5)
        
        # search input
        search_entry = Entry(frame_up, width=25, justify='left', highlightthickness=1, relief='solid')
        search_entry.place(x=285, y=6)
        # search button
        search_button = Button(frame_up, text="Search", height=1, font=('Ivy 8 bold'), bg=self.SECONDARY, command=to_search)
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
        view_button = Button(frame_down, text="View", width=self.button_width, height=1, font=('Ivy 8 bold'), bg=self.SECONDARY, command=show)
        view_button.place(x=12, y=160)
        
        # add button
        add_button = Button(frame_down, text="Add", width=self.button_width, height=1, font=('Ivy 8 bold'), bg=self.SECONDARY, command=insert)
        add_button.place(x=80, y=160)
        
        # update button
        update_button = Button(frame_down, text="Update", width=self.button_width, height=1, font=('Ivy 8 bold'), bg=self.SECONDARY, command=set_update)
        update_button.place(x=148, y=160)
        
        # delete button
        delete_button = Button(frame_down, text="Delete", width=self.button_width, height=1, font=('Ivy 8 bold'), bg=self.SECONDARY, command=to_remove)
        delete_button.place(x=216, y=160)
        
        self.window.mainloop()

if __name__ == '__main__':
    PhoneBook().main().run()