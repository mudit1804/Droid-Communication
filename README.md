# Droid-Communication
There are two droids on two different systems. figuring This python script helps to synchronize data between a folder on one device (say device A) which is of droid 1 and a folder on another device (say device B) which is of droid 2. In addition to that, a change made to the data on one device should also be made  available to the other device as well.

How this Works?
1) Run the script on the first system which is for droid A.
2) Make sure you have ssh on both the devices i.e for both Droid A and Droid B systems.
   If you dont't have this 
   Install by typing:
        sudo apt-get install openssh-server
3) Make sure that ssh is running on Port 22 on both systems.
4) In script change these lines in accordance to the droid you want to communicate with.
   host = "#public_ip_of_the_host'
   username = "#username"
   password = "#password"
   Note: Public ip of a device can be obtained by using command "curl ifconfig.me" on terminal.
5) When running script on device A, above credentials will be of device B and while running script on device B, above credentials will be of device A
6) On running the scipt say on device A, it will ask for its experiences and orders and on entering it will save that on               device A and also make that change available to device B droid. 
7) Same when we want to make a change in Droid B experiences and orders,  we will run the script on device B and change will also be reflected on device A.



