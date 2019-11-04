import tkinter as tk
from tkinter import *  

mainWindow = tk.Tk()
mainWindow.title('NBI Testbed')
mainWindow.configure(bg = 'light grey')
mainWindow.geometry('380x400')

# variable
varLableProtocol = tk.StringVar()
varProtocol = tk.StringVar()
varPSM = tk.StringVar()
varUnit = tk.StringVar()

# function
def confirm():
    # var = usecaseEntry.get()
    # text.insert('insert', var)
    # text.insert('end', ' settings...')
    # return var
    return

# def selectProtocol():
#     var = listProtocol.get(listProtocol.curselection())
#     varLableProtocol.set(var)

def selectProtocol():
    lableProtocol.config(text = varProtocol.get())

def selectPSM():
    lablePSM.config(text = varPSM.get())

def showScaleValue(var):
    var_unit = varUnit.get()
    lableInterval.config(text = var + ' ' + var_unit)

def change_dropdown(*args):
    print(varUnit.get())

def chooseUnit(var):
    var_sacle = sacleInterval.get()
    var_str = str(var_sacle)
    lableInterval.config(text = var_str + ' ' + var)

def saveValue():
    var = usecaseEntry.get()
    usecaseEntry.config(text = var)

# handle function
def handle_focus_in(_):
    usecaseEntry.delete(0, tk.END)
    usecaseEntry.config(fg='black')

def handle_focus_out(_):
    usecaseEntry.delete(0, tk.END)
    usecaseEntry.config(fg='grey')
    usecaseEntry.insert(0, "Enter usecase name")

def handle_enter(txt):
    print(usecaseEntry.get())
    handle_focus_out('dummy')

def handle_focus_in_1(_):
    deviceEntry.delete(0, tk.END)
    deviceEntry.config(fg='black')

def handle_focus_out_1(_):
    deviceEntry.delete(0, tk.END)
    deviceEntry.config(fg='grey')
    deviceEntry.insert(0, "NBI device")

def handle_enter_1(txt):
    print(deviceEntry.get())
    handle_focus_out_1('dummy')

# test framework for title
frame = tk.Frame(mainWindow)
frame.configure(background = "grey64", borderwidth = 3)
frame.pack(fill = BOTH)

#main title
mainLable = tk.Label(frame, text = "NBI power consumption testbed",bg = 'light grey')
mainLable.pack(pady = 5)

# user enter usecase
usecaseEntry = tk.Entry(frame, show = None, fg = 'grey', borderwidth = 2.5)
usecaseEntry.insert(0, "Enter usecase name")
usecaseEntry.bind("<FocusIn>", handle_focus_in)
# usecaseEntry.bind("<FocusOut>", handle_focus_out)
usecaseEntry.bind("<Return>", handle_enter)
usecaseEntry.pack(side = 'left', padx = (20,2), pady = 5)

#user enter device name
deviceEntry = tk.Entry(frame, show = None, fg = 'grey', borderwidth = 2.5, width = 10,)
deviceEntry.insert(0, "NBI device")
deviceEntry.bind("<FocusIn>", handle_focus_in_1)
# deviceEntry.bind("<FocusOut>", handle_focus_out_1)
deviceEntry.bind("<Return>", handle_enter_1)
deviceEntry.pack(side = 'right', padx = (2,20), pady = 5)

# buttomSave = tk.Button(frame, text = "Save", width = 10, height = 1, command = saveValue)
# buttomSave.pack(side = 'right', padx = (2,20), pady = 5)

# text = tk.Text(frame, height = 1, width = 30)
# text.grid(row = 2, column = 0 , columnspan = 3, padx = 10, pady = 10)

#### framework
mainFrame0 = tk.Frame(mainWindow)
mainFrame0.configure(bg = "light grey")
mainFrame0.pack(fill = BOTH)

leftFrame0 = tk.Frame(mainFrame0)
leftFrame0.pack(side = 'left')
leftFrame0.configure(bg = "light grey", padx = 5, bd = 5)
rightFrame0 = tk.Frame(mainFrame0)
rightFrame0.pack(side = 'right')
rightFrame0.configure(bg = "light grey", padx = 5, bd = 5)

mainFrame1 = tk.Frame(mainWindow)
mainFrame1.configure(bg = 'light grey')
mainFrame1.pack(fill = BOTH)

