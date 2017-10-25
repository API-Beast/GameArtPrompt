
def get_all():
	d = {}
	d["vehicle"] 		= [	"siege engine", "frigatte", "air ship"]
	d["civilian"]		= [	"{creature} tamer", "hunter", "smith", "carpenter", "builder", "alchemist", "puggilist",
											"monk", "rogue", "farmer", "artist", "engineer", "diplomat", "forester", "servant", "sage"]
	d["magician"]		= [	"elementalist", "necromancer", "illusionist", "mystic", "shaman", "cultist", "summoner", "arcanist"]
	d["warrior"]		= [	"spearman", "assassin", "archer", "mounted archer", "heavy infrantryman", "scout", "javelin thrower",
											"knight", "marksman", "commander"]
	d["faction"] 		= [	"demonic", "orcish", "human", "elvish", "werewolf", "divine", "undead", "lizard", "avian", "halfling",
											"draconic", "dwarven", "naga"]
	d["race"]				= [	"succubus", "imp", "demon", "orc", "high elf", "wood elf", "dark elf", "elf", "human", "lizard", "avian",
											"halfling", "draconid", "dwarf", "naga", "harpy", "giant", "goblin", "ogre", "kobold", "werewolf", "wererat",
											"angel"]

	d["title"]      = [	"warlord", "king", "emperor", "general", "slayer"]

	d["building"]		= [	"stables", "shrine", "barracks", "archery range", "monument", "castle", "walls", "tower", "mine", "farm",
											"house"]
	d["material"]		= [	"wood", "steel", "limestone", "sandstone", "marble", "quarrystone", "vulcanic rock", "clay"]
	d["building_adjective"] = ["solid", "rough", "improvised", "magnificiant", "destroyed"]

	d["god"] 					= [	"god", "goddess", "deity", "incarnation", "legend", "avatar", "lord", "mistress", "lady"]
	d["evil_god"] 		= [	"terror of war", "unspeakable", "spider queen", "dark lord", "demon king", "{god} of death", "{god} of madness"]
	d["good_god"]			= [	"{god} of tactics", "{god} of order", "{god} of justice", 
												"{god} of fertility", "goddess of beauty", "{god} of desire"]
	d["material_god"]	= [	"{god} of harvest", "{god} of metalurgie"]
	d["mystic_god"]		= [	"worldshaper", "one god", "feathered serpent", "two-faced god", "sun {god}", "{god} of rebirth"]
	d["specific_god"] = list(set(d["evil_god"]) | set(d["good_god"]) | set(d["mystic_god"]))

	d["rideable"] 	= ["horse", "elephant", "drake", "raptor", "giant spider", "griphon", "direwolf", "unicorn"]

	d["creature_mundane"]		= ["horse", "elephant", "fox", "wolf", "boar", "bear"]
	d["creature_fantastic"] = ["drake", "raptor", "giant spider", "griphon", "direwolf", "unicorn"]
	d["creature_mystic"]		= ["sylphid", "fire elemental", "water elemental", "earth elemental", "elemental of storms", "elemental of ice"]

	d["symbolic_animal"] = ["bull", "crow", "owl", "serpent", "spider", "dragon", "tiger", "wolf", "stallion", "eagle"]
	d["symbolic_element"] = ["fire", "earth", "water", "darkness", "frost", "wind", "life", "thunder", "death"]
	d["symbolism_of"] = ["the {symbolic_animal}", "{symbolic_element}"]

	d["profession"] = list(set(d["civilian"]) | set(d["warrior"]) | set(d["magician"]))
	d["unit"]				= list(set(d["vehicle"]) | set(d["profession"]))
	d["creature"]		= list(set(d["creature_mundane"]) | set(d["creature_fantastic"]) | set(d["creature_mystic"]))

	d["plural"]			= {"succubus":"succubi", "wolf":"wolves", "fox":"foxes", "direwolf":"direwolves", "werewolf":"werewolves"}
	return d
