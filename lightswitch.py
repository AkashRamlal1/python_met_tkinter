
from cgitb import text
import tkinter as tk


window = tk.Tk()

is_off = True

button = tk.Button(text = '')
def  licht_aan_uit():
    global is_off
    
    if is_off == True :
        window.config(bg='yellow')
        print('licht aan')
        is_off = False

    else:
        window.config(bg="black")
        print('licht uit')
        is_off = True
        
    if is_off == False:
        button.config(text = 'on')
    elif is_off == True:
        button.config(text = 'off')


button = tk.Button(text='klik op mij ', command=licht_aan_uit)

    
button.pack()




# schijf hier tussen

# schijf hier tussen je code 

window.mainloop()