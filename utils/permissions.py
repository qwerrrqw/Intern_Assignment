from enum import Enum

class UserRole(Enum):
    USER = "USER"
    GOODUSER = "GOODUSER"
    VIP = "VIP"
    
    @classmethod
    def choices(cls):
        return tuple(map(lambda x: (x.value, x.name), cls))
    
    @classmethod
    def values(cls):
        return tuple(map(lambda x: x.value, cls))