#Minecraft RCON (A bit like SSH for a MC server)

from mojang.minecraft import rcon

x = open('rcon.txt','r')
ip = ('10.0.0.28')
port = 1234
x = str(x.read())


with rcon.session((ip,port),(str(x))) as send:
    command = input("Please enter the command (no slash or CAPS): ")
    if command == 'restart':
        print('Restart is not allowed from here... try "reload", or "stop"')
    elif command == 'reload' or command == 'reload confirm':
        send('reload confirm')   
        print('Server reloaded!')
    elif command == 'stop':
        send(command)
        print('Stopping the server!')
    else:
        send(command)
        print(" ")
        print(send(command))
        

#send.stop()
    
