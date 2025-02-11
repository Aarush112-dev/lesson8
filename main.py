from tkinter import *
from tkinter.ttk import *
from tkinter.filedialog import *
from tkinter import messagebox

mainWin=Tk()
mainWin.title('Address Book')
mainWin.geometry("600x400")

#design mainwindow
my_address = {}

def clear_all():
    name.delete(0,END)
    address.delete(0,END)
    mobile.delete(0,END)
    email.delete(0,END)
    birthday.delete(0,END)

def edit():
    select = book_list.curselection()
    key = book_list.get(select)
    details = my_address[key]
    name.insert(0,key)
    address.insert(0,details[0])
    mobile.insert(0,details[1])
    email.insert(0,details[2])
    birthday.insert(0,details[3])


def add():
    name2 = name.get()
    if name2 not in my_address.keys():
        book_list.insert(END,name2)
    my_address[name2] = (address.get(),mobile.get(),email.get(),birthday.get())
    clear_all()

def delete():
    select = book_list.curselection()
    key = book_list.get(select)
    del my_address[key]
    book_list.delete(select)
    clear_all()

def save():
    file = asksaveasfile(defaultextension=".txt")
    if file is not None:
        #for item in my_address:
        print(my_address,file=file)
        my_address.clear()
        messagebox.showinfo("saved","Your file has been saved")

def open():
    global my_address
    clear_all()
    book_list.delete(0,END)
    my_address.clear()
    file = askopenfile(title="open file")
    bookName.config(text=file.name)
    if file is not None:
        #my_address.clear()
        my_address = eval(file.read())
        for item in my_address:
            book_list.insert(END,item)
        #print(my_address)
        #for item in items:
            #book_list.insert(END,item)

        



#Label address book name
bookName = Label(mainWin, text='My Address Book',width=35)
bookName.grid(row = 0, column = 1,pady = 10,columnspan=3)

#Open address book 
open_button = Button(mainWin, text='Open',command=open)
open_button.grid(row = 0, column = 4,pady = 10)

# Contact list
book_list =Listbox(mainWin,height=15,width=30)
book_list.grid(row = 2, column = 0,columnspan=3, rowspan = 5 )



### Text fields to display contact information ###
# name
name_label =Label(mainWin, text = 'Name:')
name_label.grid(row= 2, column = 3)
name =Entry(mainWin)
name.grid(row = 2, column = 4,padx=5)

# Address 
address_label =Label(mainWin, text = 'Address :')
address_label.grid(row = 3, column = 3)
address =Entry(mainWin)
address.grid(row = 3, column = 4,padx=5)

# Mobile phone
mobile_label =Label(mainWin, text = 'Mobile:')
mobile_label.grid(row = 4, column = 3)
mobile =Entry(mainWin)
mobile.grid(row = 4, column = 4,padx=5)

# Email
email_label = Label(mainWin, text = 'Email:')
email_label.grid(row = 5, column = 3)
email =Entry(mainWin)
email.grid(row = 5, column = 4,padx=5)

# Birthday
birthday_label = Label(mainWin, text = 'Birthday:')
birthday_label.grid(row = 6, column = 3)
birthday = Entry(mainWin)
birthday.grid(row =6, column = 4,padx=5)

#buttons

# Edit contact button
Edit_button = Button(mainWin, text = 'Edit',width=10,command=edit)
Edit_button.grid(row = 7, column = 0, padx = 12,pady=12) 

# Delete contact button
delete_button =Button(mainWin, text = 'Delete',width=10,command=delete)
delete_button.grid(row = 7, column = 1,pady=12 )

# Update/Add  contact button
add_button =Button(mainWin, text = 'Update/Add',command=add)
add_button.grid(row = 7, column = 4,pady=12)

#save address book button
save_button = Button(mainWin, text='Save',width=35,command=save)
save_button.grid(row = 8, column = 1,pady = 10,columnspan=3)

mainWin.mainloop()
