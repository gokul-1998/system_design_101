class ParkingLot:
    _instance = None

    def __new__(cls):
        if  cls._instance==None:
            cls._instance=super().__new__(cls)
        return  cls._instance

    def get_instance(cls):
        return cls._instance


class EntryGate:
    def __init__(self,id):
        pass

class ExitGate:
    def __init__(self,id):
        pass

class ParkingFloor:
    def __init__(self,id):
        pass

    def addSpot()
    

class ParkingSpot:
    def __init__(self,id,vehicleType):
        pass