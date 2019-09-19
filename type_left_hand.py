from tkinter import *
from tkinter import filedialog
import keyboard
import inspect, os.path

#key actions, swap, return, save, load
def swap_keys(fb, tb):
    try:
        keyboard.unhook_all_hotkeys()
    finally:
        for bind in range(len(fb.get())):
            keyboard.remap_hotkey(fb.get()[bind], tb.get()[bind])
    
        
def reset_keys(svar):
    try:
        keyboard.unhook_all_hotkeys()
        svar.set("hey, type in a char that\nwhen pressed with space types ")
    except AttributeError:
        svar.set("tried to reset reset keys")
        
def save_layout(root, lb, rb):
    filename = inspect.getframeinfo(inspect.currentframe()).filename
    path     = os.path.dirname(os.path.abspath(filename))
    saveFile =  filedialog.asksaveasfile(initialdir = path,title = "Select file",filetypes = (("text files","*.txt"),("all files","*.*"))) 
    if saveFile is not None: 
        for i in range(len(lb.get())):
            saveFile.write(lb.get()[i]+"\n")
            saveFile.write(rb.get()[i]+"\n")
        saveFile.close()
    
def load_layout(root, lb, rb):
    filename = inspect.getframeinfo(inspect.currentframe()).filename
    path     = os.path.dirname(os.path.abspath(filename))
    loadFile =  filedialog.askopenfile(initialdir = path,title = "Select file",filetypes = (("text files","*.txt"),("all files","*.*")))
    if loadFile is not None:
        lb.delete(0,END)
        rb.delete(0,END)
        i = 0
        for line in loadFile:
            if i % 2 == 0:
                lb.insert(END, line[:len(line)-1])
            else: rb.insert(END, line[:len(line)-1])
            i += 1

def addToList(fromKey, toKey, fromList, toList):
    if fromKey.get() != '' and toKey.get() != '':#have to make exceptions when binds are not legal
        fromList.insert(END,fromKey.get())
        toList.insert(END,toKey.get())
        fromKey.set('')
        toKey.set('')
    else:
        return 0

def deleteBind(fb, tb):
    left_select = fb.get(ANCHOR)
    if left_select != '':
        fb.delete(ANCHOR)
        tb.delete(fb.index(ANCHOR))
    
class app(Frame):
    def __init__(self):
        Frame.__init__(self)
        self.grid()
        self.master.title("Left Hand Typer")
        self.configure(width=300, height=400)
        self.master.resizable(0, 0)
        
        #program responses
        main_text_text = StringVar()
        main_text_text.set('hey, type in a char that\nwhen pressed with space types _')
        
        main_text = Entry(self, textvariable=main_text_text)
        main_text.grid(row=6, column=0)
        
        #frame for listboxes and entries
        twobox = Frame(self)
        twobox.grid(row=4, column=5)
        
        #frame for listboxes
        two_list_frame = Frame(twobox)
        two_list_frame.pack(side=TOP)
        
        #scrollbar for listboxes
        scrollbar = Scrollbar(two_list_frame, orient=VERTICAL)
        scrollbar.pack(side=RIGHT, fill=Y)
        
        #frombox
        emptyFrom = []
        frombinds_content = Variable(value=emptyFrom)
        frombinds = Listbox(two_list_frame, listvariable=frombinds_content, yscrollcommand=scrollbar.set)
        frombinds.pack(side=LEFT)
        
        #aesthetic padding can be improved
        padding = Label(two_list_frame, width=2)
        padding.pack(side=LEFT)
        
        #tobox
        emptyTo = []
        tobinds_content = Variable(value=emptyTo)
        tobinds = Listbox(two_list_frame, listvariable=tobinds_content, yscrollcommand=scrollbar.set)
        tobinds.pack(side=LEFT)
        
        #scrollbar command
        def yview(*args):
            frombinds.yview(*args)
            tobinds.yview(*args)
        
        #scrollbar command
        scrollbar.config(command=yview)
        
        #fill listboxes to test
        for i in range(20):
            frombinds.insert(END, i)
            tobinds.insert(END, i)
        
        #frame for from and to
        from_to = Frame(twobox)
        from_to.pack(side=TOP)
        
        
        #enter keys to swap to
        fromText = StringVar()
        textFrom = Entry(from_to, width=10, textvariable=fromText)
        textFrom.pack(side=LEFT)
        to = Label(from_to, text='to').pack(side=LEFT)
        toText = StringVar()
        textTo = Entry(from_to, width=10, textvariable=toText)
        textTo.pack(side=LEFT)
        
        #button to add entries MOVE TO MAKE MORE AESTHETIC
        add = Button(from_to, text='add', command=lambda:addToList(fromText, toText, frombinds, tobinds))
        add.pack(side=LEFT)
        
        #button to delete entries
        delete = Button(from_to, text="del", command=lambda:deleteBind(frombinds, tobinds))
        delete.pack(side=LEFT)
        
        #frame for 4 option buttons
        four_keys = Frame(self)
        four_keys.grid(row=0, column=0)
        
        #create swap button
        swap = Button(four_keys, text="swap", width = 4, command=lambda:swap_keys(frombinds_content, tobinds_content))
        swap.grid(row=0, column=0)
        
        #create reset button
        reset = Button(four_keys, text="reset", width = 4, command=lambda:reset_keys(main_text_text))
        reset.grid(row=0, column=1)
        main_text_text.set("hey, type in a char that\nwhen pressed with space types _")#this is patchworky fix later
        
        #create load button
        load = Button(four_keys, text="load", width = 4, command=lambda:load_layout(self, frombinds, tobinds))
        load.grid(row=1, column=0)
        
        #create save button
        save = Button(four_keys, text="save", width = 4, command=lambda:save_layout(self, frombinds_content, tobinds_content))
        save.grid(row=1, column=1)
        
        #keyboard frame
        key_frame = Frame(self)
        key_frame.grid(row=0, column=5,sticky="e")
    
if __name__ == '__main__':
    app().mainloop()
