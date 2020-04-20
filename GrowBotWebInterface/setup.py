import subprocess

subprocess.run("python3 SoilSensorReadOnly.py & python3 TempHumidPressSensor.py & python3 nineDofSensor.py & python3 GasSensor.py", shell=True)
