import numpy as np

def create_boolean_matrix(truth_table):
    """
    Создает матрицу для булевой функции от двух переменных
    truth_table: список из 4 значений [f(00), f(01), f(10), f(11)]
    """
    # Размер матрицы 4x4 для двух переменных (2^2 = 4)
    matrix = np.zeros((4, 4))
    
    # Заполняем матрицу на основе таблицы истинности
    for i in range(4):
        output = truth_table[i]
        matrix[output][i] = 1
    
    return matrix

def is_unitary(matrix):
    """
    Проверяет, является ли матрица унитарной
    """
    # Получаем эрмитово сопряжение матрицы
    hermitian = matrix.conj().T
    # Умножаем матрицу на её эрмитово сопряжение
    product = np.dot(matrix, hermitian)
    # Сравниваем с единичной матрицей
    identity = np.eye(len(matrix))
    return np.allclose(product, identity)

def print_truth_table(truth_table):
    """
    Выводит таблицу истинности в читаемом формате
    """
    print("\nТаблица истинности:")
    print("x1 x2 | f(x1,x2)")
    print("-" * 13)
    for i in range(4):
        x1 = i >> 1  # Первая переменная
        x2 = i & 1   # Вторая переменная
        print(f" {x1}  {x2} |    {truth_table[i]}")

def main():
    # Примеры булевых функций
    # AND
    truth_table_and = [0, 0, 0, 1]
    # OR
    truth_table_or = [0, 1, 1, 1]
    # XOR
    truth_table_xor = [0, 1, 1, 0]
    
    # Выберем XOR для демонстрации
    truth_table = truth_table_xor
    
    # Выводим таблицу истинности
    print_truth_table(truth_table)
    
    # Создаем матрицу
    matrix = create_boolean_matrix(truth_table)
    
    # Выводим результаты
    print("\nМатрица преобразования:")
    print(matrix)
    
    # Проверяем унитарность
    unitary = is_unitary(matrix)
    print("\nПроверка на унитарность:")
    print(f"Матрица {'' if unitary else 'не '}является унитарной")
    
    # Проверяем работу матрицы
    print("\nПроверка работы матрицы:")
    for i in range(4):
        # Создаем входной вектор
        input_state = np.zeros(4)
        input_state[i] = 1
        
        # Применяем матрицу
        output_state = np.dot(matrix, input_state)
        
        # Выводим результат
        x1 = i >> 1
        x2 = i & 1
        result = np.where(output_state == 1)[0][0]
        print(f"f({x1},{x2}) = {result}")

if __name__ == "__main__":
    main()