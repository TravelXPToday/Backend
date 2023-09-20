
from data_access import DataAccess
from crud_interface import CRUDInterface

class Traveler(DataAccess, CRUDInterface):
    def __init__(self):
        super().__init__('traveler')
