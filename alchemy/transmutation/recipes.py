#!/usr/bin/env python3

import elements
from .. import elements as alchemy_elements
from .. import potions


def lead_to_gold() -> str:
    air = alchemy_elements.create_air()
    strength = potions.strength_potion()
    fire = elements.create_fire()

    return f"Recipe transmuting Lead to Gold: brew '{air}' and '{strength}' mixed with '{fire}'"
