class Battle:
    def __init__(self, player_1: object = None, player_2: object = None):
        self.player_1 = player_1
        self.player_2 = player_2

    def player_1_atk_2(self):
        self.player_2.p_hp = (self.player_2.p_hp - self.player_1.p_atk) + self.player_2.p_def

    def player_2_atk_1(self):
        self.player_1.p_hp = (self.player_1.p_hp - self.player_2.p_atk) + self.player_1.p_def
