def make_fair_dice(sides):
    assert type(sides) == int and sides >= 1, 'Illegal value for sides'

    def dice():
        return randint(1, sides)

    return dice

num_rolls = int(input("Choose num rolls"))
dice = make_fair_dice(6)

# def roll_dice(num_rolls):
#     rolls = []
#     for _ in range(num_rolls):
#         rolls.append(dice())
#     if 1 in rolls:
#         score = 1
#     else:
#         score = sum(rolls)
#     return score

score = (lambda __g, __y: [None for __g['roll_dice'], roll_dice.__name__ in [(lambda num_rolls: (lambda __l: [[(lambda __items, __sentinel, __after: __y(lambda __this: lambda: (lambda __i: [(__l['rolls'].append(dice()), __this())[1] for __l['_'] in [(__i)]][0] if __i is not __sentinel else __after())(next(__items, __sentinel)))())(iter(range(__l['num_rolls'])), [], lambda: (lambda __after: [__after() for __l['score'] in [(1)]][0] if (1 in __l['rolls']) else [__after() for __l['score'] in [(sum(__l['rolls']))]][0])(lambda: __l['score'])) for __l['rolls'] in [([])]][0] for __l['num_rolls'] in [(num_rolls)]][0])({}), 'roll_dice')]][0])(globals(), (lambda f: (lambda x: x(x))(lambda y: f(lambda: y(y)()))))
print(score)