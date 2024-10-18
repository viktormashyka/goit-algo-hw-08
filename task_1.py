# Уявіть, що вам на технічному інтерв'ю дають наступну задачу, яку треба розв'язати за допомогою купи.
# Є декілька мережевих кабелів різної довжини, їх потрібно об'єднати по два за раз в один кабель, 
# використовуючи з'єднувачі, у порядку, який призведе до найменших витрат. Витрати на з'єднання двох кабелів 
# дорівнюють їхній сумі довжин, а загальні витрати дорівнюють сумі з'єднання всіх кабелів.
# Завдання полягає в тому, щоб знайти порядок об'єднання, який мінімізує загальні витрати.

import heapq

def min_cost_to_connect_cables(cables):
    # Перетворюємо список кабелів у мін-купу
    heapq.heapify(cables)
    
    total_cost = 0

    # Поки в купі більше одного елемента
    while len(cables) > 1:
        # Витягуємо два найменших кабелі
        first = heapq.heappop(cables)
        second = heapq.heappop(cables)
        
        # Об'єднуємо їх
        cost = first + second
        total_cost += cost
        
        # Додаємо новий кабель назад у купу
        heapq.heappush(cables, cost)

        print("first:", first)
        print("second:", second)
        print("total_cost = total_cost + first + second: ", total_cost)
    return total_cost

# Приклад
cables = [4, 10, 3, 5, 1]
result = min_cost_to_connect_cables(cables)
print(f"Загальна довжина кабелів: {cables}")
print(f"Мінімальні витрати на з'єднання кабелів: {result}")


