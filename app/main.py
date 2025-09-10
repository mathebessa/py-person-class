class Pessoa:
    pessoas = {}

    def __init__(self, nome: str,
                 nome_da_esposa: str = None,
                 nome_do_marido: str = None) -> None:
        self.nome = nome
        Pessoa.pessoas[nome] = self

        if nome_da_esposa is not None:
            if nome_da_esposa not in Pessoa.pessoas:
                raise ValueError(
                    f"A pessoa {nome_da_esposa} não foi registrada."
                )
            self.esposa = Pessoa.pessoas[nome_da_esposa]

        if nome_do_marido is not None:
            if nome_do_marido not in Pessoa.pessoas:
                raise ValueError(
                    f"A pessoa {nome_do_marido} não foi registrada."
                )
            self.marido = Pessoa.pessoas[nome_do_marido]

    def __str__(self) -> str:
        return f"Pessoa(nome={self.nome})"


pessoa1 = Pessoa("John",
                 nome_da_esposa="Jane")
pessoa2 = Pessoa("Jane",
                 nome_do_marido="John")
pessoa3 = Pessoa("Alice")

print(pessoa1.nome)
print(pessoa1.esposa.nome)
print(pessoa2.nome)
print(pessoa2.marido.nome)

try:
    print(pessoa3.esposa)
except AttributeError as e:
    print("AttributeError:", e)
