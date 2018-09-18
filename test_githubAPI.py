import unittest
import Shahab_Ahsan_HW4a

class TestGitHubAPI(unittest.TestCase):
    def test_Ahsan45(self):
        self.assertEqual(Shahab_Ahsan_HW4a.gitHubAPI('Ahsan45'), 117)

    def test_DavidKim15(self):
        self.assertEqual(Shahab_Ahsan_HW4a.gitHubAPI('DavidKim15'), 41)

if __name__ == '__main__':
    unittest.main()