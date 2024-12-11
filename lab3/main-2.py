import numpy as np

def create_quantum_circuit(a: int, m: int, n_qubits: int) -> np.ndarray:
    """
    Создает матрицу квантового преобразования для вычисления ax mod m
    
    Параметры:
    a: множитель
    m: модуль
    n_qubits: количество кубитов (определяет размер матрицы как 2^n_qubits)
    """
    size = 2**n_qubits
    matrix = np.zeros((size, size))
    
    # Заполняем матрицу преобразования
    for x in range(size):
        result = (a * x) % m
        matrix[result][x] = 1
    
    return matrix

def simulate_quantum_computation(x: int, a: int, m: int, n_qubits: int):
    """
    Симулирует квантовое вычисление ax mod m
    
    Параметры:
    x: входное значение
    a: множитель
    m: модуль
    n_qubits: количество кубитов
    """
    # Создаем начальный вектор состояния
    size = 2**n_qubits
    initial_state = np.zeros(size)
    initial_state[x] = 1
    
    # Получаем матрицу преобразования
    circuit = create_quantum_circuit(a, m, n_qubits)
    
    # Применяем преобразование
    final_state = np.dot(circuit, initial_state)
    
    # Получаем результат (индекс ненулевого элемента)
    result = np.where(np.abs(final_state) > 0.99)[0][0]
    
    return result, circuit

def is_unitary(matrix: np.ndarray) -> bool:
    """Проверяет, является ли матрица унитарной"""
    h = matrix.conj().T
    product = np.dot(matrix, h)
    identity = np.eye(len(matrix))
    return np.allclose(product, identity)

def main():
    # Параметры вычисления
    a = 7  # множитель
    m = 15  # модуль
    n_qubits = 4  # количество кубитов (достаточно для чисел до 15)
    
    print(f"Моделирование квантового вычисления f(x) = {a}x mod {m}")
    print(f"Используется {n_qubits} кубитов\n")
    
    # Создаем матрицу преобразования
    circuit = create_quantum_circuit(a, m, n_qubits)
    
    # Проверяем унитарность
    unitary = is_unitary(circuit)
    print(f"Матрица преобразования {'унитарная' if unitary else 'не унитарная'}\n")
    
    # Тестируем для нескольких входных значений
    test_values = [1, 2, 3, 4, 5]
    
    print("Результаты вычислений:")
    print("x | Классический результат | Квантовый результат")
    print("-" * 45)
    
    for x in test_values:
        # Классическое вычисление
        classical_result = (a * x) % m
        
        # Квантовое вычисление
        quantum_result, _ = simulate_quantum_computation(x, a, m, n_qubits)
        
        print(f"{x:2d} |         {classical_result:2d}          |        {quantum_result:2d}")
        
        # Проверка корректности
        assert classical_result == quantum_result, f"Ошибка: несоответствие результатов для x={x}"
    
    # Показываем матрицу преобразования
    print("\nМатрица квантового преобразования:")
    print(circuit)

if __name__ == "__main__":
    main()