leftFrame1 = tk.Frame(mainFrame1)
leftFrame1.pack(side = 'left')
leftFrame1.configure(bg = "light grey", padx = 5, bd = 5)
rightFrame1 = tk.Frame(mainFrame1)
rightFrame1.pack(side = 'right')
rightFrame1.configure(bg = "light grey", padx = 5, bd = 5)

#### user select protocol & PSM mode

# lableProtocol = tk.Label(leftFrim0, bg = 'yellow', width = 5, textvariable = varLableProtocol)
# lableProtocol.pack()

# buttomSelectPro = tk.Button(leftFrim0, text = "Select Protocol", width =10, height = 3, command = selectProtocol)
# buttomSelectPro.pack()

# varProtocol.set(("TCP","UDP"))
# listProtocol = tk.Listbox(leftFrim0, height = 2, listvariable = varProtocol)
# listProtocol.pack()
paned_0 = tk.PanedWindow(mainFrame0, orient = HORIZONTAL, bg = 'grey64', bd = 10)
paned_0.pack(fill = BOTH, padx = 10, pady = 10)

paned_0L = tk.PanedWindow(paned_0, orient = VERTICAL, bd = 5, bg = 'grey64')
paned_0L.pack(fill = BOTH, padx = (30,15), side = 'left')

paned_0R = tk.PanedWindow(paned_0, orient = VERTICAL, bd = 5, bg = 'grey64')
paned_0R.pack(fill = BOTH, padx = (15,30), side = 'right')

lableProtocol = tk.Label(paned_0L, bg = 'light grey', width = 10, height = 1, text = "Set Protocol")
lableProtocol.pack(padx = 10, pady = 10)

buttomTCP = tk.Radiobutton(paned_0L, bg = 'grey', text = "TCP", variable = varProtocol, value = "TCP On", command = selectProtocol)
buttomTCP.pack()

buttomUDP = tk.Radiobutton(paned_0L, bg = 'grey', text = "UDP", variable = varProtocol, value = "UDP On", command = selectProtocol)
buttomUDP.pack()

# psm mode setting
lablePSM = tk.Label(paned_0R, bg = 'light grey', width =10, height = 1, text = "Set PSM")
lablePSM.pack(fill = BOTH, padx = 10, pady = 10)

buttomPSMon = tk.Radiobutton(paned_0R, bg = 'grey', text = "On", variable = varPSM, value = "PSM On", command = selectPSM)
buttomPSMon.pack()

buttomPSMoff = tk.Radiobutton(paned_0R, bg = 'grey', text = "Off", variable = varPSM, value = "PSM Off", command = selectPSM)
buttomPSMoff.pack()

####interval setting & time unit
paned_2 = tk.PanedWindow(mainFrame1, orient = VERTICAL, bd = 5, bg = 'grey64')
paned_2.pack(fill = BOTH, padx = 10)

lableInterval = tk.Label(paned_2, bg = 'light grey', width = 10, text = 'Interval')
lableInterval.pack(padx = 10, pady = 10)

paned_2H = tk.PanedWindow(paned_2, orient = HORIZONTAL, bd = 5, bg = 'grey64')
paned_2H.pack(fill = BOTH, padx = 10)

sacleInterval = tk.Scale(paned_2H, label='', from_= 1, to = 59, orient = tk.HORIZONTAL, length = 200
                        , showvalue = 0, tickinterval = 58, resolution = 1, command = showScaleValue)
sacleInterval.pack(side = 'left', padx = 5, pady = 5)

# time unit
choices = { 'Seconds','Minutes','Hours','Days','Years'}
varUnit.set('Seconds')
unitMenu = tk.OptionMenu(paned_2H, varUnit, *choices, command = chooseUnit)
unitMenu.pack(side = 'right', padx = 5, pady = 5)
varUnit.trace('w', change_dropdown)

####confirm & result
frameBottom = tk.Frame(mainWindow)
frameBottom.configure(bg = 'grey64')
frameBottom.pack(fill = BOTH, pady = 10)

buttomConfirm = tk.Button(frameBottom, text = "Confirm", width = 10, height = 2, command = confirm)
buttomConfirm.pack(padx = 10, pady = 10)






tk.mainloop()