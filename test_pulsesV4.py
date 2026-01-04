from machine import Pin
import time

led = Pin(2, Pin.OUT)
pulse_pin = Pin(27, Pin.IN, Pin.PULL_UP)

pulse_count = 0
last_flow_time = time.ticks_ms()

# Toggle this flag for demo vs deployment
DEMO_MODE = True  

def on_pulse(pin):
    global pulse_count, last_flow_time
    pulse_count += 1
    last_flow_time = time.ticks_ms()
    led.on()
    time.sleep_ms(20)
    led.off()

pulse_pin.irq(trigger=Pin.IRQ_FALLING, handler=on_puls	e)

print("Monitoring flow...")

while True:
    start = time.ticks_ms()
    time.sleep(1)
    elapsed = time.ticks_diff(time.ticks_ms(), start) / 1000
    pulses_per_sec = pulse_count / elapsed
    pulse_count = 0

    if pulses_per_sec > 0:
        if pulses_per_sec < 2:
            if DEMO_MODE:
                print("Leak suspected! (demo mode)")
            else:
                idle_time = time.ticks_diff(time.ticks_ms(), last_flow_time) / 1000
                if idle_time > 30:
                    print("Leak suspected!")
        else:
            print("Tap in use")
