from django.shortcuts import render, HttpResponse

# Create your views here.
def hello (request,nome,idade):
    return HttpResponse('<h1>Hello {} de {} anos<h1>'.format(nome,idade))

def calc (request,num1,num2):
    soma = num1 + num2
    subtracao = num1 - num2
    multiplicacao = num1 * num2
    divisao = 0
    if divisao == 0:
        if num2 == 0:
            divisao = "-"
        else:
            divisao = num1 / num2
    return HttpResponse('<h4 align="center">Os números utilizados para os seguintes cálculos foram {} e {}.</h4>'
                        '<table align="center"><caption style="font-weight: bold; font-size: 40">Resultados</caption>'
                        '<tr align="center" style="color:blue; font-weight: bold; font-size: 30"><td>Soma</td><td>Subtração</td><td>Multiplicação</td><td>Divisão</td></tr>'
                        '<tr align="center" style="font-size: 20"><td>{}</td><td>{}</td><td>{}</td><td>{}</td></tr>'
                        '</table>'.format(num1,num2,soma,subtracao,multiplicacao,int(divisao)))