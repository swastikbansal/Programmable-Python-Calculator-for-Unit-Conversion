#Programmable Python Calculator for Unit Conversion (in metric)
# 1. Temprature
# 2. Pressure 
# 3. Length
# 4. Velocity
# 5. Force

#Input will be taken in their respective SI units

print("""Programmable Python Calculator for Unit Conversion (in metric)
 1. Temprature
 2. Pressure 
 3. Length
 4. Velocity
 5. Force""")

option = int(input("Enter the S.No. of unit of which you want conversions :"))

#1. Temprature
if option == 1:
   print("\nTemprature")
   K =  input("Enter the temp in Kelvin to convert :")
   
   if K.isalpha():
      print("\nEnter a valid input.")
      quit()
   
   else:
      K = float(K)
      #Converting in to rest of units
      C = K - 273.15
      F = (K - 273.15) * ((9/5)+32)
      R = (C + 496)

      #Printing all the obtained units value respectively
      print("\nAll the converted units are printed below")
      print("Kelvin :",K,"K")
      print("Celsius :",round(C,2),"C")
      print("Fehrenite :",round(F,2),"F")
      print("Rankine :",round(R,2),"R")

#2. Pressure
elif option == 2:
   print("\nPressure")
   Pa =  input("Enter the pressure in Pascal to convert :")

   if Pa.isalpha():
      print("\nEnter a valid input.")
      quit()

   else:
      Pa = float(Pa)
      #Extracting all the converted unit values
      bar = Pa * (10**5)
      at = Pa * 98066.5  
      atm = Pa * 101325   
      torr = Pa * 133.322

      #Printing all the obtained units value respectively
      print("\nAll the converted units are printed below")
      print(f"Pascal : {Pa} Pa")
      print(f"Bar : {round(bar,2)} bar")
      print(f"Technical Atmosphere : {round(at,2)} at")
      print(f"Standard Atmosphere : {round(atm,2)} atm")
      print(f"Torr : {round(torr,2)} Torr")

#3 Length
elif option == 3:
   print("\nLength")
   m = input("Enter the length in Meter to convert : ")

   if m.isalpha():
      print("\nEnter a valid input.")
      quit()

   else:
      m = float(m)
      #Extracting all the converted units
      mm = m* 1000
      cm = m* 100
      dm = m* 10
      dam = m* 0.1
      hm = m* 0.01
      km = m* 0.001

      #Printing all the obtained units value respectively
      print("\nAll the converted units are printed below")
      print(f"Kilometer : {round(km,3)} km")
      print(f"Hectometer : {round(hm,3)} hm")
      print(f"Dacameter : {round(dam,3)} dam")
      print(f"Meter : {round(m,3)} m")
      print(f"Decimeter : {round(dm,3)} dm")
      print(f"Centimeter : {round(cm,3)} cm")
      print(f"Milimeter : {round(mm,3)} mm")

#4 Velocity
elif option == 4:
   print("\nVelocity")
   mps = input("Enter the Velocity in m/s to convert : ")
   
   if mps.isalpha():
      print("\nEnter a valid input.")
      quit()

   else:
      mps = float(mps)
      #Extracting all the converted units
      kmph = mps * 3.6
      kmps = mps * 0.001
      mph = mps * 3600

      #Printing all the obtained units value respectively
      print(f"Meter per Second : {round(mps,3)} m/s")
      print(f"Meter per Hour : {round(mph,3)} m/hr")
      print(f"Kilometer per Second : {round(kmps,3)} km/s")
      print(f"Kilometer per Hour : {round(kmph,3)} km/hr")

#5 Force
elif option == 5:
   print("\nForce")
   N = input("Enter the force in Newton to convert : ")

   if N.isalpha():
      print("\nEnter a valid input.")
      quit()

   else:
      N = float(N)
      #Extracting all the converted units
      dyne = N * (10**5)
      gf = N * 101.971621
      kgf = N * 0.101972

      #Printing all the obtained units value respectively
      print(f"Newton : {N} N")
      print(f"dyne : {dyne} dyne")
      print(f"Gram Force : {round(gf,2)} gf")
      print(f"Kilograms Force : {round(kgf,2)} kgf")

else:
   print("\nInvalid Input.")