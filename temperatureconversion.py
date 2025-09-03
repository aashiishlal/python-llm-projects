#Convert temperature between Celsius, Fahrenheit, and Kelvin.

#Learn input/output, basic arithmetic, and conditional logic.

class temperature():
    def __init__(self,temp1,type1):
        temperature.temp=float(temp1)
        temperature.type=type1.lower()

    def convert_from_Celsius(self):
       if self.type=='c':
           #(0°C × 9/5) + 32 = 32°F
           Fahrenheit = (self.temp * 1.8)+32.0
           #0°C + 273.15 = 273.15K
           Kelvin= +273.15
           return Fahrenheit,Kelvin

    def convert_from_Fahrenheit(self):
       if self.type=='f':
           #(32°F − 32) × 5/9 = 0°C
           Celcius= (self.temp-32.0)* (5/9)
           #(32°F − 32) × 5/9 + 273.15 = 273.15K

           Kelvin= ((self.temp-32)*(5/9))+273.15
           return Celcius,Kelvin

    def convert_from_Kelvin(self):
       if self.type=='k':
           #0K − 273.15 = -273.1°C
           Celcius= (self.temp-273.15)
           #(0K − 273.15) × 9/5 + 32 = -459.7°F
           Kelvin= ((self.temp-273.15)*(9/5))+32
           return Celcius,Kelvin




temp1=input("Enter the temperature:")
type1=input("Input the type:").lower()

Temp=temperature(temp1,type1)

if Temp.type=='c':
    Fah, Kel = Temp.convert_from_Celsius()
    print(f"{Temp.temp} degree Celcius={Fah} Fahrenheit= {Kel} Kelvin")
elif Temp.type == 'f':
    Cel, Kel = Temp.convert_from_Fahrenheit()
    print(f"{Temp.temp} Fahrenheit={Cel} degree Celcius= {Kel} Kelvin")
elif Temp.type == 'k':
    Cel, Fah = Temp.convert_from_Kelvin()
    print(f"{Temp.temp} Kelvin ={Cel} degree Celcius= {Fah} Fahrenheit")
else:
    print("wrong input")



