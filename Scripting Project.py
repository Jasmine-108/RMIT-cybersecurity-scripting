import socket
hostNames = []
ipAddresses = []

# Get host names from user
hostname = input("Enter a hostname or press ENTER to quit: ")
while hostname != "":
    hostNames.append(hostname)
    hostname = input("Enter a hostname or press ENTER to quit: ")

# Check if the list is empty and if empty ends program
if len(hostNames) == 0:
    print("No host names entered. Exiting program.")
else:
    # Prints out host names with associated index
    print("here is what you input with the associated index")
    for i in range(len(hostNames)):
        print(i, hostNames[i])

    # Gets index from user
    index = input("Enter an index number to resolve the hostname or press ENTER to quit: ")
    while index != "":
        try:
            index = int(index)
            if index < 0 or index >= len(hostNames):
                print("Invalid index exiting program")
                break
            else:
                hostname = hostNames[index]
                try:
                    adress = socket.gethostbyname(hostname)
                    print("IP address for", hostname, adress)
                    ipAddresses.append(adress)
                except socket.gaierror:
                    print("Unable to resolve hostname or not a real hostname, exiting program")
                    break
        except ValueError:
            print("Invalid input exiting program")
            break

        index = input("Enter an index to resolve the hostname or press ENTER to quit: ")