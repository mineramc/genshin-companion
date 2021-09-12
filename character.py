class Character:

    def __init__(self):
        self.name = ""
        self.currentWeapon = ""
        self.characterType = ""
        self.constelationLevel = 0
        self.characterLevel = 0
        self.talentLevel = [0, 0, 0]
        self.ascensionLevel = 0

    def __init__(self, _name, _characterType, _currentWeapon, _constelationLevel,
                 _characterLevel, _talentLevel, _ascensionLevel):

        self.name = _name
        self.currentWeapon = _currentWeapon
        self.characterType = _characterType
        self.constelationLevel = _constelationLevel
        self.characterLevel = _characterLevel
        self.talentLevel = _talentLevel
        self.ascensionLevel = _ascensionLevel




