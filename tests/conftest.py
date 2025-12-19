"""
Конфигурационный файл pytest с фикстурами
"""

import random

import pytest


@pytest.fixture
def empty_list():
    """Пустой список"""
    return []


@pytest.fixture
def single_element_list():
    """Список с одним элементом"""
    return [42]


@pytest.fixture
def sorted_list():
    """Отсортированный список"""
    return [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]


@pytest.fixture
def reverse_sorted_list():
    """Обратно отсортированный список"""
    return [10, 9, 8, 7, 6, 5, 4, 3, 2, 1]


@pytest.fixture
def list_with_duplicates():
    """Список с повторяющимися элементами"""
    return [3, 1, 4, 1, 5, 9, 2, 6, 5, 3, 5]


@pytest.fixture
def list_with_negatives():
    """Список с отрицательными числами"""
    return [-5, -1, -3, -2, -4, 0, 2, 1, -6]


@pytest.fixture()
def random_list_small():
    """Маленький случайный список"""
    random.seed(42)
    return [random.randint(-100, 100) for _ in range(20)]


@pytest.fixture()
def random_list_large():
    """Большой случайный список"""
    random.seed(42)
    return [random.randint(-10000, 10000) for _ in range(1000)]


@pytest.fixture(params=[10, 100, 500])
def random_list_parametrized(request):
    """Списки разных размеров (параметризованная фикстура)"""
    random.seed(request.param)
    return [random.randint(-1000, 1000) for _ in range(request.param)]


@pytest.fixture
def edge_case_all_equal():
    """Спсиок из одинаковых элементов"""
    return [7, 7, 7, 7, 7, 7, 7]


@pytest.fixture
def edge_case_floats():
    """Список из чисел с плавающей точкой"""
    return [1.5, 2.3, 0.1, -1.2, 3.7, -0.5]
