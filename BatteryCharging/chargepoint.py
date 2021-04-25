import usb.core
import usb.util

# Notes on Turnigy charger USB Port
# There are three endpoints with device addresses of 0x4, 0x6, and 0x8
# Address 0x8 seems to be the address used when the signal to start charge is sent from the application
# 

Vendor_id = 0x0
Product_id = 0x1
CONFIGURATION_CHARGER = 1
INTERFACE_CHARGER = 0
ENDPOINT_CHARGER = 1

# find our device
dev = usb.core.find(idVendor=Vendor_id, idProduct=Product_id)

# was it found?
if dev is None:
    raise ValueError('Device not found')

# Linux kernel sets up a device driver for USB device, which you have
# to detach. Otherwise trying to interact with the device gives a
# 'Resource Busy' error.
try:
  dev.detach_kernel_driver(0)
except Exception:
  pass # already unregistered






# get an endpoint instance
cfg = dev.get_active_configuration()
interface_number = cfg[(0,0)].bInterfaceNumber
alternate_settting = usb.control.get_interface(dev,interface_number)
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


start_charging = '\x0f\x03\x5f\x00\x5f\xff\xff\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00'

start_charging2 = '0x0f035f005fffff000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000'

start_charging3 = '0x0f:03:5f:00:5f:ff:ff:00:00:00:00:00:00:00:00:00:00:00:00:00:00:00:00:00:00:00:00:00:00:00:00:00:00:00:00:00:00:00:00:00:00:00:00:00:00:00:00:00:00:00:00:00:00:00:00:00:00:00:00:00:00:00:00:00'

Idle = 'x0f\x03\x5a\x00\x5a\xff\xff\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00'

Idle2 = 'x0f:03:5a:00:5a:ff:ff:00:00:00:00:00:00:00:00:00:00:00:00:00:00:00:00:00:00:00:00:00:00:00:00:00:00:00:00:00:00:00:00:00:00:00:00:00:00:00:00:00:00:00:00:00:00:00:00:00:00:00:00:00:00:00:00:00'

Pull_data = 'x0f\x03\x55\x00\x55\xff\xff\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00'

stop_charge = '0x0f03fe00feffff000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000'

ep.write(start_charging.encode('utf-8'))





