'''
Re-write the earlier question of S02Q02 using functions :

     - Using the starting and ending values of your car’s odometer, 
            calculate its mileage
'''

def mileage(CurrentReading, PreviousReading, VolumeOfGas):
    CurrentReading = int(CurrentReading)
    PreviousReading = int(PreviousReading)
    VolumeOfGas = int(VolumeOfGas)
    mileage = (CurrentReading - PreviousReading)/VolumeOfGas
    # return milage
    print("Your mileage is", mileage)

# Main start from below
CurrentReading = input("Enter your current odometer reading: ")
PreviousReading = input("Enter your previous odometer reading: ")
VolumeOfGas = input("Enter volume of gas used for this journey: ")

mileage(CurrentReading, PreviousReading, VolumeOfGas)
