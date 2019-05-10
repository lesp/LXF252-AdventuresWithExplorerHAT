import time
import explorerhat as eh

while True:
    light = eh.analog.one.read()
    print(light)
    if light < 2.0:
        eh.light.on()
    else:
        eh.light.off()