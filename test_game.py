from unittest import TestCase

from game import Game
from game_result import GameResult


class TestGame(TestCase):
    def setUp(self):
        self.game = Game()

        super().setUp()
    def assert_illegal_argument(self, guessNumber):
        try:
            self.game.guess(guessNumber)
            self.fail()
        except TypeError:
            pass


    def test_exception_when_input_length_is_unmatched(self):
        self.assert_illegal_argument(None)
        self.assert_illegal_argument("12")
        self.assert_illegal_argument("1234")
        self.assert_illegal_argument("121")

    def test_return_solve_result_if_matched_number(self):
        self.game.question = "123"
        result: GameResult = self.game.guess("123")

        self.assertIsNotNone(result)
        self.assertTrue(result.get_solved())
        self.assertEqual(3, result.get_strikes())
        self.assertEqual(0, result.get_balls())

    def test_return_solve_result_if_unmatched_number(self):
        self.game.question = "123"
        result: GameResult = self.game.guess("456")

        self.assertIsNotNone(result.get_solved())
        self.assertFalse(result.get_solved())
        self.assertEqual(0, result.get_strikes())
        self.assertEqual(0, result.get_balls())