from django.http import HttpResponse

"""from django.http import JsonResponse"""
from django.utils.html import format_html

from .models import Question


def index(request):
    html = """
    <body>
        <p>Hello, world. You're at the polls index.</p>
    </body>
    """
    return HttpResponse(html)


def detail(request, question_id):
    question = Question.objects.filter(id=question_id).values("question_text").first()
    html = """
    <body>
        <h1>Hello, world. You're at the polls index.</h1>
    """
    html += f"""
        {question['question_text']}
    </body>
    """
    return HttpResponse(html)


def results(request, question_id):

    """Results the given question_id
    message = "Probrando funcion format_html junto con blackend-docs"
    question_id = (Question.objects.filter(
        id=question_id).values("question_text").first())
    format_html("<body><h1>{}</h1><br><p1>{}</p1></body>",
        message, question_id['question_text'])

        Args:
            request (request): The request _description_
            question_id (int): The id of the question _description_

        Returns:
            html: Retorna un html para ser renderizado
    """
    # message = "You're looking at the results of question."
    # question = Question.objects.filter(
    # id=question_id).values("question_text").first()
    # return JsonResponse({"message": message, "question": question})
    message = "Probrando funcion format_html junto con blackend-docs"
    question_id = (
        Question.objects.filter(id=question_id).values("question_text").first()
    )
    return HttpResponse(
        format_html(
            "<body><h1>{}</h1><br><p1>{}</p1></body>",
            message,
            question_id["question_text"],
        )
    )


def vote(request, question_id):

    return HttpResponse("You're voting on question %s." % question_id)
