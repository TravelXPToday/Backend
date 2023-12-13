# journey.py

from data_access import DataAccess
from crud_interface import CRUDInterface

class Journey(DataAccess, CRUDInterface):
    def __init__(self):
        print("journey self: " + str(self))
        super().__init__('Journeys')
