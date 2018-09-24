# will fail if api limit is reached
import unittest
from unittest import mock
from unittest.mock import patch
import Shahab_Ahsan_HW4a
from Shahab_Ahsan_HW4a import gitHubAPI

class TestGitHubAPI(unittest.TestCase):
    @patch('Shahab_Ahsan_HW4a.json.loads')
    def test_Ahsan45(self, mock_get):
        mock_get.return_value.count = 118
        response = gitHubAPI('Ahsan45')
        self.assertEqual(response, 0)

    @patch('Shahab_Ahsan_HW4a.json.loads')
    def test_DavidKim15(self, mock_get):
        mock_get.return_value.count = 41
        response = gitHubAPI('DavidKim15')
        self.assertEqual(response, 0)

if __name__ == '__main__':
    unittest.main()