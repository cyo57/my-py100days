import collections  # 导入collections模块，用于创建namedtuple

# 使用namedtuple创建一张扑克牌的结构，包括'rank'（点数）和'suit'（花色）
Card = collections.namedtuple('card', ['rank', 'suit'])


class FrenchDeck:
    # 定义点数（ranks）和花色（suits）的列表
    ranks = [str(n) for n in range(2, 11)] + list('JQKA')
    suits = 'spades diamonds clubs hearts'.split()

    def __init__(self) -> None:
        # 初始化法式扑克牌，生成一整副牌的列表
        self._cards = [Card(rank, suit) for suit in self.suits
                       for rank in self.ranks]

    def __len__(self):
        # 定义__len__方法，返回牌堆中的牌数
        return len(self._cards)

    def __getitem__(self, position):
        # 定义__getitem__方法，根据索引位置返回相应的扑克牌
        return self._cards[position]


deck = FrenchDeck()
print('这一摞牌有：', len(deck))

'''# 由于 __getitem__方法把操作委托给self._cards的[]运算符
# 抽三张牌
print(deck[:3])

# 抽四张A
print(deck[12::13])

# 迭代
for i in deck:
    print(i)
'''

# 按花色排序，黑桃A=51，梅花2=0
suit_values = dict(spades=3, hearts=2, diamonds=1, clubs=0)

def spades_high(card):
    # 查找 card.rank 在 FrenchDeck.ranks 列表中的索引位置，确定点数的大小
    # 例如，'2' 的索引位置为 0，'3' 的索引位置为 1，'A' 的索引位置为 12。
    rank_value = FrenchDeck.ranks.index(card.rank)
    # 根据给定的花色（card.suit），通过字典 suit_values 查找相应的花色值
    # 这个字典将不同花色映射为数字，以确定它们的排序顺序。
    # 将点数值（rank_value）乘以花色值的种类数（len(suit_values)，通常为 4，因为有四种花色）
    # 然后加上花色值。这将确保在排序时，先按点数升序排列，然后按花色的特定顺序（spades、hearts、diamonds、clubs）排列。
    return rank_value * len(suit_values) + suit_values[card.suit]

for i in sorted(deck, key = spades_high):
    print(i)