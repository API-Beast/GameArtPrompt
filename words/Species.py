def write_to(d):
	d["profession"] = {}
	d["profession"]["civilian"]  = ["Lumberjack", "Farmer", "Alchemist", "Smith", "Engineer"]
	d["profession"]["ranged"]    = ["Ranger", "Marksman", "Bowman", "Javelin Thrower"]
	d["profession"]["melee"]     = ["Berserker", "Militia", "City Guard", "Hoplite", "Spearman", "Paladin", "Swordsman", "Pikeman", "Knight", "Juggernaut"]
	d["profession"]["sneaky"]    = ["Rogue", "Assassin", "Ranger", "Scout", "Hunter"]
	d["profession"]["noble"]     = [["King", "Queen"], ["Prince", "Princess"], "Noble"]
	d["profession"]["command"]   = ["Commander", "General"]
	d["profession"]["twisted"]   = ["Warlord", "Infiltrator", "Assassin", "Torturer", "Executioner", "Mistress", "Raider", "Slaver", "Warlock", "Necromancer", "Cultist"]
	d["profession"]["primitive"] = ["Berserker", "Shaman", "Druid", "Beastmaster", "Chieftain", "Summoner"]
	d["profession"]["arcane"]    = ["Arcanist", "Enchanter", "Illusionist", "Elementalist", "Runesmith", "Summoner", "Conjurer"]
	d["profession"]["rightous"]  = ["Cleric", "Priest", "Paladin", "Knight", "Preacher"]

	d["species"] = {}
	d["species"]["special"] 	= ["Avian", "Celestial", "Draconic", "Sylvan", "Lizard", "Merman", "Demonic", "Demon", "Succubus", "Naga"]
	d["species"]["twisted"]		= ["Demonic", "Demon", "Lizard", "Demonic", "Succubus", "Orc", "Beastman", "Dark Elf", "Human"]
	d["species"]["muscular"] 	= ["Orc", "Beastman", "Half-Orc", "Draconic", "Human", "Dwarf", "Demon", "Demonic", "Lizard", "Naga"]
	d["species"]["dextrous"]  = ["Elf", "Human", "Dark Elf", "Wood Elf", "Lizard", "Halfling", "Demonic", "Succubus"]
	d["species"]["noble"]     = ["Avian", "Celestial", "Lizard", "Naga", "Elf", "Dark Elf", "Human", "Dwarf"]
	d["species"]["smart"]     = ["Dwarf", "Human", "Celestial", "Lizard", "Demon", "Succubus", "Elf", "Dark Elf", "Gnome", "Halfling"]
	#d["species"]["big"]				= ["Giant", "Ogre", "Troll"]
	d["species"]["small"] 		= ["Goblin", "Gnome", "Dwarf", "Kobold", "Halfling"]
	d["species"]["sneaky"]    = ["Goblin", "Halfling","Half-Elf", "Elf", "Dark Elf"]
	d["species"]["primitive"] = ["Goblin", "Ogre", "Troll", "Orc", "Beastman", "Wood Elf", "Sylvan", "Lizard"]
	d["species"]["rightous"]  = ["Human", "Celestial", "Beastman", "Dwarf", "Halfling", "Elf"]
	return d
