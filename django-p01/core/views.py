from django.shortcuts import render, HttpResponse

# Create your views here.

def hello(request, nome, idade):
    return HttpResponse('<h1>Hello {} de {} anos</h1>'.format(nome,idade))

def math(request, num1, num2):
    divisao = 0
    if num2 == 0:
        divisao = '-'
    else:
        divisao = num1/num2
    return HttpResponse('<center><table><tr style="text-align: center; font-weight: bold"><td>Número 1</td><td>Número 2</td><td>Soma</td><td>Subtração</td><td>Multiplicação</td><td>Divisão</td></tr><tr style="text-align: center;"><td>{}</td><td>{}</td><td>{}</td><td>{}</td><td>{}</td><td>{}</td></tr></table></center>'.format(num1,num2,num1+num2, num1-num2, num1*num2, divisao))
