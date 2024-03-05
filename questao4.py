def inverte_string(string):
    if len(string) > 0:
        if len(string) % 2 == 0:
            cabeca = len(string) // 2
            nova_string = ""
            for c in range(0, cabeca):
                nova_string += string[len(string) - c - 1]
            for c in range(cabeca, len(string)):
                nova_string += string[cabeca - (c - cabeca) - 1]
            return nova_string
        else:
            nova_string = ""
            for i in range(len(string)):
                nova_string += string[len(string) - i - 1]
            return nova_string
    else:
        return "Nenhum valor encontrado na string"


string = input("Digite uma string para ser invertida: ")
resultado = inverte_string(string)
print(resultado)
