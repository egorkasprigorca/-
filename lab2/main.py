import random
import numpy as np

H = np.array([[1 / np.sqrt(2), 1 / np.sqrt(2)], 
              [1 / np.sqrt(2), -1 / np.sqrt(2)]])

# Функция для измерения кубита в стандартном базисе
def measure_in_standard_basis(state):
    probabilities = [round(abs(state[0])**2, 2), round(abs(state[1])**2, 2)]
    result = np.random.choice([0, 1], p=probabilities)
    return result, probabilities

# Функция для измерения кубита в повернутом базисе (с использованием преобразования Адамара)
def measure_in_rotated_basis(state):
    rotated_state = np.dot(H, state)  # Преобразование в повернутый базис
    probabilities = [round(abs(rotated_state[0])**2, 2), round(abs(rotated_state[1])**2, 2)]
    result = np.random.choice([0, 1], p=probabilities)
    return result, probabilities

def generate_qubit():
    # Возможные состояния кубита
    states = [
        ('|0⟩', np.array([1, 0])),  # |0⟩
        ('|1⟩', np.array([0, 1])),  # |1⟩
        ('|+⟩', np.array([1/np.sqrt(2), 1/np.sqrt(2)])),  # |+⟩
        ('|-⟩', np.array([1/np.sqrt(2), -1/np.sqrt(2)]))  # |-⟩
    ]
    return random.choice(states)

# def measure_qubit(qubit, basis):
#     # Измерение в стандартном базисе {|0⟩, |1⟩}
#     if basis == 'standard':
#         prob_0 = abs(qubit[1][0])**2
#         result = '0' if random.random() < prob_0 else '1'
#         return result
    
#     # Измерение в диагональном базисе {|+⟩, |-⟩}
#     elif basis == 'diagonal':
#         # Преобразование в диагональный базис
#         transformed = np.array([
#             (qubit[1][0] + qubit[1][1])/np.sqrt(2),
#             (qubit[1][0] - qubit[1][1])/np.sqrt(2)
#         ])
#         prob_plus = abs(transformed[0])**2
#         result = '+' if random.random() < prob_plus else '-'
#         return result

def quantum_key_protocol():
    print("\nНачало протокола:")
    
    # Шаг 1: A генерирует кубит
    qubit = generate_qubit()
    print(f"A генерирует кубит: {qubit[0]}")
    
    # Шаг 2: B выбирает базис и измеряет
    bob_basis = random.choice(['standard', 'rotated'])
    print(f"B выбирает базис: {bob_basis}")
    if bob_basis == "standard":
        measurement = measure_in_standard_basis(qubit[1])[0]
    elif bob_basis == "rotated":
        measurement = measure_in_rotated_basis(qubit[1])[0]
    print(f"B измеряет: {measurement}")
    
    # Шаг 3: B сообщает A использованный базис
    print(f"B сообщает A об использованном базисе: {bob_basis}")
    
    # Шаг 4: A проверяет соответствие
    correct_basis = False
    if bob_basis == 'standard' and qubit[0] in ['|0⟩', '|1⟩']:
        correct_basis = True
    elif bob_basis == 'rotated' and qubit[0] in ['|+⟩', '|-⟩']:
        correct_basis = True
    
    if correct_basis:
        print("A говорит: ОК")
        # Определяем секретный бит
        if qubit[0] in ['|0⟩', '|+⟩']:
            secret_bit = '0'
        else:
            secret_bit = '1'
        print(f"Секретный бит: {secret_bit}")
        return True, secret_bit
    else:
        print("A говорит: ПОВТОР")
        return False, None

def generate_key(length):
    key = ''
    attempts = 0
    while len(key) < length:
        attempts += 1
        print(f"\nПопытка {attempts}")
        success, bit = quantum_key_protocol()
        if success:
            key += bit
    
    print(f"\nИтоговый ключ: {key}")
    print(f"Потребовалось попыток: {attempts}")
    return key

# Запуск генерации ключа
if __name__ == "__main__":
    key_length = 10  #  Длина ключа
    generate_key(key_length)
