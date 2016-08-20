from random import randint

a = randint(1, 10)
print(a)

class Player:
    def __init__(self, balance):
        self.balance = balance
        self.hands = ''

    def hands(self):
        pass

class Dealer(Player):
    pass

class Suit:
    def __init__(self):
        self.numbers = 'A23456789TJQK'
        self.marks = 'SDHC'
        self.ranks_1 = [i+1 for i in range(10)]
        for i in range(3):
            self.ranks_1.append(10)
        for i in range(3):
            self.ranks_1 += self.ranks_1
        self.ranks_Ace = [11, 2, 3, 4, 5, 6, 7, 8, 9, 10, 10, 10, 10]


class Deck(Suit):
    def cards(self):
        self.cards = [n+'/'+m for m in self.marks for n in self.numbers]
        self.score_1 = dict(zip(self.cards, self.ranks_1))

        '''
        for key in range(len(self.cards)):
            # print(self.cards[key])
            # print(self.ranks_1[key])
            self.score_1[self.cards[key]] = self.ranks_1[key]
        '''
        return self.score_1

# for playing order
class Table():

    pass

class Pot:
    pass

if __name__ == "__main__":
    deck = Deck()
    print(deck.cards())
    # deck_dict = deck.cards()
    # print(type(deck_dict))
    '''
    deck_order = list(deck_dict)
    print(deck_order)
'''

'''
    pl_1 = Player(100)
    pl_1.balance()
    pl_2 = Player(300)
    pl_2.balance()
'''