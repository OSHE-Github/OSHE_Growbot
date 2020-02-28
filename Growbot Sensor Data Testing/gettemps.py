from gpiozero import CPUTemperature

cpu = CPUTemperature()
def getTemp():
    return cpu.temperature
