import time
import explorerhat as eh
import random

while True:
    on = random.uniform(0.0,1.0)
    off = random.uniform(0.0,1.0)
    fade_in = random.uniform(0.0,1.0)
    fade_out = random.uniform(0.0,1.0)
    blow = eh.analog.one.read()
    print(blow)
    time.sleep(0.1)
    if blow > 1.5:
        eh.light.off()
        time.sleep(2)
    else:
        eh.light.pulse(on, off, fade_in, fade_out)