name = "ada lovelace"
print(name.title())
print(name.upper())
print(name.lower())

# concatenando strings
first_name = "ada"
last_name = "lovelace"
full_name = first_name + " " + last_name
print("Hello, " + full_name.title() + "!")

# Tabulacao e quebra de linha
print("Linguagens de programacao: \n\tPython\n\tJava")

# Remocao de espacos em branco
favorite_language = "Python "
# remocao de espco em branco a direta temporario
print(favorite_language.rstrip())

favorite_language = "Python "
# remocao de espco em branco a direta permanente
favorite_language = favorite_language.rstrip()
print(favorite_language)

other_language = " Java "
other_language.rstrip()  # remocao a direita
other_language.lstrip()  # remocao a esquerda
other_language.strip()  # remocao no inicio e fim
