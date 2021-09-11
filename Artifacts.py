class Artifact:

    def __init__(self):
        self.set = ""
        self.substats = []
        self.main_stat = ""
        self.main_value = 0
        self.type = ""
        self.level = 0

    def __init(self, _set, _substats, _main_stat, _main_value, _type, _level):
        self.set = _set
        self.substats = _substats
        self.main_stat = _main_stat
        self.main_value = _main_value
        self.type = _type
        self.level = _level

    def calculate_potential(self):
        self.current_value = 0
        self.potential = 0
        return
