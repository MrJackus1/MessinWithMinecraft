#Minecraft RCON (A bit like SSH for a MC server)

from mojang.minecraft import rcon
import re

x = open('rcon.txt','r')
ip = ('10.0.0.2')
port = 123
bannedColourCodes = r'\§[0-9a-z]'
inputText = "Please enter the command (no slash or CAPS): "

x = str(x.read())
while True:    
    with rcon.session((ip,port),(str(x))) as send:
        while True:
            command = input(inputText)
            print('')
            inputText = "RCON: "
            if command == 'restart':
                print('Restart is not allowed from here... try "reload", or "stop"', end='\n\n')
            elif command == 'reload' or command == 'reload confirm':
                send('reload confirm')   
                print('Reload Complete.' , end='\n\n')
            elif command == 'stop':
                send(command)
                print('Stopping the server!')
                break
            elif command == 'exit':
                break
            else:
                tempCommand = send(command) 
                tempCommand = re.sub(bannedColourCodes,'',tempCommand)#Removes minecraft colour codes
                print(tempCommand , end='\n')
        break        
print("Stopped.")
exit()

    
