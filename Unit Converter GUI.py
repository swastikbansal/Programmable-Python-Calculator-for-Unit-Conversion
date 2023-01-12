#Programmable Python Calculator for Unit Conversion (in metric)
# 1. Temprature
# 2. Pressure 
# 3. Length
# 4. Velocity
# 5. Force

from tkinter import *
from tkinter import messagebox

def check(unit):
   if (unit.get()).isnumeric() == False:
      messagebox.showerror("Input Error","Plese give a numerical input.")
      return None
   else :
      return 0 

#GUI Main Window
main_win=Tk()
main_win.title("Programmable Python Calculator for Unit Conversion")
main_win.resizable(False,False)
main_win.geometry("400x400")

head_label= Label(main_win,text = "   Programmable Python Calculator \n for Unit Conversion",font = ('Times', 20))
head_label.grid(row = 0 ,column = 0)

#Options Frame
opt_frame = Frame(main_win,bd = 1,width = 420)
opt_frame.grid()

intro_label = Label(opt_frame,text = "\nSelect the Unit from below of \nwhich you want conversion.\n",font = ('Times',14),justify="left")
intro_label.grid(row = 0,column= 0)

#Dropdown Menu Options
options = ["Temprature",
           "Pressure",
           "Length",
           "Velocity",
           "Force"]

clicked_opt = StringVar()

clicked_opt.set("Select Option")
drop = OptionMenu(opt_frame,clicked_opt,*options)
drop.grid(row=0,column = 1)

def next(clicked_opt):
   #Note Label 
   note_label = Label(main_win,text = "Note : Give input in the respective SI Units.")
   note_label.grid(row = 3)

   next_frame = Frame(main_win,bd = 0)
   next_frame.grid(row = 7)

   selected = clicked_opt.get()

   #Temperature
   if selected == "Temprature" :
      def temprature():
         temp_SI_unit_K = StringVar()
                 
         temp_label = Label(main_win,text = "\nEnter the temp in Kelvin to convert :")
         temp_label.grid(row = 4)

         temp_inp = Entry(main_win,bd = 2,textvariable=temp_SI_unit_K)
         temp_inp.grid(row = 5)

         #Conversion func for button
         def temp_convert():
            #Checking the input
            
            if check(temp_SI_unit_K) != None :  
               #Converting into other units. 
               K = float(temp_SI_unit_K.get())
               C = K - 273.15
               F = (K - 273.15) * ((9/5)+32)
               R = (C + 496)

               #Labels
               print_label = Label(next_frame,text="\nAll the converted units are printed below")
               print_label.grid(row=2)

               K_label = Label(next_frame,text = f"Kelvin    : {K}K")
               K_label.grid(row= 3)

               C_label = Label(next_frame,text = f"Celsius   : {round(C,2)}\u00B0C")
               C_label.grid(row= 4)

               F_label = Label(next_frame,text = f"Fehrenite : {round(F,2)}\u00B0F")
               F_label.grid(row= 5)

               R_label = Label(next_frame,text = f"Rankine   : {round(R,2)}\u00B0R")
               R_label.grid(row= 6)

               main_win.geometry("400x440")

         go_button = Button(main_win,text = "Go",command = temp_convert)
         go_button.grid(row = 6)

      temprature()
   
   #Pressure
   if selected == "Pressure" :
      def pressure():

         press_SI_unit_Pa = StringVar()
                 
         press_label = Label(main_win,text = "\nEnter the pressure in Pascal to convert :")
         press_label.grid(row = 4)

         press_inp = Entry(main_win,bd = 2,textvariable=press_SI_unit_Pa)
         press_inp.grid(row = 5)
         
         #Conversion func for button
         def press_convert():
            #Checking the input
            if check(press_SI_unit_Pa) != None : 
               #Converting into other units. 
               Pa = float(press_SI_unit_Pa.get())
               bar = Pa * (10**5)
               at = Pa * (98066.5)  #Technical_Atmosphere
               atm = Pa * 101325   #standard_atmosphere
               torr = Pa * 133.322
               
               #Labels
               print_label = Label(next_frame,text="\nAll the converted units are printed below")
               print_label.grid(row=2)

               Pa_label    = Label(next_frame,text = f"Pascal : {Pa} Pa")
               Pa_label.grid(row= 3)

               bar_label   = Label(next_frame,text = f"Bar : {round(bar,2)} bar")
               bar_label.grid(row= 4)

               at_label    = Label(next_frame,text = f"Technical Atmoshphere : {round(at,2)} at")
               at_label.grid(row= 5)

               atm_label   = Label(next_frame,text = f"Standard Atmosphere : {round(atm,2)} atm")
               atm_label.grid(row= 6)

               torr_label  = Label(next_frame,text = f"Torr : {round(torr,2)} torr")
               torr_label.grid(row= 7)

               main_win.geometry("400x440")

         go_button = Button(main_win,text = "Go",command = press_convert)
         go_button.grid(row = 6)
         
      pressure()

   #Length
   if selected == "Length" :
      def length():
         len_SI_unit_m = StringVar()
                 
         len_label = Label(main_win,text = "\nEnter the length in Metre to convert :")
         len_label.grid(row = 4)

         len_inp = Entry(main_win,bd = 2,textvariable=len_SI_unit_m)
         len_inp.grid(row = 5)
         
         #Conversion func for button
         def len_convert():
            #Checking the input
            if check(len_SI_unit_m) != None : 
               #Converting into other units. 
               m = float(len_SI_unit_m.get())
               mm = m * 1000
               cm = m * 100
               dm = m * 10
               dam = m * 0.1
               hm = m * 0.01
               km = m * 0.001
            
               #Labels
               print_label = Label(next_frame,text = "\nAll the converted units are printed below")
               print_label.grid(row = 2)

               mm_label = Label(next_frame,text = f"Miliometre : {round(mm,3)} mm")
               mm_label.grid(row = 3)

               cm_label = Label(next_frame,text = f"Centimetre : {round(cm,3)} cm")
               cm_label.grid(row = 4)

               dm_label = Label(next_frame,text = f"Decimetre : {round(dm,3)} dm")
               dm_label.grid(row = 5)

               m_label = Label(next_frame,text = f"Metre : {m} m")
               m_label.grid(row = 6)

               dam_label = Label(next_frame,text = f"Decametre : {round(dam,3)} dam")
               dam_label.grid(row = 7)

               hm_label = Label(next_frame,text = f"Hectometre : {round(hm,3)} hm")
               hm_label.grid(row = 8)

               km_label = Label(next_frame,text = f"Kilometre : {round(km,3)} km")
               km_label.grid(row = 9)

               main_win.geometry("400x480")

         go_button = Button(main_win,text = "Go",command = len_convert)
         go_button.grid(row = 6)

      length()

