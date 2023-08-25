import os
import random
import string

def generate_password(length=16):
    # Gera uma sequência de números aleatórios
    password = ''.join(str(random.randint(0, 9)) for _ in range(length))
    return password

# Verifica se o arquivo de senhas existe, caso contrário, cria um novo arquivo
if not os.path.exists("senhas.txt"):
    with open("senhas.txt", "w") as file:
        file.write("=== Senhas Geradas ===\n\n")

while True:
    print("\n=== Gerador de Senha ===")
    print("1. Gerar nova senha")
    print("2. Sair")
    choice = input("Digite sua escolha: ")

    if choice == "2":
        break

    elif choice == "1":
        # Solicita informações sobre a finalidade e login
        finalidade = input("\nDigite a finalidade da senha ou plataforma: ")
        login = input("Digite o login cadastrado para essa senha (email, cpf, nome, etc): ")
        password_length = int(input("Digite o comprimento desejado para a senha: "))

        # Gera a senha composta apenas por números
        password = generate_password(password_length)
        print("Sua senha gerada é:", password)

        # Salva a senha no arquivo "senhas.txt"
        with open("senhas.txt", "a") as file:
            file.write(f"Finalidade: {finalidade}\n")
            file.write(f"Login: {login}\n")
            file.write(f"Senha: {password}\n\n")

        print("Senha salva em senhas.txt!")

    else:
        print("\nOpção inválida!")

print("\nAté mais!")




