from typing import List
from piqok.piqok import Json


class Person(Json):
    name: str
    age: int


person = {
    'name': 'Gilad',
    'age': 40
}


def test_person():
    p = Person(person)
    assert p.name == 'Gilad'
    assert p.age == 40


class Bag(Json):
    size: float
    items: List[str]


bag = {
    'size': 30.4,
    'items': ['apple', 'map']
}


def test_bag():
    b = Bag(bag)
    assert b.size == 30.4
    assert b.items[1] == 'map'


class APersonWithABag(Json):
    person: Person
    bag: Bag


def test_a_person_with_a_bag():
    pwb = APersonWithABag({
        'person': person,
        'bag': bag
    })

    assert pwb.bag.items[1] == 'map'
