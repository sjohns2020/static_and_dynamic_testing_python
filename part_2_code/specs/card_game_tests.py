import unittest
from src.card import Card
from src.card_game import CardGame

class TestCardGame(unittest.TestCase):

    def setUp(self):
        self.card1 = Card("Ace", 1)
        self.card2 = Card("Jack", 11)
        self.cards = [self.card1, self.card2]
        self.card_game = CardGame()

    def test_card_has_suit(self):
        self.assertEqual("Ace", self.card1.suit)

    def test_card_has_value(self):
        self.assertEqual(1, self.card1.value)

    def test_card_game_can_check_for_ace(self):
        self.assertEqual(True, self.card_game.check_for_ace(self.card1))

    def test_card_game_can_check_for_highest_card(self):
        self.assertEqual(self.card2, self.card_game.highest_card(self.card1, self.card2))

    def test_card_game_can_check_for_total_value_of_cards(self):
        card1_value = self.card1.value
        card2_value = self.card2.value
        self.assertEqual((f'You have a total of {card1_value + card2_value}'), self.card_game.cards_total(self.cards))