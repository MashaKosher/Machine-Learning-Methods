import numpy as np
from collections import Counter

# Базовые функции дерева решений
# 1) Класс узла дерева (по заготовке)
class Node:
    def __init__(self, index, t, true_branch, false_branch):
        self.index = index  # индекс признака, по которому ведется сравнение с порогом в этом узле
        self.t = t  # значение порога
        self.true_branch = true_branch  # поддерево, удовлетворяющее условию в узле
        self.false_branch = false_branch  # поддерево, не удовлетворяющее условию в узле


# 2) Класс терминального узла (листа) (по заготовке)
class Leaf:
    def __init__(self, data, labels):
        self.data = data
        self.labels = labels
        self.prediction = self.predict()

    def predict(self):
        # подсчет количества объектов разных классов
        classes = {}  # сформируем словарь "класс: количество объектов"
        for label in self.labels:
            if label not in classes:
                classes[label] = 0
            classes[label] += 1

        # найдем класс, количество объектов которого будет максимальным в этом листе и вернем его
        prediction = max(classes, key=classes.get)
        return prediction

# 3) Расчет критерия Джини (простая версия)
def gini(labels):
    """
    Расчет критерия Джини для набора меток

    Параметры:
    labels - массив меток классов

    Возвращает:
    impurity - значение критерия Джини (от 0 до 1)
    """
    if not labels:
        return 0
    
    total = len(labels)
    counts = Counter(labels)
    return 1 - sum((count / total) ** 2 for count in counts.values())
    # # Подсчет количества объектов каждого класса
    # classes = {}
    # for label in labels:
    #     if label not in classes:
    #         classes[label] = 0
    #     classes[label] += 1

    # # Расчет критерия Джини
    # impurity = 1
    # total = len(labels)

    # for label in classes:
    #     p = classes[label] / total
    #     impurity -= p ** 2

    # return impurity


# 4) Расчет прироста информации
def gain(left_labels, right_labels, root_gini):
    """
    Расчет прироста информации (Information Gain)

    Параметры:
    left_labels - метки левой ветви
    right_labels - метки правой ветви
    root_gini - критерий Джини корневого узла

    Возвращает:
    information_gain - прирост информации
    """
    # Количество элементов в каждой ветви
    n_left = len(left_labels)
    n_right = len(right_labels)
    n_total = n_left + n_right

    # Критерий Джини для каждой ветви
    gini_left = gini(left_labels)
    gini_right = gini(right_labels)

    # Взвешенное среднее критериев Джини дочерних узлов
    weighted_gini = (n_left / n_total) * gini_left + (n_right / n_total) * gini_right

    # Прирост информации
    information_gain = root_gini - weighted_gini

    return information_gain


# 5) Разбиение датасета в узле
def split(data, labels, column_index, t):
    """
    Разбиение датасета в узле дерева решений

    Параметры:
    data - матрица признаков (numpy array)
    labels - вектор меток классов (numpy array)
    column_index - индекс колонки для разбиения
    t - пороговое значение

    Возвращает:
    true_data - данные для левой ветви (<= t)
    false_data - данные для правой ветви (> t)
    true_labels - метки для левой ветви
    false_labels - метки для правой ветви
    """
    left = np.where(data[:, column_index] <= t)
    right = np.where(data[:, column_index] > t)

    true_data = data[left]
    false_data = data[right]

    true_labels = labels[left]
    false_labels = labels[right]

    return true_data, false_data, true_labels, false_labels


# 6) Нахождение наилучшего разбиения
def find_best_split(data, labels):
    """
    Нахождение наилучшего разбиения датасета по критерию прироста информации

    Параметры:
    data - матрица признаков (numpy array)
    labels - вектор меток классов (numpy array)

    Возвращает:
    best_gain - наилучший прирост информации
    best_t - оптимальное пороговое значение
    best_index - индекс оптимального признака
    """
    # обозначим минимальное количество объектов в узле
    min_samples_leaf = 3

    root_gini = gini(labels)

    best_gain = 0
    best_t = None
    best_index = None

    n_features = data.shape[1]

    for index in range(n_features):
        t_values = np.unique(data[:, index])

        for t in t_values:
            true_data, false_data, true_labels, false_labels = split(data, labels, index, t)

            # Проверка минимального количества объектов в каждой ветви
            if len(true_labels) < min_samples_leaf or len(false_labels) < min_samples_leaf:
                continue

            current_gain = gain(true_labels, false_labels, root_gini)

            if current_gain > best_gain:
                best_gain, best_t, best_index = current_gain, t, index

    return best_gain, best_t, best_index


# 14) Основное дерево решений (базовая версия)
class DecisionTree:
    def __init__(self, max_depth=5):
        self.max_depth = max_depth
        self.tree = None

    def fit(self, X, y):
        # Заготовка для обучения
        pass

    def predict(self, X):
        # Заготовка для предсказания
        return [0] * len(X)


