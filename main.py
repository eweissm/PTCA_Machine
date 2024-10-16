import tkinter as tk
import serial
import time
from StartUp import *
from ControlButtonFunctions import *

global ser
global ConnectionStateMessage

################################################################################################
## set up Serial Coms
################################################################################################
ComsState = False

while not ComsState:
    ComsState = runStartUp()

################################################################################################
## Robot Controls
################################################################################################
# Build GUI to take Com Port---------------------------------------------
tkTop = tk.Tk()  # Create GUI Box
tkTop.geometry('600x600')  # size of GUI
tkTop.title("PTCA-Machine Controller")  # title in top left of window

Title = tk.Label(text='PTCA Machine Controller', font=("Courier", 14, 'bold')).pack()

###############################
## Tube Properties
###############################
TubePropertiesFrame = tk.Frame(master=tkTop, width=400)
TubePropertiesFrame.pack(fill=tk.BOTH, side=tk.TOP, expand=True)

TubeFrame_Label = tk.Label(master=TubePropertiesFrame, text='Tube Properties', font=("Courier", 12, 'bold')).pack(side='top', ipadx=0, padx=0, pady=0)

TubeLengthFrame = tk.Frame(master=TubePropertiesFrame, width=400)
TubeLengthFrame.pack(fill=tk.BOTH, side=tk.TOP, expand=True)

TubeLength_Label = tk.Label(master=TubeLengthFrame, text='Tube Length (mm)', font=("Courier", 12, 'bold')).pack(side='left', ipadx=0, padx=10, pady=0)
TubeLength_entry = tk.Entry(TubeLengthFrame)
TubeLength_entry.pack(side='left', ipadx=0, padx=0, pady=0)

TubeRadiusFrame = tk.Frame(master=TubePropertiesFrame, width=400)
TubeRadiusFrame.pack(fill=tk.BOTH, side=tk.TOP, expand=True)
TubeRadius_Label = tk.Label(master=TubeRadiusFrame, text='Tube Radius (mm)', font=("Courier", 12, 'bold')).pack(side='left', ipadx=0, padx=10, pady=0)
TubeRadius_entry = tk.Entry(TubeRadiusFrame)
TubeRadius_entry.pack(side='left', ipadx=0, padx=0, pady=0)

###############################
## Muscle Properties
###############################
MusclePropertiesFrame = tk.Frame(master=tkTop, width=400)
MusclePropertiesFrame.pack(fill=tk.BOTH, side=tk.TOP, expand=True)

MuscleFrame_Label = tk.Label(master=MusclePropertiesFrame, text='Muscle Properties', font=("Courier", 12, 'bold')).pack(side='top', ipadx=0, padx=0, pady=0)

TwistAngleFrame = tk.Frame(master=MusclePropertiesFrame, width=400)
TwistAngleFrame.pack(fill=tk.BOTH, side=tk.TOP, expand=True)
TwistAngle_Label = tk.Label(master=TwistAngleFrame, text='Twist Angle (Deg)', font=("Courier", 12, 'bold')).pack(side='left', ipadx=0, padx=10, pady=0)
TwistAngle_entry = tk.Entry(TwistAngleFrame)
TwistAngle_entry.pack(side='left', ipadx=0, padx=0, pady=0)

FRAngleFrame = tk.Frame(master=MusclePropertiesFrame, width=400)
FRAngleFrame.pack(fill=tk.BOTH, side=tk.TOP, expand=True)
FRAngle_Label = tk.Label(master=FRAngleFrame, text='FR Angle (Deg)', font=("Courier", 12, 'bold')).pack(side='left', ipadx=0, padx=10, pady=0)
FRAngle_entry = tk.Entry(FRAngleFrame)
FRAngle_entry.pack(side='left', ipadx=0, padx=0, pady=0)

