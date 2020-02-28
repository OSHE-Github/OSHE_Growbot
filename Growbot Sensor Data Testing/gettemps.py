from gpiozero import CPUTemperature
import time

cpu = CPUTemperature()
def getTemp():
    temp = cpu.temperature
    time.sleep(2)
    return temp
