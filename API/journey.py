# journey.py

from data_access import DataAccess
from crud_interface import CRUDInterface

class Journey(DataAccess, CRUDInterface):
    def __init__(self):
        super().__init__('Journeys')
