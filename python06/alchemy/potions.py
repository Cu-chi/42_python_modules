from . import elements


def healing_potion() -> str:
    return "Healing potion brewed with "\
           f"{elements.create_fire()} and "\
           f"{elements.create_water()}"


def strength_potion() -> str:
    return "Strength potion brewed with "\
           f"{elements.create_earth()} and "\
           f"{elements.create_fire()}"


def invisibility_potion() -> str:
    return "Invisibility potion brewed with "\
           f"{elements.create_air()} and "\
             f"{elements.create_water()}"


def wisdom_potion() -> str:
    return "Wisdom potion brewed with all elements: "\
           f"{elements.create_fire()}, "\
             f"{elements.create_water()}, "\
             f"{elements.create_earth()} and "\
             f"{elements.create_air()}"
