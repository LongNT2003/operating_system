import tkinter as tk
import fifo_page_replacement
class pageReplacment:
    def __init__(self) -> None:
        self.root=tk.Tk()
        self.root.geometry('700x400')
        self.root.title('Page replacement strategy')
        self.insertFrame=tk.Frame(self.root)
        self.insertFrame.pack(side='left')
        self.left(self.insertFrame)
        self.displayAction=tk.Frame(self.root)
        self.displayAction.pack(side='right')
        self.root.mainloop()
    def left(self,root):
        selectInput=tk.Menubutton(root,text='generate random page sequence or insert',relief=tk.RIDGE)
        selectInput.pack()
        options=tk.Menu(selectInput,tearoff=0)
        selectInput.config(menu=options)
        options.add_command(label='random page sequence with input number range',command= lambda: self.generateSequence(root))
        options.add_command(label='insert page sequence',command= lambda : self.insertSequence(root))
        selectStrategy=tk.Menubutton(root,text='Selecting strategy',relief=tk.RIDGE)
        selectStrategy.pack()
        strategies=tk.Menu(selectStrategy,tearoff=0)
        selectStrategy.config(menu=strategies)
        strategies.add_command(label='FIFO',command= lambda: self.decision('FIFO'))

        
    def decision(self,type):
        self.type=type
    def generateSequence(self,root):
        try: 
            self.generating.destroy()
        except:
            pass
        try:
            self.handling.destroy()
        except:
            pass
        self.generating=tk.Text(root,height=1,width=20)
        self.generating.pack()
        self.generating.insert(index=tk.END,chars='123455')
        self.handling=tk.Button(root,text='process',font=("Arial", 11),command=self.process)
        self.handling.pack()
    def insertSequence(self,root):
        try: 
            self.generating.destroy()
        except:
            pass
        try:
            self.handling.destroy()
        except:
            pass
        self.generating=tk.Text(root,height=1,width=20)
        self.generating.pack()
        self.handling=tk.Button(root,text='process',font=("Arial", 11),command=self.process)
        self.handling.pack()
    def process(self):
        pass
    def display(self,root):
        try: 
            self.demonstration.destroy()
        except:
            pass
        self.demonstration=tk.Text(root,height=4,width=40)






if __name__=='__main__':
    run=pageReplacment()


