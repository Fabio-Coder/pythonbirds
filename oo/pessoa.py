class Pessoa:
    def __init__(self, *filhos, nome=None, idade=42):
        self.idade = idade
        self.nome = nome
        self.filhos = list(filhos)

    def cumprimentar(self):
        return f'Olá {id(self)}'


if __name__ == '__main__':
    fabio = Pessoa(nome='Fabio')
    natalino = Pessoa(fabio, nome='Natalino', idade=69)

    print(Pessoa.cumprimentar(natalino))
    print(id(natalino))
    print(natalino.cumprimentar())
    print(natalino.nome)
    print(natalino.idade)
    for filho in natalino.filhos:
        print(filho.nome)
