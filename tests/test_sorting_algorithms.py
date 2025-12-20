import pytest

from sorting_algorithms import bubble_sort, heap_sort, merge_sort, quick_sort

SORTING_ALGORITHMS = [
    pytest.param(bubble_sort, "bubble_sort"),
    pytest.param(merge_sort, "merge_sort"),
    pytest.param(heap_sort, "heap_sort"),
    pytest.param(quick_sort, "quick_sort"),
]


class TestSortingAlgorithms:
    """Класс обычных тестов и тестов крайних случаев для всех алгоритмов сортировки"""

    @pytest.mark.parametrize("sort_func, name", SORTING_ALGORITHMS)
    def test_empty_list(self, sort_func, name, empty_list):
        """Тест сортировки пустого списка"""
        result = sort_func(empty_list.copy())
        assert result == [], f"{name}: пустой список обработан неверно"

    @pytest.mark.parametrize("sort_func, name", SORTING_ALGORITHMS)
    def test_single_element(self, sort_func, name, single_element_list):
        """Тест сортировки списка с одним элементом"""
        result = sort_func(single_element_list.copy())
        assert result == [42], f"{name}: список из одного элемента обработан неверно"

    @pytest.mark.parametrize("sort_func, name", SORTING_ALGORITHMS)
    def test_already_sorted(self, sort_func, name, sorted_list):
        """Тест сортировки уже отсортированного списка"""
        result = sort_func(sorted_list.copy())
        assert result == sorted_list, f"{name}: отсортированный список изменился"

    @pytest.mark.parametrize("sort_func, name", SORTING_ALGORITHMS)
    def test_reverse_sorted(self, sort_func, name, reverse_sorted_list):
        """Тест сортировки обратно отсортированного списка"""
        result = sort_func(reverse_sorted_list.copy())
        expected = sorted(reverse_sorted_list)
        assert result == expected, f"{name}: обратный список отсортирован неверно"

    @pytest.mark.parametrize("sort_func, name", SORTING_ALGORITHMS)
    def test_with_duplicates(self, sort_func, name, list_with_duplicates):
        """Тест сортировки списка с повторяющимися элементами"""
        result = sort_func(list_with_duplicates.copy())
        expected = sorted(list_with_duplicates)
        assert result == expected, (
            f"{name}: список с повторяющимися значениями отсортирован неверно"
        )

    @pytest.mark.parametrize("sort_func, name", SORTING_ALGORITHMS)
    def test_with_negatives(self, sort_func, name, list_with_negatives):
        """Тест сортировки списка с отрицательными числами"""
        result = sort_func(list_with_negatives.copy())
        expected = sorted(list_with_negatives)
        assert result == expected, (
            f"{name}: список с отрицательными числами отсортирован неверно"
        )

    @pytest.mark.parametrize("sort_func, name", SORTING_ALGORITHMS)
    def test_with_random_small(self, sort_func, name, random_list_small):
        """Тест сортировки маленького случайного списка"""
        result = sort_func(random_list_small.copy())
        expected = sorted(random_list_small)
        assert result == expected, (
            f"{name}: маленький случайный список отсортирован неверно"
        )

    @pytest.mark.parametrize("sort_func, name", SORTING_ALGORITHMS)
    def test_with_random_large(self, sort_func, name, random_list_large):
        """Тест сортировки большого случайного списка"""
        result = sort_func(random_list_large.copy())
        expected = sorted(random_list_large)
        assert result == expected, (
            f"{name}: большой случайный список отсортирован неверно"
        )

    @pytest.mark.parametrize("sort_func, name", SORTING_ALGORITHMS)
    def test_with_parametrized_random(self, sort_func, name, random_list_parametrized):
        """Тест сортировки списка разных размеров с параметризованной фикстурой"""
        result = sort_func(random_list_parametrized.copy())
        expected = sorted(random_list_parametrized)
        assert result == expected, (
            f"{name}: параметризованный список отсортирован неверно"
        )


