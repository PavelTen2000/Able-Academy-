import numpy as np

class Dataset:
    def __init__(self, X, y):
        self._x = X
        self._y = y
        self.num2label = {}
        self.label2num = {}
        self._transform()

    def __len__(self):
        '''
        Этот метод возвращает размер набора данных.
        '''
        # Начало вашего кода

        # Конец вашего кода

    def _transform(self):
        '''
        Этот метод очищает набор данных X, а также конвертирует y в числа.
        '''
        # Начало вашего кода

        # Конец вашего кода
        pass

    def split_dataset(self, val=0.1, test=0.1):
        datasets = {}
        '''
        Этот метод разделяет набор данных на train, validation, test, 
        и присваивает словарю "datasets" со следующие ключи: "train", "validation" и "test"
        Установите np.random.seed(1).
        '''
        # Начало вашего кода

        # Конец вашего кода
        return datasets