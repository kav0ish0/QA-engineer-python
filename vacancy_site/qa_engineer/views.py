from django.shortcuts import render
from vacancies.vacancies import get_yesterday_vacancies
from .models import Post


def get_content(name: str):
    content = {
        'content': Post.objects.filter(title=name).first(),
        'title': name
    }
    return content


def home(request):
    content = get_content('Главная')
    return render(request, 'qa_engineer/index.html', content)


def geography(request):
    content = get_content('География')
    return render(request, 'qa_engineer/index.html', content)


def demand(request):
    content = get_content('Востребованность')
    return render(request, 'qa_engineer/index.html', content)


def recent_vacancies(request):
    vacancies = get_yesterday_vacancies()
    context = {
        'vacancies': vacancies
    }
    return render(request, "qa_engineer/recent-vacancies.html", context)


def skills(request):
    content = get_content('Навыки')
    return render(request, 'qa_engineer/index.html', content)
