from tkinter import *

t = Tk()

t.mainloop()


class Carro:
    def __init__(carro, marca, ano, tipo):
        carro.marca = marca
        carro.ano = ano
        carro.tipo = tipo

    def abastecer(carro):
        print('Abastecendo o carro')

class Pessoa():
    def __init__(pess, nome, idade, Carro):
        pess.nome = nome
        pess.idade = idade
        pess.carro = Carro
        print('Chamando o construtor')

    def imprime(pess):
        print('meu nome é %s e tenho %s snos e tenho um %s'%(pess.nome, pess.idade, pess.carro.marca))

    def paraAbastecer(pess):
        pess.carro.abastecer()

carronovo = Carro('Fiesta', 2016, 'Gasolina')

Felipe = Pessoa('Felipe', 26, carronovo)
Felipe.imprime()
Felipe.paraAbastecer()

