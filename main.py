from tkinter import *

root = Tk()
root.title('Shopping List')
root.configure(bg='#f7f8fa')


label = Label(text = "Shopping List",font=('MuseoModerno',85,'bold'),fg='#09339c')
label.configure(bg='#f7f8fa')

label.pack(fill=X)

def additem():
    e = Entry(root)
    e.pack()
    def newlabel():
        Label(text=e.get(),font=('MuseoModerno',20,'bold'),width = 25,height = 2,bg='#e3e5e8',fg='#09339c').pack()
        ok1.pack_forget()
        e.pack_forget()
    
    ok1 = Button(text="Done",bg='#e3e5e8',font=('MuseoModerno',20,'bold'),command=newlabel,padx=50,pady=15,fg='#09339c')
    ok1.pack(side=BOTTOM)

neworld = Button(text = "Add Item",font=('MuseoModerno',20,'bold'),width = 25,height = 2, fg='#09339c',command=additem)
neworld.configure(bg='#e3e5e8')
neworld.place(relx=0.5, rely=0.5, anchor='center')
neworld.pack()

root.mainloop()


budget = float(input('Hello, how much was your budget?: '))
tc = float(input('How much did you spend after shopping?:'))
if budget-tc == 0:
    print('You have',budget-tc,'remaining on your budget')
    print('Wow! You spent exactly as much as the budget!')
elif budget-tc > 0:
    print('You have',budget-tc,'remaining on your budget')
    print('Amazing, you saved', budget-tc)
else:
    print('You went over your budget by', tc-budget,'\nNext time, try to follow your budget better')
