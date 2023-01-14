def string_reversa(string):
    string_reversa = ""
    # Iteração
    for i in range(len(string)-1, -1, -1):
        string_reversa += string[i]
    return string_reversa

string = input("Digite uma frase: ")

print(string_reversa(string))
