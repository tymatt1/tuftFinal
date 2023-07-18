import os
import string
import pygame as pg


path = os.path.dirname(os.path.abspath(__file__))  # need to add the path or it won't run when double clicked
def load(name: string) -> pg.Surface:
    return pg.image.load(f"{path}/{name}.png")

class Character:
    def __init__(self, name: string):
        self.stillLeft: pg.Surface = load(f"character/{name}StillLeft")
        self.stillRight: pg.Surface = load(f"character/{name}StillRight")


# characters
zach = Character("Zach")
anime = Character("Anime")
matthew = Character("Matthew")
alex = Character("Alex")
duy = Character("Duy")

# backgrounds
diningHall = load("backgrounds/diningHall/dininghall")
bedroom = load("backgrounds/bedroom")
sixFlags = load("backgrounds/Six Flags")
classroom = load("backgrounds/classroom")
vanFight = load("backgrounds/VanFight")

# misc
icon = load("misc/icon")
testImg = load("misc/phrog")
whiteVan = load("misc/White Van")
sword = load("misc/Sword")
waterGun = load("misc/WaterGun")
sus = load("misc/ඩ")