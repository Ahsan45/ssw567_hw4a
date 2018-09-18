import unittest
import Shahab_Ahsan_HW4a

class TestGitHubAPI(unittest.TestCase):
    def test_Ahsan45(self):
        self.assertEqual(len(Shahab_Ahsan_HW4a.gitHubAPI('Ahsan45')), 7)

    def test_richkempinski(self):
        self.assertEqual(len(Shahab_Ahsan_HW4a.gitHubAPI('richkempinski')), 4)

if __name__ == '__main__':
    unittest.main()