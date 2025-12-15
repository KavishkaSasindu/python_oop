class Vehicle:
    vehicle_id:int
    vehicle_name:str
    vehicle_type:str
    
    def __init__(self, vehicle_id:int, vehicle_name:str, vehicle_type:str):
        self.vehicle_id = vehicle_id    #public variable
        self._vehicle_name = vehicle_name    #protected variable (one underscore)
        self.__vehicle_type = vehicle_type    #private variable (two undescore)