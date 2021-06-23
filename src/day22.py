#day22.py

import copy

class Battler:
    def __init__(self, hp, mp, base_damage, is_player):
        self.hp = hp
        self.base_hp = hp
        self.mp = mp
        self.base_mp = mp
        self.base_damage = base_damage
        self.shield_armor = 0
        self.is_player = is_player
        self.status_effects_shield = 0
        self.status_effects_poison = 0
        self.status_effects_recharge = 0
        self.mp_counter = 0
    def reset(self):
        self.hp = self.base_hp
        self.mp = self.base_mp
        self.shield_armor = 0
        self.status_effects_shield = 0
        self.status_effects_poison = 0
        self.status_effects_recharge = 0
    def damage(self):
        return self.base_damage
    def armor(self):
        return self.shield_armor
    def fight(self, opponent):
        self_damage = self.damage() - opponent.armor()
        opponent.hp -= damage
        if opponent.hp < 0:
            opponent.hp = 0
    # note that status effects can be cast when the timer is 1 or lower
    def can_cast(self, opponent, spell):
        if spell == "Magic Missile":
            if self.mp < 53:
                return False
        elif spell == "Drain":
            if self.mp < 73:
                return False
        elif spell == "Shield":
            if self.status_effects_shield > 1:
                return False
            elif self.mp < 113:
                return False
        elif spell == "Poison":
            if opponent.status_effects_poison > 1:
                return False
            elif self.mp < 173:
                return False
        elif spell == "Recharge":
            if self.status_effects_recharge > 1:
                return False
            elif self.mp < 229:
                return False
        return True
    def apply_status(self, verbose):
        if self.status_effects_shield > 0:
            self.status_effects_shield -= 1
            self.shield_armor = 7
            if verbose:
                print("Shield's timer is now %d." % (self.status_effects_shield))
            if self.status_effects_shield == 0:
                self.shield_armor = 0
                if verbose:
                    print("Shield wears off, decreasing armor by 7.")
        if self.status_effects_poison > 0:
            self.status_effects_poison -= 1
            self.hp -= 3
            if self.hp < 0:
                self.hp = 0
            if verbose:
                print("Poison deals 3 damage. Its timer is now %d." % (self.status_effects_poison))
        elif self.status_effects_recharge > 0:
            self.status_effects_recharge -= 1
            self.mp += 101
            if verbose:
                print("Recharge provides 101 mana. Its timer is now %d." % (self.status_effects_recharge))
                
    def cast(self, opponent, spell, verbose, hard_mode = False):
        if verbose:
            print("-- Player turn --\n- Player has %d hit points, %d armor, %d mana\n- Boss has %d hit points" % (self.hp, self.armor(), self.mp, opponent.hp))
        if hard_mode:
            self.hp -= 1
            if self.hp < 0:
                self.hp =0
            if self.hp == 0:
                return
        self.apply_status(verbose)
        opponent.apply_status(verbose)
        if opponent.hp == 0 or self.hp == 0:
            if verbose:
                print("The fight is over")
            return
            
        if spell == "Magic Missile":
            self.mp -= 53
            self.mp_counter += 53
            opponent.hp -= 4
            if opponent.hp < 0:
                opponent.hp = 0
            if verbose:
                print("Player casts Magic Missile, dealing 4 damage.")
        elif spell == "Drain":
            self.mp -= 73
            self.mp_counter += 73
            opponent.hp -= 2
            self.hp += 2
            if opponent.hp < 0:
                opponent.hp = 0
            if verbose:
                print("Player casts Drain, dealing 2 damage, and healing 2 hit points.")
        elif spell == "Shield":
            self.mp -= 113
            self.mp_counter += 113
            self.status_effects_shield = 6
            self.shield_armor = 7
            if verbose:
                print("Player casts Shield, increasing armor by 7.")
        elif spell == "Poison":
            self.mp -= 173
            self.mp_counter += 173
            opponent.status_effects_poison = 6
            if verbose:
                print("Player casts Poison.")
        elif spell == "Recharge":
            self.mp -= 229
            self.mp_counter += 229
            self.status_effects_recharge = 5
            if verbose:
                print("Player casts Recharge.")
        if opponent.hp < 0:
            opponent.hp = 0
            
    def fight(self, opponent, verbose, hard_mode = False):
        if verbose:
            print("-- Boss turn --\n- Player has %d hit points, %d armor, %d mana\n- Boss has %d hit points" % (opponent.hp, opponent.armor(), opponent.mp, self.hp))
        
        self.apply_status(verbose)
        opponent.apply_status(verbose)
        if opponent.hp == 0 or self.hp == 0:
            if verbose:
                print("The fight is over")
            return
        damage = self.damage() - opponent.armor()
        if damage < 1:
            damage = 1
        opponent.hp -= damage
        if opponent.hp < 0:
            opponent.hp = 0
        if verbose:
            print("Boss attacks for %d damage!" % damage)
    
def battle_across_the_multiverse(player, boss, spell, depth, hard_mode):
    # loose heuristic as cutoff for search
    cutoff = 1.05*(boss.base_hp/4) 
    if depth > cutoff:
        return -1
    spells = ["Magic Missile", "Drain", "Shield", "Poison", "Recharge"]
    player.cast(boss, spell, False, hard_mode)
    if player.hp == 0:
        return -1
    if boss.hp == 0:
        return player.mp_counter
    boss.fight(player, False, hard_mode)
    if player.hp == 0:
        return -1
    if boss.hp == 0:
        return player.mp_counter   
    can_cast = False
    min_mp = -1
    for spell in spells:
        if player.can_cast(boss, spell):
            can_cast = True
            new_player = copy.copy(player)
            new_boss = copy.copy(boss)
            result = battle_across_the_multiverse(new_player, new_boss, spell, depth + 1, hard_mode)
            if result > 0 and (result < min_mp or min_mp == -1):
                min_mp = result
    #player loses
    if not can_cast:
        return -1
    return min_mp
            
def day22(infile):
    f = open(infile, 'r')
    lines = f.readlines()
    f.close()
    
    left, hp_str = lines[0].split(': ')
    left, dam_str = lines[1].split(': ')
    
    boss = Battler(int(hp_str), 0, int(dam_str), False)
    player = Battler(50, 500, 0, True)
    
    verbose = False

    min_mp = -1
    spells = ["Magic Missile", "Drain", "Shield", "Poison", "Recharge"]
    #poison needs to be used at some point, and we don't care about spell order for the answer.
    #starting with it removes one combinatorial layer
    part1 = battle_across_the_multiverse(player, boss, "Poison" ,0, False) #min_mp
    player.reset()
    boss.reset()
    part2 = battle_across_the_multiverse(player, boss, "Poison" ,0, True)
    
    print("Part 1: %d" % (part1))
    print("Part 2: %d" % (part2))
    
    