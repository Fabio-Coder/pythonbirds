class Pessoa:
    olhos=2

    def __init__(self, *filhos, nome=None, idade=42):
        self.idade = idade
        self.nome = nome
        self.filhos = list(filhos)

    def cumprimentar(self):
        return f'Olá {id(self)}'

    @staticmethod
    def metodo_estatico():
        return 42

    @classmethod
    def nome_e_atributos_de_classe(cls):
        return f'{cls} - olhos {cls.olhos}'

class Homem(Pessoa):
    pass

if __name__ == '__main__':
    fabio = Homem(nome='Fabio')
    natalino = Pessoa(fabio, nome='Natalino', idade=69)

    print(Pessoa.cumprimentar(natalino))
    print(id(natalino))
    print(natalino.cumprimentar())
    print(natalino.nome)
    print(natalino.idade)
    for filho in natalino.filhos:
        print(filho.nome)
    natalino.sobrenome = 'Santos'
    print(natalino.sobrenome)
    del natalino.filhos
    print(natalino.__dict__)
    print(fabio.__dict__)
    print(Pessoa.olhos)
    print(fabio.olhos)
    fabio.olhos = 1
    print(id(Pessoa.olhos),id(fabio.olhos))
    print(Pessoa.metodo_estatico())
    print(Pessoa.nome_e_atributos_de_classe(),natalino.nome_e_atributos_de_classe())
    pessoa = Pessoa('Anonimo')
    print(isinstance(pessoa, Pessoa))
    print(isinstance(pessoa, Homem))
    print(isinstance(fabio, Pessoa))
    print(isinstance(fabio, Homem))