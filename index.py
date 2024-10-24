def celsius_to_fahrenheit(celsius):
    return (celsius + 32) * 1.8
def fahrenheit_to_celsius(fahrenheit):
    return(fahrenheit - 32) / 1.8



def temperature_converter():
    print('Temperature Converter')
    print('1. Celsius to Fahrenheit')
    print('2. Fahrenheit to Celsius')
   
    
    choice = int(input('Choose an Option: '))
    
    if choice == 1:
        celsius = float(input('Enter temperature in Celsius: '))
        print(f'{celsius:.2f} C is {celsius_to_fahrenheit(celsius):.2f} F')
    elif choice == 2:
        fahrenheit = float(input('Enter temperature in Fahrenheit: '))
        print(f'{fahrenheit:.2f} F is {fahrenheit_to_celsius(fahrenheit):.2f} C')
        
temperature_converter()
