from os import system


class Verification:

    def __init__(self, text, choice):
        self.text = text
        self.choice = choice

    def verification(self):
        while True:
            print(self.text)
            for pos, val in enumerate(self.choice, start=1):
                print(f"{pos}: {val}")

            try:
                play_input = int(input(">> "))
                return self.choice[play_input - 1]

            except ValueError and IndexError:
                print("Você deve inserir um numero correspondente a um tópico")

            system("cls")
            print("Digite um valor válido!!")


def verification_tf(text):
    activate = ["yes", "sim", "ss", "s", "si", "hai", "sempre", "claro", "positivo", "óbvio", "obvio", "y"]
    negative = ["no", "não", "nao", "nunca", "jamais", "n"]
    while True:
        print(text)
        play_input = input(">> ")

        if play_input.lower in activate:
            return True

        if play_input.lower in negative:
            return False

        system("cls")
        print("Digite um valor válido!!")


class_player = Verification(text="Qual Classe Você quer ?",
                            choice=["warrior", "spellcaster"])

