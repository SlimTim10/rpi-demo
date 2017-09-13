from time import sleep
import RPi.GPIO as GPIO
from tweepy.streaming import StreamListener
from tweepy import OAuthHandler
from tweepy import Stream
import yaml

LED_PIN = 17
BUTTON_PIN = 22
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

class StdOutListener(StreamListener):
    """ A listener handles tweets that are received from the stream.
    This is a basic listener that just prints received tweets to stdout.

    """
    def on_status(self, status):
        print(status.text)
        return True

    def on_error(self, status):
        print(status)

def twitter_setup():
    l = StdOutListener()
    auth = OAuthHandler(cfg['consumer_key'], cfg['consumer_secret'])
    auth.set_access_token(cfg['access_token'], cfg['access_token_secret'])

    stream = Stream(auth, l)
    stream.userstream(_with='user')
    stream.filter(track=['red', 'green', 'blue'])

# Set up GPIO pins
gpio_setup()

# Get Twitter app settings
with open('config.yaml', 'r') as f:
    cfg = yaml.load(f)

# Set up Twitter stream listening
twitter_setup()

# Main loop
while True:
    button = GPIO.input(BUTTON_PIN)
    print(button)
    sleep(0.1)

GPIO.cleanup()
