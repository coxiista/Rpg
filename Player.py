class Player:

    def __init__(self, p_name: str = None, p_class: str = 'none'):
        status = {'spellcaster': [500, 120, 5], 'warrior': [750, 70, 10], 'none': [300, 50, 50]}
        self.p_name = p_name
        self.p_class = p_class
        self.p_hp = status[p_class][0]
        self.p_atk = status[p_class][1]
        self.p_def = status[p_class][2]
