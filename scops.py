import paramiko
import sys
import os

client = paramiko.SSHClient()
client.load_system_host_keys()
client.set_missing_host_key_policy(paramiko.AutoAddPolicy())

#enter the credentials of the droid you want to communicate with
proxy = None
#enter the public ip of the host at which droid you want to communicate is running.
host = '54.210.74.147'
#make sure that droid you are communicating with has ssh running on 22.
port = 22
transport = paramiko.Transport((host, port))
#username and password of the ssh supported user.
username = "scops"
password = "mehta123"

transport.connect(username = username, password = password)
sftp = paramiko.SFTPClient.from_transport(transport)
print("Hey droid")
experiences = raw_input("Enter your experiences separated by ; or just press ENTER if you don't have any: \n")
allexp = experiences.split(';')

if(len(allexp) != 0 and allexp[0] != ''):
    print "Experiences you entered are: \n"
    print allexp

orders = raw_input("Enter your orders separated by ; or just press ENTER if you don't have any: \n")
allorder = orders.split(';')
if(len(allorder) != 0 and allorder[0] != ''):
    print "Orders you entered are: \n" 
    print allorder

#inserting experiences in the file
if(len(allexp) != 0 and allexp[0] != ''):
    if(os.path.exists('./droid/experiences.txt') == False):
        print "in here"
        if(os.path.exists('./droid') == False):
            os.makedirs('./droid')
        file = open("./droid/experiences.txt", "w")
        file.write("Experiences of this droid are: \n")
        for exp in allexp:
            if(exp != ""):
                file.write("=>  " + exp + "\n")
        file.close()
    else:
        file = open("./droid/experiences.txt", "a")
        for exp in allexp:
            if(exp != ""):
                file.write("=>  " + exp + "\n")
        file.close()
    #there is a need to a make a update on the other side experience file i.e on another droid
    #because there is a change
    localpath = "./droid/experiences.txt"
    filepath = "itsexperiences.txt"
    remotedir = "./droid/anotherdroid/"

    #also need to check the other side files and directories
    try:
       sftp.chdir(remotedir)
       print "experience dir is on remote machine" 
    except IOError:
       try:
           sftp.chdir('./droid')
           print "in here man"
           sftp.mkdir('./anotherdroid/')
           sftp.chdir('./anotherdroid/')
    
       except IOError:
           sftp.mkdir('./droid')
           sftp.chdir('./droid')
           sftp.mkdir('./anotherdroid/')
           sftp.chdir('./anotherdroid/')

  
    sftp.put(localpath, filepath)
    sftp.close()




sftp = paramiko.SFTPClient.from_transport(transport)

#insering orders in the file
if(len(allorder) != 0 and allorder[0] != ''):
    print "in orders"
    if(os.path.exists('./droid/orders.txt') == False):
        print "in here"
        if(os.path.exists('./droid') == False):
            os.makedirs('./droid')
        file = open("./droid/orders.txt", "w")
        file.write("Orders of this droid are: \n")
        for order in allorder:
            if(order != ""):
                file.write("=>  " + order + "\n")
        file.close()
    else:
        file = open("./droid/orders.txt", "a")
        for order in allorder:
            if(order != ""):
                file.write("=>  " + order + "\n")
        file.close()
    
    #there is a need to a make a update on the other side orders file i.e order file on another droid.
    localpath = "./droid/orders.txt"
    filepath = "itsorders.txt"
    remotedir = "./droid/anotherdroid/"

    #also need to check the other side files and directories
    try:
       sftp.chdir(remotedir)
       print "orders dir is on remote machine" 
    except IOError:
       try:
           sftp.chdir('./droid')
           print "in here man"
           sftp.mkdir('./anotherdroid/')
           sftp.chdir('./anotherdroid/')
           print "it coming here"
       except IOError:
           sftp.mkdir('./droid')
           sftp.chdir('./droid')
           sftp.mkdir('./anotherdroid/')
           sftp.chdir('./anotherdroid/')

    
    sftp.put(localpath, filepath)
    sftp.close()
    transport.close()

    

