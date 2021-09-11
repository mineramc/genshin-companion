class Artifact:

    def __init__(self):
        self.set = ""
        self.substats = []
        self.main_stat = ""
        self.main_value = 0.0
        self.type = ""
        self.level = 0

    def __init__(self, _set, _substats, _main_stat, _main_value, _type, _level):
        self.set = _set
        self.substats = _substats
        self.main_stat = _main_stat
        self.main_value = _main_value
        self.type = _type
        self.level = _level

    # figuring out worth? probably do all
    def calculate_base_value(self, build_type, build_types):
        if self.level < 4:
            return self.check_desirable_substats(build_type, build_types)

    def check_desirable_substats(self, build_type, build_types):
        value = 0
        for substat in self.substats:
            for i in range(len(build_types[build_type])):
                if substat in build_types[build_type][i]:
                    value += 3 - i
        return value

    def calculate_potential(self, build_types):
        potential = {"dps": self.calculate_base_value("dps", build_types) + 3 * (5 - (self.level // 4)),
                     "hp sup": self.calculate_base_value("hp sup", build_types) + 3 * (5 - (self.level // 4)),
                     "atk sup": self.calculate_base_value("atk sup", build_types) + 3 * (5 - (self.level // 4)),
                     "anemo/em": self.calculate_base_value("anemo/em", build_types) + 3 * (5 - (self.level // 4)),
                     "def": self.calculate_base_value("def", build_types) + 3 * (5 - (self.level // 4))}
        return potential