class TestEgdeCasesSortingAlgorithms:
    @pytest.mark.parametrize("sort_func, name", SORTING_ALGORITHMS)
    def test_edge_case_all_equal(self, sort_func, name, edge_case_all_equal):
        """Тест крайнего случая: все элементы одинаковые."""
        result = sort_func(edge_case_all_equal.copy())
        assert result == edge_case_all_equal, f"{name}: одинаковые элементы изменились"

    @pytest.mark.parametrize("sort_func, name", SORTING_ALGORITHMS)
    def test_edge_case_floats(self, sort_func, name, edge_case_floats):
        """Тест крайнего случая: список из чисел с плавающей точкой"""
        result = sort_func(edge_case_floats.copy())
        expected = sorted(edge_case_floats)
        assert result == expected, (
            f"{name}: список из чисел с плавающей точкой отсортирован неверно"
        )

    @pytest.mark.parametrize("sort_func, name", SORTING_ALGORITHMS)
    def test_none_input_raises(self, sort_func, name):
        """Тест на вызов исключения при передаче None"""
        with pytest.raises((TypeError, AttributeError)):
            sort_func(None)

    @pytest.mark.parametrize("sort_func, name", SORTING_ALGORITHMS)
    def test_wrong_type_input_raises(self, sort_func, name):
        """Тест на вызов исключения при передача не-списка"""
        with pytest.raises((TypeError, AttributeError)):
            sort_func("не список")


class TestPropertyBasedSortingAlgorithms:
    """Класс property-based тестов"""

    @pytest.mark.parametrize("sort_func1, name1", SORTING_ALGORITHMS)
    @pytest.mark.parametrize("sort_func2, name2", SORTING_ALGORITHMS)
    def test_all_algorithms_consistent(
        self, sort_func1, name1, sort_func2, name2, random_list_small
    ):
        """
        Property-based тест выдачи одинакового результата всеми алгоритмами сортировки"""
        arr = random_list_small.copy()
        result1 = sort_func1(arr.copy())
        result2 = sort_func2(arr.copy())

        assert result1 == result2, (
            f"Алгоритмы {name1} и {name2} дали разные результаты:\n"
            f"{name1}: {result1}\n{name2}: {result2}"
        )

    @pytest.mark.parametrize("sort_func, name", SORTING_ALGORITHMS)
    def test_sorting_properties(self, sort_func, name, random_list_small):
        """
        Property-based тест проверки следующих свойств отсортированного массива:
        1. Длина сохраняется
        2. Все элементы из исходного массива присутствуют
        3. Массив отсортирован в неубывающем порядке
        """
        arr = random_list_small.copy()
        result = sort_func(arr.copy())

        assert len(result) == len(arr), f"{name}: длина массива изменилась"

        assert sorted(result) == sorted(arr), f"{name}: элементы не сохранились"

        for i in range(len(result) - 1):
            assert result[i] <= result[i + 1], (
                f"{name}: массив не отсортирован на позициях {i}, {i + 1}: "
                f"{result[i]} > {result[i + 1]}"
            )

    @pytest.mark.parametrize("sort_func, name", SORTING_ALGORITHMS)
    def test_idempotency(self, sort_func, name, random_list_small):
        """Property-based тест проверики того, что массив не меняется при повторной сортировке"""

        arr = random_list_small.copy()

        sorted_once = sort_func(arr.copy())

        sorted_twice = sort_func(sorted_once.copy())

        assert sorted_once == sorted_twice, (
            f"{name}: сортировка меняет уже отсортированный массив"
        )


class TestPerformanceSortingAlgorithms:
    def test_performance_comparison(self, random_list_large):
        """Тест сравнения производительности всех алгоритмов на большом списке."""
        import time

        algorithms = [
            (bubble_sort, "bubble_sort"),
            (merge_sort, "merge_sort"),
            (heap_sort, "heap_sort"),
            (quick_sort, "quick_sort"),
        ]

        results = []

        for sort_func, name in algorithms:
            arr_copy = random_list_large.copy()
            start_time = time.perf_counter()
            sort_func(arr_copy)
            end_time = time.perf_counter()

            # Проверяем корректность
            assert arr_copy == sorted(random_list_large), f"{name}: сортировка неверна"

            time_taken = end_time - start_time
            results.append((name, time_taken))

        # Сортируем по времени выполнения
        results.sort(key=lambda x: x[1])

        if len(results) > 1:
            slowest = results[-1][0]
            fastest = results[0][0]

            print(f"\nСамый быстрый: {fastest}")
            print(f"Самый медленный: {slowest}")

            if "bubble_sort" in [name for name, _ in results]:
                print("bubble_sort один из самых медленных алгоритмов")
