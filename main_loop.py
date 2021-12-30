def save_game(name: str, hp: int, atk: int, df: int):
    list_save = [name, hp, atk, df]
    with open("save.txt", "w") as arquivo:
        for x in list_save:
            arquivo.writelines(str(x) + "\n")


def load_save():
    global player_name, player_hp, player_atk, player_df
    with open("save.txt", "r") as arquivo:
        player_name = arquivo.readline()
        player_hp = arquivo.readline()
        player_atk = arquivo.readline()
        player_df = arquivo.readline()


player_name = "null"
player_hp = 0
player_atk = 0
player_df = 0


def play():
    acao = "null"
    new_save = False

    try:
        with open("save.txt", "r") as arquivo:
            pass

    except FileNotFoundError:
        with open("save.txt", "w") as arquivo:
            new_save = True
            arquivo.close()

    while acao != "quit":
        if new_save:
            print("Bem vindo jogador, qual seu nome ? ")
            player_name = input(">> ")
            save_game(player_name, 12, 15, 30)
            acao = "quit"

        acao = "quit"


play()

load_save()
print(player_atk)
