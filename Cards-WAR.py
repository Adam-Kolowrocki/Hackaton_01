# Konieczność użycia modułu random.
# Program rozdaje karty i drukuje informacje o przebiegu rozgrywki
# Pomysły na uproszczenie gry:
#   zamiast implementować talię kart, używamy liczb (0, 1, 2 ... 9, 10, 11) dla (2, 3, 4, ... Q, K, A)
#   aby gra kończyła się wcześniej, rozdajemy tylko 10 kart
#   dwa tryby: zdobyte karty dochodzą do "ręki", lub są odkładane i nie wykorzystywane

# Niezbędne jest zaimportowanie funkcji random
import random

print('Zagrajmy w wojnę!')
player_1 = input('Podaj imię pierwszego gracza -> ')
player_2 = input('Podaj imię drugiego gracza -> ')
print('Rozdaję po 10 kart dla każdego gracza...')

# rozdaję po 10 kart dla każdego gracza
# tworzę listy losowych kart dla każdego zawodnika

player_1_cards = []
player_2_cards = []
player_1_score = 0
player_2_score = 0
round_counter = 0
clear = "\n" * 50

while len(player_1_cards) <= 9:
    player_1_cards.append(random.randint(0, 12))
while len(player_2_cards) <= 9:
    player_2_cards.append(random.randint(0, 12))

player_1_hidden_cards = ['X', 'X', 'X', 'X', 'X', 'X', 'X', 'X', 'X', 'X']
player_2_hidden_cards = ['X', 'X', 'X', 'X', 'X', 'X', 'X', 'X', 'X', 'X']

print(f'{player_1} ma {len(player_1_cards)} kart {player_1_hidden_cards}')
print(f'{player_2} ma {len(player_2_cards)} kart {player_2_hidden_cards}')

input('Naciśnij Enter aby rozpocząć grę...')
print(clear)

while len(player_1_cards) > 0:
    round_counter += 1
    print((f'Runda {round_counter}'))
    print(f'{player_1} wykłada kartę -> {player_1_cards[0]}')
    print(f'{player_2} wykłada kartę -> {player_2_cards[0]}')
    if player_1_cards[0] > player_2_cards[0]:
        player_1_score += 1
        player_1_cards.pop(0)
        player_2_cards.pop(0)
        print(f'{player_1} wygrywa rundę i zdobywa punkt.')
    else:
        player_2_score += 1
        player_1_cards.pop(0)
        player_2_cards.pop(0)
        print(f'{player_2} wygrywa rundę i zdobywa punkt.')
    input('Naciśnij Enter...')
    print((clear))

if player_1_score == player_2_score:
    print(f'Remis!!! Nie często się to zdarza...')
elif player_1_score > player_2_score:
    print(f'Gratulacje {player_1}, zdobywasz {player_1_score} punktów i wygrywasz wojnę !!!')
    print(f'Twój przeciwnik zdobył tylko {player_2_score} punktów.')
else:
    print(f'Gratulacje {player_2}, zdobywasz {player_2_score} punktów i wygrywasz wojnę !!!')
    print(f'Twój przeciwnik zdobył tylko {player_1_score} punktów.')
