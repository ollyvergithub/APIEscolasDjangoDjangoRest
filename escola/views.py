from django.http import JsonResponse
from django.shortcuts import render


def alunos(request):
    if request.method == 'GET':
        alunos = {'id': 1, 'nome': 'Ollyver'}
        return JsonResponse(alunos)

