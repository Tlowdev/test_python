from asyncio import queues
import unittest
from survey import AnonSurvey

class TestAnonSurvey(unittest.TestCase):
    """Test for the class AnonSurvey"""
    def setUp(self) -> None:
        """Create a survey and a set of responses for use in all test methods"""
        question = "What language do you speak?"
        self.my_survey = AnonSurvey(question)
        self.response = ['English', 'Japanese', 'Spanish']


    def test_store_single_response(self):
       self.my_survey.store_response(self.response[0])
       self.assertIn(self.response[0], self.my_survey.response)


    def test_store_multiple_reponses(self):
        """Test three individual responses are stored correctly"""
        for responses in self.response:
            self.my_survey.store_response(responses)
        for responses in self.response:
            self.assertIn(responses, self.my_survey.response)

if __name__ == '__main__':
     unittest.main()