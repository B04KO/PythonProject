import random

def draw_card():
    cards = {'2': 2, '3': 3, '4': 4, '5': 5, '6': 6, '7': 7, '8': 8, '9': 9,
             '10': 10, 'J': 10, 'Q': 10, 'K': 10, 'A': 11}  # Туз = 11, но может быть 1
    card = random.choice(list(cards.keys()))
    return card, cards[card]

def calculate_score(cards):
    score = sum(cards)
    if score > 21 and 11 in cards:
        cards.remove(11)
        cards.append(1)
        score = sum(cards)
    return score

# Инициализация игры
player_cards, dealer_cards = [], []
player_score, dealer_score = 0, 0

# Начальная раздача
for _ in range(2):
    card, value = draw_card()
    player_cards.append(value)

    card, value = draw_card()
    dealer_cards.append(value)

print(f"Ваши карты: {player_cards} (Сумма: {calculate_score(player_cards)})")
print(f"Карта дилера: [{dealer_cards[0]}, ?]")

# Ход игрока
while calculate_score(player_cards) < 21:
    action = input("Взять ещё карту? (y/n): ").lower()
    if action == 'y':
        card, value = draw_card()
        player_cards.append(value)
        print(f"Вы взяли карту: {card} (Сумма: {calculate_score(player_cards)})")
    else:
        break

player_score = calculate_score(player_cards)

# Ход дилера
print("\nДилер открывает карты...")
print(f"Карты дилера: {dealer_cards} (Сумма: {calculate_score(dealer_cards)})")

while calculate_score(dealer_cards) < 17:
    card, value = draw_card()
    dealer_cards.append(value)
    print(f"Дилер взял карту: {card} (Сумма: {calculate_score(dealer_cards)})")

dealer_score = calculate_score(dealer_cards)

# Определение победителя
print("\nРезультат:")
if player_score > 21:
    print("Вы перебрали! Дилер победил.")
elif dealer_score > 21 or player_score > dealer_score:
    print("Поздравляем, вы выиграли!")
elif player_score < dealer_score:
    print("Дилер победил.")
else:
    print("Ничья!")
