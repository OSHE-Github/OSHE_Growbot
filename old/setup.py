import subprocess

subprocess.run("python3 SoilSensorReadOnly.py", shell=True)
subprocess.run("python3 TempHumidPressSensor.py", shell=True)
subprocess.run("python3 nineDofSensor.py", shell=True)
subprocess.run("python3 GasSensor.py", shell=True)
