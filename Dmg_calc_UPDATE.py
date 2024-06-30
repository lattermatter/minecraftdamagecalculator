if True:
    import math
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
    armor_protection_list = [{"l": 1, "g": 2, "c": 2, "i": 2, "d": 3, "n": 3}, {"l": 3, "g": 5, "c": 5, "i": 6, "d": 8, "n": 8}, 
                        {"l": 2, "g": 3, "c": 4, "i": 5, "d": 6, "n": 6}, {"l": 1, "g": 1, "c": 1, "i": 2, "d": 3, "n": 3}]
    armor_toughness_list = [{"l": 0, "g": 0, "c": 0, "i": 0, "d": 2, "n": 3}, {"l": 0, "g": 0, "c": 0, "i": 0, "d": 2, "n": 3}, 
                        {"l": 0, "g": 0, "c": 0, "i": 0, "d": 2, "n": 3}, {"l": 0, "g": 0, "c": 0, "i": 0, "d": 2, "n": 3}]
    letter_map_weapon = {'s': "Sword", "a": "Axe", "h": "Shovel", "p": "Pickaxe"}
    letter_map_material = {"w": "Wooden", "g": "Golden", "s": "Stone", "i": "Iron", "d": "Diamond", "n": "Netherite"}
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
    def process_armor_string(armorstring):
        armor_info_list = armorstring.split()
        armor_info_list = [(piece[0], int(piece[1])) for piece in armor_info_list]
        return armor_info_list


def run(arg):
    mob = arg

    counter = 0
    if mob == 'Q' or mob == 'q':
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
        # armor_points = int(input("Enter the mob's armor points: "))
        # armor_toughness = int(input("Enter the mob's armor toughness points (diamond adds 2 per piece, netherite adds 3 per piece): "))
        armor_info = input("Input a separated list for the armor, na for no armor. Press Q for help. ")
        # print(processed_armor_info)
        
        armor_points = 0
        armor_toughness = 0
        net_prot = 0
        # determine armor_points from dict
        if armor_info != "na":
            processed_armor_info = process_armor_string(armor_info)
            for count, piece in enumerate(processed_armor_info):
                armor_points += armor_protection_list[count][piece[0]]
                armor_toughness += armor_toughness_list[count][piece[0]]
                net_prot += piece[1]
        
        if armor_info == "Q":
            armor_info = input("""Input a separated list for the armor. 
    Write in order: helmet, chestplate, leggings, boots.
    Leather -> l, Gold -> g, Chainmail -> c, Iron -> i, Diamond -> d, Netherite -> n
    Example: i1 i0 d2 n4 
    means prot 1 iron helmet, no prot iron chestplate, prot 2 diamond leggins, prot 4 netherite boots 
    type na for no armor
    Enter here -> """)
            
    elif mob in mob_hp and mob != "Player":
        hp = mob_hp[mob]
        armor_points = 0
        if mob in mob_armorPoints:
            armor_points = mob_armorPoints[mob]
        armor_toughness = 0
        net_prot = 0
    else:
        print('Please a valid mob name.')


    weapon_inp = input("Enter weapon: 'wh0n' wood shovel sharp 0 no crit, 'na5c' netherite axe sharp 5 with crit, Trident for trident, na for fist: ")
    x = weapon_inp
    weapon = [char for char in x]

    if weapon_inp != 'Trident' and weapon_inp != 'na':
        dmg_nosharp_nocrit = weapon_dmg[letter_map_weapon[weapon[1]]][letter_map_material[weapon[0]]] 
        dmg_nocrit = dmg_nosharp_nocrit
        if int(weapon[2]) > 0:
            dmg_nocrit = dmg_nosharp_nocrit + 0.5 * int(weapon[2]) + 0.5
        dmg = dmg_nocrit * 1.5 if weapon[3] == "c" else dmg_nosharp_nocrit
        
        dps = weapon_dmg[letter_map_weapon[weapon[1]]][letter_map_material[weapon[0]]]
        dps = round(dps * 1.5, 2) if weapon[3] == "c" else dps
    elif weapon_inp == "na":
        dps = 2
        dmg = 1
        dmg_nosharp_nocrit = 1
        dmg_nocrit = 1
        weapon = ["w", "s", -8, "without crits"]
    else:
        dmg = 9
        dps = 9.9

    # CRITS
    crit_Bool = "with crits" if weapon[3] == "c" else "without crits"

    # ARMOR POINTS
    dmg_partial = dmg * (1 - (min(20, max(armor_points / 5, armor_points - (4 * dmg / (armor_toughness + 8)))) / 25))
    dmg_per_hit = dmg_partial * (1 - 4 * net_prot * 0.01)
    
    # FINAL VARIABLES
    hits = math.ceil(hp / dmg_per_hit)
    total_dmg_dealt = hits * dmg
    total_dmg_actual = hits * dmg_per_hit
    total_dmg_before_prot = hits * dmg_partial

    

    print(
        f'''{mob}: {hp} | {letter_map_material[weapon[0]] if weapon_inp != "na" else "na"} {letter_map_weapon[weapon[1]] if weapon_inp != "na" else "na"} sharpness {weapon[2] if weapon_inp != "na" else "na"} {crit_Bool}
    {round(hits, 6)} hits | {round(total_dmg_actual/hits, 6)} dmg per hit | {round(total_dmg_dealt)} dmg dealt | {round(total_dmg_before_prot, 6)} dmg before prot | {round(total_dmg_actual, 6)} total damage
    armor {round(1-(total_dmg_before_prot/total_dmg_dealt), 6) * 100}% reduction | prot {4 * net_prot}% reduction
    {round(total_dmg_actual - hp, 6)} extra dmg over HP | {round(hp - (total_dmg_actual- dmg_per_hit), 6)} min dmg final hit | {round(hits * dmg_nosharp_nocrit/dps, 6)} seconds to finish.
    ''')
    

while True:
    first_inp = input("Enter mob attacked (Q for options, blank for player, K for break): ")
    if first_inp == "K":
        break
    run(first_inp)

    
