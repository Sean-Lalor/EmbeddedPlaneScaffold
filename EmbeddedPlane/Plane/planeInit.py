"""This will be a module containing all of the initial setup for the embedded system this will tidy the main function
    resulting. 
    This will contain the initialisation for peripherals:
    Main Engine
    Wing / Tail Flaps
    Wifi (I2C) Transmition (Recieving/Transmission)
    
    Author: Sean Lalor
    Start Date: 31/12/2022
    """

# Pulse Width Modulation Settings
# Placeholders for accurate voltages 
HIGH = 1024
MIDDLE = 512
LOW = 0

#Hash Defines power ON/OFF
ON = 1
OFF = 0

#These are hardware dependent so will be left for now

#WIFI_MAC ff:ff:ff:ff


intialize() {
    #Activate GPIO for sending power to Main Engine 
    #Set GPIO to default ON Keeps the plane from dropping
    #out of the sky

    #Activate GPIO's for Wings and Tail fins 5 total
    #set them to MIDDLE

    #Active relevant GPIO pins for WiFI chip
}