# 8) Построение дерева с помощью рекурсивной функции
def build_tree(data, labels, max_depth=10, min_samples_split=2, min_samples_leaf=1, current_depth=0):
    """
    Рекурсивное построение дерева решений с критериями останова

    Параметры:
    data - матрица признаков
    labels - вектор меток классов
    max_depth - максимальная глубина дерева
    min_samples_split - минимальное количество объектов для разбиения
    min_samples_leaf - минимальное количество объектов в листе
    current_depth - текущая глубина рекурсии

    Возвращает:
    node - узел дерева (Node или Leaf)
    """
    # Критерий останова 1: максимальная глубина
    if max_depth is not None and current_depth >= max_depth:
        return Leaf(data, labels)

    # Критерий останова 2: недостаточно объектов для разбиения
    if len(labels) < min_samples_split:
        return Leaf(data, labels)

    # Критерий останова 3: все объекты одного класса
    unique_labels = np.unique(labels)
    if len(unique_labels) == 1:
        return Leaf(data, labels)

    gain_val, t, index = find_best_split(data, labels)

    # Критерий останова 4: нет прироста качества
    if gain_val == 0:
        return Leaf(data, labels)

    true_data, false_data, true_labels, false_labels = split(data, labels, index, t)

    # Критерий останова 5: проверка минимального количества объектов в листьях
    if len(true_labels) < min_samples_leaf or len(false_labels) < min_samples_leaf:
        return Leaf(data, labels)

    # Рекурсивно строим два поддерева
    true_branch = build_tree(true_data, true_labels, max_depth, min_samples_split,
                            min_samples_leaf, current_depth + 1)
    false_branch = build_tree(false_data, false_labels, max_depth, min_samples_split,
                             min_samples_leaf, current_depth + 1)

    # Возвращаем класс узла со всеми поддеревьями
    return Node(index, t, true_branch, false_branch)


# 9) Классификация одного объекта
def classify_object(obj, node):
    """
    Классификация одного объекта по дереву решений

    Параметры:
    obj - вектор признаков объекта
    node - узел дерева

    Возвращает:
    prediction - предсказанный класс
    """
    # Останавливаем рекурсию, если достигли листа
    if isinstance(node, Leaf):
        answer = node.prediction
        return answer

    if obj[node.index] <= node.t:
        return classify_object(obj, node.true_branch)
    else:
        return classify_object(obj, node.false_branch)


# 10) Предсказание для набора данных
def predict(data, tree):
    """
    Предсказание классов для набора данных

    Параметры:
    data - матрица признаков
    tree - обученное дерево решений

    Возвращает:
    classes - список предсказанных классов
    """
    classes = []
    for obj in data:
        prediction = classify_object(obj, tree)
        classes.append(prediction)
    return classes


# 11) Подсчет точности классификации
def accuracy_metric(actual, predicted):
    """
    Подсчет точности как доли правильных ответов

    Параметры:
    actual - истинные метки классов
    predicted - предсказанные метки классов

    Возвращает:
    accuracy - доля правильных предсказаний (от 0 до 1)
    """
    # Проверка на пустые списки
    if len(actual) == 0:
        return 0.0

    correct = 0
    total = len(actual)

    for i in range(total):
        if actual[i] == predicted[i]:
            correct += 1

    accuracy = correct / total
    return accuracy


# 12) Подсчет метрик качества модели
def evaluate_model(actual, predicted):
    """
    Подсчет комплексных метрик качества модели классификации

    Параметры:
    actual - истинные метки классов
    predicted - предсказанные метки классов

    Возвращает:
    metrics - словарь с метриками качества
    """
    # Проверка на пустые списки
    if len(actual) == 0:
        return {
            'accuracy': 0.0,
            'precision': 0.0,
            'recall': 0.0,
            'f1_score': 0.0,
            'total_samples': 0
        }

    total = len(actual)
    unique_classes = np.unique(actual)

    # Accuracy
    accuracy = accuracy_metric(actual, predicted)

    # Precision, Recall, F1 для каждого класса
    precision_total = 0
    recall_total = 0
    f1_total = 0

    for class_label in unique_classes:
        # True Positives, False Positives, False Negatives
        tp = sum(1 for a, p in zip(actual, predicted) if a == class_label and p == class_label)
        fp = sum(1 for a, p in zip(actual, predicted) if a != class_label and p == class_label)
        fn = sum(1 for a, p in zip(actual, predicted) if a == class_label and p != class_label)

        # Precision
        precision = tp / (tp + fp) if (tp + fp) > 0 else 0

        # Recall
        recall = tp / (tp + fn) if (tp + fn) > 0 else 0

        # F1-score
        f1 = 2 * precision * recall / (precision + recall) if (precision + recall) > 0 else 0

        precision_total += precision
        recall_total += recall
        f1_total += f1

    # Средние значения метрик (macro averaging)
    num_classes = len(unique_classes)
    avg_precision = precision_total / num_classes
    avg_recall = recall_total / num_classes
    avg_f1 = f1_total / num_classes

    return {
        'accuracy': accuracy,
        'precision': avg_precision,
        'recall': avg_recall,
        'f1_score': avg_f1,
        'total_samples': total
    }


# 13) Печать структуры дерева
def print_tree(node, spacing=""):
    """
    Рекурсивная печать структуры дерева решений

    Параметры:
    node - узел дерева
    spacing - отступ для визуализации
    """
    # Если лист, то выводим его прогноз
    if isinstance(node, Leaf):
        print(spacing + "Прогноз:", node.prediction)
        return

    # Выведем значение индекса и порога на этом узле
    print(spacing + 'Индекс', str(node.index), '<=', str(node.t))

    # Рекурсионный вызов функции на положительном поддереве
    print(spacing + '--> True:')
    print_tree(node.true_branch, spacing + "  ")

    # Рекурсионный вызов функции на отрицательном поддереве
    print(spacing + '--> False:')
    print_tree(node.false_branch, spacing + "  ")


