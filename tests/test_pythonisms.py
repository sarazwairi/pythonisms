import pytest
from pythonisms.pythonisms import LinkedList

def test_for_in():
    snack = LinkedList(('apple', 'orange', 'kiwi'))
    snack_list = []

    for fruit in snack:
        snack_list.append(fruit)

    assert snack_list == ['apple', 'orange', 'kiwi']

def test_list_comp():
    snack = LinkedList(('seedless', 'plums', 'flushy'))
    upper_snack = [fruit.upper() for fruit in snack]
    assert upper_snack == ['SEEDLESS', 'PLUMS', 'FLUSHY']

def test_str():
    foods = LinkedList(['seedless', 'plums', 'flushy'])
    assert str(foods) == '[ seedless ] -> [ plums ] -> [ flushy ] -> None'

def test_list_cast():
    snack_list = ['seedless', 'plums', 'flushy']
    snack = LinkedList(snack_list)
    assert list(snack) == snack_list

def test_equals():
    lla = LinkedList(['seedless', 'plums', 'flushy'])
    llb = LinkedList(['seedless', 'plums', 'flushy'])
    assert lla == llb


def test_range():
    num_range = range(1, 20+1)
    nums = LinkedList(num_range)
    assert len(nums) == 20

def test_filter():
    nums = LinkedList(range(1, 10))
    odds = [num for num in nums if num % 2]
    assert odds == [1, 3, 5, 7, 9]

def test_next():
    snack_list = ['seedless', 'plums', 'flushy']
    iterator = iter(snack_list)
    assert next(iterator) == 'seedless'
    assert next(iterator) == 'plums'
    assert next(iterator) == 'flushy'

def test_get_item():
    snack = LinkedList(('seedless', 'plums', 'flushy'))
    assert snack[0] == 'seedless'

def test_get_item_out_of_range():
    snack = LinkedList(('seedless', 'plums', 'flushy'))
    with pytest.raises(IndexError):
        snack[100]