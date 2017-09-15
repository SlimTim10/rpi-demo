# Raspberry Pi Demo

## GPIO Demo

On button press, turns on the LED for one second, then back off.

## Twitter Demo

Listens to tweets on a specified user's Twitter stream. If the message contains any of the words "red", "green", "blue", "purple", or "orage", it sets the RGB LED to that colour.

## Wiring

| Raspberry Pi | Component |
| :--- | :--- |
| 11 (BCM 17) | LED |
| 13 (BCM 27) | Button |
| 19 (BCM 10) | RGB_R |
| 23 (BCM 11) | RGB_G |
| 21 (BCM 9) | RGB_B |

## Installing Dependencies

```bash
pip install RPi.GPIO
pip install tweepy
pip install pyyaml
```