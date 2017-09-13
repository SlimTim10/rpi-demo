import RPi.GPIO as GPIO
from tweepy.streaming import StreamListener
from tweepy import OAuthHandler
from tweepy import Stream
import yaml

from demo_gpio import *

class StdOutListener(StreamListener):
    """ A listener handles tweets that are received from the stream.
    This is a basic listener that just prints received tweets to stdout.

    """
    def on_connect(self):
        print('Listening to Twitter stream')

    def on_status(self, status):
        print(status.text)
        if 'red' in status.text:
            rgb_red()
        if 'green' in status.text:
            rgb_green()
        if 'blue' in status.text:
            rgb_blue()
        if 'purple' in status.text:
            rgb_purple()
        if 'orange' in status.text:
            rgb_orange()
        return True

    def on_error(self, status):
        print(status)

def twitter_setup(cfg):
    l = StdOutListener()
    auth = OAuthHandler(cfg['consumer_key'], cfg['consumer_secret'])
    auth.set_access_token(cfg['access_token'], cfg['access_token_secret'])

    stream = Stream(auth, l)
    stream.userstream(_with='user')
    stream.filter(track=['red', 'green', 'blue'])

# Set up GPIO pins
gpio_setup()
print('GPIO pins ready')

# Get Twitter app settings
with open('config.yaml', 'r') as f:
    cfg = yaml.load(f)

# Set up Twitter stream listening
twitter_setup(cfg)

GPIO.cleanup()
