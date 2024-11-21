class StepValueError(ValueError):  # Пользовательское исключение для шага = 0
    pass


class Iterator:
    def __init__(self, start, stop, step=1):
        """Инициализация итератора с началом, концом и шагом."""
        self.start = start  # Начальное значение итерации
        self.stop = stop  # Граница завершения итерации
        if step == 0:  # Проверяем, что шаг не равен 0
            raise StepValueError('Шаг не может быть равен 0')
        self.step = step  # Шаг итерации
        self.pointer = start  # Указатель текущего значения итерации

    def __iter__(self):
        """Возвращает объект самого себя как итератор."""
        self.pointer = self.start  # Сбрасываем указатель
        return self

    def __next__(self):
        """
        Возвращает следующее значение итератора.
        Завершает итерацию, если указатель выходит за границы.
        """
        # Проверка завершения итерации
        if (self.step > 0 and self.pointer > self.stop) or (self.step < 0 and self.pointer < self.stop):
            raise StopIteration

        # Сохраняем текущее значение для возврата
        current = self.pointer
        # Увеличиваем указатель на шаг
        self.pointer += self.step
        return current


# Примеры использования итератора
try:
    # Создаем итератор с шагом 0 (это вызовет ошибку)
    iter1 = Iterator(100, 200, 0)
    for i in iter1:
        print(i, end=' ')
except StepValueError as e:
    print(f'Error: {e}')  # Выводим сообщение об ошибке

# Другие примеры с корректными шагами
iter2 = Iterator(-5, 1)  # Шаг по умолчанию: 1
iter3 = Iterator(6, 15, 2)  # Положительный шаг
iter4 = Iterator(5, 1, -1)  # Отрицательный шаг
iter5 = Iterator(10, 1)  # Шаг по умолчанию: 1

# Вывод значений для каждого итератора
for i in iter2:
    print(i, end=' ')  # -5 -4 -3 -2 -1 0 1
print()
for i in iter3:
    print(i, end=' ')  # 6 8 10 12 14
print()
for i in iter4:
    print(i, end=' ')  # 5 4 3 2 1
print()
for i in iter5:
    print(i, end=' ')  # Ничего не выведется, т.к. шаг по умолчанию: 1
print()
