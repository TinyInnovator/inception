import time
from PIL import ImageGrab
print("Starting in 3 seconds...")
time.sleep(3)
while True:
    ImageGrab.grab().show()
    