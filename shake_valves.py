import RPi.GPIO as GPIO 
import time


def open_repeats(outports, opentime, repeats):
    for rep in range(repeats):
        for j in outports:
            GPIO.output(j,1)
        time.sleep(opentime)
        for j in outports:
            GPIO.output(j,0)
        time.sleep(0.01)
  

if __name__ == '__main__':
    GPIO.setmode(GPIO.BOARD)
    GPIO.setwarnings(False)
    outports = [31,33,35,37]
    for i in outports:
        GPIO.setup(i, GPIO.OUT)
        
    opentime = 0.01
    repeats = 100
    
    run = True
    while run:
        print("""
              Main Menu:
                1. Shake valve 1 (31)
                2. Shake valve 2 (33)
                3. Shake valve 3 (35)
                4. Shake valve 4 (37)
                5. Change opentime
                6. Change repeats
                7. Exit
                
                Current settings are:
                opentime: """ + str(opentime) + """
                repeats: """ + str(repeats) + """
              """)
        sel = raw_input("Enter selection: ")
        if sel == '1':
            open_repeats([31], opentime, repeats)
        elif sel == '2':
            open_repeats([33], opentime, repeats)
        elif sel == '3':
            open_repeats([35], opentime, repeats)
        elif sel == '4':
            open_repeats([37], opentime, repeats)
        elif sel == '5':
            opentime = float(raw_input("Enter opentime: "))
            print("Opentime set to " + str(opentime) + " seconds.")
        elif sel == '6':
            repeats = int(raw_input("Enter repeats: "))
            print("Repeats set to " + str(repeats) + ".")  
        elif sel == '7':
            run = False
            
    GPIO.cleanup()
    print("Goodbye!")
    