from models import ParkingLot,EntryGate,ExitGate,ParkingFloor



# later : make this a singleton class
lot=ParkingLot().get_instance()

entryGate=EntryGate("EG1")

exitGate=ExitGate("XG1")

# lot.setPricing

floor = ParkingFloor("Floor1")

