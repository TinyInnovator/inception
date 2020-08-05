import time
# use 'pip install Pillow' in cmd to install PIL
# visit https://pypi.org/project/Pillow/ for more details
from PIL import ImageGrab
print("Starting in 3 seconds...")
time.sleep(3)
while True:
    ImageGrab.grab().show()
    
