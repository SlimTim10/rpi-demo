from time import sleep
import RPi.GPIO as GPIO

LED_PIN = 17
BUTTON_PIN = 27
RGB_R_PIN = 10
RGB_G_PIN = 11
RGB_B_PIN = 9

def gpio_setup():
    GPIO.setmode(GPIO.BCM)
    GPIO.setwarnings(False)

    GPIO.setup(LED_PIN, GPIO.OUT)
    GPIO.setup(RGB_R_PIN, GPIO.OUT)
    GPIO.setup(RGB_G_PIN, GPIO.OUT)
    GPIO.setup(RGB_B_PIN, GPIO.OUT)
    GPIO.setup(BUTTON_PIN, GPIO.IN, pull_up_down=GPIO.PUD_DOWN)

    led_off()
    rgb_off()

def led_on():
    GPIO.output(LED_PIN, GPIO.HIGH)

def led_off():
    GPIO.output(LED_PIN, GPIO.LOW)

def rgb_off():
    GPIO.output(RGB_R_PIN, GPIO.LOW)
    GPIO.output(RGB_G_PIN, GPIO.LOW)
    GPIO.output(RGB_B_PIN, GPIO.LOW)
    
def rgb_red():
    rgb_off()
    GPIO.output(RGB_R_PIN, GPIO.HIGH)

def rgb_green():
    rgb_off()
    GPIO.output(RGB_G_PIN, GPIO.HIGH)

def rgb_blue():
    rgb_off()
    GPIO.output(RGB_B_PIN, GPIO.HIGH)

def rgb_purple():
    rgb_off()
    GPIO.output(RGB_R_PIN, GPIO.HIGH)
    GPIO.output(RGB_B_PIN, GPIO.HIGH)

def rgb_orange():
    rgb_off()
    GPIO.output(RGB_R_PIN, GPIO.HIGH)
    GPIO.output(RGB_G_PIN, GPIO.HIGH)

def button_pressed():
    return (GPIO.input(BUTTON_PIN) == True)

if __name__ == '__main__':
    # Set up GPIO pins
    gpio_setup()
    print('GPIO pins ready')

    # Main loop
    while True:
        if button_pressed():
            print('Button pressed!')
            # Flash the light for 1 second
            led_on()
            sleep(1)
            led_off()
        sleep(0.1)

    GPIO.cleanup()
