import pywhatkit

phoneNumber = input("Enter phone number of recipient: ")
message = input("Type message here: ")
hour = int(input("Time in hours: "))
minutes = int(input("Time in minutes: "))

no_of_times = int(input("Number of times you want to send the message: "))

for _ in range(no_of_times):
    pywhatkit.sendwhatmsg(phoneNumber, message, hour, minutes)
