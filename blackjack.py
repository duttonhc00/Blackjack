DECK_SIZE = 52
SUITS = 4
ACE_LOW = 1
ACE_HIGH = 11
FACE = 10
FACES_DECK = SUITS * 4 # the number of faces in a deck - 16

DECK = []
for i in range(2, ACE_HIGH):
    if i != FACE:
        cards=[i] * SUITS
    else:
        cards=[i] * FACES_DECK
    DECK = DECK + cards

DECK_LOW = [ACE_LOW] * SUITS + DECK
DECK_HIGH = DECK + [ACE_HIGH] * SUITS

print(DECK)
print(DECK_LOW)
print(DECK_HIGH)

def prob_draw(val):
    if val != FACE:
        prob = SUITS / DECK_SIZE
    else:
        prob = FACES_DECK / DECK_SIZE
    return prob

PROB_FOUR = prob_draw(4)        
print(PROB_FOUR)

def prob_greater_equal_high(val):
    prob = 0
    for i in range(val, ACE_HIGH + 1):
        prob += prob_draw(i)
    return prob

PROB_GREATER_FOUR_HIGH = prob_greater_equal_high(4)
print(PROB_GREATER_FOUR_HIGH)