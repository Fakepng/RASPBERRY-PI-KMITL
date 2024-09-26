from gpiozero import Button, LED
import time

yellow_btn = Button(27)

led_green = LED(14)
led_white = LED(15)
led_blue = LED(18)
led_red = LED(2)
led_yellow = LED(3)

sleep = .1
continue_led5 = 0

def continue_callback():
  print("Button press")
  global continue_led5
  continue_led5 = 1

yellow_btn.when_activated = continue_callback


while True:
  led_yellow.on()
  # print("LED1 on")
  time.sleep(sleep)
  led_yellow.off()
  # print("LED1 off")
  led_red.on()
  # print("LED2 on")
  time.sleep(sleep)
  led_red.off()
  # print("LED2 off")
  led_blue.on()
  # print("LED3 on")
  time.sleep(sleep)
  led_blue.off()
  # print("LED3 off")
  led_white.on()
  # print("LED4 on")
  time.sleep(sleep)
  led_white.off()
  # print("LED4 off")
  if continue_led5:
    led_green.on()
    # print("LED5 on")
    time.sleep(sleep)
    led_green.off()
    # print("LED5 off")
    continue_led5 = 0
