from tkinter import *
from Encryptor import *
from Decryptor import *

class Gui:
    def __init__(self, root):

        self.encryptor = Encryptor()
        self.decryptor = Decryptor()

        self.root = root
        self.width = 400
        self.height = 160
        self.screen_width = self.root.winfo_screenwidth()
        self.screen_height = self.root.winfo_screenheight()
        self.x = (self.screen_width / 2) - (self.width / 2)
        self.y = ((self.screen_height / 2) - (self.height / 2)) * 0.6
        self.root.geometry("%dx%d+%d+%d" % (self.width, self.height, self.x, self.y))

        self.root.configure(background='#3B3B3B')
        self.root.title("timi")
        self.root.resizable(False, False)

        self.input_entry = Entry(self.root, font="Arial 10", relief="flat")
        self.input_entry.place(x=40, y=18, width=320, height=25)

        self.encrypt_button = Button(self.root, command=self.encrypt, fg="#000000", font="Arial 8 bold", activeforeground="#FFFFFF",
                             activebackground="#ADADAD", bg="#D3D3D3", text='encrypt', relief="flat")
        self.encrypt_button.place(x=120, y=55, width=70)

        self.decrypt_button = Button(self.root, command=self.decrypt, fg="#000000", font="Arial 8 bold", activeforeground="#FFFFFF",
                                     activebackground="#ADADAD", bg="#D3D3D3", text='decrypt', relief="flat")
        self.decrypt_button.place(x=210, y=55, width=70)

        self.scrollbar = Scrollbar(root)
        self.output_field = Text(root, height=3)
        self.scrollbar.place(x=342, y=92, width=18, height=52)
        self.output_field.place(x=40, y=92, width=300)
        self.output_field.config(yscrollcommand=self.scrollbar.set)
        self.scrollbar.config(command=self.output_field.yview)

    def encrypt(self):
        self.output_field.delete('1.0',END)
        inputs = self.input_entry.get()
        #if len(inputs) < 10 and len(inputs) != 0:
        #    self.output_field.insert(END, self.encryptor.run(inputs))
        start = 0
        end = 9
        output = ""
        while True:
            if end >= len(inputs):
                output += self.encryptor.run(inputs[start:len(inputs)])
                break
            else:
                output += self.encryptor.run(inputs[start:end]) + "00"
                start,end = end,end+9
        self.output_field.insert(END, output)

    def decrypt(self):
        self.output_field.delete('1.0', END)
        inputs = self.input_entry.get()
    #    if self.input_entry.get() != "":
    #        self.output_field.insert(END, self.decryptor.run(self.input_entry.get()))
        output = ""
        end = 0
        while True:
            if inputs[end:end+2] == "00":
                output += self.decryptor.run(inputs[:end])
                inputs = inputs[end+2:]
                end = 0
            elif end == len(inputs):
                output += self.decryptor.run(inputs[:end])
                break
            end += 1
            print(end)
        self.output_field.insert(END, output)

root = Tk()
window = Gui(root)
root.mainloop()