#Velocity
   if selected == "Velocity" :
      def Velocity():
         vel_SI_unit_mps = StringVar()
                 
         vel_label = Label(main_win,text = "\nEnter the Velocty in metre/sec to convert :")
         vel_label.grid(row = 4)

         vel_inp = Entry(main_win,bd = 2,textvariable=vel_SI_unit_mps)
         vel_inp.grid(row = 5)
              
         #Conversion func for button
         def vel_convert():
            #Checking the input
             if check(vel_SI_unit_mps) != None : 
               #Converting into other units. 
               mps = float(vel_SI_unit_mps.get())
               kmph = mps * 3.6
               kmps = mps * 0.001
               mph = mps * 3600

               #Labels
               print_label = Label(next_frame,text="\nAll the converted units are printed below")
               print_label.grid(row=2)

               mph_label = Label(next_frame,text = f"Metre/Hour  : {round(mph,2)} m/hr")
               mph_label.grid(row= 3)

               mps_label = Label(next_frame,text = f"Metre/sec : {mps} m/s")
               mps_label.grid(row= 4)

               kmph_label = Label(next_frame,text = f"Km/hr : {round(kmph,2)} km/hr")
               kmph_label.grid(row= 5)

               kmps_label = Label(next_frame,text = f"Km/Sec : {round(kmps,2)} km/s")
               kmps_label.grid(row= 6)

               main_win.geometry("400x440")

         go_button = Button(main_win,text = "Go",command = vel_convert)
         go_button.grid(row = 6)

      Velocity()

#Force
   if selected == "Force" :
      def Force():
         f_SI_unit_n = StringVar()
                 
         force_label = Label(main_win,text = "\nEnter the force in Newton to convert :")
         force_label.grid(row = 4)

         force_inp = Entry(main_win,bd = 2,textvariable=f_SI_unit_n)
         force_inp.grid(row = 5)
              
         #Conversion func for button
         def for_convert():
            #Checking the input
            if check(f_SI_unit_n) != None : 
               N = float(f_SI_unit_n.get())
               dyne = N * (10**5)
               gf = N * 101.971621
               kgf = N * 0.101972

               #Labels
               print_label = Label(next_frame,text="\nAll the converted units are printed below")
               print_label.grid(row=2)

               dyne_label = Label(next_frame,text = f"Metre/Hour  : {round(dyne,3)} dyne")
               dyne_label.grid(row= 3)

               gf_label = Label(next_frame,text = f"Metre/sec : {round(gf,3)} gf")
               gf_label.grid(row= 4)

               kgf_label = Label(next_frame,text = f"Km/hr : {round(kgf,3)} kgf")
               kgf_label.grid(row= 5)

               main_win.geometry("400x440")

         go_button = Button(main_win,text = "Go",command = for_convert)
         go_button.grid(row = 6)

      Force()

# OK Button
proceed_button = Button(main_win,text = "Proceed",command = lambda: next(clicked_opt))
proceed_button.grid(row = 2)
   
main_win.mainloop()

