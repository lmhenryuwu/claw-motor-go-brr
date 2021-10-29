import RPi.GPIO as GPIO          
import time

in1 = 24
in2 = 23
en = 25
temp1=1

GPIO.setmode(GPIO.BCM)
GPIO.setup(in1,GPIO.OUT)
GPIO.setup(in2,GPIO.OUT)
GPIO.setup(en,GPIO.OUT)
GPIO.output(in1,GPIO.LOW)
GPIO.output(in2,GPIO.LOW)
GPIO.setup(5, GPIO.IN, pull_up_down=GPIO.PUD_UP)#Button to GPIO23
GPIO.setup(6, GPIO.OUT)  #LED to GPIO24

#GPIO 6, Pin 31 > Orange >
#GPIO 5, Pin 29 > Grey > 
#Ground, Pin 25 > Red > 
#GPIO 23, Pin 16 > Black >
#GPIO 24, Pin 18 > Green >

p=GPIO.PWM(en,1000)
p.start(25)
print("\n")
print("The default speed & direction of motor is LOW & Forward.....")
print("r-run s-stop f-forward b-backward l-low m-medium h-high e-exit")
print("\n")    

while(1):
    
    motor_state = False
    i = 0
    x = "s"
    
    if 1 == 1:
    
        while i<=10:
            
            button_state = GPIO.input(5)
            if button_state == False and motor_state == False:
                x = "r"
                #time.sleep(0.5)
            elif button_state == False and motor_state == True:
                x = "s"
                #time.sleep(0.5)
            
            if x=='r':
                #print("run")
                if(temp1==1):
                    p.ChangeDutyCycle(25)
                    GPIO.output(23,GPIO.HIGH)
                    GPIO.output(24,GPIO.LOW)
                    print("forward")
                    temp1 = 1
                    x='z'
                    motor_state = True
                    time.sleep(0.5)
                #else:
                 #GPIO.output(in1,GPIO.LOW)
                 #GPIO.output(in2,GPIO.HIGH)
                 #print("backward")
                 #temp1 = 1
                 #x='z'

            elif x=='s':
                print("stop")
                GPIO.output(23,GPIO.LOW)
                GPIO.output(24,GPIO.LOW)
                x='z'
                motor_state = False
                time.sleep(0.5)

            elif x=='f':
                print("forward")
                GPIO.output(in1,GPIO.HIGH)
                GPIO.output(in2,GPIO.LOW)
                temp1=1
                x='z'

            elif x=='b':
                print("backward")
                GPIO.output(in1,GPIO.LOW)
                GPIO.output(in2,GPIO.HIGH)
             
            elif x=='e':
                GPIO.cleanup()
                break
        
        #else:
            #print("<<<  wrong data  >>>")
            #print("please enter the defined data to continue.....")
    
        

