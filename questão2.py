def fibonacci(numero):
    v1 = 0
    v2 = 1
    proximo = 0

    while proximo < numero:
        proximo = v1 + v2
        v1 = v2
        v2 = proximo

    if abs(proximo - numero) < abs(v1 - numero):
        return (
            f"O número {numero} não pertence à sequência de Fibonacci. "
            f"O valor mais próximo do número informado que pertence a sequencia é {proximo}."
        )
    else:
        return (
            f"O número {numero} não pertence à sequência de Fibonacci. "
            f"O valor mais próximo do número informado que pertence a sequencia é {v1}."
        )

numero = int(input("Informe um número para verificar se ele pertence à sequência de Fibonacci:"))
mensagem = fibonacci(numero)
print(mensagem)
