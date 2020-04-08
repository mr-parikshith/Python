'''
S02AQ02
Re-write the earlier question of S02Q02 using functions :

     - Using the starting and ending values of your car’s odometer, 
            and the measure of fuel consumed, 
            calculate the number of stops one should make for refuelling 
            while travelling from Bangalore to Goa, 
            a distance of 560 kms.
'''

def Mileage(CurrentReading, PreviousReading, VolumeOfGas):
    CurrentReading = int(CurrentReading)
    PreviousReading = int(PreviousReading)
    VolumeOfGas = int(VolumeOfGas)
    KMPL = (CurrentReading - PreviousReading)/VolumeOfGas
    #KMPL = int(KMPL)
    return KMPL
    # print("Your KMPL is", KMPL)

def Refuel_Stops (KMPL):
    Distance = 560
    Stops = Distance/KMPL
    Stops = int(Stops)
    print("You need to make about", Stops, "refueling stops between Bangalore to Goa")

# Main start from below
CurrentReading = input("Enter your current odometer reading in Kms.: ")
PreviousReading = input("Enter your previous odometer reading in Kms.: ")
VolumeOfGas = input("Enter volume of gas consumed for this journey in Lts.: ")
KMPL = Mileage(CurrentReading, PreviousReading, VolumeOfGas)
print("Your KMPL is", KMPL)
TankVolume = input("What is your gas tank volume in Lts.?: ")
print("Distance from Bangalore to Goa is 560 Kms.")
Refuel_Stops (KMPL)
