import db
from tkinter import *
from tkinter.ttk import *

LARGE_FONT = ("Verdana", 32)

class ExpenseTracker:
    def __init__(self, master):
        self.frame = Frame(master)
        self.frame.pack()
        self.main_window()
        
    def added(self, boxaile):
        myLabel = Label(boxaile, text="The value has been inserted")
        myLabel.grid(row=4, column=1)
        
    def delete(self, boxaile):
        myLabel = Label(boxaile, text="    The value was deleted     ")
        myLabel.grid(row=4, column=1)

    def clear(self, boxaile, e1, e2, e3):
        e1.delete(0, END)
        e2.delete(0, END)
        e3.delete(0, END)
       
    def display_all(self, database):
        select_all = database
        return select_all

    def insert(self, database, val1, val2, val3):
        goods = val1.get()
        price = val2.get()
        date = val3.get()
        insertion = database(goods, price, date)
        return insertion

    def find_expense(self, database, val1, val2):
        goods = val1.get()
        price = val2.get()
        find = database(goods, price)
        return find

    def delete_expense(self, database, val1, val2):
        goods = val1.get()
        price = val2.get()
        delete = database(goods, price)
        return delete

    ###MAIN WINDOW###
    def main_window(self):
        button1 = Button(self.frame, text="Personal expenses", command=self.personal)
        button1.pack()

        button2 = Button(self.frame, text="Household expenses", command=self.household)
        button2.pack()

        button3 = Button(self.frame, text="Necessities expenses", command=self.necessities)
        button3.pack()

        button4 = Button(self.frame, text="Entertainment expenses", command=self.entertainment)
        button4.pack()

        button5 = Button(self.frame, text="Other expenses", command=self.other)
        button5.pack()

        button6 = Button(self.frame, text="EXIT", command=exit)
        button6.pack()
        
    ###INSERT VALUES###
    def personal(self):
        top = Toplevel(self.frame)
        top.title('Personal expenses')
        l1 = Label(top, text="Name of good").grid(row=1, column=0, sticky=W, pady=2)
        l2 = Label(top, text="Price").grid(row=2, column=0, sticky=W, pady=2)
        l3 = Label(top, text="Date of purchase").grid(row=3, column=0, sticky=W, pady=2)

        e1 = Entry(top)
        e1.grid(row=1, column=1, sticky=W, pady=2)
        e2 = Entry(top)
        e2.grid(row=2, column=1, sticky=W, pady=2)
        e3 = Entry(top)
        e3.grid(row=3, column=1, sticky=W, pady=2)

        text = Text(top, width=40, height=10)
        text.grid(row=5, column=1, columnspan=2)

        def clear():
            e1.delete(0, END)
            e2.delete(0, END)
            e3.delete(0, END)

        # BUTTONS###
        B1 = Button(top, text="Insert Values", command=lambda: (self.insert(db.insert_personal, e1, e2, e3), self.added(top), self.clear(top, e1, e2, e3)))
        B1.grid(row=4, column=0)

        B2 = Button(top, text="Select All", command=lambda: (text.delete(1.0, END), text.insert(END, self.display_all(db.select_all_personal())), self.clear(top, e1, e2, e3)))
        B2.grid(row=1, column=2)

        B4 = Button(top, text="Delete expense", command=lambda: (self.delete_expense(db.delete_personal, e1, e2), self.delete(top), self.clear(top, e1, e2, e3)))
        B4.grid(row=2, column=2)

        B5 = Button(top, text="Exit", command=exit)
        B5.grid(row=3, column=2)

        B6 = Button(top, text='Clear', command=clear)
        B6.grid(row=4, column=2)

    def household(self):
        top = Toplevel(self.frame)
        top.title('Household expenses')
        l1 = Label(top, text="Name of good").grid(row=1, column=0, sticky=W, pady=2)
        l2 = Label(top, text="Price").grid(row=2, column=0, sticky=W, pady=2)
        l3 = Label(top, text="Date of purchase").grid(row=3, column=0, sticky=W, pady=2)

        e1 = Entry(top)
        e1.grid(row=1, column=1, sticky=W, pady=2)
        e2 = Entry(top)
        e2.grid(row=2, column=1, sticky=W, pady=2)
        e3 = Entry(top)
        e3.grid(row=3, column=1, sticky=W, pady=2)

        text = Text(top, width=40, height=10)
        text.grid(row=5, column=1, columnspan=2)

        def clear():
            e1.delete(0, END)
            e2.delete(0, END)
            e3.delete(0, END)

        # BUTTONS###
        B1 = Button(top, text="Insert Values", command=lambda: (self.insert(db.insert_household, e1, e2, e3), self.added(top), self.clear(top, e1, e2, e3)))
        B1.grid(row=4, column=0)

        B2 = Button(top, text="Select All", command=lambda: (text.delete(1.0, END), text.insert(END, self.display_all(db.select_all_household())), self.clear(top, e1, e2, e3)))
        B2.grid(row=1, column=2)

        B3 = Button(top, text="Delete expense", command=lambda: (self.delete_expense(db.delete_household, e1, e2), self.delete(top), self.clear(top, e1, e2, e3)))
        B3.grid(row=2, column=2)

        B4 = Button(top, text="Exit", command=exit)
        B4.grid(row=3, column=2)

        B5 = Button(top, text='Clear', command=clear)
        B5.grid(row=4, column=2)

    def necessities(self):
        top = Toplevel(self.frame)
        top.title('Necessities expenses')
        l1 = Label(top, text="Name of good").grid(row=1, column=0, sticky=W, pady=2)
        l2 = Label(top, text="Price").grid(row=2, column=0, sticky=W, pady=2)
        l3 = Label(top, text="Date of purchase").grid(row=3, column=0, sticky=W, pady=2)

        e1 = Entry(top)
        e1.grid(row=1, column=1, sticky=W, pady=2)
        e2 = Entry(top)
        e2.grid(row=2, column=1, sticky=W, pady=2)
        e3 = Entry(top)
        e3.grid(row=3, column=1, sticky=W, pady=2)

        text = Text(top, width=40, height=10)
        text.grid(row=5, column=1, columnspan=2)

        def clear():
            e1.delete(0, END)
            e2.delete(0, END)
            e3.delete(0, END)

        # BUTTONS###
        B1 = Button(top, text="Insert Values", command=lambda: (self.insert(db.insert_necessities, e1, e2, e3), self.added(top), self.clear(top, e1, e2, e3)))
        B1.grid(row=4, column=0)

        B2 = Button(top, text="Select All", command=lambda: (text.delete(1.0, END), text.insert(END, self.display_all(db.select_all_necessities())), self.clear(top, e1, e2, e3)))
        B2.grid(row=1, column=2)

        B3 = Button(top, text="Delete expense", command=lambda: (self.delete_expense(db.delete_necessities, e1, e2), self.delete(top), self.clear(top, e1, e2, e3)))
        B3.grid(row=2, column=2)

        B4 = Button(top, text="Exit", command=exit)
        B4.grid(row=3, column=2)

        B5 = Button(top, text='Clear', command=clear)
        B5.grid(row=4, column=2)

    def entertainment(self):
        top = Toplevel(self.frame)
        top.title('Entertainment expenses')
        l1 = Label(top, text="Name of good").grid(row=1, column=0, sticky=W, pady=2)
        l2 = Label(top, text="Price").grid(row=2, column=0, sticky=W, pady=2)
        l3 = Label(top, text="Date of purchase").grid(row=3, column=0, sticky=W, pady=2)

        e1 = Entry(top)
        e1.grid(row=1, column=1, sticky=W, pady=2)
        e2 = Entry(top)
        e2.grid(row=2, column=1, sticky=W, pady=2)
        e3 = Entry(top)
        e3.grid(row=3, column=1, sticky=W, pady=2)

        text = Text(top, width=40, height=10)
        text.grid(row=5, column=1, columnspan=2)

        def clear():
            e1.delete(0, END)
            e2.delete(0, END)
            e3.delete(0, END)

        # BUTTONS###
        B1 = Button(top, text="Insert Values", command=lambda: (self.insert(db.insert_entertainment, e1, e2, e3), self.added(top), self.clear(top, e1, e2, e3)))
        B1.grid(row=4, column=0)

        B2 = Button(top, text="Select All", command=lambda: (text.delete(1.0, END), text.insert(END, self.display_all(db.select_all_entertainment())), self.clear(top, e1, e2, e3)))
        B2.grid(row=1, column=2)

        B3 = Button(top, text="Delete expense", command=lambda: (self.delete_expense(db.delete_entertainment, e1, e2), self.delete(top), self.clear(top, e1, e2, e3)))
        B3.grid(row=2, column=2)

        B4 = Button(top, text="Exit", command=exit)
        B4.grid(row=3, column=2)

        B5 = Button(top, text='Clear', command=clear)
        B5.grid(row=4, column=2)

    def other(self):
        top = Toplevel(self.frame)
        top.title('Other expenses')
        l1 = Label(top, text="Name of good").grid(row=1, column=0, sticky=W, pady=2)
        l2 = Label(top, text="Price").grid(row=2, column=0, sticky=W, pady=2)
        l3 = Label(top, text="Date of purchase").grid(row=3, column=0, sticky=W, pady=2)

        e1 = Entry(top)
        e1.grid(row=1, column=1, sticky=W, pady=2)
        e2 = Entry(top)
        e2.grid(row=2, column=1, sticky=W, pady=2)
        e3 = Entry(top)
        e3.grid(row=3, column=1, sticky=W, pady=2)

        text = Text(top, width=40, height=10)
        text.grid(row=5, column=1, columnspan=2)

        def clear():
            e1.delete(0, END)
            e2.delete(0, END)
            e3.delete(0, END)

        # BUTTONS###
        B1 = Button(top, text="Insert Values", command=lambda: (self.insert(db.insert_other, e1, e2, e3), self.added(top), self.clear(top, e1, e2, e3)))
        B1.grid(row=4, column=0)

        B2 = Button(top, text="Select All", command=lambda: (text.delete(1.0, END), text.insert(END, self.display_all(db.select_all_other())), self.clear(top, e1, e2, e3)))
        B2.grid(row=1, column=2)

        B3 = Button(top, text="Delete expense", command=lambda: (self.delete_expense(db.delete_other, e1, e2), self.delete(top), self.clear(top, e1, e2, e3)))
        B3.grid(row=2, column=2)

        B4 = Button(top, text="Exit", command=exit)
        B4.grid(row=3, column=2)

        B5 = Button(top, text='Clear', command=clear)
        B5.grid(row=4, column=2)

        
def main():
    root = Tk()
    root.geometry('250x200')
    root.title("Expense Tracker")
    ExpenseTracker(root)

    root.mainloop()
        

main()
