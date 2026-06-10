#!/usr/bin/env python3

from .dark_spellbook import dark_spell_allowed_ingredients as white_list


def validate_ingredients(ingredients: str) -> str:
    lower_input = ingredients.lower()

    for valid_spell in white_list():
        if valid_spell in lower_input:
            return f"{ingredients} VALID"

    return f"{ingredients} INVALID"
