from gpiozero import CPUTemperature
import time

cpu = CPUTemperature()
def getTemp():
<<<<<<< HEAD
    time.sleep(1)
=======
>>>>>>> a9455c0743e53592c18645b5161455d057d7ccc4
    return cpu.temperature
