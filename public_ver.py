from os import system


class Verification:
    text = ""
    choice = []

    def verification(self):
        while True:
            print(self.text)
            play_input = input(">> ")

            if play_input.lower() in self.choice:
                return play_input

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




