import os.path
import os
import time
import RPi.GPIO as GPIO
import time
n=1
a=1
m=0
b=0
x=1
GPIO.setmode(GPIO.BCM)
GPIO.setwarnings(False)
GPIO.setup(21, GPIO.OUT)
GPIO.setup(18, GPIO.IN,pull_up_down=GPIO.PUD_UP)
GPIO.setup(23, GPIO.IN,pull_up_down=GPIO.PUD_UP)
GPIO.output(21,False)

time.sleep(5)
os.system('espeak -ven+f5 -g10 "Hi I am your virtual doctor" 2>/dev/null')
os.system('espeak -ven+f5 -g10 "Just answer to my questions" 2>/dev/null')

os.system('espeak -ven+f5 -g10 "Do you have cold " 2>/dev/null')

    

while(n):
    if GPIO.input(18)==0:
        print ("Yes")
        GPIO.output(21,True)
        time.sleep(.1)
        m=1
        n=0
    if GPIO.input(23)==0:
        print ("No")
        GPIO.output(21,False)
        time.sleep(.1)
        m=2
        n=0
if m==1:
    os.system('espeak -ven+f5 -g10 "Ok, so u have cold" 2>/dev/null')
    GPIO.output(21,False)
if m==2:
    os.system('espeak -ven+f5 -g10 "OK, then you are alright" 2>/dev/null')
    GPIO.output(21,False)

    

os.system('espeak -ven+f5 -g10 "Do you have Headache" 2>/dev/null')
while(a):
    if GPIO.input(18)==0:
        print ("Yes")
        GPIO.output(21,True)
        time.sleep(.1)
        b=0
        a=0
    if GPIO.input(23)==0:
        print ("No")
        GPIO.output(21,False)
        time.sleep(.1)
        b=1
        a=0
if b==0:
    os.system('espeak -ven+f5 -g10 "Ok, so u have Headache" 2>/dev/null')
    GPIO.output(21,False)
if b==1:
    os.system('espeak -ven+f5 -g10 "Ok, then you are alright" 2>/dev/null')
    GPIO.output(21,False)


    
if m==1:
    if b==0:
        os.system('espeak -ven+f5 -g10 "Please Visit the Real Doctor, As I have less Knowledge on your Problem" 2>/dev/null')
        #print "ASPIRINE 200mg"
    
    if b==1:
        os.system('espeak -ven+f5 -g10 "Take This Medicine called Coldact 200 m g" 2>/dev/null')
        print ("coldact 200mg")
        
if m==2:
    if b==0:
        os.system('espeak -ven+f5 -g10 "Take This Medicine called Aspirine 200 m g" 2>/dev/null')
        print ("ASPIRINE 200mg")
        
    if b==1:
        os.system('espeak -ven+f5 -g10 "You are totally fine, jjust go home and take rest" 2>/dev/null')
        #print "coldact 200mg"
        
#os.system('espeak -g10 "pravvesh howe r u" 2>/dev/null')
#GPIO.output(21,True)
#time.sleep(2)
#os.system('espeak -g10 "pravvesh" 2>/dev/null')
#GPIO.output(21,False)

