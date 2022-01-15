from datetime import datetime
from tkinter import *

window = Tk()
window.title('My One Tkinter')
window.geometry('600x600')

result = Label(text = 'Result', bg = 'white')
result.place(x = 130, y = 200, width = 200, height = 40)

yil = Entry()
yil.place(x = 130, y = 100, width = 200, height = 40)

def farq():
    bugun = datetime.today()
    result.config(text = bugun.year - int(yil.get()))
    
tugma = Button(text = 'Hisoblash', command=farq)
tugma.place(x = 335, y = 100, width = 150, height = 40)

window.mainloop()