from typing import List
from piqok.piqok import Json


class Person(Json):
    name: str
    age: int


p = Person({
    'name': 'Gilad',
    'age': 40
})


def test_person():
    assert p.name == 'Gilad'
    assert p.age == 40


class Bag(Json):
    size: float
    items: List[str]


b = Bag({
    'size': 30.4,
    'items': ['apple', 'map']
})


def test_bag():
    assert b.size == 30.4
    assert b.items[1] == 'map'


class APersonWithABag(Json):
    person: Person
    bag: Bag


def test_a_person_with_a_bag():
    pwb = APersonWithABag({
        'person': p,
        'bag': b
    })

    assert pwb.bag.items[1] == 'map'
