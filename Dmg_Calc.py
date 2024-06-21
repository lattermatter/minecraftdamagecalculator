import math

# MOB - add mobs
mob_hp = {'Player': 20, 'Axolotl': 14, 'Bat': 6, 'Cat': 10, 'Chicken': 4, 'Cod': 3,
          'Cow': 10, 'Donkey': 30, 'Fox': 10, 'Glow Squid': 10, 'Horse': 30, 'Mooshroom': 10,
          'Mule': 30, 'Ocelot': 10, 'Parrot': 6, 'Pig': 10, 'Pufferfish': 3, 'Rabbit': 3,
          'Salmon': 3, 'Sheep': 8, 'Skeleton Horse': 15, 'Snow Golem': 4, 'Squid': 10,
          'Strider': 20, 'Tropical Fish': 3, 'Turtle': 30, 'Villager': 20, 'Wandering Trader': 20,
          'Bee': 10, 'Cave Spider': 12, 'Dolphin': 10, 'Enderman': 40, 'Goat': 10, 'Iron Golem': 100,
          'Llama': 30, 'Panda': 20, 'Weak Panda': 10, 'Piglin': 16, 'Polar Bear': 30, 'Spider': 16,
          'Trader Llama': 30, 'Wolf': 8, 'Tamed Wolf': 20, 'Zombified Piglin': 20, 'Blaze': 20,
          'Creeper': 20, 'Drowned': 20, 'Elder Guardian': 80, 'Endermite': 8, 'Evoker': 24,
          'Ghast': 10, 'Guardian': 30, 'Hoglin': 40, 'Husk': 20, 'Large Magma Cube': 16,
          'Medium Magma Cube': 4, 'Small Magma Cube': 1, 'Phantom': 20, 'Piglin Brute': 50,
          'Pillager': 24, 'Ravager': 100, 'Shulker': 30, 'Silverfish': 8, 'Skeleton': 20,
          'Large Slime': 16, 'Medium Slime': 4, 'Small Slime': 1, 'Stray': 20, 'Vex': 14,
          'Vindicator': 24, 'Witch': 26, 'Wither Skeleton': 20, 'Zoglin': 40, 'Zombie': 20,
          'Zombie Villager': 20, 'Ender Dragon': 200, 'Wither': 300, 'Giant': 100, 'Illusioner': 32,
          'Old Villager': 20, 'Old Zombie Villager': 20, 'Zombie Horse': 15
          }
mob_armorPoints = {'Zombie': 2, 'Zombified Piglin': 2, 'Zombie Villager': 2, 'Husk': 2, 'Drowned': 2,
                   'Small Magma Cube': 3,
                   'Wither': 4, 'Medium Magma Cube': 6, 'Killer Rabbit': 8, 'Large Magma Cube': 12, 'Shulker': 20}
mob = input("Enter mob attacked (Q for options, blank for player): ")


counter = 0
if mob == 'Q' or mob == 'q':
    print('Playable: ')
    for i in mob_hp:
        counter += 1
        if counter == 2:
            print('\nPassive Mobs:')
        if counter == 29:
            print('\nNeutral Mobs:')
        if counter == 45:
            print('\nHostile Mobs:')
        print(f'{counter}. {i}')
    mob = input("\nEnter mob attacked: ")

if mob == "" or mob == "Player":
    mob = "Player"
    hp = mob_hp[mob]
    armor_points = int(input("Enter the mob's armor points: "))
    armor_toughness = int(input("Enter the mob's armor toughness points (diamond adds 2 per piece, netherite adds 3 per piece): "))
elif mob in mob_hp:
    hp = mob_hp[mob]
else:
    print('Please a valid mob name.')

if mob in mob_armorPoints and armor_points == 0 and armor_toughness == 0:
    armor_points = mob_armorPoints[mob]
    armor_toughness = 0

# WEAPON
weapon_type = input('Enter weapon used (e.g. Sword, Axe, Shovel, Pickaxe, Trident): ')
weapon_material = input('Enter weapon used (e.g. Wooden, Gold, Iron, Diamond, Netherite): ')

weapon_dmg = {'Sword': {'Wooden': 4, 'Golden': 4, 'Stone': 5, 'Iron': 6, 'Diamond': 7, 'Netherite': 8},
              'Axe': {'Wooden': 7, 'Golden': 7, 'Stone': 9, 'Iron': 9, 'Diamond': 9, 'Netherite': 10},
              'Shovel': {'Wooden': 2.5, 'Golden': 2.5, 'Stone': 3.5, 'Iron': 4.5, 'Diamond': 5.5, 'Netherite': 6.5},
              'Pickaxe': {'Wooden': 2, 'Golden': 2, 'Stone': 3, 'Iron': 4, 'Diamond': 5, 'Netherite': 6}
              }
weapon_dps = {'Sword': {'Wooden': 6.4, 'Golden': 6.4, 'Stone': 8, 'Iron': 9.6, 'Diamond': 11.2, 'Netherite': 12.8},
              'Axe': {'Wooden': 5.6, 'Golden': 7, 'Stone': 7.2, 'Iron': 8.1, 'Diamond': 9, 'Netherite': 10},
              'Shovel': {'Wooden': 2.5, 'Golden': 2.5, 'Stone': 3.5, 'Iron': 4.5, 'Diamond': 5.5, 'Netherite': 6.5},
              'Pickaxe': {'Wooden': 2.4, 'Golden': 2.4, 'Stone': 3.6, 'Iron': 4.8, 'Diamond': 6, 'Netherite': 7.2}
              }

if weapon_type != 'Trident':
    dmg = weapon_dmg[weapon_type][weapon_material]
    dps = weapon_dps[weapon_type][weapon_material]
else:
    dmg = 9
    dps = 9.9

# CRITS
crit = input('Crit? ')
if crit == 'Yes' or crit == 'y' or crit == 'yes' or crit == 'Y':
    crit_Bool = 'with crits'
    dmg = dmg * 1.5
    dps = round(dps * 1.5, 2)
else:
    crit_Bool = 'without crits'

# ARMOR POINTS
dmg = dmg * (1 - (min(20, max(armor_points / 5, armor_points - (4 * dmg / (armor_toughness + 8)))) / 25))

# FINAL VARIABLES
dmg = round(dmg, 2)
hits = math.ceil(hp / dmg)
total_dmg = hits * dmg

print(
    f'''To get a(n) {mob} ({hp} HP) with a(n) {weapon_material} {weapon_type} {crit_Bool},
with {armor_points} defense points and {armor_toughness} toughness points, 
it would take {hits} hits.
Each hit would do {dmg} damage, amounting to {round(total_dmg, 2)} total damage.
The total damage done would be {round(total_dmg - hp, 2)} more than the mob's HP ({hp}) It would take at least {total_dmg/dps} seconds to finish.
''')
