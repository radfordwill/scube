# Ausführen mit
# sudo python3 scany.py

import time
import RPi.GPIO as GPIO
from picamera import PiCamera
import board
import neopixel

print ("Scan Gestartet")
pixel_pin = board.D18
num_pixels = 12
ORDER = neopixel.RGB
pixels = neopixel.NeoPixel(pixel_pin, num_pixels, brightness=0.2,auto_write=False,pixel_order=ORDER)

class Motor:
    GPIO.setmode(GPIO.BCM)

    # Verwendete Pins am Rapberry Pi
    A=21
    B=20
    C=16
    D=12
    step_time=0.004

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


class MotorKamera:

    step_time = 0.001

    #Pins definieren für den 2. Motor

    E = 26
    F = 19
    G = 13
    H = 6


    GPIO.setmode(GPIO.BCM)
    # Pins aus Ausgänge definieren

    GPIO.setup(E, GPIO.OUT)
    GPIO.setup(F, GPIO.OUT)
    GPIO.setup(G, GPIO.OUT)
    GPIO.setup(H, GPIO.OUT)
    GPIO.output(E, False)
    GPIO.output(F, False)
    GPIO.output(G, False)
    GPIO.output(H, False)

    # Schritte 1 - 8 festlegen Motor 2
    def Step1D():
        GPIO.output(MotorKamera.H, True)
        time.sleep(MotorKamera.step_time)
        GPIO.output(MotorKamera.H, False)
    def Step2D():
        GPIO.output(MotorKamera.H, True)
        GPIO.output(MotorKamera.G, True)
        time.sleep(MotorKamera.step_time)
        GPIO.output(MotorKamera.H, False)
        GPIO.output(MotorKamera.G, False)
    def Step3D():
        GPIO.output(MotorKamera.G, True)
        time.sleep(MotorKamera.step_time)
        GPIO.output(MotorKamera.G, False)
    def Step4D():
        GPIO.output(MotorKamera.F, True)
        GPIO.output(MotorKamera.G, True)
        time.sleep(MotorKamera.step_time)
        GPIO.output(MotorKamera.F, False)
        GPIO.output(MotorKamera.G, False)
    def Step5D():
        GPIO.output(MotorKamera.F, True)
        time.sleep(MotorKamera.step_time)
        GPIO.output(MotorKamera.F, False)
    def Step6D():
        GPIO.output(MotorKamera.E, True)
        GPIO.output(MotorKamera.F, True)
        time.sleep(MotorKamera.step_time)
        GPIO.output(MotorKamera.E, False)
        GPIO.output(MotorKamera.F, False)
    def Step7D():
        GPIO.output(MotorKamera.E, True)
        time.sleep(MotorKamera.step_time)
        GPIO.output(MotorKamera.E, False)
    def Step8D():
        GPIO.output(MotorKamera.H, True)
        GPIO.output(MotorKamera.E, True)
        time.sleep(MotorKamera.step_time)
        GPIO.output(MotorKamera.H, False)
        GPIO.output(MotorKamera.E, False)

    def turnStartPosition():

        for i in range(400):
            MotorKamera.Step8D()
            MotorKamera.Step7D()
            MotorKamera.Step6D()
            MotorKamera.Step5D()
            MotorKamera.Step4D()
            MotorKamera.Step3D()
            MotorKamera.Step2D()
            MotorKamera.Step1D()

    def turnPosition():

        for i in range(100):
            MotorKamera.Step8D()
            MotorKamera.Step7D()
            MotorKamera.Step6D()
            MotorKamera.Step5D()
            MotorKamera.Step4D()
            MotorKamera.Step3D()
            MotorKamera.Step2D()
            MotorKamera.Step1D()
    
    def turnHome():

        for i in range(1610):
            MotorKamera.Step1D()
            MotorKamera.Step2D()
            MotorKamera.Step3D()
            MotorKamera.Step4D()
            MotorKamera.Step5D()
            MotorKamera.Step6D()
            MotorKamera.Step7D()
            MotorKamera.Step8D()
#-----------------------------------------------



class Light:
    pixels = neopixel.NeoPixel(board.D18, 12)
    def on ():
        Light.pixels.fill((40, 40, 40))
    def off ():
        Light.pixels.fill((0, 0, 0))

    def green ():
        Light.pixels.fill((0, 255, 0))
    
    def done ():
        Light.pixels.fill((0, 255, 0))
    #################################################################
def wheel(pos):
    # Input a value 0 to 255 to get a color value.
    # The colours are a transition r - g - b - back to r.
    if pos < 0 or pos > 255:
        r = g = b = 0
    elif pos < 85:
        r = int(pos * 3)
        g = int(255 - pos * 3)
        b = 0
    elif pos < 170:
        pos -= 85
        r = int(255 - pos * 3)
        g = 0
        b = int(pos * 3)
    else:
        pos -= 170
        r = 0
        g = int(pos * 3)
        b = int(255 - pos * 3)
    return (r, g, b) if ORDER in (neopixel.RGB, neopixel.GRB) else (r, g, b, 0)

def rainbow_cycle(wait):
    for j in range(255):
        for i in range(num_pixels):
            pixel_index = (i * 256 // num_pixels) + j
            pixels[i] = wheel(pixel_index & 255)
        pixels.show()
        time.sleep(wait)
#################################################
class Cam:
    cam = PiCamera()
    cam.resolution = (1024, 768)
    cam.rotation = 0

    def take (filename):
        Cam.cam.capture(filename)

import datetime,os

def run ():
    Zaehler = 0
    now = datetime.datetime.now().isoformat()
    folder = f"/home/pi/scube_output/{now}"
    os.makedirs(folder)
    print("rainow")
    
    ###########################################
    MotorKamera.turnStartPosition()

    rainbow_cycle(0.01)
    rainbow_cycle(0.001)
    time.sleep(1)
    Light.off()

    Light.on()
    time.sleep(0.5)
    umdrehungen = 1
    anzahlfotos = 24
    anzahlEbene = 12
   
   
    for i in range(0,anzahlEbene):
        MotorKamera.turnPosition()
        for i in range(0,anzahlfotos):
            print(f"Bild {i + 1}/{anzahlfotos}")
            Cam.take(f"{folder}/{i}{Zaehler}.jpg")
            time.sleep(0.5)
            Motor.turn(umdrehungen*360/anzahlfotos)

        Zaehler = Zaehler+i;
        print(Zaehler)

    Light.done()
    
    MotorKamera.turnHome()
    time.sleep(0.5)
    Light.off()
    GPIO.cleanup()
    return(folder)


if __name__ == "__main__":
    print(run())
