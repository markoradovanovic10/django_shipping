from .admin_site import admin_site
from .user import *
from .vehicle import *
from .vehicle_log import *
from .country import *
from .city import *
from .company import *
from .shipment import *


admin_site.register(VehicleLog)
admin_site.register(Vehicle)
admin_site.register(Country)
admin_site.register(City)
admin_site.register(Company)
admin_site.register(Shipment)

