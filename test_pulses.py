from machine import Pin
import time

led= Pin(2, Pin.OUT)   #onboard LED for feedback

pulse_pin= Pin(27, Pin.IN, Pin.PULL_UP)   #sensor signal pin (GPIO27) with internal pull-up

pulse_count= 0

def on_pulse(pin):
    global pulse_count
    pulse_count+= 1
    # quick LED flash when a pulse is detected
    led.on()
    time.sleep_ms(30)
    led.off()

pulse_pin.irq(trigger=Pin.IRQ_FALLING, handler=on_pulse)    #attach interrupt to count pulses

print("Ready. Tap GPIO27 to GND to simulate pulses.")

while True:
    time.sleep(1)
    print("Pulses in last second:", pulse_count)
    pulse_count= 0

"""this program sets up the ESP32 to act like a simple pulse counter that mimics how the water flow sensor works. The board
listens on GPIO27, and every time the pin is tapped to GND, registers a pulse, flashes the onboard LED and adds 1 to pulse_count
"""