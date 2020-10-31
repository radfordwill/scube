import time
import RPi.GPIO as GPIO
from picamera import PiCamera
import board
import neopixel

class Motor:
    GPIO.setmode(GPIO.BCM)

    # Verwendete Pins am Rapberry Pi
    A=21
    B=20
    C=16
    D=12
    step_time=0.005

    # Pins aus Ausgänge definieren
    GPIO.setup(A,GPIO.OUT)
    GPIO.setup(B,GPIO.OUT)
    GPIO.setup(C,GPIO.OUT)
    GPIO.setup(D,GPIO.OUT)
    GPIO.output(A, False)
    GPIO.output(B, False)
    GPIO.output(C, False)
    GPIO.output(D, False)

    # Schritte 1 - 8 festlegen
    def Step1():
        GPIO.output(Motor.D, True)
        time.sleep(Motor.step_time)
        GPIO.output(Motor.D, False)

    def Step2():
        GPIO.output(Motor.D, True)
        GPIO.output(Motor.C, True)
        time.sleep(Motor.step_time)
        GPIO.output(Motor.D, False)
        GPIO.output(Motor.C, False)

    def Step3():
        GPIO.output(Motor.C, True)
        time.sleep(Motor.step_time)
        GPIO.output(Motor.C, False)

    def Step4():
        GPIO.output(Motor.B, True)
        GPIO.output(Motor.C, True)
        time.sleep(Motor.step_time)
        GPIO.output(Motor.B, False)
        GPIO.output(Motor.C, False)

    def Step5():
        GPIO.output(Motor.B, True)
        time.sleep(Motor.step_time)
        GPIO.output(Motor.B, False)

    def Step6():
        GPIO.output(Motor.A, True)
        GPIO.output(Motor.B, True)
        time.sleep(Motor.step_time)
        GPIO.output(Motor.A, False)
        GPIO.output(Motor.B, False)

    def Step7():
        GPIO.output(Motor.A, True)
        time.sleep(Motor.step_time)
        GPIO.output(Motor.A, False)

    def Step8():
        GPIO.output(Motor.D, True)
        GPIO.output(Motor.A, True)
        time.sleep(Motor.step_time)
        GPIO.output(Motor.D, False)
        GPIO.output(Motor.A, False)

    def turn (degree):
        full = 512
        for i in range (int(degree / 360 * full)):
            Motor.Step1()
            Motor.Step2()
            Motor.Step3()
            Motor.Step4()
            Motor.Step5()
            Motor.Step6()
            Motor.Step7()
            Motor.Step8()
            
def main ():
    Light.on()
    time.sleep(0.2)
    for i in range(0,24):
        print(f"Bild {i + 1}/24")
        Cam.take(f"/tmp/{i}.jpg")
        time.sleep(0.1)
        Motor.turn(360/24)
    Light.off()
    GPIO.cleanup()

main()