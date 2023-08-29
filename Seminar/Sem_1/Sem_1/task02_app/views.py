from django.shortcuts import render
from random import randint
from django.http import HttpResponse
import logging

def text(title, result):
    return f'<h1>{title}</h1>'\
        f'<p> Результат: {result}</p>'

logger = logging.getLogger(__name__)


def coin(request):
    title = 'Бросок монеты'
    temp = randint(1, 2)
    if temp == 1:
        result = 'Решка'
    else:
        result = 'Орел'
    logger.info(f'Результат - {result}')
    return HttpResponse(text(title, result))

def cube(request):
    title = 'Бросок кубика'
    result = randint(1,6)
    logger.info(f'Результат - {result}')
    return HttpResponse(text(title, result)) 

def rand100(request):
    title = 'Случайное число'
    result = randint(1, 100)
    logger.info(f'Результат - {result}')
    return HttpResponse(text(title, result))
