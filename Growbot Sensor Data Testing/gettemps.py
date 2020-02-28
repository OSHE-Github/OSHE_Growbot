from gpiozero import CPUTemperature
import time

cpu = CPUTemperature()
def getTemp():
    return cpu.temperature
