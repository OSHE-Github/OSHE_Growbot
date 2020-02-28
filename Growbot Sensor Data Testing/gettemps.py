from gpiozero import CPUTemperature
import time

cpu = CPUTemperature()
def getTemp():
    temp = cpu.temperature
    time.sleep(1)
    return temp
