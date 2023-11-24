# RMIT-cybersecurity-scripting
RMIT Cert 4 Cybersecuirty Scripting class

# Summary and Purpose of Assessment
This is the second (2) assessment task of two (2) assessments that you must satisfactorily complete, in order to be deemed competent for this unit.
This assessment is designed to allow you to demonstrate their skills and knowledge in the development of a script for software functions related to cyber security. This requires you to demonstrate the following:

* Determine the requirements for building the script
* Design the script
* Write the script

# Assessment Instructions
You are required to develop and test a script to meet the client’s requirements.

# What
The following tasks must be completed in this assessment:

You have recently been employed as a Cyber Security Consultant for IT Assurance Services. IT Assurance Services specialises in the provision of ICT services to a range of small and medium enterprises, including the conduct of cyber security vulnerability assessments and the subsequent design and implementation of risk mitigation solutions to secure client systems.

Your employer has asked you to develop a script that can be used to map a series of host names to their IPv4 addresses. To achieve this, you need to produce a python script that will read in a series of host names entered by the user, with the series terminated by entering a null line. The script iteratively outputs to screen the stored host names with an associated index (starting at 0), allowing the user to specify the index of a host. The script then outputs the selected host name and it’s IP address. A null line will terminate the iteration. The script should terminate with appropriate error messages if the user:
* Failed to enter any host names	
* Failed to enter a valid index
* Selected an invalid host name for resolving to an IP address

# Demonstration 

**Program fully working**

![image](https://github.com/Jasmine-108/RMIT-cybersecurity-scripting/assets/151819725/944f3da3-cd24-418b-9dbf-7c2141e7a61d)

**Failed to enter any host names**

![image](https://github.com/Jasmine-108/RMIT-cybersecurity-scripting/assets/151819725/2c5ed8a3-ca76-4630-aef6-64c2c8cb961a)

**Selected an invalid host name for resolving to an IP address**

![image](https://github.com/Jasmine-108/RMIT-cybersecurity-scripting/assets/151819725/785f4b87-00d8-49ea-b7aa-906a98870dda)

# Pseudo Code
```
BEGIN
SET hostNames to an empty list
SET ipAddresses to an empty list
PRINT "Enter a hostname or press ENTER to quit:"
READ hostname from the user
WHILE hostname is NOT empty:
ADD hostname to hostNames
READ hostname from the user
IF the length of hostNames is 0:
PRINT "No host names entered. Exiting program."
ELSE:
PRINT "Here is what you input with the associated index"
FOR i in range of the length of hostNames:
PRINT i and hostNames
READ index from the user
WHILE index is NOT empty:
TRY:
CONVERT index to an integer
IF index is less than 0 OR index is greater than OR equal to the length of hostNames:
PRINT "Invalid index exiting program"
BREAK
ELSE:
SET hostname to hostNames
TRY:
COMPUTE address
PRINT "IP address for", hostname, address
ADD address to ipAddresses
EXCEPT cannot find a valid address
PRINT "Unable to resolve hostname or not a real hostname, exiting program"
BREAK
EXCEPT wrong value entered
PRINT "Invalid input exiting program"
BREAK
READ index from the user
END
```
