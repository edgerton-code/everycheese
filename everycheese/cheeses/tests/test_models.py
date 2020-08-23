import pytest

#connects our tests with our database
pytestmark = pytest.mark.django_db

from ..models import Cheese
from everycheese.cheeses.tests.factories import CheeseFactory

def test__str__():
    cheese = Cheese.objects.create(
        name = "Stracchino",
        description = "Semi-sweet cheese that goes well with starches.",
        firmness = Cheese.Firmness.SOFT,
    )
    assert cheese.__str__() == "Stracchino"
    assert str(cheese) == "Stracchino"

def test_get_absolute_url():
    cheese = CheeseFactory()
    url = cheese.get_absolute_url()
    assert url == f'/cheeses/{cheese.slug}/'