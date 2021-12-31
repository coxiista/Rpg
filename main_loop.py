import PublicVerification
import Player

status_player = Player.Player(p_name="", p_class="none")


def save_game():
    list_save = [status_player.p_name, status_player.p_hp, status_player.p_atk,
                 status_player.p_def]

    with open("save.txt", "w") as arquivo:
        for x in list_save:
            arquivo.writelines(str(x).lstrip() + "\n")


def load_save():
    try:
        global status_player, sucesso_load
        with open("save.txt", "r") as arquivo:
            status_player.p_name = arquivo.readline().replace("\n", "")
            status_player.p_hp = arquivo.readline().replace("\n", "")
            status_player.p_atk = arquivo.readline().replace("\n", "")
            status_player.p_def = arquivo.readline().replace("\n", "")

    except FileNotFoundError:
        print("Bem vindo jogador, qual seu nome ? ")
        player_input = input(">> ")
        status_player = Player.Player(p_name=player_input, p_class=PublicVerification.class_player.verification())
        save_game()


def play():
    acao = "null"

    while acao != "quit":
        acao = "quit"


load_save()
play()
save_game()

