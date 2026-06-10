#!/usr/bin/env python3

import alchemy.grimoire

print("=== Kaboom 0 ===")
print("Using grimoire module directly")

record_spell = alchemy.grimoire.light_spellbook.light_spell_record
print(f"Testing record light spell: "
      f"{record_spell('Fantasy', 'Earth, wind and fire')}")
