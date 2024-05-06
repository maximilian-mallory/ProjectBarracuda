import unittest

def scoregame(time_left, num_guesses, hintOne, hintTwo):
    score = 1000 - abs(int(time_left) - 300) * (500 / 300) - (50 * (int(num_guesses) - 1))
            
    if hintOne is not False:
        score -= 100
    if hintTwo is not False:
        score -= 100  

    return score  

class TestScoreGame(unittest.TestCase):
    def test_scoregame_no_hint(self):
        self.assertEqual(scoregame(300, 1, False, False), 1000)  # Test score without hints
    
    def test_scoregame_hint_one(self):
        self.assertEqual(scoregame(200, 3, True, False), 400)  # Test score with hintOne
    
    def test_scoregame_hint_two(self):
        self.assertEqual(scoregame(0, 3, True, True), 200)  # Test score with hintTwo
    
    def test_scoregame_both_hints(self):
        self.assertEqual(scoregame(300, 3, True, True), 1100)  # Test score with both hints

if __name__ == '__main__':
    unittest.main()