from time import sleep
import RPi.GPIO as GPIO
from tweepy.streaming import StreamListener
from tweepy import OAuthHandler
from tweepy import Stream

consumer_key=""
consumer_secret=""

access_token=""
access_token_secret=""

GPIO.setmode(GPIO.BCM)
GPIO.setwarnings(False)

led_pin = 17
button_pin = 22
rgb_r_pin = 10
rgb_g_pin = 11
rgb_b_pin = 9

GPIO.setup(led_pin, GPIO.OUT)
GPIO.setup(rgb_r_pin, GPIO.OUT)
GPIO.setup(rgb_g_pin, GPIO.OUT)
GPIO.setup(rgb_b_pin, GPIO.OUT)
GPIO.setup(button_pin, GPIO.IN, pull_up_down=GPIO.PUD_DOWN)

def led_on():
    GPIO.output(led_pin, GPIO.HIGH)

def led_off():
    GPIO.output(led_pin, GPIO.LOW)

def rgb_off():
    GPIO.output(rgb_r_pin, GPIO.LOW)
    GPIO.output(rgb_g_pin, GPIO.LOW)
    GPIO.output(rgb_b_pin, GPIO.LOW)
    
def rgb_red():
    rgb_off()
    GPIO.output(rgb_r_pin, GPIO.HIGH)

def rgb_green():
    rgb_off()
    GPIO.output(rgb_g_pin, GPIO.HIGH)

def rgb_blue():
    rgb_off()
    GPIO.output(rgb_b_pin, GPIO.HIGH)

class StdOutListener(StreamListener):
    """ A listener handles tweets that are received from the stream.
    This is a basic listener that just prints received tweets to stdout.

    """
    def on_status(self, status):
        print(status.text)
        return True

    def on_error(self, status):
        print(status)

led_on()
sleep(1)
led_off()

rgb_red()
sleep(1)
rgb_green()
sleep(1)
rgb_blue()
sleep(1)
rgb_off()
sleep(1)

l = StdOutListener()
auth = OAuthHandler(consumer_key, consumer_secret)
auth.set_access_token(access_token, access_token_secret)

stream = Stream(auth, l)
stream.userstream(_with='user')
stream.filter(track=['green'])

while True:
    button = GPIO.input(button_pin)
    print(button)
    sleep(0.1)

GPIO.cleanup()
