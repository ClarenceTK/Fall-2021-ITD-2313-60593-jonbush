"""
File: blackjack.py
This module defines the Blackjack, Player, and Dealer classes.
"""
from cards import Deck, Card

class Player(object):
    """This class represents a player in
    a blackjack game."""

    def __init__(self, cards):
        self.cards = cards

    def __str__(self):
        """Returns string rep of cards and points."""
        result = ", ".join(map(str, self.cards))
        result += "\n  " + str(self.getPoints()) + " points"
        return result

    def hit(self, card):
        self.cards.append(card)

    def getPoints(self):
        """Returns the number of points in the hand."""
        count = 0
        for card in self.cards:
            if card.rank > 9:
                count += 10
            elif card.rank == 1:
                count += 11
            else:
                count += card.rank
        # Deduct 10 if Ace is available and needed as 1
        for card in self.cards:
            if count <= 21:
                break
            elif card.rank == 1:
                count -= 10
        return count

    def hasBlackjack(self):
        """Dealt 21 or not."""
        return len(self.cards) == 2 and self.getPoints() == 21 


class Dealer(Player):
    """Like a Player, but with some restrictions."""

    def __init__(self, cards):
        """Initial state: show one card only."""
        Player.__init__(self, cards)
        self.showOneCard = True

    def __str__(self):
        """Return just one card if not hit yet."""
        if self.showOneCard:
            return str(self.cards[0])
        else:
            return Player.__str__(self)

    def hit(self, deck):
        """Add cards while points < 17,
        then allow all to be shown."""
        self.showOneCard = False
        while self.getPoints() < 17:
            self.cards.append(deck.deal())

class Blackjack(object):

    def __init__(self):
        self.deck = Deck()
        self.deck.shuffle()
        self.player = Player([self.deck.deal(), self.deck.deal()])
        self.dealer = Dealer([self.deck.deal(), self.deck.deal()])

    def play(self):
        print("Player:\n", self.player)
        print("Dealer:\n", self.dealer)
        while True:
            choice = input("Do you want a hit? [y/n]: ")
            if choice in ("Y", "y"):
                self.player.hit(self.deck.deal())
                points = self.player.getPoints()
                print("Player:\n", self.player)
                if points >= 21:
                    break
            else:
                break
        playerPoints = self.player.getPoints()
        if playerPoints > 21:
            print("You bust and lose")
        else:
            self.dealer.hit(self.deck)
            print("Dealer:\n", self.dealer)
            dealerPoints = self.dealer.getPoints()
            if dealerPoints > 21:
                print("Dealer busts and you win")
            elif dealerPoints > playerPoints:
                print("Dealer wins")
            elif dealerPoints < playerPoints and playerPoints <= 21:
                print("You win")
            elif dealerPoints == playerPoints:
                if self.player.hasBlackjack() and not self.dealer.hasBlackjack():
                    print("You win")
                elif not self.player.hasBlackjack() and self.dealer.hasBlackjack():
                    print("Dealer wins")
                else:
                    print("There is a tie")
        
def main():
    """Instantiate the model and play the game."""
    game = Blackjack()
    game.play()

if __name__ == "__main__":
    main()
  
