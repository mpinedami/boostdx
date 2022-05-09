from factory import Faker, SubFactory
from factory.django import DjangoModelFactory

from polls.models import Choice, Question


class QuestionFactory(DjangoModelFactory):
    class Meta:
        model = Question

    question_text = Faker("lorem")


class ChoiceFactory(DjangoModelFactory):
    class Meta:
        model = Choice

    question = SubFactory(QuestionFactory)
    choice_text = Faker("lorem")
    votes = 5
