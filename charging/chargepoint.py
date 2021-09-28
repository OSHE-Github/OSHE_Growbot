import usb.core
import usb.util

# Notes on Turnigy charger USB Port
# There are three endpoints with device addresses of 0x4, 0x6, and 0x8
# Address 0x8 seems to be the address used when the signal to start charge is sent from the application
# 

class TurnigyCharger(object):
   VID = 0x0000 #According to Windows, This value is 0x8086
   PID = 0x0001 #According to Windows, this value is 0x9d2f
   START = 0x0f035f005fffff00
   STOP = 0x0f03fe00feffff00
   

Vendor_id = 0x8086
Product_id = 0x9d2f
CONFIGURATION_CHARGER = 1
INTERFACE_CHARGER = 0
ENDPOINT_CHARGER = 1


# find our device
def_init_(self):
self._had_driver = False
self._dev = usb.core.find(idVendor=Vendor_id, idProduct=Product_id)
if self._dev is None: # was it found?
    raise ValueError('Device not found')

# Linux kernel sets up a device driver for USB device, which you have
# to detach. Otherwise trying to interact with the device gives a
# 'Resource Busy' error.
try:
  self.detach_kernel_driver(0)
except Exception:
  pass # already unregistered
  
if self._dev.is_kernel_driver_driver(0):
   self._dev.detach_kernel_driver(0)
   self._had_driver = True

self._dev.set_configuration()

self._dev.set_configuration(1)
usb.util.claim_interface(0)

def release(self):
   us.util.release_interface(self._dev,0)
   if self._had_driver:
      self._dev.attach_kernel_driver(0)

#this is defining the ability to charge the battery
def charge(self,status):
   ret = self._dev.ctrl_transfer(0x21,)
   return ret == 1

# get an endpoint instance
cfg = self.get_active_configuration()
interface_number = cfg[(0,0)].bInterfaceNumber
alternate_settting = usb.control.get_interface(self,interface_number)
intf = usb.util.find_descriptor(
cfg, bInterfaceNumber = interface_number,
bAlternateSetting = 0
)

ep = usb.util.find_descriptor(
intf,
# match the first OUT endpoint
custom_match = \
lambda e: \
usb.util.endpoint_direction(e.bEndpointAddress) == \
usb.util.ENDPOINT_OUT
)

assert ep is not None



#interface = cfg[(0,0)]

# write the data
print("attempting to send command")

#ENDPOINT_CHARGER = 0x1
#endpoint = interface[ENDPOINT_CHARGER]


ep.write(START.encode('utf-8'))





