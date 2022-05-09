from django.contrib.sites.models import Site
from django.core.management.base import BaseCommand, CommandError
from django.db import transaction

from polls.models import Choice, Question


class Command(BaseCommand):
    """_summary_

    Args:
        BaseCommand (_type_): _description_

    Raises:
        CommandError: _description_
    """

    help = "Seed database with sample data"

    @transaction.atomic
    def handle(self, *args, **options):
        if Question.objects.exists():
            raise CommandError(
                "This command cannot be run when any questions exist, to guard"
                + " against accidental use on production."
            )

        self.stdout.write("Seeding database...")

        update_site()

        create_question_and_choice()

        self.stdout.write("Done.")


def update_site():
    """
    Actualiza el dominio del sitio
    """
    domain = "localhost:8000"
    Site.objects.filter(domain="example.com").update(domain=domain, name=domain)


def create_question_and_choice():
    """
    Create two Question objects and two Choice Objects too
    """

    def make_choice(question, choice_text, votes):
        Choice.objects.bulk_create(
            [Choice(question=question, choice_text=choice_text, votes=votes)]
        )

    question1 = Question.objects.create(question_text="Hola, que hace?")

    make_choice(question1, "Eleccion mia, por hola que hace", 4)

    question2 = Question.objects.create(question_text="Que pepes?")

    make_choice(question2, "Eleccion mia, por que pepes", 6)
