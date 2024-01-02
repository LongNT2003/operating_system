import tkinter as tk
import NRULFU
import FIFOMFU
import random
import OPT_LRU
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
        self.display(self.displayAction)
        self.root.mainloop()
    def left(self,root):
        selectInput=tk.Menubutton(root,text='generate random page sequence or insert',relief=tk.RIDGE)
        selectInput.pack()
        options=tk.Menu(selectInput,tearoff=0)
        selectInput.config(menu=options)
        options.add_command(label='random page sequence with input number range',command= lambda: self.generateSequence(root))
        options.add_command(label='insert page sequence',command= lambda : self.insertSequence(root))

    def generateSequence(self,root):
        try: 
            self.generating.destroy()
        except:
            pass
        self.generating=tk.Text(root,height=2,width=40)
        self.generating.pack()
        sequence_length = 15
        numbers_range = range(10)

        random_sequence = [random.choice(numbers_range) for _ in range(sequence_length)]
        self.generating.insert(index=tk.END,chars=str(random_sequence)[1:-1])
        self.select_strategy()

    def insertSequence(self,root):
        try: 
            self.generating.destroy()
        except:
            pass
        self.generating=tk.Text(root,height=2,width=40)
        self.generating.pack()

        self.select_strategy()
    def select_strategy(self):
        try:
            self.selectStrategy.destroy()
            self.insertMemorySize.destroy()
        except:
            pass
        self.insertMemorySize=tk.Entry(self.insertFrame)
        self.insertMemorySize.pack()       
        self.selectStrategy=tk.Menubutton(self.insertFrame,text='Selecting strategy',relief=tk.RIDGE)
        self.selectStrategy.pack()
        strategies=tk.Menu(self.selectStrategy,tearoff=0)
        self.selectStrategy.config(menu=strategies)
        strategies.add_command(label='FIFO',command= lambda: self.process('FIFO'))
        strategies.add_command(label='MFU',command= lambda: self.process('MFU'))
        strategies.add_command(label='NRU',command= lambda: self.process('NRU'))
        strategies.add_command(label='LFU',command= lambda: self.process('LFU'))
        strategies.add_command(label='OPT',command= lambda: self.process('OPT'))
        strategies.add_command(label='LRU',command= lambda: self.process('LRU')) 

    def process(self,type):
        memorySize=int(self.insertMemorySize.get())
        self.demonstration.delete("1.0", tk.END)
        input_content = [int(x) for x in self.generating.get("1.0", tk.END).split(',')]
        if type=='FIFO':
            fault, states = FIFOMFU.fifo_page_replacement(input_content, memorySize)
        elif type=='MFU':
            fault,states= FIFOMFU.mfu_page_replacement(input_content,memorySize)
        elif type=='NRU':
            fault,states=NRULFU.nru(input_content,memorySize)
        elif type=='LFU':
            fault,states=NRULFU.lfu(input_content,memorySize)
        elif type=='OPT':
            fault,states=OPT_LRU.optimal(input_content,memorySize)
        elif type=='LRU':
            fault,states=OPT_LRU.lru(input_content,memorySize)    
        for index in range(len(states)):
            self.demonstration.insert(tk.END, f"{states[index]}   {input_content[index]}\n")
        self.demonstration.insert(tk.END, f"number of page fault: {fault}\n")
    def display(self,root):
        self.demonstration=tk.Text(root,height=40,width=40)
        self.demonstration.pack()






if __name__=='__main__':
    run=pageReplacment()


