#day21.py

class Battler:
    def __init__(self, hp, base_damage, base_armor, is_player):
        self.hp = hp
        self.base_hp = hp
        self.base_damage = base_damage
        self.base_armor = base_armor
        self.weapon_id = -1
        self.armor_id = -1
        self.ring1_id = -1
        self.ring2_id = -1
        self.is_player = is_player
    def reset(self):
        self.hp = self.base_hp
    def set_equip(self, weapon_id, armor_id, ring1_id, ring2_id):
        self.weapon_id = weapon_id
        self.armor_id = armor_id
        self.ring1_id = ring1_id
        self.ring2_id = ring2_id
    def armor(self, armors, rings):
        if not self.is_player:
            return self.base_armor
        armor = self.base_armor
        if self.armor_id >= 0 and self.armor_id < len(armors):
            armor += armors[self.armor_id]['armor']
        if self.ring1_id >= 0 and self.ring1_id < len(rings):
            armor += rings[self.ring1_id]['armor']
        if self.ring2_id >= 0 and self.ring2_id < len(rings):
            armor += rings[self.ring2_id]['armor']
        return armor
    def damage(self, weapons, rings):
        if not self.is_player:
            return self.base_damage
        damage = self.base_damage
        if self.weapon_id >= 0 and self.weapon_id < len(weapons):
            damage += weapons[self.weapon_id]['damage']
        if self.ring1_id >= 0 and self.ring1_id < len(rings):
            damage += rings[self.ring1_id]['damage']
        if self.ring2_id >= 0 and self.ring2_id < len(rings):
            damage += rings[self.ring2_id]['damage']
        return damage
    def fight(self, opponent, weapons, armors, rings):
        self_damage = self.damage(weapons, rings)
        opponent_armor = opponent.armor(armors, rings)
        damage = self_damage - opponent_armor
        if damage < 1:
            damage = 1
        opponent.hp -= damage
        if opponent.hp < 0:
            opponent.hp = 0

def battle(boss, player, weapons, armors, rings):
    boss.reset()
    player.reset()
    step = 0
    player_win = False
    while(boss.hp > 0 and player.hp > 0):
        if step % 2 == 0:
            player.fight(boss, weapons, armors, rings)
            if boss.hp == 0:
                return True
                break
        else:
            boss.fight(player, weapons, armors, rings)
            if player.hp == 0:
                return False
                break
        step += 1
    return player_win
            
def day21(infile):
    f = open(infile, 'r')
    lines = f.readlines()
    f.close()
    
    left, hp_str = lines[0].split(': ')
    left, dam_str = lines[1].split(': ')
    left, arm_str = lines[2].split(': ')
    
    boss = Battler(int(hp_str), int(dam_str), int(arm_str), False)
    player = Battler(100, 0, 0, True)
    
    weapons = []
    weapons.append({'name':'Dagger','cost':8,'damage':4,'armor':0})
    weapons.append({'name':'Shortsword','cost':10,'damage':5,'armor':0})
    weapons.append({'name':'Warhammer','cost':25,'damage':6,'armor':0})
    weapons.append({'name':'Longsword','cost':40,'damage':7,'armor':0})
    weapons.append({'name':'Greataxe','cost':74,'damage':8,'armor':0})
    
    armors = []
    armors.append({'name':'Leather','cost':13,'damage':0,'armor':1})
    armors.append({'name':'Chainmail','cost':31,'damage':0,'armor':2})
    armors.append({'name':'Splintmail','cost':53,'damage':0,'armor':3})
    armors.append({'name':'Bandedmail','cost':75,'damage':0,'armor':4})
    armors.append({'name':'Platemail','cost':102,'damage':0,'armor':5})
    
    rings = []
    rings.append({'name':'Damage +1','cost':25,'damage':1,'armor':0})
    rings.append({'name':'Damage +2','cost':50,'damage':2,'armor':0})
    rings.append({'name':'Damage +3','cost':100,'damage':3,'armor':0})
    rings.append({'name':'Defense +1','cost':20,'damage':0,'armor':1})
    rings.append({'name':'Defense +2','cost':40,'damage':0,'armor':2})
    rings.append({'name':'Defense +3','cost':80,'damage':0,'armor':3})
    
    min_gold = -1
    max_gold = -1
    for weapon in range(0, len(weapons)):
        for armor in range(-1, len(armors)):
            for ring1 in range(-1, len(rings)):
                for ring2 in range(-1, len(rings)):
                    if(ring1 >= 0 and ring2 >= 0 and ring1 == ring2):
                        continue
                    gold = weapons[weapon]['cost'] 
                    if armor >= 0:
                        gold += armors[armor]['cost']
                    if ring1 >= 0:
                        gold += rings[ring1]['cost']
                    if ring2 >= 0:
                        gold += rings[ring2]['cost']
                    player.set_equip(weapon, armor, ring1, ring2)
                    win = battle(boss, player, weapons, armors, rings)
                    if win:
                        if min_gold < 0 or gold < min_gold:
                            min_gold = gold
                    else: 
                        if max_gold < 0 or gold > max_gold:
                            max_gold = gold
    
    part1 = min_gold
    part2 = max_gold
    
    print("Part 1: %d" % (part1))
    print("Part 2: %d" % (part2))
