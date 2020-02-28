from gpiozero import CPUTemperature
import time

cpu = CPUTemperature()
def getTemp():
    time.sleep(1)
    return cpu.temperature
