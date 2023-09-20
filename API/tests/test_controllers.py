import unittest
import logging
from unittest.mock import patch
from controllers import create_traveler, create_journey, get_all_travelers, get_all_journeys, update_traveler, update_journey, delete_traveler, delete_journey
# python -m unittest discover tests
logging.basicConfig(level=logging.DEBUG)
logger = logging.getLogger(__name__)

class TestControllers(unittest.TestCase):
    @patch('controllers.Traveler.read')
    def test_get_all_travelers(self, mock_read):
        logger.info("\nRunning test_get_all_travelers test case")
        mock_data = [{"name": "Art"}, {"name": "Jelle"}]
        mock_read.return_value = mock_data

        result = get_all_travelers()
        self.assertEqual(result, mock_data)
        logger.debug(f"Mocked data: {mock_data}")
        logger.debug(f"Result: {result}")
    
    @patch('controllers.Traveler.create')
    def test_create_traveler(self, mock_create):
        logger.info("\nRunning test_create_traveler test case")
        mock_data = {
            "name": "Art",
            "age": 30,
            "destination": "London"
        }
        mock_response = {"inserted_id": "5f4abc56e12b5c34a3c5821e"}
        mock_create.return_value = mock_response

        result = create_traveler(mock_data)
        self.assertEqual(result["inserted_id"], mock_response["inserted_id"])
        logger.debug(f"Mocked data: {mock_data}")
        logger.debug(f"Result: {result}")

    @patch('controllers.Traveler.update')
    def test_update_traveler(self, mock_update):
        logger.info("\nRunning test_update_traveler test case")
        criteria = {"name": "Art"}
        updates = {"age": 31}
        mock_response = {"modified_count": 1}
        mock_update.return_value = mock_response

        result = update_traveler(criteria, updates)
        self.assertEqual(result["modified_count"], mock_response["modified_count"])
        logger.debug(f"Criteria: {criteria}")
        logger.debug(f"Updates: {updates}")
        logger.debug(f"Result: {result}")


    @patch('controllers.Traveler.delete')
    def test_delete_traveler(self, mock_delete):
        logger.info("\nRunning test_delete_traveler test case")
        criteria = {"name": "Art"}
        mock_delete.return_value = None

        result = delete_traveler(criteria)
        self.assertIsNone(result)
        logger.debug(f"Criteria: {criteria}")
        logger.debug(f"Result: {result}")


    @patch('controllers.Journey.read')
    def test_get_all_journeys(self, mock_read):
        logger.info("\nRunning test_get_all_journeys test case")
        mock_data = [
            {"origin": "Paris", "destination": "London", "travel_date": "2023-09-22"},
            {"origin": "London", "destination": "Berlin", "travel_date": "2023-09-25"}
        ]
        mock_read.return_value = mock_data

        result = get_all_journeys()
        self.assertEqual(result, mock_data)
        logger.debug(f"Mocked data: {mock_data}")
        logger.debug(f"Result: {result}")

    @patch('controllers.Journey.create')
    def test_create_journey(self, mock_create):
        logger.info("\n Running test_create_journey test case")
        mock_data = {
            "origin": "Paris",
            "destination": "London",
            "travel_date": "2023-09-22"
        }
        mock_response = {"inserted_id": "5f4abc56e12b5c34a3c5821e"}
        mock_create.return_value = mock_response

        result = create_journey(mock_data)
        self.assertEqual(result["inserted_id"], mock_response["inserted_id"])
        logger.debug(f"Mocked data: {mock_data}")
        logger.debug(f"Result: {result}")

    @patch('controllers.Journey.update')
    def test_update_journey(self, mock_update):
        logger.info("\nRunning test_update_journey test case" )
        criteria = {"origin": "Paris", "destination": "London"}
        updates = {"travel_date": "2023-09-23"}
        mock_response = {"modified_count": 1}
        mock_update.return_value = mock_response

        result = update_journey(criteria, updates)
        self.assertEqual(result["modified_count"], mock_response["modified_count"])
        logger.debug(f"Criteria: {criteria}")
        logger.debug(f"Updates: {updates}")
        logger.debug(f"Result: {result}")

    @patch('controllers.Journey.delete')
    def test_delete_journey(self, mock_delete):
        logger.info("\nRunning test_delete_journey test case")
        criteria = {"origin": "Paris", "destination": "London"}
        mock_delete.return_value = None

        result = delete_journey(criteria)
        self.assertIsNone(result)
        logger.debug(f"Criteria: {criteria}")
        logger.debug(f"Result: {result}")



