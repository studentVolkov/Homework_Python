class Address:
    index = "592308"
    town = "Tomsk"
    street = "Dobrai"
    home = "1"
    kvartira = "33"

    def __init__(self, index, town, street, home, kvartira):
        self.index = index
        self.town = town
        self.street = street
        self.home = home
        self.kvartira = kvartira

    def __str__(self):
        return (f"{self.index}, {self.town}, {self.street}, {self.home}"
                "- {self.kvartira}")
