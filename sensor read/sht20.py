from sensor.SHT20 import SHT20
import sys

# Initialize SHT20 sensor outside the try block
try:
    sht = SHT20(1, 0x40)
    h, t = sht.all()
    print("Relative Humidity:", h.RH)
    print("Temperature (Celsius):", t.C)
except OSError as e:
    print("An OSError occurred while initializing the sensor:", e)
    sys.exit(1)
