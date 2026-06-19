#Crie um programa que peça uma senha ao usuário. Para ser segura, ela precisa obedecer a três regras:
# Ter pelo menos 8 caracteres.
# Ter pelo menos uma letra maiúscula.
# Ter pelo menos um número.
# Informe ao usuário se a senha dele é "Segura" ou "Insegura".
print("Sua senha deve conter ao menos 8 caracteres, uma letra maiscula e um número")
senha = input("informe a senha: ")
caracteres = list(senha)
if len(caracteres) < 8:
    estado = "insegura"
elif any(letra.isupper() for letra in senha) == False:
    estado = "insegura"
elif any(letra.isnumeric() for letra in senha) == False:
    estado = "insegura"
else:
    estado = "segura"
print(f"sua senha é {estado}")