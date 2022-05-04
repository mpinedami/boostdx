from django.http import HttpResponse, JsonResponse
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
    message = "You're looking at the results of question."
    question = Question.objects.filter(id=question_id).values("question_text").first()
    return JsonResponse({"message": message, "question": question})


def vote(request, question_id):
    return HttpResponse("You're voting on question %s." % question_id)
