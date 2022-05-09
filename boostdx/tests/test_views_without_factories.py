from django.test import TestCase

from polls.models import Choice, Question


class ChoiceDetailTest(TestCase):
    def test_success(self):
        question = Question.objects.create(question_text="Hola weee")
        choice = Choice.objects.create(
            question=question, choice_text="Adios weee", votes=3
        )

        response = self.client.get(f"/choice/{choice.id}/")

        self.assertContains(response, choice.choice_text, choice.votes)
        self.assertContains(
            response,
            choice.question.question_text,
        )