coldDrawRatioFrame = tk.Frame(master=MusclePropertiesFrame, width=400)
coldDrawRatioFrame.pack(fill=tk.BOTH, side=tk.TOP, expand=True)
coldDrawRatio_Label = tk.Label(master=coldDrawRatioFrame, text='Cold Draw Ratio', font=("Courier", 12, 'bold')).pack(side='left', ipadx=0, padx=10, pady=0)
coldDrawRatio_entry = tk.Entry(coldDrawRatioFrame)
coldDrawRatio_entry.pack(side='left', ipadx=0, padx=0, pady=0)

CoilAngleFrame = tk.Frame(master=MusclePropertiesFrame, width=400)
CoilAngleFrame.pack(fill=tk.BOTH, side=tk.TOP, expand=True)
CoilAngle_Label = tk.Label(master=CoilAngleFrame, text='Coil Angle (Deg)', font=("Courier", 12, 'bold')).pack(side='left', ipadx=0, padx=10, pady=0)
CoilAngle_entry = tk.Entry(CoilAngleFrame)
CoilAngle_entry.pack(side='left', ipadx=0, padx=0, pady=0)

###############################
## Controls
###############################
ControlsFrame = tk.Frame(master=tkTop, width=400)
ControlsFrame.pack(fill=tk.BOTH, side=tk.TOP, expand=True)

ControlsFrame_Label = tk.Label(master=ControlsFrame, text='Controls', font=("Courier", 12, 'bold')).pack(side='top', ipadx=0, padx=0, pady=0)

TopRowControlsFrame=tk.Frame(master=ControlsFrame, width=400)
TopRowControlsFrame.pack(fill=tk.BOTH, side=tk.TOP, expand=True)

HomeButton = tk.Button(TopRowControlsFrame,
                                       text="Home",
                                       command= Home,
                                       height=3,
                                       fg="black",
                                       width=10,
                                       bd=5,
                                       activebackground='green'
                                       ).pack(side='left', ipadx=10, padx=10, pady=40)

ColdDrawButton = tk.Button(TopRowControlsFrame,
                                       text="Cold Draw",
                                       command= lambda: ColdDraw(TubeLength_entry.get(), coldDrawRatio_entry.get()),
                                       height=3,
                                       fg="black",
                                       width=10,
                                       bd=5,
                                       activebackground='green'
                                       ).pack(side='left', ipadx=10, padx=10, pady=40)

FrButton = tk.Button(TopRowControlsFrame,
                                       text="Fiber Reinforce",
                                       command= lambda: FiberReinforce(FRAngle_entry.get(), TubeRadius_entry.get()),
                                       height=3,
                                       fg="black",
                                       width=10,
                                       bd=5,
                                       activebackground='green'
                                       ).pack(side='left', ipadx=10, padx=10, pady=40)

TwistButton = tk.Button(TopRowControlsFrame,
                                       text="Twist",
                                       command= lambda: Twist(TwistAngle_entry.get, TubeLength_entry.get(), coldDrawRatio_entry.get()),
                                       height=3,
                                       fg="black",
                                       width=10,
                                       bd=5,
                                       activebackground='green'
                                       ).pack(side='left', ipadx=10, padx=10, pady=40)

CoilButton = tk.Button(TopRowControlsFrame,
                                       text="Coil",
                                       command= lambda: Coil(CoilAngle_entry.get()),
                                       height=3,
                                       fg="black",
                                       width=10,
                                       bd=5,
                                       activebackground='green'
                                       ).pack(side='left', ipadx=10, padx=10, pady=40)

BottomRowControlsFrame=tk.Frame(master=ControlsFrame, width=400)
BottomRowControlsFrame.pack(fill=tk.BOTH, side=tk.TOP, expand=True)
StopButton = tk.Button(BottomRowControlsFrame,
                                       text="Stop",
                                       command= Stop,
                                       height=3,
                                       fg="black",
                                       width=10,
                                       bd=5,
                                       activebackground='red'
                                       ).pack(side='bottom', ipadx=10, padx=10, pady=40)

tk.mainloop()