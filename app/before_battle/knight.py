class Knight:
    def __init__(self, name: str, power: int, hp: int, **kwargs) -> None:
        self.name = name
        self.hp = hp
        self.power = power
        self.ammunition = kwargs
        self.apply_ammunition()

    def apply_ammunition(self) -> None:
        self.potion_of_knight()
        self.armor_of_knight()
        self.weapon_of_knight()

    def weapon_of_knight(self) -> None:
        if self.ammunition["weapon"]:
            self.power += self.ammunition["weapon"]["power"]

    def potion_of_knight(self) -> None:
        if self.ammunition["potion"]:
            for item in self.ammunition["potion"]["effect"]:
                if item == "power":
                    self.power += self.ammunition["potion"]["effect"][item]
                if item == "hp":
                    self.hp += self.ammunition["potion"]["effect"][item]
                if item == "protection":
                    self.hp += self.ammunition["potion"]["effect"][item]

    def armor_of_knight(self) -> None:
        if self.ammunition["armour"]:
            for arm in self.ammunition["armour"]:
                self.hp += arm["protection"]
