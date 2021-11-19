import pymongo
from config import *

client = pymongo.MongoClient(MONGO_URL)
db = client[MONGO_DB]
template_words = db["TEMPLATE_WORDS"]

primary_words = ["a", "about", "afraid", "after", "afternoon", "again", "all", "also", "always", "and", "angry", "animal", "answer", "any", "apple", "arm", "art", "ask", "at", "aunt", "autumn", "baby", "back", "bad", "bag", "ball", "banana", "basketball", "be", "bear", "beautiful", "bed", "before", "begin", "behind", "beside", "between", "big", "bike", "bird", "birthday", "black", "blackboard", "blue", "boat", "body", "book", "box", "boy", "bread", "breakfast", "bring", "brother", "brown", "bus", "busy", "but", "buy", "by", "cake", "call", "can", "candy", "cap", "car", "card", "cat", "chair", "chicken", "child", "children", "China", "Chinese", "cinema", "city", "class", "clean", "clever", "clock", "close", "clothes", "cloudy", "coat", "cold", "colour", "come", "computer", "cook", "cool", "cousin", "cow", "crayon", "cry", "dad", "dance", "day", "dear", "desk", "difficult", "dinner", "dirty", "do", "doctor", "dog", "door", "down", "draw", "dress", "drink", "driver", "duck", "ear", "early", "easy", "eat", "egg", "elephant", "email", "English", "evening", "every", "exercise", "eye", "face", "family", "fan", "far", "farm", "farmer", "fast", "father", "favourite", "feel", "film", "find", "fine", "fish", "floor", "flower", "fly", "food", "foot", "football", "for", "friend", "from", "fruit", "game", "get", "girl", "give", "go", "good", "goodbye", "grandfather", "grandmother", "grass", "great", "green", "hair", "half", "hand", "happy", "have", "he", "head", "healthy", "hear", "heavy", "hello", "help", "her", "here", "hi", "high", "him", "his", "holiday", "home", "horse", "hospital", "hot", "hour", "house", "how", "hungry", "I", "ice-cream", "idea", "ill", "in", "interesting", "it", "its", "juice", "jump", "kid", "kind", "kitchen", "kite", "know", "lake", "late", "left", "leg", "lesson", "let", "library", "light", "like", "listen", "llittle", "live", "long", "look", "love", "lunch", "make", "man", "many", "map", "maths", "me", "meet", "milk", "minute", "Miss", "monkey", "month", "moon", "morning", "mother", "mouth", "Mr", "Mrs", "Ms", "much", "mum", "music", "my", "name", "near", "new", "next", "nice", "night", "no", "noodle", "nose", "not", "now", "nurse", "of", "often", "old", "on", "open", "or", "orange", "our", "panda", "parent", "park", "party", "PE", "pen", "pencil", "people", "photo", "picture", "pig", "place", "plane", "plant", "play", "playground", "please", "police", "potato", "pupil", "put", "rain", "read", "red", "rice", "right", "river", "room", "ruler", "run", "sad", "say", "school", "schoolbag", "science", "season", "see", "she", "sheep", "ship", "shirt", "shoe", "shop", "short", "shorts", "sing", "sister", "sit", "skirt", "sleep", "slow", "small", "snow", "sock", "some", "sometimes", "song", "sorry", "soup", "speak", "sport", "spring", "stand", "star", "stop", "story", "street", "strong", "study", "subject", "summer", "sun", "sunny", "supermarket", "sweater", "swim", "table", "take", "talk", "tall", "taxi", "tea", "teacher", "tell", "thank", "that", "the", "their", "them", "then", "there", "these", "they", "thin", "think", "this", "those", "tiger", "time", "tired", "to", "today", "toilet", "tomato", "tomorrow", "too", "toy", "train", "travel", "tree", "trousers", "try", "turn", "TV", "umbrella", "uncle", "under", "up", "us", "use", "vegetable", "very", "visit", "wait", "walk", "want", "warm", "wash", "watch", "water", "way", "we", "wear", "weather", "week", "welcome", "well", "what", "when", "where", "white", "who", "whose", "why", "window", "windy", "winter", "with", "woman", "wonderful", "word", "work", "worker", "worry", "write", "wrong", "year", "yellow", "yes", "yesterday", "you", "young", "your", "zoo"]
middle_words = ["journey", "garden", "unless", "chocolate", "glove", "product", "straight", "calendar", "television", "hobby", "bamboo", "must", "enter", "successful", "excited", "point", "scissors", "review", "skate", "secretary", "carry", "rich", "single", "proud", "purple", "during", "collect", "February", "private", "mean", "across", "double", "X-ray", "gentleman", "part", "twenty", "beach", "metre", "own", "promise", "thirsty", "hold", "ground", "lot", "countryside", "stupid", "nine", "perhaps", "twelve", "everybody", "outside", "borrow", "number", "meal", "later", "chess", "conversation", "population", "actor", "stamp", "village", "trip", "lonely", "rainy", "railway", "programme", "record", "birth", "shine", "glue", "France", "achieve", "cheap", "lay", "handsome", "continue", "neighbour", "list", "market", "fourth", "director", "Russian", "habit", "ten", "brain", "winner", "risk", "both", "sixth", "European", "stranger", "spend", "guess", "classroom", "tonight", "skill", "describe", "once", "Canada", "May", "sentence", "progress", "itself", "Australian", "shape", "musician", "only", "homework", "fair", "meat", "training", "classmate", "search", "key", "pull", "shake", "July", "mine", "road", "cent", "machine", "shower", "step", "move", "person", "physics", "army", "patient", "Japan", "silence", "twice", "fact", "than", "grey", "treat", "arrive", "dead", "because", "dialogue", "inside", "pioneer", "wife", "French", "tenth", "movie", "victory", "heat", "main", "share", "shoulder", "whole", "worth", "northern", "express", "lively", "hers", "lie", "mobile-phone", "upon", "choose", "natural", "western", "fear", "success", "noise", "November", "as", "southern", "realise", "island", "player", "soon", "gift", "tooth", "engineer", "lose", "pleasure", "someone", "alive", "problem", "Russia", "ready", "sick", "shy", "myself", "cost", "pet", "agreement", "giraffe", "rose", "survey", "prepare", "standard", "factory", "sell", "government", "neck", "along", "full", "choice", "diary", "model", "ring", "pretty", "difficulty", "safe", "anything", "protect", "according-to", "sweet", "grade", "personal", "note", "provide", "more", "else", "fill", "influence", "news", "manage", "Saturday", "volleyball", "thirty", "smart", "ant", "glass", "tail", "necessary", "action", "win", "post", "Tuesday", "Africa", "wing", "tourist", "finger", "hardly", "result", "British", "mark", "asleep", "empty", "include", "human", "anywhere", "situation", "anyway", "member", "eighteen", "secret", "seldom", "Internet", "instead", "sugar", "language", "hard", "divide", "dream", "service", "consider", "friendly", "glad", "without", "nearly", "worse", "true", "boss", "bridge", "two", "safety", "seven", "lend", "poem", "surprise", "eighty", "primary", "Japanese", "produce", "advantage", "beat", "poor", "paper", "dry", "pardon", "student", "require", "England", "six", "change", "print", "best", "experience", "third", "visitor", "wet", "business", "sofa", "deal", "real", "hit", "fire", "shall", "crazy", "university", "palace", "area", "side", "husband", "square", "tie", "club", "seventy", "each", "article", "exciting", "stay", "term", "out", "useful", "stick", "usually", "field", "modern", "form", "ton", "away", "fix", "return", "bit", "delicious", "watermelon", "wake", "notice", "although", "while", "concert", "Sunday", "direction", "celebrate", "enough", "pain", "catch", "direct", "June", "method", "such", "project", "college", "degree", "wound", "develop", "illness", "website", "America", "wish", "ability", "research", "force", "station", "housework", "cover", "enemy", "awful", "Germany", "low", "discuss", "attention", "spread", "meaning", "video", "hall", "kilo", "law", "explain", "postman", "restaurant", "save", "anybody", "thirteen", "underground", "plan", "weight", "bank", "which", "dollar", "date", "deaf", "pollution", "soft", "sure", "son", "forest", "India", "Australia", "five", "coffee", "silk", "vacation", "yours", "lion", "screen", "mountain", "letter", "reply", "weigh", "lucky", "question", "speech", "town", "circle", "into", "towards", "pool", "below", "yet", "wise", "separate", "baseball", "if", "nervous", "luck", "speaker", "rope", "phone", "stomachache", "teach", "pair", "coal", "guitar", "store", "die", "learn", "lemon", "care", "absent", "bill", "blood", "wonder", "connect", "build", "mix", "country", "money", "tidy", "US", "spoon", "start", "tennis", "opposite", "friendship", "control", "corner", "praise", "Thursday", "actress", "d", "swimming", "even", "show", "scientist", "able", "nobody", "truth", "condition", "address", "wealth", "better", "nineteen", "technology", "king", "trust", "copy", "temperature", "neither", "either", "local", "London", "would", "eastern", "hurry", "lazy", "basic", "meeting", "none", "less", "perfect", "level", "brave", "whether", "middle", "practice", "sign", "candle", "quiet", "foreign", "deep", "report", "abroad", "pancake", "stomach", "surface", "certainly", "shame", "course", "feeling", "block", "might", "menu", "century", "central", "count", "thick", "snowy", "earthquake", "speed", "join", "among", "impossible", "fever", "chopsticks", "airport", "discussion", "create", "born", "unit", "against", "introduction", "grow", "brush", "thing", "bored", "terrible", "ride", "seem", "blouse", "keyboard", "hamburger", "OK", "communication", "raise", "sleepy", "polite", "public", "expensive", "American", "fifth", "lock", "cross", "hurt", "dining", "match", "solve", "act", "miss", "manager", "Asia", "lead", "coach", "add", "seat", "drive", "doubt", "three", "quick", "dark", "radio", "careful", "top", "fork", "advise", "relative", "coast", "bedroom", "artist", "twentieth", "refuse", "aloud", "joke", "mile", "snake", "Canadian", "office", "satisfy", "should", "taste", "team", "granddaughter", "shut", "couple", "advice", "used", "society", "ours", "Christmas", "mad", "trouble", "remain", "gold", "Monday", "finish", "elder", "decision", "lab", "Asian", "allow", "around", "wallet", "background", "famous", "forty", "centre", "pale", "September", "hate", "harmful", "gate", "translate", "bell", "flag", "African", "jacket", "pride", "lovely", "eighth", "themselves", "nature", "humorous", "similar", "grandson", "avoid", "smoke", "mess", "expect", "tape", "relationship", "bright", "herself", "dumpling", "leaf", "everywhere", "gun", "pity", "pound", "though", "corn", "instruction", "passport", "ice", "so", "usual", "however", "grape", "bean", "fantastic", "west", "fight", "instrument", "rubbish", "seventh", "communicate", "little", "strict", "serious", "over", "April", "mouse", "lady", "encourage", "reason", "complete", "German", "writer", "need", "happen", "mention", "already", "task", "eraser", "send", "passenger", "knock", "peace", "social", "except", "culture", "sound", "noon", "kiss", "something", "knife", "customer", "sandwich", "headache", "waste", "fifty", "everyone", "common", "dish", "chance", "period", "different", "Olympics", "pollute", "mind", "life", "dictionary", "policeman", "cute", "world", "really", "blow", "fat", "break", "pronunciation", "knowledge", "fun", "smooth", "truck", "bottle", "repair", "queen", "east", "just", "traffic", "pocket", "rule", "ourselves", "fourteen", "danger", "wide", "hang", "regret", "exactly", "silent", "cancel", "Friday", "postcard", "knee", "decide", "strange", "through", "eight", "cup", "guard", "planet", "dig", "pilot", "spare", "medical", "order", "weekday", "Wednesday", "ever", "cartoon", "fifteen", "off", "grammar", "funny", "accept", "clear", "war", "ninety", "push", "one", "ugly", "noisy", "drop", "lift", "industry", "last", "reach", "salad", "blind", "cookie", "recently", "feed", "burn", "interest", "prize", "toothache", "capital", "same", "development", "attend", "discover", "line", "least", "fresh", "suggestion", "health", "silver", "heart", "tiny", "special", "object", "future", "UK", "anyone", "difference", "check", "price", "alone", "job", "never", "climb", "paint", "almost", "weekend", "active", "beef", "everyday", "quite", "yourself", "serve", "guest", "hope", "handbag", "text", "electronic", "pass", "increase", "total", "thought", "missing", "excuse", "since", "nor", "sir", "page", "o'clock", "large", "courage", "voice", "telephone", "daily", "daughter", "whenever", "wheel", "whatever", "wild", "December", "everything", "row", "cause", "repeat", "trade", "twelfth", "Indian", "hotel", "huge", "earth", "correct", "ancient", "land", "forget", "information", "proper", "interview", "shout", "museum", "pear", "value", "depend", "sea", "finally", "few", "sixty", "laugh", "hill", "tool", "leave", "mistake", "tour", "round", "January", "hero", "race", "balloon", "sand", "litter", "will", "appear", "wall", "pick", "tower", "medicine", "certain", "present", "hole", "smile", "weak", "steal", "March", "past", "carrot", "Europe", "offer", "August", "geography", "thousand", "awake", "important", "purpose", "suggest", "biscuit", "exam", "board", "hundred", "punish", "wood", "sixteen", "invent", "treasure", "group", "maybe", "most", "festival", "helpful", "pay", "theatre", "fisherman", "valuable", "pronounce", "believe", "bathroom", "fit", "enjoy", "bowl", "oil", "sale", "rabbit", "example", "message", "excellent", "national", "leader", "somewhere", "bottom", "seventeen", "south", "discovery", "online", "rise", "simple", "front", "spirit", "second", "size", "score", "sudden", "himself", "probably", "fall", "test", "general", "role", "community", "yard", "chemistry", "scarf", "competition", "hide", "strawberry", "boring", "imagine", "rush", "north", "kilometre", "camp", "first", "receive", "rock", "basket", "fail", "hen", "officer", "end", "warn", "popular", "smell", "traditional", "space", "rest", "understand", "Pacific", "somebody", "robot", "camera", "magic", "president", "quarter", "relax", "eyeface", "stone", "careless", "honest", "salt", "kick", "ticket", "magazine", "compare", "another", "education", "afford", "may", "cheer", "plenty", "spell", "cut", "support", "grandparent", "activity", "matter", "follow", "state", "keep", "zero", "cough", "nothing", "piece", "height", "building", "especially", "coin", "several", "set", "still", "notebook", "until", "T-shirt", "sky", "storm", "wind", "free", "cloud", "marry", "above", "introduce", "touch", "invention", "picnic", "become", "four", "guide", "possible", "age", "ninth", "suppose", "agree", "kill", "environment", "silly", "international", "loud", "eleven", "violin", "fridge", "whom", "succeed", "ago", "pink", "sense", "air", "hometown", "chalk", "history", "hat", "rapid", "invite", "Britain", "October", "could", "dangerous", "comfortable", "pie", "together", "other", "worst", "remember"]
high_words = ["desert", "delay", "precious", "supper", "participate", "criminal", "illegal", "tortoise", "dam", "litre", "growth", "businessman", "disease", "jet", "aside", "punctual", "studio", "balance", "shabby", "bonus", "tick", "golf", "likely", "triangle", "representative", "escape", "administration", "sweat", "eager", "sow", "weed", "permit", "recite", "abstract", "throughout", "P.C.", "substitute", "remove", "self", "physical", "virtue", "bathtub", "edge", "exchange", "fiber", "corporation", "diploma", "recorder", "spaceship", "airplane", "boundary", "attractive", "sob", "confidential", "fragile", "poisonous", "spray", "parallel", "collar", "thunderstorm", "border", "struggle", "postcode", "slip", "human-being", "container", "division", "consequence", "sleeve", "literary", "net", "event", "TV", "yell", "mm", "toothpaste", "package", "tournament", "armchair", "version", "cocoa", "specific", "melon", "mailbox", "jam", "butter", "spear", "flame", "carbon", "elegant", "minus", "sneaker", "crowd", "passage", "terrify", "style", "furnished", "grandpa", "defend", "mop", "band", "photographer", "thrill", "partner", "recover", "sideway", "fortnight", "sacred", "respect", "beneath", "fingernail", "e-mail", "cone", "foresee", "supply", "handy", "bandage", "wage", "peach", "apologize", "plain", "brick", "bee", "existence", "kilogramme", "view", "independence", "identity", "effort", "nowhere", "harm", "slat", "independent", "mud", "liquid", "civilian", "stadium", "musical", "tension", "cheat", "native", "nutrition", "classify", "supreme", "responsibility", "pop", "fax", "bleed", "arise", "astronomy", "disabled", "owner", "pin", "referee", "creature", "expand", "character", "strength", "conscience", "obvious", "wrist", "author", "skeptical", "honour", "troop", "brief", "fuel", "institution", "enlarge", "boxing", "defeat", "neat", "crew", "painter", "button", "consult", "schoolboy", "apply", "outline", "pleased", "recommend", "warmth", "boot", "jungle", "complex", "replace", "certificate", "fence", "herb", "appeal", "assistance", "clumsy", "pressure", "cash", "dignity", "quarrel", "gym", "truly", "franc", "precise", "champion", "folk", "salesman", "affect", "jaw", "vital", "arrival", "mankind", "unemployment", "shallow", "preserve", "behalf", "associate", "multiply", "agent", "adventure", "grill", "murder", "skip", "per", "waiter", "tube", "pm", "settlement", "servant", "seed", "found", "circumstance", "hearing", "fantasy", "equip", "soccer", "innocent", "unite", "wealthy", "universal", "sour", "final", "delight", "roof", "bid", "ahead", "bakery", "fibre", "appointment", "homeland", "mobile", "P.E.", "intent", "aircraft", "powder", "lounge", "flood", "nut", "pan", "regular", "bunch", "severe", "assessment", "gas", "painting", "positive", "mutton", "roundabout", "turning", "enquiry", "owe", "undertake", "throat", "casual", "survive", "refresh", "contradictory", "No.", "alongside", "approximately", "distinguish", "outdoors", "bridegroom", "eyesight", "goal", "greeting", "eggplant", "drawback", "shortcoming", "parcel", "acquaintance", "arrest", "relay", "angle", "appropriate", "claw", "approve", "fireworks", "hopeful", "leak", "dialog", "bat", "directory", "assess", "preparation", "inn", "spoonful", "tense", "metal", "dip", "tough", "fetch", "secure", "disappointed", "parking", "bay", "candidate", "buffet", "stare", "satisfaction", "root", "disappear", "chew", "entire", "reference", "youth", "kingdom", "prescription", "breathe", "rooster", "outwards", "engine", "disk", "harvest", "junior", "abolish", "vase", "carpet", "split", "Ms.", "abuse", "bungalow", "funeral", "deadline", "journalist", "chest", "relevant", "moral", "brewery", "power", "surgeon", "association", "remark", "vague", "lawyer", "centimetre", "acre", "exact", "fond", "bare", "official", "mummy", "delete", "mature", "spot", "province", "frighten", "catholic", "cheese", "tentative", "actual", "allergic", "pot", "amateur", "float", "rude", "upper", "virus", "pure", "sincerely", "stout", "oppose", "tremble", "altitude", "bother", "acid", "optional", "electric", "gradual", "arrow", "thriller", "discrimination", "bless", "essay", "balcony", "contrary", "sympathy", "swift", "literature", "diet", "socialist", "kangaroo", "rubber", "cupboard", "tendency", "outstanding", "generation", "skin", "selfish", "cell", "alcohol", "westwards", "DVD", "absolute", "slave", "architect", "security", "design", "considerate", "cotton", "uncomfortable", "unique", "crossing", "transport", "waitress", "crossroads", "exhibition", "belly", "quit", "admit", "opinion", "controversial", "pea", "zip", "suffering", "electricity", "insist", "employ", "breakthrough", "accident", "network", "acquisition", "differ", "forgive", "sniff", "beard", "fortune", "prison", "strait", "lemonade", "lightening", "carve", "dessert", "pepper", "arrange", "accelerate", "spy", "commit", "videophone", "destination", "newspaper", "outcome", "hire", "impress", "suitable", "textbook", "personally", "trunk", "Antarctic", "detective", "superior", "vinegar", "politician", "rat", "tomb", "harmony", "slide", "childhood", "campaign", "theme", "sculpture", "conflict", "fragrant", "calm", "decorate", "unconscious", "captain", "burglar", "appendix", "promote", "madam", "cure", "dilemma", "various", "pour", "relate", "constitution", "ample", "starve", "are", "pace", "accuracy", "apology", "sadness", "jazz", "suspension", "adore", "agenda", "rather", "comfort", "Easter", "minimum", "apron", "departure", "educate", "terminal", "audience", "component", "possess", "recognize", "socialism", "equipment", "injure", "outer", "AD", "explore", "cautious", "examine", "airline", "otherwise", "headmaster", "advertisement", "appreciation", "cube", "measure", "grateful", "attract", "skyscraper", "dorm", "rainfall", "straw", "advertise", "battery", "suit", "violate", "terror", "unable", "bravery", "clap", "lamb", "compensate", "tight", "numb", "alarm", "protection", "operator", "lid", "pence", "frequent", "tire", "grandchild", "bishop", "comprehension", "being", "nephew", "ham", "Oceania", "thread", "catalog", "instant", "besides", "accompany", "survival", "belief", "pill", "forever", "rocket", "subscribe", "unusual", "content", "psychology", "scenery", "duty", "mistaken", "squirrel", "unwilling", "dull", "doll", "faith", "cyclist", "anxiety", "monument", "glance", "female", "ambassadress", "abrupt", "behaviour", "embarrass", "gravity", "cheers", "flour", "poison", "insure", "lung", "attach", "accent", "patience", "company", "means", "document", "regardless", "semicircle", "request", "whale", "profit", "atom", "sickness", "sting", "dormitory", "thinking", "zone", "composition", "shaver", "choke", "admission", "memorial", "drug", "poet", "afterwards", "addicted", "phenomenon", "identification", "sharp", "bark", "communism", "broad", "cooker", "soap", "weakness", "pulse", "absorb", "ought", "flexible", "monitor", "reality", "topic", "annoy", "equal", "royal", "position", "cuisine", "flesh", "nationwide", "pub", "exist", "ceremony", "admirable", "seek", "continent", "messy", "schoolmate", "adjust", "persuade", "zoom", "explanation", "northeast", "nod", "represent", "solid", "arithmetic", "punctuation", "garbage", "host", "remind", "handle", "fur", "comment", "basis", "raincoat", "tutor", "idiom", "shave", "consideration", "experiment", "eye", "framework", "done", "swallow", "fool", "volleyballl", "dare", "applaud", "function", "bureaucratic", "Moslem", "treatment", "commercial", "fortunate", "conclude", "anchor", "fare", "humour", "improve", "random", "turkey", "absence", "tractor", "favour", "interval", "shrink", "significance", "allocate", "unfit", "cigar", "contradict", "gifted", "bean-curd", "horrible", "publish", "convey", "minibus", "troublesome", "award", "announce", "sideroad", "loose", "bacterium", "granny", "donate", "motherland", "union", "comedy", "accountant", "ecology", "gymnastics", "punishment", "reserve", "necklace", "bench", "bathe", "rely", "bush", "sharpen", "sightseeing", "goods", "premier", "steward", "welfare", "CD", "cabbage", "roast", "disappoint", "evidence", "operate", "bend", "twin", "spokesman", "cycle", "status", "companion", "chairwoman", "percent", "butterfly", "edition", "chef", "analysis", "suite", "urban", "properly", "perform", "deliberately", "stage", "rent", "defence", "ad", "benefit", "organ", "god", "rebuild", "pillow", "challenging", "surround", "deed", "communist", "confuse", "unbelievable", "meanwhile", "scar", "grand", "reading", "pump", "fundamental", "switch", "arrangement", "connection", "guilty", "Madame", "ancestor", "correction", "pork", "trial", "editor", "march", "demand", "pleasant", "church", "centigrade", "concern", "sink", "envy", "impression", "desperate", "reputation", "therefore", "fiction", "radiation", "bride", "error", "pedestrian", "obtain", "surplus", "correspond", "vote", "endless", "govern", "sailor", "Buddhism", "gallon", "furniture", "slice", "aspect", "decade", "personnel", "bacon", "seashell", "ward", "piano", "hurricane", "determine", "partly", "porter", "potential", "ballet", "badminton", "beg", "typical", "ceiling", "react", "seminar", "Mr.", "argue", "occur", "competence", "chief", "maid", "electrical", "debt", "extreme", "civilizasation", "political", "pianist", "onto", "blanket", "recreation", "hopeless", "liberty", "conductor", "garment", "insurance", "hunter", "divorce", "artificial", "AM", "Atlantic", "devotion", "damage", "typhoon", "battle", "forgetful", "shuttle", "sidewalk", "enjoyable", "merciful", "greedy", "expression", "reward", "tasteless", "collection", "adolescent", "allowance", "retell", "crop", "dislike", "drawer", "portable", "did", "digital", "unconditional", "cleaner", "movement", "cloth", "reset", "motto", "arbitrary", "shoot", "signal", "vain", "remote", "compass", "fog", "thankful", "onion", "belong", "tam", "embassy", "tasty", "chat", "revolution", "chemist", "eagle", "approval", "sword", "compete", "dinosaur", "mom", "phrase", "bow", "delicate", "outing", "normal", "finance", "rhyme", "mountainous", "awesome", "cheerful", "accurate", "justice", "settler", "postage", "urge", "incident", "gentle", "concrete", "trap", "institute", "curtain", "radioactive", "thunder", "cheek", "emperor", "stainless", "shot", "erupt", "disagree", "maximum", "cab", "mask", "bargain", "criterion", "gallery", "cafe", "consistent", "drag", "needle", "alternative", "modem", "theory", "tent", "enthusiastic", "courtyard", "compulsory", "systematic", "spit", "draft", "accomplish", "leather", "maple", "excite", "broom", "housewife", "accumulate", "indeed", "pattern", "sew", "waiting-room", "moment", "prohibit", "luggage", "agency", "ambulance", "dusty", "handwriting", "racial", "import", "handkerchief", "recent", "ashamed", "abnormal", "transparent", "paddle", "trick", "statesman", "bacteria", "pack", "reduce", "emergency", "scan", "interpreter", "regard", "cheque", "concept", "foreigner", "microscope", "pest", "drill", "wax", "quantity", "conduct", "slavery", "tease", "coke", "feather", "scare", "ocean", "pension", "wrestle", "privilege", "accustomed", "dynasty", "failure", "enterprise", "cottage", "specialist", "eventually", "caution", "beer", "command", "hunt", "swell", "chemical", "sunshine", "prevent", "cast", "elect", "purse", "thief", "assumption", "type", "headline", "ending", "cave", "curriculum", "tiresome", "upwards", "till", "circuit", "barbershop", "presentation", "spelling", "seagull", "user", "loaf", "analyse", "amuse", "washroom", "prejudice", "queue", "intention", "firm", "symbol", "update", "dive", "preview", "handful", "alcoholic", "forehead", "mirror", "cubic", "freeze", "salute", "transform", "arch", "gather", "former", "defense", "sponsor", "encouragement", "grocer", "construction", "shadow", "adult", "forecast", "brake", "voyage", "decoration", "crime", "anniversary", "plastic", "restriction", "jar", "purchase", "betray", "devote", "deliver", "achievement", "credit", "crash", "backwards", "track", "barrier", "teamwork", "disturb", "earn", "fellow", "athlete", "convenience", "attitude", "evolution", "facial", "fim", "expense", "climate", "chairman", "teapot", "classic", "alley", "amaze", "seal", "tissue", "digest", "downstairs", "cassette", "pint", "gesture", "ripen", "somehow", "souvenir", "unrest", "click", "distant", "astonish", "outspoken", "wheat", "cushion", "ambiguous", "scold", "entry", "challenge", "budget", "tablet", "ownership", "major", "bomb", "acquire", "passer-by", "pyramid", "oval", "weep", "wherever", "dad", "path", "socket", "attain", "recipe", "powerful", "caption", "abundant", "seize", "happiness", "clay", "aim", "manner", "explode", "simplify", "jeep", "baggage", "colleague", "is", "reporter", "VCD", "extension", "ping-pong", "mat", "regulation", "teenager", "lantern", "discount", "astronomer", "hug", "principle", "reject", "squeeze", "unfortunate", "disaster", "bent", "assist", "disgusting", "stair", "biology", "mercy", "sharpener", "steak", "occupy", "performance", "generous", "grasp", "walnut", "Christian", "staff", "overcome", "immigration", "platform", "fee", "hunger", "convince", "abortion", "missile", "trolleybus", "bachelor", "circulate", "salary", "super", "waist", "castle", "daddy", "mineral", "oh", "accessible", "kindness", "telescope", "rainbow", "behave", "observe", "steep", "quiz", "rank", "clothing", "fluency", "surrounding", "optimistic", "vocabulary", "civil", "fox", "requirement", "upstairs", "ambition", "blank", "ordinary", "smog", "universe", "Dr", "hotdog", "material", "ink", "tongue", "corrupt", "fountain", "radium", "saucer", "shade", "symptom", "apparent", "hesitate", "cattle", "petrol", "porridge", "skillful", "pavement", "camel", "apartment", "medium", "soul", "account", "avenue", "breathless", "policy", "hook", "reception", "stocking", "uncertain", "filll", "affair", "oxygen", "tend", "contribution", "celebration", "grain", "advance", "disadvantage", "dentist", "inspire", "yoghurt", "paragraph", "forbid", "alphabet", "extra", "grandparents", "temporary", "vest", "kettle", "dictation", "deserve", "headmistress", "tourism", "AIDS", "airmail", "consume", "solar", "affection", "organise", "graduation", "tune", "currency", "offshore", "familiar", "carrier", "conservative", "lip", "mainland", "nationality", "chart", "talent", "pile", "graph", "basin", "sight", "resemble", "energy", "graduate", "steady", "canteen", "sweep", "toothbrush", "botanical", "spade", "explicit", "postpone", "biography", "brand", "customs", "limit", "tax", "hammer", "saying", "bound", "scholar", "bath", "calculate", "liberation", "cage", "concentrate", "rot", "flash", "mild", "media", "rag", "strengthen", "freeway", "grandma", "pineapple", "Mrs.", "narrow", "smoker", "howl", "zebra", "southeast", "origin", "hardworking", "procedure", "friction", "contain", "sacrifice", "adapt", "available", "sneeze", "rugby", "tale", "cream", "packet", "nest", "toast", "sex", "recycle", "holy", "haircut", "acute", "disagreement", "false", "sigh", "architecture", "greet", "millionaire", "reservation", "conservation", "fierce", "iron", "uniform", "resign", "counter", "thus", "case", "midnight", "foolish", "mustard", "expert", "admire", "wag", "biochemistry", "rid", "forward", "kindergarten", "disturbing", "entertainment", "pine", "table-tennis", "depth", "senior", "riddle", "lorry", "category", "mathematics", "dial", "physicist", "yummy", "highway", "description", "chapter", "register", "dot", "mum", "exit", "cancer", "contribute", "freedom", "district", "apart", "link", "ridiculous", "unlike", "delighted", "politics", "amazing", "overhead", "educator", "O.K.", "extraordinary", "storage", "vice", "stubborn", "nuclear", "destroy", "flight", "theirs", "theoretical", "aggressive", "plot", "popcorn", "visa", "ferry", "bitter", "department", "retire", "twist", "revision", "merely", "boil", "offence", "sunburnt", "coincidence", "instruct", "addition", "oral", "warehouse", "beyond", "ambassador", "victim", "death", "statistics", "microwave", "receiver", "sail", "minister", "patent", "reflect", "wander", "album", "overweight", "bury", "violent", "shelf", "hatch", "ignore", "novel", "mend", "predict", "butcher", "effect", "hostess", "rigid", "thorough", "attack", "signature", "importance", "dash", "brunch", "algebra", "inspect", "volcano", "pole", "adequate", "output", "harbour", "steel", "changeable", "straightforward", "photograph", "towel", "broken", "cigarette", "bone", "tank", "prove", "commitment", "combine", "insect", "reform", "length", "ripe", "quality", "religious", "swing", "bounce", "advocate", "appearance", "slim", "conclusion", "oilfield", "motor", "amount", "absurd", "evident", "section", "capsule", "negotiate", "gray", "ash", "suck", "seaside", "dizzy", "broadcast", "dozen", "channel", "anger", "irrigation", "skateboard", "greengrocer", "practical", "outgoing", "adaptation", "operation", "tear", "occupation", "authority", "clarify", "insert", "librarian", "variety", "relief", "curious", "inform", "scholarship", "autonomous", "modest", "urgent", "volunteer", "chaos", "annual", "ski", "previous", "expectation", "select", "aware", "foggy", "perfume", "taxpayer", "accommodation", "mourn", "access", "dusk", "press", "schoolgirl", "oneself", "stove", "sideways", "suspect", "rare", "thirst", "basement", "refer", "file", "soldier", "deer", "thermos", "glare", "appetite", "panic", "clone", "garage", "nowadays", "performer", "academy", "amusement", "scratch", "awkward", "chant", "lack", "settle", "shark", "flashlight", "ministry", "shelter", "decline", "aluminum", "flee", "decrease", "anyhow", "villager", "bicycle", "guarantee", "session", "figure", "assume", "plate", "bingo", "rescue", "tobacco", "heel", "joy", "possibility", "refrigerator", "freezing", "vacant", "bowling", "male", "league", "energetic", "particular", "download", "raw", "altogether", "birthplace", "razor", "routine", "submit", "confirm", "diamond", "weekly", "consensus", "violinist", "fry", "marble", "plug", "disc", "quake", "frontier", "initial", "master", "orbit", "percentage", "inch", "valley", "brochure", "nation", "cater", "merry", "cafeteria", "pretend", "frost", "due", "dynamic", "overcoat", "congratulate", "distance", "choir", "labour", "prisoner", "gay", "production", "prayer", "neighbourhood", "southwest", "splendid", "astronaut", "misunderstand", "resist", "judgement", "feast", "satellite", "lap", "heaven", "medal", "polish", "traveler", "dismiss", "acknowledge", "attempt", "possession", "applicant", "process", "statement", "construct", "translation", "consist", "rough", "shore", "bar", "swap", "globe", "spin", "zipper", "technical", "religion", "beneficial", "motivation", "penny", "chain", "peaceful", "motorcycle", "stable", "clinic", "charge", "authentic", "condemn", "custom", "mommy", "obey", "vast", "appoint", "goose", "laundry", "jewllery", "ox", "damp", "helicopter", "opera", "typist", "dawn", "helmet", "face", "navy", "barbecue", "range", "atmosphere", "envelope", "attraction", "translator", "useless", "overlook", "suffer", "agricultural", "pause", "fluent", "timetable", "profession", "am", "receipt", "export", "tyre", "part-time", "chorus", "glory", "clerk", "dustbin", "parrot", "jeans", "shoppping", "scientific", "gram", "confident", "invitation", "port", "permission", "comb", "latter", "adopt", "anxious", "primitive", "average", "lame", "discourage", "prefer", "rewind", "judge", "automatic", "contemporary", "system", "vivid", "license", "expose", "golden", "physician", "reliable", "legal", "darkness", "distribute", "bite", "painful", "ache", "hydrogen", "tip", "disability", "laughter", "mental", "reasonable", "immediately", "noble", "ruin", "shortly", "professor", "title", "diverse", "northwest", "web", "starvation", "court", "sunlight", "shopkeeper", "soil", "merchant", "qualification", "burden", "theft", "belt", "tap", "rate", "lamp", "underwear", "indicate", "math", "voluntary", "temple", "sort", "drunk", "target", "wrinkle", "dimension", "nearby", "burst", "vehicle", "mixture", "academic", "adolescence", "BC", "debate", "appreciate", "pond", "separation", "beauty", "fist", "subjective", "equality", "rectangle", "statue", "tradition", "accuse", "muddy", "carriage", "strike", "beddings", "interrupt", "honey", "scene", "roll", "mosquito", "via", "focus", "technique", "typewriter", "entrance", "summary", "compromise", "barber", "fold", "salty", "sceptical", "boom", "characteristic", "stewardess", "frog", "gain", "relation", "scream", "ankle", "data", "circus", "fancy", "ban", "abandon", "unfair", "format", "dioxide", "lecture", "committee", "sorrow", "tin", "superb", "antique", "grocery", "application", "bond", "sensitive", "alike", "drum", "constant", "assistant", "aboard", "conventional", "software", "mushroom", "organization", "nursery", "questionnaire", "cozy", "jog", "ray", "visual", "respond", "steam", "quilt", "anecdote", "mail", "shock", "diagram", "opening", "spoken", "bye", "fasten", "plus", "adjustment", "flu", "sparrow", "database", "tolerate", "pipe", "flow", "airspace", "civilization", "botany", "beast", "underline", "symphony", "practise", "approach", "marathon", "Arctic", "wedding", "throw", "fade", "tailor", "blame", "rail", "majority", "pray", "convenient", "mist", "salesgirl", "yawn", "athletic", "distinction", "republic", "vertical", "collision", "loss", "passive", "stress", "examination", "stream", "desire", "base", "memory", "trend", "receptionist", "guidance", "slight", "load", "seaweed", "stain", "hardship", "permanent", "federal", "spiritual", "evaluate", "schedule", "brilliant", "moustache", "citizen", "geometry", "consultant", "branch", "intelligence", "conference", "niece", "unbearable", "agriculture", "canal", "novelist", "flat", "pregnant", "wave", "cruel", "deposit", "marriage", "puzzle", "aid", "boycott", "rob", "violence", "argument", "declare", "catastrophe", "breath", "breast", "income", "upset", "mass", "poster", "fault", "injury", "suitcase", "preference", "garlic", "nail", "sausage", "analyze", "paperwork", "swear", "valid", "congratulation", "downtown"]

template_words.insert_one({
    "level": "primary",
    "words": primary_words,
})

template_words.insert_one({
    "level": "middle",
    "words": middle_words,
})

template_words.insert_one({
    "level": "high",
    "words": high_words,
})

