import sys
sys.path.append("../app")

import pymongo
from config import *

client = pymongo.MongoClient(MONGO_URL)
db = client[MONGO_DB]
word = db[WORD_DB]

words_data = [
{
	"word": "a",
	"group": "A",
	"level": "primary",
},
{
	"word": "about",
	"group": "A",
	"level": "primary",
},
{
	"word": "afraid",
	"group": "A",
	"level": "primary",
},
{
	"word": "after",
	"group": "A",
	"level": "primary",
},
{
	"word": "afternoon",
	"group": "A",
	"level": "primary",
},
{
	"word": "again",
	"group": "A",
	"level": "primary",
},
{
	"word": "all",
	"group": "A",
	"level": "primary",
},
{
	"word": "also",
	"group": "A",
	"level": "primary",
},
{
	"word": "always",
	"group": "A",
	"level": "primary",
},
{
	"word": "and",
	"group": "A",
	"level": "primary",
},
{
	"word": "angry",
	"group": "A",
	"level": "primary",
},
{
	"word": "animal",
	"group": "A",
	"level": "primary",
},
{
	"word": "answer",
	"group": "A",
	"level": "primary",
},
{
	"word": "any",
	"group": "A",
	"level": "primary",
},
{
	"word": "apple",
	"group": "A",
	"level": "primary",
},
{
	"word": "arm",
	"group": "A",
	"level": "primary",
},
{
	"word": "art",
	"group": "A",
	"level": "primary",
},
{
	"word": "ask",
	"group": "A",
	"level": "primary",
},
{
	"word": "at",
	"group": "A",
	"level": "primary",
},
{
	"word": "aunt",
	"group": "A",
	"level": "primary",
},
{
	"word": "autumn",
	"group": "A",
	"level": "primary",
},
{
	"word": "baby",
	"group": "B",
	"level": "primary",
},
{
	"word": "back",
	"group": "B",
	"level": "primary",
},
{
	"word": "bad",
	"group": "B",
	"level": "primary",
},
{
	"word": "bag",
	"group": "B",
	"level": "primary",
},
{
	"word": "ball",
	"group": "B",
	"level": "primary",
},
{
	"word": "banana",
	"group": "B",
	"level": "primary",
},
{
	"word": "basketball",
	"group": "B",
	"level": "primary",
},
{
	"word": "be",
	"group": "B",
	"level": "primary",
},
{
	"word": "bear",
	"group": "B",
	"level": "primary",
},
{
	"word": "beautiful",
	"group": "B",
	"level": "primary",
},
{
	"word": "bed",
	"group": "B",
	"level": "primary",
},
{
	"word": "before",
	"group": "B",
	"level": "primary",
},
{
	"word": "begin",
	"group": "B",
	"level": "primary",
},
{
	"word": "behind",
	"group": "B",
	"level": "primary",
},
{
	"word": "beside",
	"group": "B",
	"level": "primary",
},
{
	"word": "between",
	"group": "B",
	"level": "primary",
},
{
	"word": "big",
	"group": "B",
	"level": "primary",
},
{
	"word": "bike",
	"group": "B",
	"level": "primary",
},
{
	"word": "bird",
	"group": "B",
	"level": "primary",
},
{
	"word": "birthday",
	"group": "B",
	"level": "primary",
},
{
	"word": "black",
	"group": "B",
	"level": "primary",
},
{
	"word": "blackboard",
	"group": "B",
	"level": "primary",
},
{
	"word": "blue",
	"group": "B",
	"level": "primary",
},
{
	"word": "boat",
	"group": "B",
	"level": "primary",
},
{
	"word": "body",
	"group": "B",
	"level": "primary",
},
{
	"word": "book",
	"group": "B",
	"level": "primary",
},
{
	"word": "box",
	"group": "B",
	"level": "primary",
},
{
	"word": "boy",
	"group": "B",
	"level": "primary",
},
{
	"word": "bread",
	"group": "B",
	"level": "primary",
},
{
	"word": "breakfast",
	"group": "B",
	"level": "primary",
},
{
	"word": "bring",
	"group": "B",
	"level": "primary",
},
{
	"word": "brother",
	"group": "B",
	"level": "primary",
},
{
	"word": "brown",
	"group": "B",
	"level": "primary",
},
{
	"word": "bus",
	"group": "B",
	"level": "primary",
},
{
	"word": "busy",
	"group": "B",
	"level": "primary",
},
{
	"word": "but",
	"group": "B",
	"level": "primary",
},
{
	"word": "buy",
	"group": "B",
	"level": "primary",
},
{
	"word": "by",
	"group": "B",
	"level": "primary",
},
{
	"word": "cake",
	"group": "C",
	"level": "primary",
},
{
	"word": "call",
	"group": "C",
	"level": "primary",
},
{
	"word": "can",
	"group": "C",
	"level": "primary",
},
{
	"word": "candy",
	"group": "C",
	"level": "primary",
},
{
	"word": "cap",
	"group": "C",
	"level": "primary",
},
{
	"word": "car",
	"group": "C",
	"level": "primary",
},
{
	"word": "card",
	"group": "C",
	"level": "primary",
},
{
	"word": "cat",
	"group": "C",
	"level": "primary",
},
{
	"word": "chair",
	"group": "C",
	"level": "primary",
},
{
	"word": "chicken",
	"group": "C",
	"level": "primary",
},
{
	"word": "child",
	"group": "C",
	"level": "primary",
},
{
	"word": "children",
	"group": "C",
	"level": "primary",
},
{
	"word": "China",
	"group": "C",
	"level": "primary",
},
{
	"word": "Chinese",
	"group": "C",
	"level": "primary",
},
{
	"word": "cinema",
	"group": "C",
	"level": "primary",
},
{
	"word": "city",
	"group": "C",
	"level": "primary",
},
{
	"word": "class",
	"group": "C",
	"level": "primary",
},
{
	"word": "clean",
	"group": "C",
	"level": "primary",
},
{
	"word": "clever",
	"group": "C",
	"level": "primary",
},
{
	"word": "clock",
	"group": "C",
	"level": "primary",
},
{
	"word": "close",
	"group": "C",
	"level": "primary",
},
{
	"word": "clothes",
	"group": "C",
	"level": "primary",
},
{
	"word": "cloudy",
	"group": "C",
	"level": "primary",
},
{
	"word": "coat",
	"group": "C",
	"level": "primary",
},
{
	"word": "cold",
	"group": "C",
	"level": "primary",
},
{
	"word": "colour",
	"group": "C",
	"level": "primary",
},
{
	"word": "come",
	"group": "C",
	"level": "primary",
},
{
	"word": "computer",
	"group": "C",
	"level": "primary",
},
{
	"word": "cook",
	"group": "C",
	"level": "primary",
},
{
	"word": "cool",
	"group": "C",
	"level": "primary",
},
{
	"word": "cousin",
	"group": "C",
	"level": "primary",
},
{
	"word": "cow",
	"group": "C",
	"level": "primary",
},
{
	"word": "crayon",
	"group": "C",
	"level": "primary",
},
{
	"word": "cry",
	"group": "C",
	"level": "primary",
},
{
	"word": "dad",
	"group": "D",
	"level": "primary",
},
{
	"word": "dance",
	"group": "D",
	"level": "primary",
},
{
	"word": "day",
	"group": "D",
	"level": "primary",
},
{
	"word": "dear",
	"group": "D",
	"level": "primary",
},
{
	"word": "desk",
	"group": "D",
	"level": "primary",
},
{
	"word": "difficult",
	"group": "D",
	"level": "primary",
},
{
	"word": "dinner",
	"group": "D",
	"level": "primary",
},
{
	"word": "dirty",
	"group": "D",
	"level": "primary",
},
{
	"word": "do",
	"group": "D",
	"level": "primary",
},
{
	"word": "doctor",
	"group": "D",
	"level": "primary",
},
{
	"word": "dog",
	"group": "D",
	"level": "primary",
},
{
	"word": "door",
	"group": "D",
	"level": "primary",
},
{
	"word": "down",
	"group": "D",
	"level": "primary",
},
{
	"word": "draw",
	"group": "D",
	"level": "primary",
},
{
	"word": "dress",
	"group": "D",
	"level": "primary",
},
{
	"word": "drink",
	"group": "D",
	"level": "primary",
},
{
	"word": "driver",
	"group": "D",
	"level": "primary",
},
{
	"word": "duck",
	"group": "D",
	"level": "primary",
},
{
	"word": "ear",
	"group": "E",
	"level": "primary",
},
{
	"word": "early",
	"group": "E",
	"level": "primary",
},
{
	"word": "easy",
	"group": "E",
	"level": "primary",
},
{
	"word": "eat",
	"group": "E",
	"level": "primary",
},
{
	"word": "egg",
	"group": "E",
	"level": "primary",
},
{
	"word": "elephant",
	"group": "E",
	"level": "primary",
},
{
	"word": "email",
	"group": "E",
	"level": "primary",
},
{
	"word": "English",
	"group": "E",
	"level": "primary",
},
{
	"word": "evening",
	"group": "E",
	"level": "primary",
},
{
	"word": "every",
	"group": "E",
	"level": "primary",
},
{
	"word": "exercise",
	"group": "E",
	"level": "primary",
},
{
	"word": "eye",
	"group": "E",
	"level": "primary",
},
{
	"word": "face",
	"group": "F",
	"level": "primary",
},
{
	"word": "family",
	"group": "F",
	"level": "primary",
},
{
	"word": "fan",
	"group": "F",
	"level": "primary",
},
{
	"word": "far",
	"group": "F",
	"level": "primary",
},
{
	"word": "farm",
	"group": "F",
	"level": "primary",
},
{
	"word": "farmer",
	"group": "F",
	"level": "primary",
},
{
	"word": "fast",
	"group": "F",
	"level": "primary",
},
{
	"word": "father",
	"group": "F",
	"level": "primary",
},
{
	"word": "favourite",
	"group": "F",
	"level": "primary",
},
{
	"word": "feel",
	"group": "F",
	"level": "primary",
},
{
	"word": "film",
	"group": "F",
	"level": "primary",
},
{
	"word": "find",
	"group": "F",
	"level": "primary",
},
{
	"word": "fine",
	"group": "F",
	"level": "primary",
},
{
	"word": "fish",
	"group": "F",
	"level": "primary",
},
{
	"word": "floor",
	"group": "F",
	"level": "primary",
},
{
	"word": "flower",
	"group": "F",
	"level": "primary",
},
{
	"word": "fly",
	"group": "F",
	"level": "primary",
},
{
	"word": "food",
	"group": "F",
	"level": "primary",
},
{
	"word": "foot",
	"group": "F",
	"level": "primary",
},
{
	"word": "football",
	"group": "F",
	"level": "primary",
},
{
	"word": "for",
	"group": "F",
	"level": "primary",
},
{
	"word": "friend",
	"group": "F",
	"level": "primary",
},
{
	"word": "from",
	"group": "F",
	"level": "primary",
},
{
	"word": "fruit",
	"group": "F",
	"level": "primary",
},
{
	"word": "game",
	"group": "G",
	"level": "primary",
},
{
	"word": "get",
	"group": "G",
	"level": "primary",
},
{
	"word": "girl",
	"group": "G",
	"level": "primary",
},
{
	"word": "give",
	"group": "G",
	"level": "primary",
},
{
	"word": "go",
	"group": "G",
	"level": "primary",
},
{
	"word": "good",
	"group": "G",
	"level": "primary",
},
{
	"word": "goodbye",
	"group": "G",
	"level": "primary",
},
{
	"word": "grandfather",
	"group": "G",
	"level": "primary",
},
{
	"word": "grandmother",
	"group": "G",
	"level": "primary",
},
{
	"word": "grass",
	"group": "G",
	"level": "primary",
},
{
	"word": "great",
	"group": "G",
	"level": "primary",
},
{
	"word": "green",
	"group": "G",
	"level": "primary",
},
{
	"word": "hair",
	"group": "H",
	"level": "primary",
},
{
	"word": "half",
	"group": "H",
	"level": "primary",
},
{
	"word": "hand",
	"group": "H",
	"level": "primary",
},
{
	"word": "happy",
	"group": "H",
	"level": "primary",
},
{
	"word": "have",
	"group": "H",
	"level": "primary",
},
{
	"word": "he",
	"group": "H",
	"level": "primary",
},
{
	"word": "head",
	"group": "H",
	"level": "primary",
},
{
	"word": "healthy",
	"group": "H",
	"level": "primary",
},
{
	"word": "hear",
	"group": "H",
	"level": "primary",
},
{
	"word": "heavy",
	"group": "H",
	"level": "primary",
},
{
	"word": "hello",
	"group": "H",
	"level": "primary",
},
{
	"word": "help",
	"group": "H",
	"level": "primary",
},
{
	"word": "her",
	"group": "H",
	"level": "primary",
},
{
	"word": "here",
	"group": "H",
	"level": "primary",
},
{
	"word": "hi",
	"group": "H",
	"level": "primary",
},
{
	"word": "high",
	"group": "H",
	"level": "primary",
},
{
	"word": "him",
	"group": "H",
	"level": "primary",
},
{
	"word": "his",
	"group": "H",
	"level": "primary",
},
{
	"word": "holiday",
	"group": "H",
	"level": "primary",
},
{
	"word": "home",
	"group": "H",
	"level": "primary",
},
{
	"word": "horse",
	"group": "H",
	"level": "primary",
},
{
	"word": "hospital",
	"group": "H",
	"level": "primary",
},
{
	"word": "hot",
	"group": "H",
	"level": "primary",
},
{
	"word": "hour",
	"group": "H",
	"level": "primary",
},
{
	"word": "house",
	"group": "H",
	"level": "primary",
},
{
	"word": "how",
	"group": "H",
	"level": "primary",
},
{
	"word": "hungry",
	"group": "H",
	"level": "primary",
},
{
	"word": "I",
	"group": "I",
	"level": "primary",
},
{
	"word": "ice-cream",
	"group": "I",
	"level": "primary",
},
{
	"word": "idea",
	"group": "I",
	"level": "primary",
},
{
	"word": "ill",
	"group": "I",
	"level": "primary",
},
{
	"word": "in",
	"group": "I",
	"level": "primary",
},
{
	"word": "interesting",
	"group": "I",
	"level": "primary",
},
{
	"word": "it",
	"group": "I",
	"level": "primary",
},
{
	"word": "its",
	"group": "I",
	"level": "primary",
},
{
	"word": "juice",
	"group": "J",
	"level": "primary",
},
{
	"word": "jump",
	"group": "J",
	"level": "primary",
},
{
	"word": "kid",
	"group": "K",
	"level": "primary",
},
{
	"word": "kind",
	"group": "K",
	"level": "primary",
},
{
	"word": "kitchen",
	"group": "K",
	"level": "primary",
},
{
	"word": "kite",
	"group": "K",
	"level": "primary",
},
{
	"word": "know",
	"group": "K",
	"level": "primary",
},
{
	"word": "lake",
	"group": "L",
	"level": "primary",
},
{
	"word": "late",
	"group": "L",
	"level": "primary",
},
{
	"word": "left",
	"group": "L",
	"level": "primary",
},
{
	"word": "leg",
	"group": "L",
	"level": "primary",
},
{
	"word": "lesson",
	"group": "L",
	"level": "primary",
},
{
	"word": "let",
	"group": "L",
	"level": "primary",
},
{
	"word": "library",
	"group": "L",
	"level": "primary",
},
{
	"word": "light",
	"group": "L",
	"level": "primary",
},
{
	"word": "like",
	"group": "L",
	"level": "primary",
},
{
	"word": "listen",
	"group": "L",
	"level": "primary",
},
{
	"word": "llittle",
	"group": "L",
	"level": "primary",
},
{
	"word": "live",
	"group": "L",
	"level": "primary",
},
{
	"word": "long",
	"group": "L",
	"level": "primary",
},
{
	"word": "look",
	"group": "L",
	"level": "primary",
},
{
	"word": "love",
	"group": "L",
	"level": "primary",
},
{
	"word": "lunch",
	"group": "L",
	"level": "primary",
},
{
	"word": "make",
	"group": "M",
	"level": "primary",
},
{
	"word": "man",
	"group": "M",
	"level": "primary",
},
{
	"word": "many",
	"group": "M",
	"level": "primary",
},
{
	"word": "map",
	"group": "M",
	"level": "primary",
},
{
	"word": "maths",
	"group": "M",
	"level": "primary",
},
{
	"word": "me",
	"group": "M",
	"level": "primary",
},
{
	"word": "meet",
	"group": "M",
	"level": "primary",
},
{
	"word": "milk",
	"group": "M",
	"level": "primary",
},
{
	"word": "minute",
	"group": "M",
	"level": "primary",
},
{
	"word": "Miss",
	"group": "M",
	"level": "primary",
},
{
	"word": "monkey",
	"group": "M",
	"level": "primary",
},
{
	"word": "month",
	"group": "M",
	"level": "primary",
},
{
	"word": "moon",
	"group": "M",
	"level": "primary",
},
{
	"word": "morning",
	"group": "M",
	"level": "primary",
},
{
	"word": "mother",
	"group": "M",
	"level": "primary",
},
{
	"word": "mouth",
	"group": "M",
	"level": "primary",
},
{
	"word": "Mr",
	"group": "M",
	"level": "primary",
},
{
	"word": "Mrs",
	"group": "M",
	"level": "primary",
},
{
	"word": "Ms",
	"group": "M",
	"level": "primary",
},
{
	"word": "much",
	"group": "M",
	"level": "primary",
},
{
	"word": "mum",
	"group": "M",
	"level": "primary",
},
{
	"word": "music",
	"group": "M",
	"level": "primary",
},
{
	"word": "my",
	"group": "M",
	"level": "primary",
},
{
	"word": "name",
	"group": "N",
	"level": "primary",
},
{
	"word": "near",
	"group": "N",
	"level": "primary",
},
{
	"word": "new",
	"group": "N",
	"level": "primary",
},
{
	"word": "next",
	"group": "N",
	"level": "primary",
},
{
	"word": "nice",
	"group": "N",
	"level": "primary",
},
{
	"word": "night",
	"group": "N",
	"level": "primary",
},
{
	"word": "no",
	"group": "N",
	"level": "primary",
},
{
	"word": "noodle",
	"group": "N",
	"level": "primary",
},
{
	"word": "nose",
	"group": "N",
	"level": "primary",
},
{
	"word": "not",
	"group": "N",
	"level": "primary",
},
{
	"word": "now",
	"group": "N",
	"level": "primary",
},
{
	"word": "nurse",
	"group": "N",
	"level": "primary",
},
{
	"word": "of",
	"group": "O",
	"level": "primary",
},
{
	"word": "often",
	"group": "O",
	"level": "primary",
},
{
	"word": "old",
	"group": "O",
	"level": "primary",
},
{
	"word": "on",
	"group": "O",
	"level": "primary",
},
{
	"word": "open",
	"group": "O",
	"level": "primary",
},
{
	"word": "or",
	"group": "O",
	"level": "primary",
},
{
	"word": "orange",
	"group": "O",
	"level": "primary",
},
{
	"word": "our",
	"group": "O",
	"level": "primary",
},
{
	"word": "panda",
	"group": "P",
	"level": "primary",
},
{
	"word": "parent",
	"group": "P",
	"level": "primary",
},
{
	"word": "park",
	"group": "P",
	"level": "primary",
},
{
	"word": "party",
	"group": "P",
	"level": "primary",
},
{
	"word": "PE",
	"group": "P",
	"level": "primary",
},
{
	"word": "pen",
	"group": "P",
	"level": "primary",
},
{
	"word": "pencil",
	"group": "P",
	"level": "primary",
},
{
	"word": "people",
	"group": "P",
	"level": "primary",
},
{
	"word": "photo",
	"group": "P",
	"level": "primary",
},
{
	"word": "picture",
	"group": "P",
	"level": "primary",
},
{
	"word": "pig",
	"group": "P",
	"level": "primary",
},
{
	"word": "place",
	"group": "P",
	"level": "primary",
},
{
	"word": "plane",
	"group": "P",
	"level": "primary",
},
{
	"word": "plant",
	"group": "P",
	"level": "primary",
},
{
	"word": "play",
	"group": "P",
	"level": "primary",
},
{
	"word": "playground",
	"group": "P",
	"level": "primary",
},
{
	"word": "please",
	"group": "P",
	"level": "primary",
},
{
	"word": "police",
	"group": "P",
	"level": "primary",
},
{
	"word": "potato",
	"group": "P",
	"level": "primary",
},
{
	"word": "pupil",
	"group": "P",
	"level": "primary",
},
{
	"word": "put",
	"group": "P",
	"level": "primary",
},
{
	"word": "rain",
	"group": "R",
	"level": "primary",
},
{
	"word": "read",
	"group": "R",
	"level": "primary",
},
{
	"word": "red",
	"group": "R",
	"level": "primary",
},
{
	"word": "rice",
	"group": "R",
	"level": "primary",
},
{
	"word": "right",
	"group": "R",
	"level": "primary",
},
{
	"word": "river",
	"group": "R",
	"level": "primary",
},
{
	"word": "room",
	"group": "R",
	"level": "primary",
},
{
	"word": "ruler",
	"group": "R",
	"level": "primary",
},
{
	"word": "run",
	"group": "R",
	"level": "primary",
},
{
	"word": "sad",
	"group": "S",
	"level": "primary",
},
{
	"word": "say",
	"group": "S",
	"level": "primary",
},
{
	"word": "school",
	"group": "S",
	"level": "primary",
},
{
	"word": "schoolbag",
	"group": "S",
	"level": "primary",
},
{
	"word": "science",
	"group": "S",
	"level": "primary",
},
{
	"word": "season",
	"group": "S",
	"level": "primary",
},
{
	"word": "see",
	"group": "S",
	"level": "primary",
},
{
	"word": "she",
	"group": "S",
	"level": "primary",
},
{
	"word": "sheep",
	"group": "S",
	"level": "primary",
},
{
	"word": "ship",
	"group": "S",
	"level": "primary",
},
{
	"word": "shirt",
	"group": "S",
	"level": "primary",
},
{
	"word": "shoe",
	"group": "S",
	"level": "primary",
},
{
	"word": "shop",
	"group": "S",
	"level": "primary",
},
{
	"word": "short",
	"group": "S",
	"level": "primary",
},
{
	"word": "shorts",
	"group": "S",
	"level": "primary",
},
{
	"word": "sing",
	"group": "S",
	"level": "primary",
},
{
	"word": "sister",
	"group": "S",
	"level": "primary",
},
{
	"word": "sit",
	"group": "S",
	"level": "primary",
},
{
	"word": "skirt",
	"group": "S",
	"level": "primary",
},
{
	"word": "sleep",
	"group": "S",
	"level": "primary",
},
{
	"word": "slow",
	"group": "S",
	"level": "primary",
},
{
	"word": "small",
	"group": "S",
	"level": "primary",
},
{
	"word": "snow",
	"group": "S",
	"level": "primary",
},
{
	"word": "sock",
	"group": "S",
	"level": "primary",
},
{
	"word": "some",
	"group": "S",
	"level": "primary",
},
{
	"word": "sometimes",
	"group": "S",
	"level": "primary",
},
{
	"word": "song",
	"group": "S",
	"level": "primary",
},
{
	"word": "sorry",
	"group": "S",
	"level": "primary",
},
{
	"word": "soup",
	"group": "S",
	"level": "primary",
},
{
	"word": "speak",
	"group": "S",
	"level": "primary",
},
{
	"word": "sport",
	"group": "S",
	"level": "primary",
},
{
	"word": "spring",
	"group": "S",
	"level": "primary",
},
{
	"word": "stand",
	"group": "S",
	"level": "primary",
},
{
	"word": "star",
	"group": "S",
	"level": "primary",
},
{
	"word": "stop",
	"group": "S",
	"level": "primary",
},
{
	"word": "story",
	"group": "S",
	"level": "primary",
},
{
	"word": "street",
	"group": "S",
	"level": "primary",
},
{
	"word": "strong",
	"group": "S",
	"level": "primary",
},
{
	"word": "study",
	"group": "S",
	"level": "primary",
},
{
	"word": "subject",
	"group": "S",
	"level": "primary",
},
{
	"word": "summer",
	"group": "S",
	"level": "primary",
},
{
	"word": "sun",
	"group": "S",
	"level": "primary",
},
{
	"word": "sunny",
	"group": "S",
	"level": "primary",
},
{
	"word": "supermarket",
	"group": "S",
	"level": "primary",
},
{
	"word": "sweater",
	"group": "S",
	"level": "primary",
},
{
	"word": "swim",
	"group": "S",
	"level": "primary",
},
{
	"word": "table",
	"group": "T",
	"level": "primary",
},
{
	"word": "take",
	"group": "T",
	"level": "primary",
},
{
	"word": "talk",
	"group": "T",
	"level": "primary",
},
{
	"word": "tall",
	"group": "T",
	"level": "primary",
},
{
	"word": "taxi",
	"group": "T",
	"level": "primary",
},
{
	"word": "tea",
	"group": "T",
	"level": "primary",
},
{
	"word": "teacher",
	"group": "T",
	"level": "primary",
},
{
	"word": "tell",
	"group": "T",
	"level": "primary",
},
{
	"word": "thank",
	"group": "T",
	"level": "primary",
},
{
	"word": "that",
	"group": "T",
	"level": "primary",
},
{
	"word": "the",
	"group": "T",
	"level": "primary",
},
{
	"word": "their",
	"group": "T",
	"level": "primary",
},
{
	"word": "them",
	"group": "T",
	"level": "primary",
},
{
	"word": "then",
	"group": "T",
	"level": "primary",
},
{
	"word": "there",
	"group": "T",
	"level": "primary",
},
{
	"word": "these",
	"group": "T",
	"level": "primary",
},
{
	"word": "they",
	"group": "T",
	"level": "primary",
},
{
	"word": "thin",
	"group": "T",
	"level": "primary",
},
{
	"word": "think",
	"group": "T",
	"level": "primary",
},
{
	"word": "this",
	"group": "T",
	"level": "primary",
},
{
	"word": "those",
	"group": "T",
	"level": "primary",
},
{
	"word": "tiger",
	"group": "T",
	"level": "primary",
},
{
	"word": "time",
	"group": "T",
	"level": "primary",
},
{
	"word": "tired",
	"group": "T",
	"level": "primary",
},
{
	"word": "to",
	"group": "T",
	"level": "primary",
},
{
	"word": "today",
	"group": "T",
	"level": "primary",
},
{
	"word": "toilet",
	"group": "T",
	"level": "primary",
},
{
	"word": "tomato",
	"group": "T",
	"level": "primary",
},
{
	"word": "tomorrow",
	"group": "T",
	"level": "primary",
},
{
	"word": "too",
	"group": "T",
	"level": "primary",
},
{
	"word": "toy",
	"group": "T",
	"level": "primary",
},
{
	"word": "train",
	"group": "T",
	"level": "primary",
},
{
	"word": "travel",
	"group": "T",
	"level": "primary",
},
{
	"word": "tree",
	"group": "T",
	"level": "primary",
},
{
	"word": "trousers",
	"group": "T",
	"level": "primary",
},
{
	"word": "try",
	"group": "T",
	"level": "primary",
},
{
	"word": "turn",
	"group": "T",
	"level": "primary",
},
{
	"word": "TV",
	"group": "T",
	"level": "primary",
},
{
	"word": "umbrella",
	"group": "U",
	"level": "primary",
},
{
	"word": "uncle",
	"group": "U",
	"level": "primary",
},
{
	"word": "under",
	"group": "U",
	"level": "primary",
},
{
	"word": "up",
	"group": "U",
	"level": "primary",
},
{
	"word": "us",
	"group": "U",
	"level": "primary",
},
{
	"word": "use",
	"group": "U",
	"level": "primary",
},
{
	"word": "vegetable",
	"group": "V",
	"level": "primary",
},
{
	"word": "very",
	"group": "V",
	"level": "primary",
},
{
	"word": "visit",
	"group": "V",
	"level": "primary",
},
{
	"word": "wait",
	"group": "W",
	"level": "primary",
},
{
	"word": "walk",
	"group": "W",
	"level": "primary",
},
{
	"word": "want",
	"group": "W",
	"level": "primary",
},
{
	"word": "warm",
	"group": "W",
	"level": "primary",
},
{
	"word": "wash",
	"group": "W",
	"level": "primary",
},
{
	"word": "watch",
	"group": "W",
	"level": "primary",
},
{
	"word": "water",
	"group": "W",
	"level": "primary",
},
{
	"word": "way",
	"group": "W",
	"level": "primary",
},
{
	"word": "we",
	"group": "W",
	"level": "primary",
},
{
	"word": "wear",
	"group": "W",
	"level": "primary",
},
{
	"word": "weather",
	"group": "W",
	"level": "primary",
},
{
	"word": "week",
	"group": "W",
	"level": "primary",
},
{
	"word": "welcome",
	"group": "W",
	"level": "primary",
},
{
	"word": "well",
	"group": "W",
	"level": "primary",
},
{
	"word": "what",
	"group": "W",
	"level": "primary",
},
{
	"word": "when",
	"group": "W",
	"level": "primary",
},
{
	"word": "where",
	"group": "W",
	"level": "primary",
},
{
	"word": "white",
	"group": "W",
	"level": "primary",
},
{
	"word": "who",
	"group": "W",
	"level": "primary",
},
{
	"word": "whose",
	"group": "W",
	"level": "primary",
},
{
	"word": "why",
	"group": "W",
	"level": "primary",
},
{
	"word": "window",
	"group": "W",
	"level": "primary",
},
{
	"word": "windy",
	"group": "W",
	"level": "primary",
},
{
	"word": "winter",
	"group": "W",
	"level": "primary",
},
{
	"word": "with",
	"group": "W",
	"level": "primary",
},
{
	"word": "woman",
	"group": "W",
	"level": "primary",
},
{
	"word": "wonderful",
	"group": "W",
	"level": "primary",
},
{
	"word": "word",
	"group": "W",
	"level": "primary",
},
{
	"word": "work",
	"group": "W",
	"level": "primary",
},
{
	"word": "worker",
	"group": "W",
	"level": "primary",
},
{
	"word": "worry",
	"group": "W",
	"level": "primary",
},
{
	"word": "write",
	"group": "W",
	"level": "primary",
},
{
	"word": "wrong",
	"group": "W",
	"level": "primary",
},
{
	"word": "year",
	"group": "Y",
	"level": "primary",
},
{
	"word": "yellow",
	"group": "Y",
	"level": "primary",
},
{
	"word": "yes",
	"group": "Y",
	"level": "primary",
},
{
	"word": "yesterday",
	"group": "Y",
	"level": "primary",
},
{
	"word": "you",
	"group": "Y",
	"level": "primary",
},
{
	"word": "young",
	"group": "Y",
	"level": "primary",
},
{
	"word": "your",
	"group": "Y",
	"level": "primary",
},
{
	"word": "zoo",
	"group": "Z",
	"level": "primary",
},
{
	"word": "ability",
	"group": "A",
	"level": "middle",
},
{
	"word": "able",
	"group": "A",
	"level": "middle",
},
{
	"word": "above",
	"group": "A",
	"level": "middle",
},
{
	"word": "abroad",
	"group": "A",
	"level": "middle",
},
{
	"word": "absent",
	"group": "A",
	"level": "middle",
},
{
	"word": "accept",
	"group": "A",
	"level": "middle",
},
{
	"word": "according-to",
	"group": "A",
	"level": "middle",
},
{
	"word": "achieve",
	"group": "A",
	"level": "middle",
},
{
	"word": "across",
	"group": "A",
	"level": "middle",
},
{
	"word": "act",
	"group": "A",
	"level": "middle",
},
{
	"word": "action",
	"group": "A",
	"level": "middle",
},
{
	"word": "active",
	"group": "A",
	"level": "middle",
},
{
	"word": "activity",
	"group": "A",
	"level": "middle",
},
{
	"word": "actor",
	"group": "A",
	"level": "middle",
},
{
	"word": "actress",
	"group": "A",
	"level": "middle",
},
{
	"word": "add",
	"group": "A",
	"level": "middle",
},
{
	"word": "address",
	"group": "A",
	"level": "middle",
},
{
	"word": "advantage",
	"group": "A",
	"level": "middle",
},
{
	"word": "advice",
	"group": "A",
	"level": "middle",
},
{
	"word": "advise",
	"group": "A",
	"level": "middle",
},
{
	"word": "afford",
	"group": "A",
	"level": "middle",
},
{
	"word": "Africa",
	"group": "A",
	"level": "middle",
},
{
	"word": "African",
	"group": "A",
	"level": "middle",
},
{
	"word": "against",
	"group": "A",
	"level": "middle",
},
{
	"word": "age",
	"group": "A",
	"level": "middle",
},
{
	"word": "ago",
	"group": "A",
	"level": "middle",
},
{
	"word": "agree",
	"group": "A",
	"level": "middle",
},
{
	"word": "agreement",
	"group": "A",
	"level": "middle",
},
{
	"word": "air",
	"group": "A",
	"level": "middle",
},
{
	"word": "airport",
	"group": "A",
	"level": "middle",
},
{
	"word": "alive",
	"group": "A",
	"level": "middle",
},
{
	"word": "allow",
	"group": "A",
	"level": "middle",
},
{
	"word": "almost",
	"group": "A",
	"level": "middle",
},
{
	"word": "alone",
	"group": "A",
	"level": "middle",
},
{
	"word": "along",
	"group": "A",
	"level": "middle",
},
{
	"word": "aloud",
	"group": "A",
	"level": "middle",
},
{
	"word": "already",
	"group": "A",
	"level": "middle",
},
{
	"word": "although",
	"group": "A",
	"level": "middle",
},
{
	"word": "America",
	"group": "A",
	"level": "middle",
},
{
	"word": "American",
	"group": "A",
	"level": "middle",
},
{
	"word": "among",
	"group": "A",
	"level": "middle",
},
{
	"word": "ancient",
	"group": "A",
	"level": "middle",
},
{
	"word": "another",
	"group": "A",
	"level": "middle",
},
{
	"word": "ant",
	"group": "A",
	"level": "middle",
},
{
	"word": "anybody",
	"group": "A",
	"level": "middle",
},
{
	"word": "anyone",
	"group": "A",
	"level": "middle",
},
{
	"word": "anything",
	"group": "A",
	"level": "middle",
},
{
	"word": "anyway",
	"group": "A",
	"level": "middle",
},
{
	"word": "anywhere",
	"group": "A",
	"level": "middle",
},
{
	"word": "appear",
	"group": "A",
	"level": "middle",
},
{
	"word": "April",
	"group": "A",
	"level": "middle",
},
{
	"word": "area",
	"group": "A",
	"level": "middle",
},
{
	"word": "army",
	"group": "A",
	"level": "middle",
},
{
	"word": "around",
	"group": "A",
	"level": "middle",
},
{
	"word": "arrive",
	"group": "A",
	"level": "middle",
},
{
	"word": "article",
	"group": "A",
	"level": "middle",
},
{
	"word": "artist",
	"group": "A",
	"level": "middle",
},
{
	"word": "as",
	"group": "A",
	"level": "middle",
},
{
	"word": "Asia",
	"group": "A",
	"level": "middle",
},
{
	"word": "Asian",
	"group": "A",
	"level": "middle",
},
{
	"word": "asleep",
	"group": "A",
	"level": "middle",
},
{
	"word": "attend",
	"group": "A",
	"level": "middle",
},
{
	"word": "attention",
	"group": "A",
	"level": "middle",
},
{
	"word": "August",
	"group": "A",
	"level": "middle",
},
{
	"word": "Australia",
	"group": "A",
	"level": "middle",
},
{
	"word": "Australian",
	"group": "A",
	"level": "middle",
},
{
	"word": "avoid",
	"group": "A",
	"level": "middle",
},
{
	"word": "awake",
	"group": "A",
	"level": "middle",
},
{
	"word": "away",
	"group": "A",
	"level": "middle",
},
{
	"word": "awful",
	"group": "A",
	"level": "middle",
},
{
	"word": "background",
	"group": "B",
	"level": "middle",
},
{
	"word": "balloon",
	"group": "B",
	"level": "middle",
},
{
	"word": "bamboo",
	"group": "B",
	"level": "middle",
},
{
	"word": "bank",
	"group": "B",
	"level": "middle",
},
{
	"word": "baseball",
	"group": "B",
	"level": "middle",
},
{
	"word": "basic",
	"group": "B",
	"level": "middle",
},
{
	"word": "basket",
	"group": "B",
	"level": "middle",
},
{
	"word": "bathroom",
	"group": "B",
	"level": "middle",
},
{
	"word": "beach",
	"group": "B",
	"level": "middle",
},
{
	"word": "bean",
	"group": "B",
	"level": "middle",
},
{
	"word": "beat",
	"group": "B",
	"level": "middle",
},
{
	"word": "because",
	"group": "B",
	"level": "middle",
},
{
	"word": "become",
	"group": "B",
	"level": "middle",
},
{
	"word": "bedroom",
	"group": "B",
	"level": "middle",
},
{
	"word": "beef",
	"group": "B",
	"level": "middle",
},
{
	"word": "believe",
	"group": "B",
	"level": "middle",
},
{
	"word": "bell",
	"group": "B",
	"level": "middle",
},
{
	"word": "below",
	"group": "B",
	"level": "middle",
},
{
	"word": "best",
	"group": "B",
	"level": "middle",
},
{
	"word": "better",
	"group": "B",
	"level": "middle",
},
{
	"word": "bill",
	"group": "B",
	"level": "middle",
},
{
	"word": "birth",
	"group": "B",
	"level": "middle",
},
{
	"word": "biscuit",
	"group": "B",
	"level": "middle",
},
{
	"word": "bit",
	"group": "B",
	"level": "middle",
},
{
	"word": "blind",
	"group": "B",
	"level": "middle",
},
{
	"word": "block",
	"group": "B",
	"level": "middle",
},
{
	"word": "blood",
	"group": "B",
	"level": "middle",
},
{
	"word": "blouse",
	"group": "B",
	"level": "middle",
},
{
	"word": "blow",
	"group": "B",
	"level": "middle",
},
{
	"word": "board",
	"group": "B",
	"level": "middle",
},
{
	"word": "bored",
	"group": "B",
	"level": "middle",
},
{
	"word": "boring",
	"group": "B",
	"level": "middle",
},
{
	"word": "born",
	"group": "B",
	"level": "middle",
},
{
	"word": "borrow",
	"group": "B",
	"level": "middle",
},
{
	"word": "boss",
	"group": "B",
	"level": "middle",
},
{
	"word": "both",
	"group": "B",
	"level": "middle",
},
{
	"word": "bottle",
	"group": "B",
	"level": "middle",
},
{
	"word": "bottom",
	"group": "B",
	"level": "middle",
},
{
	"word": "bowl",
	"group": "B",
	"level": "middle",
},
{
	"word": "brain",
	"group": "B",
	"level": "middle",
},
{
	"word": "brave",
	"group": "B",
	"level": "middle",
},
{
	"word": "break",
	"group": "B",
	"level": "middle",
},
{
	"word": "bridge",
	"group": "B",
	"level": "middle",
},
{
	"word": "bright",
	"group": "B",
	"level": "middle",
},
{
	"word": "Britain",
	"group": "B",
	"level": "middle",
},
{
	"word": "British",
	"group": "B",
	"level": "middle",
},
{
	"word": "brush",
	"group": "B",
	"level": "middle",
},
{
	"word": "build",
	"group": "B",
	"level": "middle",
},
{
	"word": "building",
	"group": "B",
	"level": "middle",
},
{
	"word": "burn",
	"group": "B",
	"level": "middle",
},
{
	"word": "business",
	"group": "B",
	"level": "middle",
},
{
	"word": "calendar",
	"group": "C",
	"level": "middle",
},
{
	"word": "camera",
	"group": "C",
	"level": "middle",
},
{
	"word": "camp",
	"group": "C",
	"level": "middle",
},
{
	"word": "Canada",
	"group": "C",
	"level": "middle",
},
{
	"word": "Canadian",
	"group": "C",
	"level": "middle",
},
{
	"word": "cancel",
	"group": "C",
	"level": "middle",
},
{
	"word": "candle",
	"group": "C",
	"level": "middle",
},
{
	"word": "capital",
	"group": "C",
	"level": "middle",
},
{
	"word": "care",
	"group": "C",
	"level": "middle",
},
{
	"word": "careful",
	"group": "C",
	"level": "middle",
},
{
	"word": "careless",
	"group": "C",
	"level": "middle",
},
{
	"word": "carrot",
	"group": "C",
	"level": "middle",
},
{
	"word": "carry",
	"group": "C",
	"level": "middle",
},
{
	"word": "cartoon",
	"group": "C",
	"level": "middle",
},
{
	"word": "catch",
	"group": "C",
	"level": "middle",
},
{
	"word": "cause",
	"group": "C",
	"level": "middle",
},
{
	"word": "celebrate",
	"group": "C",
	"level": "middle",
},
{
	"word": "cent",
	"group": "C",
	"level": "middle",
},
{
	"word": "central",
	"group": "C",
	"level": "middle",
},
{
	"word": "centre",
	"group": "C",
	"level": "middle",
},
{
	"word": "century",
	"group": "C",
	"level": "middle",
},
{
	"word": "certain",
	"group": "C",
	"level": "middle",
},
{
	"word": "certainly",
	"group": "C",
	"level": "middle",
},
{
	"word": "chalk",
	"group": "C",
	"level": "middle",
},
{
	"word": "chance",
	"group": "C",
	"level": "middle",
},
{
	"word": "change",
	"group": "C",
	"level": "middle",
},
{
	"word": "cheap",
	"group": "C",
	"level": "middle",
},
{
	"word": "check",
	"group": "C",
	"level": "middle",
},
{
	"word": "cheer",
	"group": "C",
	"level": "middle",
},
{
	"word": "chemistry",
	"group": "C",
	"level": "middle",
},
{
	"word": "chess",
	"group": "C",
	"level": "middle",
},
{
	"word": "chocolate",
	"group": "C",
	"level": "middle",
},
{
	"word": "choice",
	"group": "C",
	"level": "middle",
},
{
	"word": "choose",
	"group": "C",
	"level": "middle",
},
{
	"word": "chopsticks",
	"group": "C",
	"level": "middle",
},
{
	"word": "Christmas",
	"group": "C",
	"level": "middle",
},
{
	"word": "circle",
	"group": "C",
	"level": "middle",
},
{
	"word": "classmate",
	"group": "C",
	"level": "middle",
},
{
	"word": "classroom",
	"group": "C",
	"level": "middle",
},
{
	"word": "clear",
	"group": "C",
	"level": "middle",
},
{
	"word": "climb",
	"group": "C",
	"level": "middle",
},
{
	"word": "cloud",
	"group": "C",
	"level": "middle",
},
{
	"word": "club",
	"group": "C",
	"level": "middle",
},
{
	"word": "coach",
	"group": "C",
	"level": "middle",
},
{
	"word": "coal",
	"group": "C",
	"level": "middle",
},
{
	"word": "coast",
	"group": "C",
	"level": "middle",
},
{
	"word": "coffee",
	"group": "C",
	"level": "middle",
},
{
	"word": "coin",
	"group": "C",
	"level": "middle",
},
{
	"word": "collect",
	"group": "C",
	"level": "middle",
},
{
	"word": "college",
	"group": "C",
	"level": "middle",
},
{
	"word": "comfortable",
	"group": "C",
	"level": "middle",
},
{
	"word": "common",
	"group": "C",
	"level": "middle",
},
{
	"word": "communicate",
	"group": "C",
	"level": "middle",
},
{
	"word": "communication",
	"group": "C",
	"level": "middle",
},
{
	"word": "community",
	"group": "C",
	"level": "middle",
},
{
	"word": "compare",
	"group": "C",
	"level": "middle",
},
{
	"word": "competition",
	"group": "C",
	"level": "middle",
},
{
	"word": "complete",
	"group": "C",
	"level": "middle",
},
{
	"word": "concert",
	"group": "C",
	"level": "middle",
},
{
	"word": "condition",
	"group": "C",
	"level": "middle",
},
{
	"word": "connect",
	"group": "C",
	"level": "middle",
},
{
	"word": "consider",
	"group": "C",
	"level": "middle",
},
{
	"word": "continue",
	"group": "C",
	"level": "middle",
},
{
	"word": "control",
	"group": "C",
	"level": "middle",
},
{
	"word": "conversation",
	"group": "C",
	"level": "middle",
},
{
	"word": "cookie",
	"group": "C",
	"level": "middle",
},
{
	"word": "copy",
	"group": "C",
	"level": "middle",
},
{
	"word": "corn",
	"group": "C",
	"level": "middle",
},
{
	"word": "corner",
	"group": "C",
	"level": "middle",
},
{
	"word": "correct",
	"group": "C",
	"level": "middle",
},
{
	"word": "cost",
	"group": "C",
	"level": "middle",
},
{
	"word": "cough",
	"group": "C",
	"level": "middle",
},
{
	"word": "could",
	"group": "C",
	"level": "middle",
},
{
	"word": "count",
	"group": "C",
	"level": "middle",
},
{
	"word": "country",
	"group": "C",
	"level": "middle",
},
{
	"word": "countryside",
	"group": "C",
	"level": "middle",
},
{
	"word": "couple",
	"group": "C",
	"level": "middle",
},
{
	"word": "courage",
	"group": "C",
	"level": "middle",
},
{
	"word": "course",
	"group": "C",
	"level": "middle",
},
{
	"word": "cover",
	"group": "C",
	"level": "middle",
},
{
	"word": "crazy",
	"group": "C",
	"level": "middle",
},
{
	"word": "create",
	"group": "C",
	"level": "middle",
},
{
	"word": "cross",
	"group": "C",
	"level": "middle",
},
{
	"word": "culture",
	"group": "C",
	"level": "middle",
},
{
	"word": "cup",
	"group": "C",
	"level": "middle",
},
{
	"word": "customer",
	"group": "C",
	"level": "middle",
},
{
	"word": "cut",
	"group": "C",
	"level": "middle",
},
{
	"word": "cute",
	"group": "C",
	"level": "middle",
},
{
	"word": "d",
	"group": "D",
	"level": "middle",
},
{
	"word": "daily",
	"group": "D",
	"level": "middle",
},
{
	"word": "danger",
	"group": "D",
	"level": "middle",
},
{
	"word": "dangerous",
	"group": "D",
	"level": "middle",
},
{
	"word": "dark",
	"group": "D",
	"level": "middle",
},
{
	"word": "date",
	"group": "D",
	"level": "middle",
},
{
	"word": "daughter",
	"group": "D",
	"level": "middle",
},
{
	"word": "dead",
	"group": "D",
	"level": "middle",
},
{
	"word": "deaf",
	"group": "D",
	"level": "middle",
},
{
	"word": "deal",
	"group": "D",
	"level": "middle",
},
{
	"word": "December",
	"group": "D",
	"level": "middle",
},
{
	"word": "decide",
	"group": "D",
	"level": "middle",
},
{
	"word": "decision",
	"group": "D",
	"level": "middle",
},
{
	"word": "deep",
	"group": "D",
	"level": "middle",
},
{
	"word": "degree",
	"group": "D",
	"level": "middle",
},
{
	"word": "delicious",
	"group": "D",
	"level": "middle",
},
{
	"word": "depend",
	"group": "D",
	"level": "middle",
},
{
	"word": "describe",
	"group": "D",
	"level": "middle",
},
{
	"word": "develop",
	"group": "D",
	"level": "middle",
},
{
	"word": "development",
	"group": "D",
	"level": "middle",
},
{
	"word": "dialogue",
	"group": "D",
	"level": "middle",
},
{
	"word": "diary",
	"group": "D",
	"level": "middle",
},
{
	"word": "dictionary",
	"group": "D",
	"level": "middle",
},
{
	"word": "die",
	"group": "D",
	"level": "middle",
},
{
	"word": "difference",
	"group": "D",
	"level": "middle",
},
{
	"word": "different",
	"group": "D",
	"level": "middle",
},
{
	"word": "difficulty",
	"group": "D",
	"level": "middle",
},
{
	"word": "dig",
	"group": "D",
	"level": "middle",
},
{
	"word": "dining",
	"group": "D",
	"level": "middle",
},
{
	"word": "direct",
	"group": "D",
	"level": "middle",
},
{
	"word": "direction",
	"group": "D",
	"level": "middle",
},
{
	"word": "director",
	"group": "D",
	"level": "middle",
},
{
	"word": "discover",
	"group": "D",
	"level": "middle",
},
{
	"word": "discovery",
	"group": "D",
	"level": "middle",
},
{
	"word": "discuss",
	"group": "D",
	"level": "middle",
},
{
	"word": "discussion",
	"group": "D",
	"level": "middle",
},
{
	"word": "dish",
	"group": "D",
	"level": "middle",
},
{
	"word": "divide",
	"group": "D",
	"level": "middle",
},
{
	"word": "dollar",
	"group": "D",
	"level": "middle",
},
{
	"word": "double",
	"group": "D",
	"level": "middle",
},
{
	"word": "doubt",
	"group": "D",
	"level": "middle",
},
{
	"word": "dream",
	"group": "D",
	"level": "middle",
},
{
	"word": "drive",
	"group": "D",
	"level": "middle",
},
{
	"word": "drop",
	"group": "D",
	"level": "middle",
},
{
	"word": "dry",
	"group": "D",
	"level": "middle",
},
{
	"word": "dumpling",
	"group": "D",
	"level": "middle",
},
{
	"word": "during",
	"group": "D",
	"level": "middle",
},
{
	"word": "each",
	"group": "E",
	"level": "middle",
},
{
	"word": "earth",
	"group": "E",
	"level": "middle",
},
{
	"word": "earthquake",
	"group": "E",
	"level": "middle",
},
{
	"word": "east",
	"group": "E",
	"level": "middle",
},
{
	"word": "eastern",
	"group": "E",
	"level": "middle",
},
{
	"word": "education",
	"group": "E",
	"level": "middle",
},
{
	"word": "eight",
	"group": "E",
	"level": "middle",
},
{
	"word": "eighteen",
	"group": "E",
	"level": "middle",
},
{
	"word": "eighth",
	"group": "E",
	"level": "middle",
},
{
	"word": "eighty",
	"group": "E",
	"level": "middle",
},
{
	"word": "either",
	"group": "E",
	"level": "middle",
},
{
	"word": "elder",
	"group": "E",
	"level": "middle",
},
{
	"word": "electronic",
	"group": "E",
	"level": "middle",
},
{
	"word": "eleven",
	"group": "E",
	"level": "middle",
},
{
	"word": "else",
	"group": "E",
	"level": "middle",
},
{
	"word": "empty",
	"group": "E",
	"level": "middle",
},
{
	"word": "encourage",
	"group": "E",
	"level": "middle",
},
{
	"word": "end",
	"group": "E",
	"level": "middle",
},
{
	"word": "enemy",
	"group": "E",
	"level": "middle",
},
{
	"word": "engineer",
	"group": "E",
	"level": "middle",
},
{
	"word": "England",
	"group": "E",
	"level": "middle",
},
{
	"word": "enjoy",
	"group": "E",
	"level": "middle",
},
{
	"word": "enough",
	"group": "E",
	"level": "middle",
},
{
	"word": "enter",
	"group": "E",
	"level": "middle",
},
{
	"word": "environment",
	"group": "E",
	"level": "middle",
},
{
	"word": "eraser",
	"group": "E",
	"level": "middle",
},
{
	"word": "especially",
	"group": "E",
	"level": "middle",
},
{
	"word": "Europe",
	"group": "E",
	"level": "middle",
},
{
	"word": "European",
	"group": "E",
	"level": "middle",
},
{
	"word": "even",
	"group": "E",
	"level": "middle",
},
{
	"word": "ever",
	"group": "E",
	"level": "middle",
},
{
	"word": "everybody",
	"group": "E",
	"level": "middle",
},
{
	"word": "everyday",
	"group": "E",
	"level": "middle",
},
{
	"word": "everyone",
	"group": "E",
	"level": "middle",
},
{
	"word": "everything",
	"group": "E",
	"level": "middle",
},
{
	"word": "everywhere",
	"group": "E",
	"level": "middle",
},
{
	"word": "exactly",
	"group": "E",
	"level": "middle",
},
{
	"word": "exam",
	"group": "E",
	"level": "middle",
},
{
	"word": "example",
	"group": "E",
	"level": "middle",
},
{
	"word": "excellent",
	"group": "E",
	"level": "middle",
},
{
	"word": "except",
	"group": "E",
	"level": "middle",
},
{
	"word": "excited",
	"group": "E",
	"level": "middle",
},
{
	"word": "exciting",
	"group": "E",
	"level": "middle",
},
{
	"word": "excuse",
	"group": "E",
	"level": "middle",
},
{
	"word": "expect",
	"group": "E",
	"level": "middle",
},
{
	"word": "expensive",
	"group": "E",
	"level": "middle",
},
{
	"word": "experience",
	"group": "E",
	"level": "middle",
},
{
	"word": "explain",
	"group": "E",
	"level": "middle",
},
{
	"word": "express",
	"group": "E",
	"level": "middle",
},
{
	"word": "eyeface",
	"group": "E",
	"level": "middle",
},
{
	"word": "fact",
	"group": "F",
	"level": "middle",
},
{
	"word": "factory",
	"group": "F",
	"level": "middle",
},
{
	"word": "fail",
	"group": "F",
	"level": "middle",
},
{
	"word": "fair",
	"group": "F",
	"level": "middle",
},
{
	"word": "fall",
	"group": "F",
	"level": "middle",
},
{
	"word": "famous",
	"group": "F",
	"level": "middle",
},
{
	"word": "fantastic",
	"group": "F",
	"level": "middle",
},
{
	"word": "fat",
	"group": "F",
	"level": "middle",
},
{
	"word": "fear",
	"group": "F",
	"level": "middle",
},
{
	"word": "February",
	"group": "F",
	"level": "middle",
},
{
	"word": "feed",
	"group": "F",
	"level": "middle",
},
{
	"word": "feeling",
	"group": "F",
	"level": "middle",
},
{
	"word": "festival",
	"group": "F",
	"level": "middle",
},
{
	"word": "fever",
	"group": "F",
	"level": "middle",
},
{
	"word": "few",
	"group": "F",
	"level": "middle",
},
{
	"word": "field",
	"group": "F",
	"level": "middle",
},
{
	"word": "fifteen",
	"group": "F",
	"level": "middle",
},
{
	"word": "fifth",
	"group": "F",
	"level": "middle",
},
{
	"word": "fifty",
	"group": "F",
	"level": "middle",
},
{
	"word": "fight",
	"group": "F",
	"level": "middle",
},
{
	"word": "fill",
	"group": "F",
	"level": "middle",
},
{
	"word": "finally",
	"group": "F",
	"level": "middle",
},
{
	"word": "finger",
	"group": "F",
	"level": "middle",
},
{
	"word": "finish",
	"group": "F",
	"level": "middle",
},
{
	"word": "fire",
	"group": "F",
	"level": "middle",
},
{
	"word": "first",
	"group": "F",
	"level": "middle",
},
{
	"word": "fisherman",
	"group": "F",
	"level": "middle",
},
{
	"word": "fit",
	"group": "F",
	"level": "middle",
},
{
	"word": "five",
	"group": "F",
	"level": "middle",
},
{
	"word": "fix",
	"group": "F",
	"level": "middle",
},
{
	"word": "flag",
	"group": "F",
	"level": "middle",
},
{
	"word": "follow",
	"group": "F",
	"level": "middle",
},
{
	"word": "force",
	"group": "F",
	"level": "middle",
},
{
	"word": "foreign",
	"group": "F",
	"level": "middle",
},
{
	"word": "forest",
	"group": "F",
	"level": "middle",
},
{
	"word": "forget",
	"group": "F",
	"level": "middle",
},
{
	"word": "fork",
	"group": "F",
	"level": "middle",
},
{
	"word": "form",
	"group": "F",
	"level": "middle",
},
{
	"word": "forty",
	"group": "F",
	"level": "middle",
},
{
	"word": "four",
	"group": "F",
	"level": "middle",
},
{
	"word": "fourteen",
	"group": "F",
	"level": "middle",
},
{
	"word": "fourth",
	"group": "F",
	"level": "middle",
},
{
	"word": "France",
	"group": "F",
	"level": "middle",
},
{
	"word": "free",
	"group": "F",
	"level": "middle",
},
{
	"word": "French",
	"group": "F",
	"level": "middle",
},
{
	"word": "fresh",
	"group": "F",
	"level": "middle",
},
{
	"word": "Friday",
	"group": "F",
	"level": "middle",
},
{
	"word": "fridge",
	"group": "F",
	"level": "middle",
},
{
	"word": "friendly",
	"group": "F",
	"level": "middle",
},
{
	"word": "friendship",
	"group": "F",
	"level": "middle",
},
{
	"word": "front",
	"group": "F",
	"level": "middle",
},
{
	"word": "full",
	"group": "F",
	"level": "middle",
},
{
	"word": "fun",
	"group": "F",
	"level": "middle",
},
{
	"word": "funny",
	"group": "F",
	"level": "middle",
},
{
	"word": "future",
	"group": "F",
	"level": "middle",
},
{
	"word": "garden",
	"group": "G",
	"level": "middle",
},
{
	"word": "gate",
	"group": "G",
	"level": "middle",
},
{
	"word": "general",
	"group": "G",
	"level": "middle",
},
{
	"word": "gentleman",
	"group": "G",
	"level": "middle",
},
{
	"word": "geography",
	"group": "G",
	"level": "middle",
},
{
	"word": "German",
	"group": "G",
	"level": "middle",
},
{
	"word": "Germany",
	"group": "G",
	"level": "middle",
},
{
	"word": "gift",
	"group": "G",
	"level": "middle",
},
{
	"word": "giraffe",
	"group": "G",
	"level": "middle",
},
{
	"word": "glad",
	"group": "G",
	"level": "middle",
},
{
	"word": "glass",
	"group": "G",
	"level": "middle",
},
{
	"word": "glove",
	"group": "G",
	"level": "middle",
},
{
	"word": "glue",
	"group": "G",
	"level": "middle",
},
{
	"word": "gold",
	"group": "G",
	"level": "middle",
},
{
	"word": "government",
	"group": "G",
	"level": "middle",
},
{
	"word": "grade",
	"group": "G",
	"level": "middle",
},
{
	"word": "grammar",
	"group": "G",
	"level": "middle",
},
{
	"word": "granddaughter",
	"group": "G",
	"level": "middle",
},
{
	"word": "grandparent",
	"group": "G",
	"level": "middle",
},
{
	"word": "grandson",
	"group": "G",
	"level": "middle",
},
{
	"word": "grape",
	"group": "G",
	"level": "middle",
},
{
	"word": "grey",
	"group": "G",
	"level": "middle",
},
{
	"word": "ground",
	"group": "G",
	"level": "middle",
},
{
	"word": "group",
	"group": "G",
	"level": "middle",
},
{
	"word": "grow",
	"group": "G",
	"level": "middle",
},
{
	"word": "guard",
	"group": "G",
	"level": "middle",
},
{
	"word": "guess",
	"group": "G",
	"level": "middle",
},
{
	"word": "guest",
	"group": "G",
	"level": "middle",
},
{
	"word": "guide",
	"group": "G",
	"level": "middle",
},
{
	"word": "guitar",
	"group": "G",
	"level": "middle",
},
{
	"word": "gun",
	"group": "G",
	"level": "middle",
},
{
	"word": "habit",
	"group": "H",
	"level": "middle",
},
{
	"word": "hall",
	"group": "H",
	"level": "middle",
},
{
	"word": "hamburger",
	"group": "H",
	"level": "middle",
},
{
	"word": "handbag",
	"group": "H",
	"level": "middle",
},
{
	"word": "handsome",
	"group": "H",
	"level": "middle",
},
{
	"word": "hang",
	"group": "H",
	"level": "middle",
},
{
	"word": "happen",
	"group": "H",
	"level": "middle",
},
{
	"word": "hard",
	"group": "H",
	"level": "middle",
},
{
	"word": "hardly",
	"group": "H",
	"level": "middle",
},
{
	"word": "harmful",
	"group": "H",
	"level": "middle",
},
{
	"word": "hat",
	"group": "H",
	"level": "middle",
},
{
	"word": "hate",
	"group": "H",
	"level": "middle",
},
{
	"word": "headache",
	"group": "H",
	"level": "middle",
},
{
	"word": "health",
	"group": "H",
	"level": "middle",
},
{
	"word": "heart",
	"group": "H",
	"level": "middle",
},
{
	"word": "heat",
	"group": "H",
	"level": "middle",
},
{
	"word": "height",
	"group": "H",
	"level": "middle",
},
{
	"word": "helpful",
	"group": "H",
	"level": "middle",
},
{
	"word": "hen",
	"group": "H",
	"level": "middle",
},
{
	"word": "hero",
	"group": "H",
	"level": "middle",
},
{
	"word": "hers",
	"group": "H",
	"level": "middle",
},
{
	"word": "herself",
	"group": "H",
	"level": "middle",
},
{
	"word": "hide",
	"group": "H",
	"level": "middle",
},
{
	"word": "hill",
	"group": "H",
	"level": "middle",
},
{
	"word": "himself",
	"group": "H",
	"level": "middle",
},
{
	"word": "history",
	"group": "H",
	"level": "middle",
},
{
	"word": "hit",
	"group": "H",
	"level": "middle",
},
{
	"word": "hobby",
	"group": "H",
	"level": "middle",
},
{
	"word": "hold",
	"group": "H",
	"level": "middle",
},
{
	"word": "hole",
	"group": "H",
	"level": "middle",
},
{
	"word": "hometown",
	"group": "H",
	"level": "middle",
},
{
	"word": "homework",
	"group": "H",
	"level": "middle",
},
{
	"word": "honest",
	"group": "H",
	"level": "middle",
},
{
	"word": "hope",
	"group": "H",
	"level": "middle",
},
{
	"word": "hotel",
	"group": "H",
	"level": "middle",
},
{
	"word": "housework",
	"group": "H",
	"level": "middle",
},
{
	"word": "however",
	"group": "H",
	"level": "middle",
},
{
	"word": "huge",
	"group": "H",
	"level": "middle",
},
{
	"word": "human",
	"group": "H",
	"level": "middle",
},
{
	"word": "humorous",
	"group": "H",
	"level": "middle",
},
{
	"word": "hundred",
	"group": "H",
	"level": "middle",
},
{
	"word": "hurry",
	"group": "H",
	"level": "middle",
},
{
	"word": "hurt",
	"group": "H",
	"level": "middle",
},
{
	"word": "husband",
	"group": "H",
	"level": "middle",
},
{
	"word": "ice",
	"group": "I",
	"level": "middle",
},
{
	"word": "if",
	"group": "I",
	"level": "middle",
},
{
	"word": "illness",
	"group": "I",
	"level": "middle",
},
{
	"word": "imagine",
	"group": "I",
	"level": "middle",
},
{
	"word": "important",
	"group": "I",
	"level": "middle",
},
{
	"word": "impossible",
	"group": "I",
	"level": "middle",
},
{
	"word": "include",
	"group": "I",
	"level": "middle",
},
{
	"word": "increase",
	"group": "I",
	"level": "middle",
},
{
	"word": "India",
	"group": "I",
	"level": "middle",
},
{
	"word": "Indian",
	"group": "I",
	"level": "middle",
},
{
	"word": "industry",
	"group": "I",
	"level": "middle",
},
{
	"word": "influence",
	"group": "I",
	"level": "middle",
},
{
	"word": "information",
	"group": "I",
	"level": "middle",
},
{
	"word": "inside",
	"group": "I",
	"level": "middle",
},
{
	"word": "instead",
	"group": "I",
	"level": "middle",
},
{
	"word": "instruction",
	"group": "I",
	"level": "middle",
},
{
	"word": "instrument",
	"group": "I",
	"level": "middle",
},
{
	"word": "interest",
	"group": "I",
	"level": "middle",
},
{
	"word": "international",
	"group": "I",
	"level": "middle",
},
{
	"word": "Internet",
	"group": "I",
	"level": "middle",
},
{
	"word": "interview",
	"group": "I",
	"level": "middle",
},
{
	"word": "into",
	"group": "I",
	"level": "middle",
},
{
	"word": "introduce",
	"group": "I",
	"level": "middle",
},
{
	"word": "introduction",
	"group": "I",
	"level": "middle",
},
{
	"word": "invent",
	"group": "I",
	"level": "middle",
},
{
	"word": "invention",
	"group": "I",
	"level": "middle",
},
{
	"word": "invite",
	"group": "I",
	"level": "middle",
},
{
	"word": "island",
	"group": "I",
	"level": "middle",
},
{
	"word": "itself",
	"group": "I",
	"level": "middle",
},
{
	"word": "jacket",
	"group": "J",
	"level": "middle",
},
{
	"word": "January",
	"group": "J",
	"level": "middle",
},
{
	"word": "Japan",
	"group": "J",
	"level": "middle",
},
{
	"word": "Japanese",
	"group": "J",
	"level": "middle",
},
{
	"word": "job",
	"group": "J",
	"level": "middle",
},
{
	"word": "join",
	"group": "J",
	"level": "middle",
},
{
	"word": "joke",
	"group": "J",
	"level": "middle",
},
{
	"word": "journey",
	"group": "J",
	"level": "middle",
},
{
	"word": "July",
	"group": "J",
	"level": "middle",
},
{
	"word": "June",
	"group": "J",
	"level": "middle",
},
{
	"word": "just",
	"group": "J",
	"level": "middle",
},
{
	"word": "keep",
	"group": "K",
	"level": "middle",
},
{
	"word": "key",
	"group": "K",
	"level": "middle",
},
{
	"word": "keyboard",
	"group": "K",
	"level": "middle",
},
{
	"word": "kick",
	"group": "K",
	"level": "middle",
},
{
	"word": "kill",
	"group": "K",
	"level": "middle",
},
{
	"word": "kilo",
	"group": "K",
	"level": "middle",
},
{
	"word": "kilometre",
	"group": "K",
	"level": "middle",
},
{
	"word": "king",
	"group": "K",
	"level": "middle",
},
{
	"word": "kiss",
	"group": "K",
	"level": "middle",
},
{
	"word": "knee",
	"group": "K",
	"level": "middle",
},
{
	"word": "knife",
	"group": "K",
	"level": "middle",
},
{
	"word": "knock",
	"group": "K",
	"level": "middle",
},
{
	"word": "knowledge",
	"group": "K",
	"level": "middle",
},
{
	"word": "lab",
	"group": "L",
	"level": "middle",
},
{
	"word": "lady",
	"group": "L",
	"level": "middle",
},
{
	"word": "land",
	"group": "L",
	"level": "middle",
},
{
	"word": "language",
	"group": "L",
	"level": "middle",
},
{
	"word": "large",
	"group": "L",
	"level": "middle",
},
{
	"word": "last",
	"group": "L",
	"level": "middle",
},
{
	"word": "later",
	"group": "L",
	"level": "middle",
},
{
	"word": "laugh",
	"group": "L",
	"level": "middle",
},
{
	"word": "law",
	"group": "L",
	"level": "middle",
},
{
	"word": "lay",
	"group": "L",
	"level": "middle",
},
{
	"word": "lazy",
	"group": "L",
	"level": "middle",
},
{
	"word": "lead",
	"group": "L",
	"level": "middle",
},
{
	"word": "leader",
	"group": "L",
	"level": "middle",
},
{
	"word": "leaf",
	"group": "L",
	"level": "middle",
},
{
	"word": "learn",
	"group": "L",
	"level": "middle",
},
{
	"word": "least",
	"group": "L",
	"level": "middle",
},
{
	"word": "leave",
	"group": "L",
	"level": "middle",
},
{
	"word": "lemon",
	"group": "L",
	"level": "middle",
},
{
	"word": "lend",
	"group": "L",
	"level": "middle",
},
{
	"word": "less",
	"group": "L",
	"level": "middle",
},
{
	"word": "letter",
	"group": "L",
	"level": "middle",
},
{
	"word": "level",
	"group": "L",
	"level": "middle",
},
{
	"word": "lie",
	"group": "L",
	"level": "middle",
},
{
	"word": "life",
	"group": "L",
	"level": "middle",
},
{
	"word": "lift",
	"group": "L",
	"level": "middle",
},
{
	"word": "line",
	"group": "L",
	"level": "middle",
},
{
	"word": "lion",
	"group": "L",
	"level": "middle",
},
{
	"word": "list",
	"group": "L",
	"level": "middle",
},
{
	"word": "litter",
	"group": "L",
	"level": "middle",
},
{
	"word": "little",
	"group": "L",
	"level": "middle",
},
{
	"word": "lively",
	"group": "L",
	"level": "middle",
},
{
	"word": "local",
	"group": "L",
	"level": "middle",
},
{
	"word": "lock",
	"group": "L",
	"level": "middle",
},
{
	"word": "London",
	"group": "L",
	"level": "middle",
},
{
	"word": "lonely",
	"group": "L",
	"level": "middle",
},
{
	"word": "lose",
	"group": "L",
	"level": "middle",
},
{
	"word": "lot",
	"group": "L",
	"level": "middle",
},
{
	"word": "loud",
	"group": "L",
	"level": "middle",
},
{
	"word": "lovely",
	"group": "L",
	"level": "middle",
},
{
	"word": "low",
	"group": "L",
	"level": "middle",
},
{
	"word": "luck",
	"group": "L",
	"level": "middle",
},
{
	"word": "lucky",
	"group": "L",
	"level": "middle",
},
{
	"word": "machine",
	"group": "M",
	"level": "middle",
},
{
	"word": "mad",
	"group": "M",
	"level": "middle",
},
{
	"word": "magazine",
	"group": "M",
	"level": "middle",
},
{
	"word": "magic",
	"group": "M",
	"level": "middle",
},
{
	"word": "main",
	"group": "M",
	"level": "middle",
},
{
	"word": "manage",
	"group": "M",
	"level": "middle",
},
{
	"word": "manager",
	"group": "M",
	"level": "middle",
},
{
	"word": "March",
	"group": "M",
	"level": "middle",
},
{
	"word": "mark",
	"group": "M",
	"level": "middle",
},
{
	"word": "market",
	"group": "M",
	"level": "middle",
},
{
	"word": "marry",
	"group": "M",
	"level": "middle",
},
{
	"word": "match",
	"group": "M",
	"level": "middle",
},
{
	"word": "matter",
	"group": "M",
	"level": "middle",
},
{
	"word": "May",
	"group": "M",
	"level": "middle",
},
{
	"word": "may",
	"group": "M",
	"level": "middle",
},
{
	"word": "maybe",
	"group": "M",
	"level": "middle",
},
{
	"word": "meal",
	"group": "M",
	"level": "middle",
},
{
	"word": "mean",
	"group": "M",
	"level": "middle",
},
{
	"word": "meaning",
	"group": "M",
	"level": "middle",
},
{
	"word": "meat",
	"group": "M",
	"level": "middle",
},
{
	"word": "medical",
	"group": "M",
	"level": "middle",
},
{
	"word": "medicine",
	"group": "M",
	"level": "middle",
},
{
	"word": "meeting",
	"group": "M",
	"level": "middle",
},
{
	"word": "member",
	"group": "M",
	"level": "middle",
},
{
	"word": "mention",
	"group": "M",
	"level": "middle",
},
{
	"word": "menu",
	"group": "M",
	"level": "middle",
},
{
	"word": "mess",
	"group": "M",
	"level": "middle",
},
{
	"word": "message",
	"group": "M",
	"level": "middle",
},
{
	"word": "method",
	"group": "M",
	"level": "middle",
},
{
	"word": "metre",
	"group": "M",
	"level": "middle",
},
{
	"word": "middle",
	"group": "M",
	"level": "middle",
},
{
	"word": "might",
	"group": "M",
	"level": "middle",
},
{
	"word": "mile",
	"group": "M",
	"level": "middle",
},
{
	"word": "mind",
	"group": "M",
	"level": "middle",
},
{
	"word": "mine",
	"group": "M",
	"level": "middle",
},
{
	"word": "miss",
	"group": "M",
	"level": "middle",
},
{
	"word": "missing",
	"group": "M",
	"level": "middle",
},
{
	"word": "mistake",
	"group": "M",
	"level": "middle",
},
{
	"word": "mix",
	"group": "M",
	"level": "middle",
},
{
	"word": "mobile-phone",
	"group": "M",
	"level": "middle",
},
{
	"word": "model",
	"group": "M",
	"level": "middle",
},
{
	"word": "modern",
	"group": "M",
	"level": "middle",
},
{
	"word": "Monday",
	"group": "M",
	"level": "middle",
},
{
	"word": "money",
	"group": "M",
	"level": "middle",
},
{
	"word": "more",
	"group": "M",
	"level": "middle",
},
{
	"word": "most",
	"group": "M",
	"level": "middle",
},
{
	"word": "mountain",
	"group": "M",
	"level": "middle",
},
{
	"word": "mouse",
	"group": "M",
	"level": "middle",
},
{
	"word": "move",
	"group": "M",
	"level": "middle",
},
{
	"word": "movie",
	"group": "M",
	"level": "middle",
},
{
	"word": "museum",
	"group": "M",
	"level": "middle",
},
{
	"word": "musician",
	"group": "M",
	"level": "middle",
},
{
	"word": "must",
	"group": "M",
	"level": "middle",
},
{
	"word": "myself",
	"group": "M",
	"level": "middle",
},
{
	"word": "national",
	"group": "N",
	"level": "middle",
},
{
	"word": "natural",
	"group": "N",
	"level": "middle",
},
{
	"word": "nature",
	"group": "N",
	"level": "middle",
},
{
	"word": "nearly",
	"group": "N",
	"level": "middle",
},
{
	"word": "necessary",
	"group": "N",
	"level": "middle",
},
{
	"word": "neck",
	"group": "N",
	"level": "middle",
},
{
	"word": "need",
	"group": "N",
	"level": "middle",
},
{
	"word": "neighbour",
	"group": "N",
	"level": "middle",
},
{
	"word": "neither",
	"group": "N",
	"level": "middle",
},
{
	"word": "nervous",
	"group": "N",
	"level": "middle",
},
{
	"word": "never",
	"group": "N",
	"level": "middle",
},
{
	"word": "news",
	"group": "N",
	"level": "middle",
},
{
	"word": "nine",
	"group": "N",
	"level": "middle",
},
{
	"word": "nineteen",
	"group": "N",
	"level": "middle",
},
{
	"word": "ninety",
	"group": "N",
	"level": "middle",
},
{
	"word": "ninth",
	"group": "N",
	"level": "middle",
},
{
	"word": "nobody",
	"group": "N",
	"level": "middle",
},
{
	"word": "noise",
	"group": "N",
	"level": "middle",
},
{
	"word": "noisy",
	"group": "N",
	"level": "middle",
},
{
	"word": "none",
	"group": "N",
	"level": "middle",
},
{
	"word": "noon",
	"group": "N",
	"level": "middle",
},
{
	"word": "nor",
	"group": "N",
	"level": "middle",
},
{
	"word": "north",
	"group": "N",
	"level": "middle",
},
{
	"word": "northern",
	"group": "N",
	"level": "middle",
},
{
	"word": "note",
	"group": "N",
	"level": "middle",
},
{
	"word": "notebook",
	"group": "N",
	"level": "middle",
},
{
	"word": "nothing",
	"group": "N",
	"level": "middle",
},
{
	"word": "notice",
	"group": "N",
	"level": "middle",
},
{
	"word": "November",
	"group": "N",
	"level": "middle",
},
{
	"word": "number",
	"group": "N",
	"level": "middle",
},
{
	"word": "object",
	"group": "O",
	"level": "middle",
},
{
	"word": "o'clock",
	"group": "O",
	"level": "middle",
},
{
	"word": "October",
	"group": "O",
	"level": "middle",
},
{
	"word": "off",
	"group": "O",
	"level": "middle",
},
{
	"word": "offer",
	"group": "O",
	"level": "middle",
},
{
	"word": "office",
	"group": "O",
	"level": "middle",
},
{
	"word": "officer",
	"group": "O",
	"level": "middle",
},
{
	"word": "oil",
	"group": "O",
	"level": "middle",
},
{
	"word": "OK",
	"group": "O",
	"level": "middle",
},
{
	"word": "Olympics",
	"group": "O",
	"level": "middle",
},
{
	"word": "once",
	"group": "O",
	"level": "middle",
},
{
	"word": "one",
	"group": "O",
	"level": "middle",
},
{
	"word": "online",
	"group": "O",
	"level": "middle",
},
{
	"word": "only",
	"group": "O",
	"level": "middle",
},
{
	"word": "opposite",
	"group": "O",
	"level": "middle",
},
{
	"word": "order",
	"group": "O",
	"level": "middle",
},
{
	"word": "other",
	"group": "O",
	"level": "middle",
},
{
	"word": "ours",
	"group": "O",
	"level": "middle",
},
{
	"word": "ourselves",
	"group": "O",
	"level": "middle",
},
{
	"word": "out",
	"group": "O",
	"level": "middle",
},
{
	"word": "outside",
	"group": "O",
	"level": "middle",
},
{
	"word": "over",
	"group": "O",
	"level": "middle",
},
{
	"word": "own",
	"group": "O",
	"level": "middle",
},
{
	"word": "Pacific",
	"group": "P",
	"level": "middle",
},
{
	"word": "page",
	"group": "P",
	"level": "middle",
},
{
	"word": "pain",
	"group": "P",
	"level": "middle",
},
{
	"word": "paint",
	"group": "P",
	"level": "middle",
},
{
	"word": "pair",
	"group": "P",
	"level": "middle",
},
{
	"word": "palace",
	"group": "P",
	"level": "middle",
},
{
	"word": "pale",
	"group": "P",
	"level": "middle",
},
{
	"word": "pancake",
	"group": "P",
	"level": "middle",
},
{
	"word": "paper",
	"group": "P",
	"level": "middle",
},
{
	"word": "pardon",
	"group": "P",
	"level": "middle",
},
{
	"word": "part",
	"group": "P",
	"level": "middle",
},
{
	"word": "pass",
	"group": "P",
	"level": "middle",
},
{
	"word": "passenger",
	"group": "P",
	"level": "middle",
},
{
	"word": "passport",
	"group": "P",
	"level": "middle",
},
{
	"word": "past",
	"group": "P",
	"level": "middle",
},
{
	"word": "patient",
	"group": "P",
	"level": "middle",
},
{
	"word": "pay",
	"group": "P",
	"level": "middle",
},
{
	"word": "peace",
	"group": "P",
	"level": "middle",
},
{
	"word": "pear",
	"group": "P",
	"level": "middle",
},
{
	"word": "perfect",
	"group": "P",
	"level": "middle",
},
{
	"word": "perhaps",
	"group": "P",
	"level": "middle",
},
{
	"word": "period",
	"group": "P",
	"level": "middle",
},
{
	"word": "person",
	"group": "P",
	"level": "middle",
},
{
	"word": "personal",
	"group": "P",
	"level": "middle",
},
{
	"word": "pet",
	"group": "P",
	"level": "middle",
},
{
	"word": "phone",
	"group": "P",
	"level": "middle",
},
{
	"word": "physics",
	"group": "P",
	"level": "middle",
},
{
	"word": "pick",
	"group": "P",
	"level": "middle",
},
{
	"word": "picnic",
	"group": "P",
	"level": "middle",
},
{
	"word": "pie",
	"group": "P",
	"level": "middle",
},
{
	"word": "piece",
	"group": "P",
	"level": "middle",
},
{
	"word": "pilot",
	"group": "P",
	"level": "middle",
},
{
	"word": "pink",
	"group": "P",
	"level": "middle",
},
{
	"word": "pioneer",
	"group": "P",
	"level": "middle",
},
{
	"word": "pity",
	"group": "P",
	"level": "middle",
},
{
	"word": "plan",
	"group": "P",
	"level": "middle",
},
{
	"word": "planet",
	"group": "P",
	"level": "middle",
},
{
	"word": "player",
	"group": "P",
	"level": "middle",
},
{
	"word": "pleasure",
	"group": "P",
	"level": "middle",
},
{
	"word": "plenty",
	"group": "P",
	"level": "middle",
},
{
	"word": "pocket",
	"group": "P",
	"level": "middle",
},
{
	"word": "poem",
	"group": "P",
	"level": "middle",
},
{
	"word": "point",
	"group": "P",
	"level": "middle",
},
{
	"word": "policeman",
	"group": "P",
	"level": "middle",
},
{
	"word": "polite",
	"group": "P",
	"level": "middle",
},
{
	"word": "pollute",
	"group": "P",
	"level": "middle",
},
{
	"word": "pollution",
	"group": "P",
	"level": "middle",
},
{
	"word": "pool",
	"group": "P",
	"level": "middle",
},
{
	"word": "poor",
	"group": "P",
	"level": "middle",
},
{
	"word": "popular",
	"group": "P",
	"level": "middle",
},
{
	"word": "population",
	"group": "P",
	"level": "middle",
},
{
	"word": "possible",
	"group": "P",
	"level": "middle",
},
{
	"word": "post",
	"group": "P",
	"level": "middle",
},
{
	"word": "postcard",
	"group": "P",
	"level": "middle",
},
{
	"word": "postman",
	"group": "P",
	"level": "middle",
},
{
	"word": "pound",
	"group": "P",
	"level": "middle",
},
{
	"word": "practice",
	"group": "P",
	"level": "middle",
},
{
	"word": "praise",
	"group": "P",
	"level": "middle",
},
{
	"word": "prepare",
	"group": "P",
	"level": "middle",
},
{
	"word": "present",
	"group": "P",
	"level": "middle",
},
{
	"word": "president",
	"group": "P",
	"level": "middle",
},
{
	"word": "pretty",
	"group": "P",
	"level": "middle",
},
{
	"word": "price",
	"group": "P",
	"level": "middle",
},
{
	"word": "pride",
	"group": "P",
	"level": "middle",
},
{
	"word": "primary",
	"group": "P",
	"level": "middle",
},
{
	"word": "print",
	"group": "P",
	"level": "middle",
},
{
	"word": "private",
	"group": "P",
	"level": "middle",
},
{
	"word": "prize",
	"group": "P",
	"level": "middle",
},
{
	"word": "probably",
	"group": "P",
	"level": "middle",
},
{
	"word": "problem",
	"group": "P",
	"level": "middle",
},
{
	"word": "produce",
	"group": "P",
	"level": "middle",
},
{
	"word": "product",
	"group": "P",
	"level": "middle",
},
{
	"word": "programme",
	"group": "P",
	"level": "middle",
},
{
	"word": "progress",
	"group": "P",
	"level": "middle",
},
{
	"word": "project",
	"group": "P",
	"level": "middle",
},
{
	"word": "promise",
	"group": "P",
	"level": "middle",
},
{
	"word": "pronounce",
	"group": "P",
	"level": "middle",
},
{
	"word": "pronunciation",
	"group": "P",
	"level": "middle",
},
{
	"word": "proper",
	"group": "P",
	"level": "middle",
},
{
	"word": "protect",
	"group": "P",
	"level": "middle",
},
{
	"word": "proud",
	"group": "P",
	"level": "middle",
},
{
	"word": "provide",
	"group": "P",
	"level": "middle",
},
{
	"word": "public",
	"group": "P",
	"level": "middle",
},
{
	"word": "pull",
	"group": "P",
	"level": "middle",
},
{
	"word": "punish",
	"group": "P",
	"level": "middle",
},
{
	"word": "purple",
	"group": "P",
	"level": "middle",
},
{
	"word": "purpose",
	"group": "P",
	"level": "middle",
},
{
	"word": "push",
	"group": "P",
	"level": "middle",
},
{
	"word": "quarter",
	"group": "Q",
	"level": "middle",
},
{
	"word": "queen",
	"group": "Q",
	"level": "middle",
},
{
	"word": "question",
	"group": "Q",
	"level": "middle",
},
{
	"word": "quick",
	"group": "Q",
	"level": "middle",
},
{
	"word": "quiet",
	"group": "Q",
	"level": "middle",
},
{
	"word": "quite",
	"group": "Q",
	"level": "middle",
},
{
	"word": "rabbit",
	"group": "R",
	"level": "middle",
},
{
	"word": "race",
	"group": "R",
	"level": "middle",
},
{
	"word": "radio",
	"group": "R",
	"level": "middle",
},
{
	"word": "railway",
	"group": "R",
	"level": "middle",
},
{
	"word": "rainy",
	"group": "R",
	"level": "middle",
},
{
	"word": "raise",
	"group": "R",
	"level": "middle",
},
{
	"word": "rapid",
	"group": "R",
	"level": "middle",
},
{
	"word": "reach",
	"group": "R",
	"level": "middle",
},
{
	"word": "ready",
	"group": "R",
	"level": "middle",
},
{
	"word": "real",
	"group": "R",
	"level": "middle",
},
{
	"word": "realise",
	"group": "R",
	"level": "middle",
},
{
	"word": "really",
	"group": "R",
	"level": "middle",
},
{
	"word": "reason",
	"group": "R",
	"level": "middle",
},
{
	"word": "receive",
	"group": "R",
	"level": "middle",
},
{
	"word": "recently",
	"group": "R",
	"level": "middle",
},
{
	"word": "record",
	"group": "R",
	"level": "middle",
},
{
	"word": "refuse",
	"group": "R",
	"level": "middle",
},
{
	"word": "regret",
	"group": "R",
	"level": "middle",
},
{
	"word": "relationship",
	"group": "R",
	"level": "middle",
},
{
	"word": "relative",
	"group": "R",
	"level": "middle",
},
{
	"word": "relax",
	"group": "R",
	"level": "middle",
},
{
	"word": "remain",
	"group": "R",
	"level": "middle",
},
{
	"word": "remember",
	"group": "R",
	"level": "middle",
},
{
	"word": "repair",
	"group": "R",
	"level": "middle",
},
{
	"word": "repeat",
	"group": "R",
	"level": "middle",
},
{
	"word": "reply",
	"group": "R",
	"level": "middle",
},
{
	"word": "report",
	"group": "R",
	"level": "middle",
},
{
	"word": "require",
	"group": "R",
	"level": "middle",
},
{
	"word": "research",
	"group": "R",
	"level": "middle",
},
{
	"word": "rest",
	"group": "R",
	"level": "middle",
},
{
	"word": "restaurant",
	"group": "R",
	"level": "middle",
},
{
	"word": "result",
	"group": "R",
	"level": "middle",
},
{
	"word": "return",
	"group": "R",
	"level": "middle",
},
{
	"word": "review",
	"group": "R",
	"level": "middle",
},
{
	"word": "rich",
	"group": "R",
	"level": "middle",
},
{
	"word": "ride",
	"group": "R",
	"level": "middle",
},
{
	"word": "ring",
	"group": "R",
	"level": "middle",
},
{
	"word": "rise",
	"group": "R",
	"level": "middle",
},
{
	"word": "risk",
	"group": "R",
	"level": "middle",
},
{
	"word": "road",
	"group": "R",
	"level": "middle",
},
{
	"word": "robot",
	"group": "R",
	"level": "middle",
},
{
	"word": "rock",
	"group": "R",
	"level": "middle",
},
{
	"word": "role",
	"group": "R",
	"level": "middle",
},
{
	"word": "rope",
	"group": "R",
	"level": "middle",
},
{
	"word": "rose",
	"group": "R",
	"level": "middle",
},
{
	"word": "round",
	"group": "R",
	"level": "middle",
},
{
	"word": "row",
	"group": "R",
	"level": "middle",
},
{
	"word": "rubbish",
	"group": "R",
	"level": "middle",
},
{
	"word": "rule",
	"group": "R",
	"level": "middle",
},
{
	"word": "rush",
	"group": "R",
	"level": "middle",
},
{
	"word": "Russia",
	"group": "R",
	"level": "middle",
},
{
	"word": "Russian",
	"group": "R",
	"level": "middle",
},
{
	"word": "safe",
	"group": "S",
	"level": "middle",
},
{
	"word": "safety",
	"group": "S",
	"level": "middle",
},
{
	"word": "salad",
	"group": "S",
	"level": "middle",
},
{
	"word": "sale",
	"group": "S",
	"level": "middle",
},
{
	"word": "salt",
	"group": "S",
	"level": "middle",
},
{
	"word": "same",
	"group": "S",
	"level": "middle",
},
{
	"word": "sand",
	"group": "S",
	"level": "middle",
},
{
	"word": "sandwich",
	"group": "S",
	"level": "middle",
},
{
	"word": "satisfy",
	"group": "S",
	"level": "middle",
},
{
	"word": "Saturday",
	"group": "S",
	"level": "middle",
},
{
	"word": "save",
	"group": "S",
	"level": "middle",
},
{
	"word": "scarf",
	"group": "S",
	"level": "middle",
},
{
	"word": "scientist",
	"group": "S",
	"level": "middle",
},
{
	"word": "scissors",
	"group": "S",
	"level": "middle",
},
{
	"word": "score",
	"group": "S",
	"level": "middle",
},
{
	"word": "screen",
	"group": "S",
	"level": "middle",
},
{
	"word": "sea",
	"group": "S",
	"level": "middle",
},
{
	"word": "search",
	"group": "S",
	"level": "middle",
},
{
	"word": "seat",
	"group": "S",
	"level": "middle",
},
{
	"word": "second",
	"group": "S",
	"level": "middle",
},
{
	"word": "secret",
	"group": "S",
	"level": "middle",
},
{
	"word": "secretary",
	"group": "S",
	"level": "middle",
},
{
	"word": "seem",
	"group": "S",
	"level": "middle",
},
{
	"word": "seldom",
	"group": "S",
	"level": "middle",
},
{
	"word": "sell",
	"group": "S",
	"level": "middle",
},
{
	"word": "send",
	"group": "S",
	"level": "middle",
},
{
	"word": "sense",
	"group": "S",
	"level": "middle",
},
{
	"word": "sentence",
	"group": "S",
	"level": "middle",
},
{
	"word": "separate",
	"group": "S",
	"level": "middle",
},
{
	"word": "September",
	"group": "S",
	"level": "middle",
},
{
	"word": "serious",
	"group": "S",
	"level": "middle",
},
{
	"word": "serve",
	"group": "S",
	"level": "middle",
},
{
	"word": "service",
	"group": "S",
	"level": "middle",
},
{
	"word": "set",
	"group": "S",
	"level": "middle",
},
{
	"word": "seven",
	"group": "S",
	"level": "middle",
},
{
	"word": "seventeen",
	"group": "S",
	"level": "middle",
},
{
	"word": "seventh",
	"group": "S",
	"level": "middle",
},
{
	"word": "seventy",
	"group": "S",
	"level": "middle",
},
{
	"word": "several",
	"group": "S",
	"level": "middle",
},
{
	"word": "shake",
	"group": "S",
	"level": "middle",
},
{
	"word": "shall",
	"group": "S",
	"level": "middle",
},
{
	"word": "shame",
	"group": "S",
	"level": "middle",
},
{
	"word": "shape",
	"group": "S",
	"level": "middle",
},
{
	"word": "share",
	"group": "S",
	"level": "middle",
},
{
	"word": "shine",
	"group": "S",
	"level": "middle",
},
{
	"word": "should",
	"group": "S",
	"level": "middle",
},
{
	"word": "shoulder",
	"group": "S",
	"level": "middle",
},
{
	"word": "shout",
	"group": "S",
	"level": "middle",
},
{
	"word": "show",
	"group": "S",
	"level": "middle",
},
{
	"word": "shower",
	"group": "S",
	"level": "middle",
},
{
	"word": "shut",
	"group": "S",
	"level": "middle",
},
{
	"word": "shy",
	"group": "S",
	"level": "middle",
},
{
	"word": "sick",
	"group": "S",
	"level": "middle",
},
{
	"word": "side",
	"group": "S",
	"level": "middle",
},
{
	"word": "sign",
	"group": "S",
	"level": "middle",
},
{
	"word": "silence",
	"group": "S",
	"level": "middle",
},
{
	"word": "silent",
	"group": "S",
	"level": "middle",
},
{
	"word": "silk",
	"group": "S",
	"level": "middle",
},
{
	"word": "silly",
	"group": "S",
	"level": "middle",
},
{
	"word": "silver",
	"group": "S",
	"level": "middle",
},
{
	"word": "similar",
	"group": "S",
	"level": "middle",
},
{
	"word": "simple",
	"group": "S",
	"level": "middle",
},
{
	"word": "since",
	"group": "S",
	"level": "middle",
},
{
	"word": "single",
	"group": "S",
	"level": "middle",
},
{
	"word": "sir",
	"group": "S",
	"level": "middle",
},
{
	"word": "situation",
	"group": "S",
	"level": "middle",
},
{
	"word": "six",
	"group": "S",
	"level": "middle",
},
{
	"word": "sixteen",
	"group": "S",
	"level": "middle",
},
{
	"word": "sixth",
	"group": "S",
	"level": "middle",
},
{
	"word": "sixty",
	"group": "S",
	"level": "middle",
},
{
	"word": "size",
	"group": "S",
	"level": "middle",
},
{
	"word": "skate",
	"group": "S",
	"level": "middle",
},
{
	"word": "skill",
	"group": "S",
	"level": "middle",
},
{
	"word": "sky",
	"group": "S",
	"level": "middle",
},
{
	"word": "sleepy",
	"group": "S",
	"level": "middle",
},
{
	"word": "smart",
	"group": "S",
	"level": "middle",
},
{
	"word": "smell",
	"group": "S",
	"level": "middle",
},
{
	"word": "smile",
	"group": "S",
	"level": "middle",
},
{
	"word": "smoke",
	"group": "S",
	"level": "middle",
},
{
	"word": "smooth",
	"group": "S",
	"level": "middle",
},
{
	"word": "snake",
	"group": "S",
	"level": "middle",
},
{
	"word": "snowy",
	"group": "S",
	"level": "middle",
},
{
	"word": "so",
	"group": "S",
	"level": "middle",
},
{
	"word": "social",
	"group": "S",
	"level": "middle",
},
{
	"word": "society",
	"group": "S",
	"level": "middle",
},
{
	"word": "sofa",
	"group": "S",
	"level": "middle",
},
{
	"word": "soft",
	"group": "S",
	"level": "middle",
},
{
	"word": "solve",
	"group": "S",
	"level": "middle",
},
{
	"word": "somebody",
	"group": "S",
	"level": "middle",
},
{
	"word": "someone",
	"group": "S",
	"level": "middle",
},
{
	"word": "something",
	"group": "S",
	"level": "middle",
},
{
	"word": "somewhere",
	"group": "S",
	"level": "middle",
},
{
	"word": "son",
	"group": "S",
	"level": "middle",
},
{
	"word": "soon",
	"group": "S",
	"level": "middle",
},
{
	"word": "sound",
	"group": "S",
	"level": "middle",
},
{
	"word": "south",
	"group": "S",
	"level": "middle",
},
{
	"word": "southern",
	"group": "S",
	"level": "middle",
},
{
	"word": "space",
	"group": "S",
	"level": "middle",
},
{
	"word": "spare",
	"group": "S",
	"level": "middle",
},
{
	"word": "speaker",
	"group": "S",
	"level": "middle",
},
{
	"word": "special",
	"group": "S",
	"level": "middle",
},
{
	"word": "speech",
	"group": "S",
	"level": "middle",
},
{
	"word": "speed",
	"group": "S",
	"level": "middle",
},
{
	"word": "spell",
	"group": "S",
	"level": "middle",
},
{
	"word": "spend",
	"group": "S",
	"level": "middle",
},
{
	"word": "spirit",
	"group": "S",
	"level": "middle",
},
{
	"word": "spoon",
	"group": "S",
	"level": "middle",
},
{
	"word": "spread",
	"group": "S",
	"level": "middle",
},
{
	"word": "square",
	"group": "S",
	"level": "middle",
},
{
	"word": "stamp",
	"group": "S",
	"level": "middle",
},
{
	"word": "standard",
	"group": "S",
	"level": "middle",
},
{
	"word": "start",
	"group": "S",
	"level": "middle",
},
{
	"word": "state",
	"group": "S",
	"level": "middle",
},
{
	"word": "station",
	"group": "S",
	"level": "middle",
},
{
	"word": "stay",
	"group": "S",
	"level": "middle",
},
{
	"word": "steal",
	"group": "S",
	"level": "middle",
},
{
	"word": "step",
	"group": "S",
	"level": "middle",
},
{
	"word": "stick",
	"group": "S",
	"level": "middle",
},
{
	"word": "still",
	"group": "S",
	"level": "middle",
},
{
	"word": "stomach",
	"group": "S",
	"level": "middle",
},
{
	"word": "stomachache",
	"group": "S",
	"level": "middle",
},
{
	"word": "stone",
	"group": "S",
	"level": "middle",
},
{
	"word": "store",
	"group": "S",
	"level": "middle",
},
{
	"word": "storm",
	"group": "S",
	"level": "middle",
},
{
	"word": "straight",
	"group": "S",
	"level": "middle",
},
{
	"word": "strange",
	"group": "S",
	"level": "middle",
},
{
	"word": "stranger",
	"group": "S",
	"level": "middle",
},
{
	"word": "strawberry",
	"group": "S",
	"level": "middle",
},
{
	"word": "strict",
	"group": "S",
	"level": "middle",
},
{
	"word": "student",
	"group": "S",
	"level": "middle",
},
{
	"word": "stupid",
	"group": "S",
	"level": "middle",
},
{
	"word": "succeed",
	"group": "S",
	"level": "middle",
},
{
	"word": "success",
	"group": "S",
	"level": "middle",
},
{
	"word": "successful",
	"group": "S",
	"level": "middle",
},
{
	"word": "such",
	"group": "S",
	"level": "middle",
},
{
	"word": "sudden",
	"group": "S",
	"level": "middle",
},
{
	"word": "sugar",
	"group": "S",
	"level": "middle",
},
{
	"word": "suggest",
	"group": "S",
	"level": "middle",
},
{
	"word": "suggestion",
	"group": "S",
	"level": "middle",
},
{
	"word": "Sunday",
	"group": "S",
	"level": "middle",
},
{
	"word": "support",
	"group": "S",
	"level": "middle",
},
{
	"word": "suppose",
	"group": "S",
	"level": "middle",
},
{
	"word": "sure",
	"group": "S",
	"level": "middle",
},
{
	"word": "surface",
	"group": "S",
	"level": "middle",
},
{
	"word": "surprise",
	"group": "S",
	"level": "middle",
},
{
	"word": "survey",
	"group": "S",
	"level": "middle",
},
{
	"word": "sweet",
	"group": "S",
	"level": "middle",
},
{
	"word": "swimming",
	"group": "S",
	"level": "middle",
},
{
	"word": "tail",
	"group": "T",
	"level": "middle",
},
{
	"word": "tape",
	"group": "T",
	"level": "middle",
},
{
	"word": "task",
	"group": "T",
	"level": "middle",
},
{
	"word": "taste",
	"group": "T",
	"level": "middle",
},
{
	"word": "teach",
	"group": "T",
	"level": "middle",
},
{
	"word": "team",
	"group": "T",
	"level": "middle",
},
{
	"word": "technology",
	"group": "T",
	"level": "middle",
},
{
	"word": "telephone",
	"group": "T",
	"level": "middle",
},
{
	"word": "television",
	"group": "T",
	"level": "middle",
},
{
	"word": "temperature",
	"group": "T",
	"level": "middle",
},
{
	"word": "ten",
	"group": "T",
	"level": "middle",
},
{
	"word": "tennis",
	"group": "T",
	"level": "middle",
},
{
	"word": "tenth",
	"group": "T",
	"level": "middle",
},
{
	"word": "term",
	"group": "T",
	"level": "middle",
},
{
	"word": "terrible",
	"group": "T",
	"level": "middle",
},
{
	"word": "test",
	"group": "T",
	"level": "middle",
},
{
	"word": "text",
	"group": "T",
	"level": "middle",
},
{
	"word": "than",
	"group": "T",
	"level": "middle",
},
{
	"word": "theatre",
	"group": "T",
	"level": "middle",
},
{
	"word": "themselves",
	"group": "T",
	"level": "middle",
},
{
	"word": "thick",
	"group": "T",
	"level": "middle",
},
{
	"word": "thing",
	"group": "T",
	"level": "middle",
},
{
	"word": "third",
	"group": "T",
	"level": "middle",
},
{
	"word": "thirsty",
	"group": "T",
	"level": "middle",
},
{
	"word": "thirteen",
	"group": "T",
	"level": "middle",
},
{
	"word": "thirty",
	"group": "T",
	"level": "middle",
},
{
	"word": "though",
	"group": "T",
	"level": "middle",
},
{
	"word": "thought",
	"group": "T",
	"level": "middle",
},
{
	"word": "thousand",
	"group": "T",
	"level": "middle",
},
{
	"word": "three",
	"group": "T",
	"level": "middle",
},
{
	"word": "through",
	"group": "T",
	"level": "middle",
},
{
	"word": "Thursday",
	"group": "T",
	"level": "middle",
},
{
	"word": "ticket",
	"group": "T",
	"level": "middle",
},
{
	"word": "tidy",
	"group": "T",
	"level": "middle",
},
{
	"word": "tie",
	"group": "T",
	"level": "middle",
},
{
	"word": "tiny",
	"group": "T",
	"level": "middle",
},
{
	"word": "together",
	"group": "T",
	"level": "middle",
},
{
	"word": "ton",
	"group": "T",
	"level": "middle",
},
{
	"word": "tonight",
	"group": "T",
	"level": "middle",
},
{
	"word": "tool",
	"group": "T",
	"level": "middle",
},
{
	"word": "tooth",
	"group": "T",
	"level": "middle",
},
{
	"word": "toothache",
	"group": "T",
	"level": "middle",
},
{
	"word": "top",
	"group": "T",
	"level": "middle",
},
{
	"word": "total",
	"group": "T",
	"level": "middle",
},
{
	"word": "touch",
	"group": "T",
	"level": "middle",
},
{
	"word": "tour",
	"group": "T",
	"level": "middle",
},
{
	"word": "tourist",
	"group": "T",
	"level": "middle",
},
{
	"word": "towards",
	"group": "T",
	"level": "middle",
},
{
	"word": "tower",
	"group": "T",
	"level": "middle",
},
{
	"word": "town",
	"group": "T",
	"level": "middle",
},
{
	"word": "trade",
	"group": "T",
	"level": "middle",
},
{
	"word": "traditional",
	"group": "T",
	"level": "middle",
},
{
	"word": "traffic",
	"group": "T",
	"level": "middle",
},
{
	"word": "training",
	"group": "T",
	"level": "middle",
},
{
	"word": "translate",
	"group": "T",
	"level": "middle",
},
{
	"word": "treasure",
	"group": "T",
	"level": "middle",
},
{
	"word": "treat",
	"group": "T",
	"level": "middle",
},
{
	"word": "trip",
	"group": "T",
	"level": "middle",
},
{
	"word": "trouble",
	"group": "T",
	"level": "middle",
},
{
	"word": "truck",
	"group": "T",
	"level": "middle",
},
{
	"word": "true",
	"group": "T",
	"level": "middle",
},
{
	"word": "trust",
	"group": "T",
	"level": "middle",
},
{
	"word": "truth",
	"group": "T",
	"level": "middle",
},
{
	"word": "T-shirt",
	"group": "T",
	"level": "middle",
},
{
	"word": "Tuesday",
	"group": "T",
	"level": "middle",
},
{
	"word": "twelfth",
	"group": "T",
	"level": "middle",
},
{
	"word": "twelve",
	"group": "T",
	"level": "middle",
},
{
	"word": "twentieth",
	"group": "T",
	"level": "middle",
},
{
	"word": "twenty",
	"group": "T",
	"level": "middle",
},
{
	"word": "twice",
	"group": "T",
	"level": "middle",
},
{
	"word": "two",
	"group": "T",
	"level": "middle",
},
{
	"word": "ugly",
	"group": "U",
	"level": "middle",
},
{
	"word": "UK",
	"group": "U",
	"level": "middle",
},
{
	"word": "underground",
	"group": "U",
	"level": "middle",
},
{
	"word": "understand",
	"group": "U",
	"level": "middle",
},
{
	"word": "unit",
	"group": "U",
	"level": "middle",
},
{
	"word": "university",
	"group": "U",
	"level": "middle",
},
{
	"word": "unless",
	"group": "U",
	"level": "middle",
},
{
	"word": "until",
	"group": "U",
	"level": "middle",
},
{
	"word": "upon",
	"group": "U",
	"level": "middle",
},
{
	"word": "US",
	"group": "U",
	"level": "middle",
},
{
	"word": "used",
	"group": "U",
	"level": "middle",
},
{
	"word": "useful",
	"group": "U",
	"level": "middle",
},
{
	"word": "usual",
	"group": "U",
	"level": "middle",
},
{
	"word": "usually",
	"group": "U",
	"level": "middle",
},
{
	"word": "vacation",
	"group": "V",
	"level": "middle",
},
{
	"word": "valuable",
	"group": "V",
	"level": "middle",
},
{
	"word": "value",
	"group": "V",
	"level": "middle",
},
{
	"word": "victory",
	"group": "V",
	"level": "middle",
},
{
	"word": "video",
	"group": "V",
	"level": "middle",
},
{
	"word": "village",
	"group": "V",
	"level": "middle",
},
{
	"word": "violin",
	"group": "V",
	"level": "middle",
},
{
	"word": "visitor",
	"group": "V",
	"level": "middle",
},
{
	"word": "voice",
	"group": "V",
	"level": "middle",
},
{
	"word": "volleyball",
	"group": "V",
	"level": "middle",
},
{
	"word": "wake",
	"group": "W",
	"level": "middle",
},
{
	"word": "wall",
	"group": "W",
	"level": "middle",
},
{
	"word": "wallet",
	"group": "W",
	"level": "middle",
},
{
	"word": "war",
	"group": "W",
	"level": "middle",
},
{
	"word": "warn",
	"group": "W",
	"level": "middle",
},
{
	"word": "waste",
	"group": "W",
	"level": "middle",
},
{
	"word": "watermelon",
	"group": "W",
	"level": "middle",
},
{
	"word": "weak",
	"group": "W",
	"level": "middle",
},
{
	"word": "wealth",
	"group": "W",
	"level": "middle",
},
{
	"word": "website",
	"group": "W",
	"level": "middle",
},
{
	"word": "Wednesday",
	"group": "W",
	"level": "middle",
},
{
	"word": "weekday",
	"group": "W",
	"level": "middle",
},
{
	"word": "weekend",
	"group": "W",
	"level": "middle",
},
{
	"word": "weigh",
	"group": "W",
	"level": "middle",
},
{
	"word": "weight",
	"group": "W",
	"level": "middle",
},
{
	"word": "west",
	"group": "W",
	"level": "middle",
},
{
	"word": "western",
	"group": "W",
	"level": "middle",
},
{
	"word": "wet",
	"group": "W",
	"level": "middle",
},
{
	"word": "whatever",
	"group": "W",
	"level": "middle",
},
{
	"word": "wheel",
	"group": "W",
	"level": "middle",
},
{
	"word": "whenever",
	"group": "W",
	"level": "middle",
},
{
	"word": "whether",
	"group": "W",
	"level": "middle",
},
{
	"word": "which",
	"group": "W",
	"level": "middle",
},
{
	"word": "while",
	"group": "W",
	"level": "middle",
},
{
	"word": "whole",
	"group": "W",
	"level": "middle",
},
{
	"word": "whom",
	"group": "W",
	"level": "middle",
},
{
	"word": "wide",
	"group": "W",
	"level": "middle",
},
{
	"word": "wife",
	"group": "W",
	"level": "middle",
},
{
	"word": "wild",
	"group": "W",
	"level": "middle",
},
{
	"word": "will",
	"group": "W",
	"level": "middle",
},
{
	"word": "win",
	"group": "W",
	"level": "middle",
},
{
	"word": "wind",
	"group": "W",
	"level": "middle",
},
{
	"word": "wing",
	"group": "W",
	"level": "middle",
},
{
	"word": "winner",
	"group": "W",
	"level": "middle",
},
{
	"word": "wise",
	"group": "W",
	"level": "middle",
},
{
	"word": "wish",
	"group": "W",
	"level": "middle",
},
{
	"word": "without",
	"group": "W",
	"level": "middle",
},
{
	"word": "wonder",
	"group": "W",
	"level": "middle",
},
{
	"word": "wood",
	"group": "W",
	"level": "middle",
},
{
	"word": "world",
	"group": "W",
	"level": "middle",
},
{
	"word": "worse",
	"group": "W",
	"level": "middle",
},
{
	"word": "worst",
	"group": "W",
	"level": "middle",
},
{
	"word": "worth",
	"group": "W",
	"level": "middle",
},
{
	"word": "would",
	"group": "W",
	"level": "middle",
},
{
	"word": "wound",
	"group": "W",
	"level": "middle",
},
{
	"word": "writer",
	"group": "W",
	"level": "middle",
},
{
	"word": "X-ray",
	"group": "X",
	"level": "middle",
},
{
	"word": "yard",
	"group": "Y",
	"level": "middle",
},
{
	"word": "yet",
	"group": "Y",
	"level": "middle",
},
{
	"word": "yours",
	"group": "Y",
	"level": "middle",
},
{
	"word": "yourself",
	"group": "Y",
	"level": "middle",
},
{
	"word": "zero",
	"group": "Z",
	"level": "middle",
},
{
	"word": "abandon",
	"group": "A",
	"level": "high",
},
{
	"word": "abnormal",
	"group": "A",
	"level": "high",
},
{
	"word": "aboard",
	"group": "A",
	"level": "high",
},
{
	"word": "abolish",
	"group": "A",
	"level": "high",
},
{
	"word": "abortion",
	"group": "A",
	"level": "high",
},
{
	"word": "abrupt",
	"group": "A",
	"level": "high",
},
{
	"word": "absence",
	"group": "A",
	"level": "high",
},
{
	"word": "absolute",
	"group": "A",
	"level": "high",
},
{
	"word": "absorb",
	"group": "A",
	"level": "high",
},
{
	"word": "abstract",
	"group": "A",
	"level": "high",
},
{
	"word": "absurd",
	"group": "A",
	"level": "high",
},
{
	"word": "abundant",
	"group": "A",
	"level": "high",
},
{
	"word": "abuse",
	"group": "A",
	"level": "high",
},
{
	"word": "academic",
	"group": "A",
	"level": "high",
},
{
	"word": "academy",
	"group": "A",
	"level": "high",
},
{
	"word": "accelerate",
	"group": "A",
	"level": "high",
},
{
	"word": "accent",
	"group": "A",
	"level": "high",
},
{
	"word": "access",
	"group": "A",
	"level": "high",
},
{
	"word": "accessible",
	"group": "A",
	"level": "high",
},
{
	"word": "accident",
	"group": "A",
	"level": "high",
},
{
	"word": "accommodation",
	"group": "A",
	"level": "high",
},
{
	"word": "accompany",
	"group": "A",
	"level": "high",
},
{
	"word": "accomplish",
	"group": "A",
	"level": "high",
},
{
	"word": "account",
	"group": "A",
	"level": "high",
},
{
	"word": "accountant",
	"group": "A",
	"level": "high",
},
{
	"word": "accumulate",
	"group": "A",
	"level": "high",
},
{
	"word": "accuracy",
	"group": "A",
	"level": "high",
},
{
	"word": "accurate",
	"group": "A",
	"level": "high",
},
{
	"word": "accuse",
	"group": "A",
	"level": "high",
},
{
	"word": "accustomed",
	"group": "A",
	"level": "high",
},
{
	"word": "ache",
	"group": "A",
	"level": "high",
},
{
	"word": "achievement",
	"group": "A",
	"level": "high",
},
{
	"word": "acid",
	"group": "A",
	"level": "high",
},
{
	"word": "acknowledge",
	"group": "A",
	"level": "high",
},
{
	"word": "acquaintance",
	"group": "A",
	"level": "high",
},
{
	"word": "acquire",
	"group": "A",
	"level": "high",
},
{
	"word": "acquisition",
	"group": "A",
	"level": "high",
},
{
	"word": "acre",
	"group": "A",
	"level": "high",
},
{
	"word": "actual",
	"group": "A",
	"level": "high",
},
{
	"word": "acute",
	"group": "A",
	"level": "high",
},
{
	"word": "AD",
	"group": "A",
	"level": "high",
},
{
	"word": "ad",
	"group": "A",
	"level": "high",
},
{
	"word": "adapt",
	"group": "A",
	"level": "high",
},
{
	"word": "adaptation",
	"group": "A",
	"level": "high",
},
{
	"word": "addicted",
	"group": "A",
	"level": "high",
},
{
	"word": "addition",
	"group": "A",
	"level": "high",
},
{
	"word": "adequate",
	"group": "A",
	"level": "high",
},
{
	"word": "adjust",
	"group": "A",
	"level": "high",
},
{
	"word": "adjustment",
	"group": "A",
	"level": "high",
},
{
	"word": "administration",
	"group": "A",
	"level": "high",
},
{
	"word": "admirable",
	"group": "A",
	"level": "high",
},
{
	"word": "admire",
	"group": "A",
	"level": "high",
},
{
	"word": "admission",
	"group": "A",
	"level": "high",
},
{
	"word": "admit",
	"group": "A",
	"level": "high",
},
{
	"word": "adolescence",
	"group": "A",
	"level": "high",
},
{
	"word": "adolescent",
	"group": "A",
	"level": "high",
},
{
	"word": "adopt",
	"group": "A",
	"level": "high",
},
{
	"word": "adore",
	"group": "A",
	"level": "high",
},
{
	"word": "adult",
	"group": "A",
	"level": "high",
},
{
	"word": "advance",
	"group": "A",
	"level": "high",
},
{
	"word": "adventure",
	"group": "A",
	"level": "high",
},
{
	"word": "advertise",
	"group": "A",
	"level": "high",
},
{
	"word": "advertisement",
	"group": "A",
	"level": "high",
},
{
	"word": "advocate",
	"group": "A",
	"level": "high",
},
{
	"word": "affair",
	"group": "A",
	"level": "high",
},
{
	"word": "affect",
	"group": "A",
	"level": "high",
},
{
	"word": "affection",
	"group": "A",
	"level": "high",
},
{
	"word": "afterwards",
	"group": "A",
	"level": "high",
},
{
	"word": "agency",
	"group": "A",
	"level": "high",
},
{
	"word": "agenda",
	"group": "A",
	"level": "high",
},
{
	"word": "agent",
	"group": "A",
	"level": "high",
},
{
	"word": "aggressive",
	"group": "A",
	"level": "high",
},
{
	"word": "agricultural",
	"group": "A",
	"level": "high",
},
{
	"word": "agriculture",
	"group": "A",
	"level": "high",
},
{
	"word": "ahead",
	"group": "A",
	"level": "high",
},
{
	"word": "aid",
	"group": "A",
	"level": "high",
},
{
	"word": "AIDS",
	"group": "A",
	"level": "high",
},
{
	"word": "aim",
	"group": "A",
	"level": "high",
},
{
	"word": "aircraft",
	"group": "A",
	"level": "high",
},
{
	"word": "airline",
	"group": "A",
	"level": "high",
},
{
	"word": "airmail",
	"group": "A",
	"level": "high",
},
{
	"word": "airplane",
	"group": "A",
	"level": "high",
},
{
	"word": "airspace",
	"group": "A",
	"level": "high",
},
{
	"word": "alarm",
	"group": "A",
	"level": "high",
},
{
	"word": "album",
	"group": "A",
	"level": "high",
},
{
	"word": "alcohol",
	"group": "A",
	"level": "high",
},
{
	"word": "alcoholic",
	"group": "A",
	"level": "high",
},
{
	"word": "algebra",
	"group": "A",
	"level": "high",
},
{
	"word": "alike",
	"group": "A",
	"level": "high",
},
{
	"word": "allergic",
	"group": "A",
	"level": "high",
},
{
	"word": "alley",
	"group": "A",
	"level": "high",
},
{
	"word": "allocate",
	"group": "A",
	"level": "high",
},
{
	"word": "allowance",
	"group": "A",
	"level": "high",
},
{
	"word": "alongside",
	"group": "A",
	"level": "high",
},
{
	"word": "alphabet",
	"group": "A",
	"level": "high",
},
{
	"word": "alternative",
	"group": "A",
	"level": "high",
},
{
	"word": "altitude",
	"group": "A",
	"level": "high",
},
{
	"word": "altogether",
	"group": "A",
	"level": "high",
},
{
	"word": "aluminum",
	"group": "A",
	"level": "high",
},
{
	"word": "AM",
	"group": "A",
	"level": "high",
},
{
	"word": "am",
	"group": "A",
	"level": "high",
},
{
	"word": "amateur",
	"group": "A",
	"level": "high",
},
{
	"word": "amaze",
	"group": "A",
	"level": "high",
},
{
	"word": "amazing",
	"group": "A",
	"level": "high",
},
{
	"word": "ambassador",
	"group": "A",
	"level": "high",
},
{
	"word": "ambassadress",
	"group": "A",
	"level": "high",
},
{
	"word": "ambiguous",
	"group": "A",
	"level": "high",
},
{
	"word": "ambition",
	"group": "A",
	"level": "high",
},
{
	"word": "ambulance",
	"group": "A",
	"level": "high",
},
{
	"word": "amount",
	"group": "A",
	"level": "high",
},
{
	"word": "ample",
	"group": "A",
	"level": "high",
},
{
	"word": "amuse",
	"group": "A",
	"level": "high",
},
{
	"word": "amusement",
	"group": "A",
	"level": "high",
},
{
	"word": "analyse",
	"group": "A",
	"level": "high",
},
{
	"word": "analysis",
	"group": "A",
	"level": "high",
},
{
	"word": "analyze",
	"group": "A",
	"level": "high",
},
{
	"word": "ancestor",
	"group": "A",
	"level": "high",
},
{
	"word": "anchor",
	"group": "A",
	"level": "high",
},
{
	"word": "anecdote",
	"group": "A",
	"level": "high",
},
{
	"word": "anger",
	"group": "A",
	"level": "high",
},
{
	"word": "angle",
	"group": "A",
	"level": "high",
},
{
	"word": "ankle",
	"group": "A",
	"level": "high",
},
{
	"word": "anniversary",
	"group": "A",
	"level": "high",
},
{
	"word": "announce",
	"group": "A",
	"level": "high",
},
{
	"word": "annoy",
	"group": "A",
	"level": "high",
},
{
	"word": "annual",
	"group": "A",
	"level": "high",
},
{
	"word": "Antarctic",
	"group": "A",
	"level": "high",
},
{
	"word": "antique",
	"group": "A",
	"level": "high",
},
{
	"word": "anxiety",
	"group": "A",
	"level": "high",
},
{
	"word": "anxious",
	"group": "A",
	"level": "high",
},
{
	"word": "anyhow",
	"group": "A",
	"level": "high",
},
{
	"word": "apart",
	"group": "A",
	"level": "high",
},
{
	"word": "apartment",
	"group": "A",
	"level": "high",
},
{
	"word": "apologize",
	"group": "A",
	"level": "high",
},
{
	"word": "apology",
	"group": "A",
	"level": "high",
},
{
	"word": "apparent",
	"group": "A",
	"level": "high",
},
{
	"word": "appeal",
	"group": "A",
	"level": "high",
},
{
	"word": "appearance",
	"group": "A",
	"level": "high",
},
{
	"word": "appendix",
	"group": "A",
	"level": "high",
},
{
	"word": "appetite",
	"group": "A",
	"level": "high",
},
{
	"word": "applaud",
	"group": "A",
	"level": "high",
},
{
	"word": "applicant",
	"group": "A",
	"level": "high",
},
{
	"word": "application",
	"group": "A",
	"level": "high",
},
{
	"word": "apply",
	"group": "A",
	"level": "high",
},
{
	"word": "appoint",
	"group": "A",
	"level": "high",
},
{
	"word": "appointment",
	"group": "A",
	"level": "high",
},
{
	"word": "appreciate",
	"group": "A",
	"level": "high",
},
{
	"word": "appreciation",
	"group": "A",
	"level": "high",
},
{
	"word": "approach",
	"group": "A",
	"level": "high",
},
{
	"word": "appropriate",
	"group": "A",
	"level": "high",
},
{
	"word": "approval",
	"group": "A",
	"level": "high",
},
{
	"word": "approve",
	"group": "A",
	"level": "high",
},
{
	"word": "approximately",
	"group": "A",
	"level": "high",
},
{
	"word": "apron",
	"group": "A",
	"level": "high",
},
{
	"word": "arbitrary",
	"group": "A",
	"level": "high",
},
{
	"word": "arch",
	"group": "A",
	"level": "high",
},
{
	"word": "architect",
	"group": "A",
	"level": "high",
},
{
	"word": "architecture",
	"group": "A",
	"level": "high",
},
{
	"word": "Arctic",
	"group": "A",
	"level": "high",
},
{
	"word": "are",
	"group": "A",
	"level": "high",
},
{
	"word": "argue",
	"group": "A",
	"level": "high",
},
{
	"word": "argument",
	"group": "A",
	"level": "high",
},
{
	"word": "arise",
	"group": "A",
	"level": "high",
},
{
	"word": "arithmetic",
	"group": "A",
	"level": "high",
},
{
	"word": "armchair",
	"group": "A",
	"level": "high",
},
{
	"word": "arrange",
	"group": "A",
	"level": "high",
},
{
	"word": "arrangement",
	"group": "A",
	"level": "high",
},
{
	"word": "arrest",
	"group": "A",
	"level": "high",
},
{
	"word": "arrival",
	"group": "A",
	"level": "high",
},
{
	"word": "arrow",
	"group": "A",
	"level": "high",
},
{
	"word": "artificial",
	"group": "A",
	"level": "high",
},
{
	"word": "ash",
	"group": "A",
	"level": "high",
},
{
	"word": "ashamed",
	"group": "A",
	"level": "high",
},
{
	"word": "aside",
	"group": "A",
	"level": "high",
},
{
	"word": "aspect",
	"group": "A",
	"level": "high",
},
{
	"word": "assess",
	"group": "A",
	"level": "high",
},
{
	"word": "assessment",
	"group": "A",
	"level": "high",
},
{
	"word": "assist",
	"group": "A",
	"level": "high",
},
{
	"word": "assistance",
	"group": "A",
	"level": "high",
},
{
	"word": "assistant",
	"group": "A",
	"level": "high",
},
{
	"word": "associate",
	"group": "A",
	"level": "high",
},
{
	"word": "association",
	"group": "A",
	"level": "high",
},
{
	"word": "assume",
	"group": "A",
	"level": "high",
},
{
	"word": "assumption",
	"group": "A",
	"level": "high",
},
{
	"word": "astonish",
	"group": "A",
	"level": "high",
},
{
	"word": "astronaut",
	"group": "A",
	"level": "high",
},
{
	"word": "astronomer",
	"group": "A",
	"level": "high",
},
{
	"word": "astronomy",
	"group": "A",
	"level": "high",
},
{
	"word": "athlete",
	"group": "A",
	"level": "high",
},
{
	"word": "athletic",
	"group": "A",
	"level": "high",
},
{
	"word": "Atlantic",
	"group": "A",
	"level": "high",
},
{
	"word": "atmosphere",
	"group": "A",
	"level": "high",
},
{
	"word": "atom",
	"group": "A",
	"level": "high",
},
{
	"word": "attach",
	"group": "A",
	"level": "high",
},
{
	"word": "attack",
	"group": "A",
	"level": "high",
},
{
	"word": "attain",
	"group": "A",
	"level": "high",
},
{
	"word": "attempt",
	"group": "A",
	"level": "high",
},
{
	"word": "attitude",
	"group": "A",
	"level": "high",
},
{
	"word": "attract",
	"group": "A",
	"level": "high",
},
{
	"word": "attraction",
	"group": "A",
	"level": "high",
},
{
	"word": "attractive",
	"group": "A",
	"level": "high",
},
{
	"word": "audience",
	"group": "A",
	"level": "high",
},
{
	"word": "authentic",
	"group": "A",
	"level": "high",
},
{
	"word": "author",
	"group": "A",
	"level": "high",
},
{
	"word": "authority",
	"group": "A",
	"level": "high",
},
{
	"word": "automatic",
	"group": "A",
	"level": "high",
},
{
	"word": "autonomous",
	"group": "A",
	"level": "high",
},
{
	"word": "available",
	"group": "A",
	"level": "high",
},
{
	"word": "avenue",
	"group": "A",
	"level": "high",
},
{
	"word": "average",
	"group": "A",
	"level": "high",
},
{
	"word": "award",
	"group": "A",
	"level": "high",
},
{
	"word": "aware",
	"group": "A",
	"level": "high",
},
{
	"word": "awesome",
	"group": "A",
	"level": "high",
},
{
	"word": "awkward",
	"group": "A",
	"level": "high",
},
{
	"word": "bachelor",
	"group": "B",
	"level": "high",
},
{
	"word": "backwards",
	"group": "B",
	"level": "high",
},
{
	"word": "bacon",
	"group": "B",
	"level": "high",
},
{
	"word": "bacteria",
	"group": "B",
	"level": "high",
},
{
	"word": "bacterium",
	"group": "B",
	"level": "high",
},
{
	"word": "badminton",
	"group": "B",
	"level": "high",
},
{
	"word": "baggage",
	"group": "B",
	"level": "high",
},
{
	"word": "bakery",
	"group": "B",
	"level": "high",
},
{
	"word": "balance",
	"group": "B",
	"level": "high",
},
{
	"word": "balcony",
	"group": "B",
	"level": "high",
},
{
	"word": "ballet",
	"group": "B",
	"level": "high",
},
{
	"word": "ban",
	"group": "B",
	"level": "high",
},
{
	"word": "band",
	"group": "B",
	"level": "high",
},
{
	"word": "bandage",
	"group": "B",
	"level": "high",
},
{
	"word": "bar",
	"group": "B",
	"level": "high",
},
{
	"word": "barbecue",
	"group": "B",
	"level": "high",
},
{
	"word": "barber",
	"group": "B",
	"level": "high",
},
{
	"word": "barbershop",
	"group": "B",
	"level": "high",
},
{
	"word": "bare",
	"group": "B",
	"level": "high",
},
{
	"word": "bargain",
	"group": "B",
	"level": "high",
},
{
	"word": "bark",
	"group": "B",
	"level": "high",
},
{
	"word": "barrier",
	"group": "B",
	"level": "high",
},
{
	"word": "base",
	"group": "B",
	"level": "high",
},
{
	"word": "basement",
	"group": "B",
	"level": "high",
},
{
	"word": "basin",
	"group": "B",
	"level": "high",
},
{
	"word": "basis",
	"group": "B",
	"level": "high",
},
{
	"word": "bat",
	"group": "B",
	"level": "high",
},
{
	"word": "bath",
	"group": "B",
	"level": "high",
},
{
	"word": "bathe",
	"group": "B",
	"level": "high",
},
{
	"word": "bathtub",
	"group": "B",
	"level": "high",
},
{
	"word": "battery",
	"group": "B",
	"level": "high",
},
{
	"word": "battle",
	"group": "B",
	"level": "high",
},
{
	"word": "bay",
	"group": "B",
	"level": "high",
},
{
	"word": "BC",
	"group": "B",
	"level": "high",
},
{
	"word": "bean-curd",
	"group": "B",
	"level": "high",
},
{
	"word": "beard",
	"group": "B",
	"level": "high",
},
{
	"word": "beast",
	"group": "B",
	"level": "high",
},
{
	"word": "beauty",
	"group": "B",
	"level": "high",
},
{
	"word": "beddings",
	"group": "B",
	"level": "high",
},
{
	"word": "bee",
	"group": "B",
	"level": "high",
},
{
	"word": "beer",
	"group": "B",
	"level": "high",
},
{
	"word": "beg",
	"group": "B",
	"level": "high",
},
{
	"word": "behalf",
	"group": "B",
	"level": "high",
},
{
	"word": "behave",
	"group": "B",
	"level": "high",
},
{
	"word": "behaviour",
	"group": "B",
	"level": "high",
},
{
	"word": "being",
	"group": "B",
	"level": "high",
},
{
	"word": "belief",
	"group": "B",
	"level": "high",
},
{
	"word": "belly",
	"group": "B",
	"level": "high",
},
{
	"word": "belong",
	"group": "B",
	"level": "high",
},
{
	"word": "belt",
	"group": "B",
	"level": "high",
},
{
	"word": "bench",
	"group": "B",
	"level": "high",
},
{
	"word": "bend",
	"group": "B",
	"level": "high",
},
{
	"word": "beneath",
	"group": "B",
	"level": "high",
},
{
	"word": "beneficial",
	"group": "B",
	"level": "high",
},
{
	"word": "benefit",
	"group": "B",
	"level": "high",
},
{
	"word": "bent",
	"group": "B",
	"level": "high",
},
{
	"word": "besides",
	"group": "B",
	"level": "high",
},
{
	"word": "betray",
	"group": "B",
	"level": "high",
},
{
	"word": "beyond",
	"group": "B",
	"level": "high",
},
{
	"word": "bicycle",
	"group": "B",
	"level": "high",
},
{
	"word": "bid",
	"group": "B",
	"level": "high",
},
{
	"word": "bingo",
	"group": "B",
	"level": "high",
},
{
	"word": "biochemistry",
	"group": "B",
	"level": "high",
},
{
	"word": "biography",
	"group": "B",
	"level": "high",
},
{
	"word": "biology",
	"group": "B",
	"level": "high",
},
{
	"word": "birthplace",
	"group": "B",
	"level": "high",
},
{
	"word": "bishop",
	"group": "B",
	"level": "high",
},
{
	"word": "bite",
	"group": "B",
	"level": "high",
},
{
	"word": "bitter",
	"group": "B",
	"level": "high",
},
{
	"word": "blame",
	"group": "B",
	"level": "high",
},
{
	"word": "blank",
	"group": "B",
	"level": "high",
},
{
	"word": "blanket",
	"group": "B",
	"level": "high",
},
{
	"word": "bleed",
	"group": "B",
	"level": "high",
},
{
	"word": "bless",
	"group": "B",
	"level": "high",
},
{
	"word": "boil",
	"group": "B",
	"level": "high",
},
{
	"word": "bomb",
	"group": "B",
	"level": "high",
},
{
	"word": "bond",
	"group": "B",
	"level": "high",
},
{
	"word": "bone",
	"group": "B",
	"level": "high",
},
{
	"word": "bonus",
	"group": "B",
	"level": "high",
},
{
	"word": "boom",
	"group": "B",
	"level": "high",
},
{
	"word": "boot",
	"group": "B",
	"level": "high",
},
{
	"word": "border",
	"group": "B",
	"level": "high",
},
{
	"word": "botanical",
	"group": "B",
	"level": "high",
},
{
	"word": "botany",
	"group": "B",
	"level": "high",
},
{
	"word": "bother",
	"group": "B",
	"level": "high",
},
{
	"word": "bounce",
	"group": "B",
	"level": "high",
},
{
	"word": "bound",
	"group": "B",
	"level": "high",
},
{
	"word": "boundary",
	"group": "B",
	"level": "high",
},
{
	"word": "bow",
	"group": "B",
	"level": "high",
},
{
	"word": "bowling",
	"group": "B",
	"level": "high",
},
{
	"word": "boxing",
	"group": "B",
	"level": "high",
},
{
	"word": "boycott",
	"group": "B",
	"level": "high",
},
{
	"word": "brake",
	"group": "B",
	"level": "high",
},
{
	"word": "branch",
	"group": "B",
	"level": "high",
},
{
	"word": "brand",
	"group": "B",
	"level": "high",
},
{
	"word": "bravery",
	"group": "B",
	"level": "high",
},
{
	"word": "breakthrough",
	"group": "B",
	"level": "high",
},
{
	"word": "breast",
	"group": "B",
	"level": "high",
},
{
	"word": "breath",
	"group": "B",
	"level": "high",
},
{
	"word": "breathe",
	"group": "B",
	"level": "high",
},
{
	"word": "breathless",
	"group": "B",
	"level": "high",
},
{
	"word": "brewery",
	"group": "B",
	"level": "high",
},
{
	"word": "brick",
	"group": "B",
	"level": "high",
},
{
	"word": "bride",
	"group": "B",
	"level": "high",
},
{
	"word": "bridegroom",
	"group": "B",
	"level": "high",
},
{
	"word": "brief",
	"group": "B",
	"level": "high",
},
{
	"word": "brilliant",
	"group": "B",
	"level": "high",
},
{
	"word": "broad",
	"group": "B",
	"level": "high",
},
{
	"word": "broadcast",
	"group": "B",
	"level": "high",
},
{
	"word": "brochure",
	"group": "B",
	"level": "high",
},
{
	"word": "broken",
	"group": "B",
	"level": "high",
},
{
	"word": "broom",
	"group": "B",
	"level": "high",
},
{
	"word": "brunch",
	"group": "B",
	"level": "high",
},
{
	"word": "Buddhism",
	"group": "B",
	"level": "high",
},
{
	"word": "budget",
	"group": "B",
	"level": "high",
},
{
	"word": "buffet",
	"group": "B",
	"level": "high",
},
{
	"word": "bunch",
	"group": "B",
	"level": "high",
},
{
	"word": "bungalow",
	"group": "B",
	"level": "high",
},
{
	"word": "burden",
	"group": "B",
	"level": "high",
},
{
	"word": "bureaucratic",
	"group": "B",
	"level": "high",
},
{
	"word": "burglar",
	"group": "B",
	"level": "high",
},
{
	"word": "burst",
	"group": "B",
	"level": "high",
},
{
	"word": "bury",
	"group": "B",
	"level": "high",
},
{
	"word": "bush",
	"group": "B",
	"level": "high",
},
{
	"word": "businessman",
	"group": "B",
	"level": "high",
},
{
	"word": "butcher",
	"group": "B",
	"level": "high",
},
{
	"word": "butter",
	"group": "B",
	"level": "high",
},
{
	"word": "butterfly",
	"group": "B",
	"level": "high",
},
{
	"word": "button",
	"group": "B",
	"level": "high",
},
{
	"word": "bye",
	"group": "B",
	"level": "high",
},
{
	"word": "cab",
	"group": "C",
	"level": "high",
},
{
	"word": "cabbage",
	"group": "C",
	"level": "high",
},
{
	"word": "cafe",
	"group": "C",
	"level": "high",
},
{
	"word": "cafeteria",
	"group": "C",
	"level": "high",
},
{
	"word": "cage",
	"group": "C",
	"level": "high",
},
{
	"word": "calculate",
	"group": "C",
	"level": "high",
},
{
	"word": "calm",
	"group": "C",
	"level": "high",
},
{
	"word": "camel",
	"group": "C",
	"level": "high",
},
{
	"word": "campaign",
	"group": "C",
	"level": "high",
},
{
	"word": "canal",
	"group": "C",
	"level": "high",
},
{
	"word": "cancer",
	"group": "C",
	"level": "high",
},
{
	"word": "candidate",
	"group": "C",
	"level": "high",
},
{
	"word": "canteen",
	"group": "C",
	"level": "high",
},
{
	"word": "capsule",
	"group": "C",
	"level": "high",
},
{
	"word": "captain",
	"group": "C",
	"level": "high",
},
{
	"word": "caption",
	"group": "C",
	"level": "high",
},
{
	"word": "carbon",
	"group": "C",
	"level": "high",
},
{
	"word": "carpet",
	"group": "C",
	"level": "high",
},
{
	"word": "carriage",
	"group": "C",
	"level": "high",
},
{
	"word": "carrier",
	"group": "C",
	"level": "high",
},
{
	"word": "carve",
	"group": "C",
	"level": "high",
},
{
	"word": "case",
	"group": "C",
	"level": "high",
},
{
	"word": "cash",
	"group": "C",
	"level": "high",
},
{
	"word": "cassette",
	"group": "C",
	"level": "high",
},
{
	"word": "cast",
	"group": "C",
	"level": "high",
},
{
	"word": "castle",
	"group": "C",
	"level": "high",
},
{
	"word": "casual",
	"group": "C",
	"level": "high",
},
{
	"word": "catalog",
	"group": "C",
	"level": "high",
},
{
	"word": "catastrophe",
	"group": "C",
	"level": "high",
},
{
	"word": "category",
	"group": "C",
	"level": "high",
},
{
	"word": "cater",
	"group": "C",
	"level": "high",
},
{
	"word": "catholic",
	"group": "C",
	"level": "high",
},
{
	"word": "cattle",
	"group": "C",
	"level": "high",
},
{
	"word": "caution",
	"group": "C",
	"level": "high",
},
{
	"word": "cautious",
	"group": "C",
	"level": "high",
},
{
	"word": "cave",
	"group": "C",
	"level": "high",
},
{
	"word": "CD",
	"group": "C",
	"level": "high",
},
{
	"word": "ceiling",
	"group": "C",
	"level": "high",
},
{
	"word": "celebration",
	"group": "C",
	"level": "high",
},
{
	"word": "cell",
	"group": "C",
	"level": "high",
},
{
	"word": "centigrade",
	"group": "C",
	"level": "high",
},
{
	"word": "centimetre",
	"group": "C",
	"level": "high",
},
{
	"word": "ceremony",
	"group": "C",
	"level": "high",
},
{
	"word": "certificate",
	"group": "C",
	"level": "high",
},
{
	"word": "chain",
	"group": "C",
	"level": "high",
},
{
	"word": "chairman",
	"group": "C",
	"level": "high",
},
{
	"word": "chairwoman",
	"group": "C",
	"level": "high",
},
{
	"word": "challenge",
	"group": "C",
	"level": "high",
},
{
	"word": "challenging",
	"group": "C",
	"level": "high",
},
{
	"word": "champion",
	"group": "C",
	"level": "high",
},
{
	"word": "changeable",
	"group": "C",
	"level": "high",
},
{
	"word": "channel",
	"group": "C",
	"level": "high",
},
{
	"word": "chant",
	"group": "C",
	"level": "high",
},
{
	"word": "chaos",
	"group": "C",
	"level": "high",
},
{
	"word": "chapter",
	"group": "C",
	"level": "high",
},
{
	"word": "character",
	"group": "C",
	"level": "high",
},
{
	"word": "characteristic",
	"group": "C",
	"level": "high",
},
{
	"word": "charge",
	"group": "C",
	"level": "high",
},
{
	"word": "chart",
	"group": "C",
	"level": "high",
},
{
	"word": "chat",
	"group": "C",
	"level": "high",
},
{
	"word": "cheat",
	"group": "C",
	"level": "high",
},
{
	"word": "cheek",
	"group": "C",
	"level": "high",
},
{
	"word": "cheerful",
	"group": "C",
	"level": "high",
},
{
	"word": "cheers",
	"group": "C",
	"level": "high",
},
{
	"word": "cheese",
	"group": "C",
	"level": "high",
},
{
	"word": "chef",
	"group": "C",
	"level": "high",
},
{
	"word": "chemical",
	"group": "C",
	"level": "high",
},
{
	"word": "chemist",
	"group": "C",
	"level": "high",
},
{
	"word": "cheque",
	"group": "C",
	"level": "high",
},
{
	"word": "chest",
	"group": "C",
	"level": "high",
},
{
	"word": "chew",
	"group": "C",
	"level": "high",
},
{
	"word": "chief",
	"group": "C",
	"level": "high",
},
{
	"word": "childhood",
	"group": "C",
	"level": "high",
},
{
	"word": "choir",
	"group": "C",
	"level": "high",
},
{
	"word": "choke",
	"group": "C",
	"level": "high",
},
{
	"word": "chorus",
	"group": "C",
	"level": "high",
},
{
	"word": "Christian",
	"group": "C",
	"level": "high",
},
{
	"word": "church",
	"group": "C",
	"level": "high",
},
{
	"word": "cigar",
	"group": "C",
	"level": "high",
},
{
	"word": "cigarette",
	"group": "C",
	"level": "high",
},
{
	"word": "circuit",
	"group": "C",
	"level": "high",
},
{
	"word": "circulate",
	"group": "C",
	"level": "high",
},
{
	"word": "circumstance",
	"group": "C",
	"level": "high",
},
{
	"word": "circus",
	"group": "C",
	"level": "high",
},
{
	"word": "citizen",
	"group": "C",
	"level": "high",
},
{
	"word": "civil",
	"group": "C",
	"level": "high",
},
{
	"word": "civilian",
	"group": "C",
	"level": "high",
},
{
	"word": "civilizasation",
	"group": "C",
	"level": "high",
},
{
	"word": "civilization",
	"group": "C",
	"level": "high",
},
{
	"word": "clap",
	"group": "C",
	"level": "high",
},
{
	"word": "clarify",
	"group": "C",
	"level": "high",
},
{
	"word": "classic",
	"group": "C",
	"level": "high",
},
{
	"word": "classify",
	"group": "C",
	"level": "high",
},
{
	"word": "claw",
	"group": "C",
	"level": "high",
},
{
	"word": "clay",
	"group": "C",
	"level": "high",
},
{
	"word": "cleaner",
	"group": "C",
	"level": "high",
},
{
	"word": "clerk",
	"group": "C",
	"level": "high",
},
{
	"word": "click",
	"group": "C",
	"level": "high",
},
{
	"word": "climate",
	"group": "C",
	"level": "high",
},
{
	"word": "clinic",
	"group": "C",
	"level": "high",
},
{
	"word": "clone",
	"group": "C",
	"level": "high",
},
{
	"word": "cloth",
	"group": "C",
	"level": "high",
},
{
	"word": "clothing",
	"group": "C",
	"level": "high",
},
{
	"word": "clumsy",
	"group": "C",
	"level": "high",
},
{
	"word": "cocoa",
	"group": "C",
	"level": "high",
},
{
	"word": "coincidence",
	"group": "C",
	"level": "high",
},
{
	"word": "coke",
	"group": "C",
	"level": "high",
},
{
	"word": "collar",
	"group": "C",
	"level": "high",
},
{
	"word": "colleague",
	"group": "C",
	"level": "high",
},
{
	"word": "collection",
	"group": "C",
	"level": "high",
},
{
	"word": "collision",
	"group": "C",
	"level": "high",
},
{
	"word": "comb",
	"group": "C",
	"level": "high",
},
{
	"word": "combine",
	"group": "C",
	"level": "high",
},
{
	"word": "comedy",
	"group": "C",
	"level": "high",
},
{
	"word": "comfort",
	"group": "C",
	"level": "high",
},
{
	"word": "command",
	"group": "C",
	"level": "high",
},
{
	"word": "comment",
	"group": "C",
	"level": "high",
},
{
	"word": "commercial",
	"group": "C",
	"level": "high",
},
{
	"word": "commit",
	"group": "C",
	"level": "high",
},
{
	"word": "commitment",
	"group": "C",
	"level": "high",
},
{
	"word": "committee",
	"group": "C",
	"level": "high",
},
{
	"word": "communism",
	"group": "C",
	"level": "high",
},
{
	"word": "communist",
	"group": "C",
	"level": "high",
},
{
	"word": "companion",
	"group": "C",
	"level": "high",
},
{
	"word": "company",
	"group": "C",
	"level": "high",
},
{
	"word": "compass",
	"group": "C",
	"level": "high",
},
{
	"word": "compensate",
	"group": "C",
	"level": "high",
},
{
	"word": "compete",
	"group": "C",
	"level": "high",
},
{
	"word": "competence",
	"group": "C",
	"level": "high",
},
{
	"word": "complex",
	"group": "C",
	"level": "high",
},
{
	"word": "component",
	"group": "C",
	"level": "high",
},
{
	"word": "composition",
	"group": "C",
	"level": "high",
},
{
	"word": "comprehension",
	"group": "C",
	"level": "high",
},
{
	"word": "compromise",
	"group": "C",
	"level": "high",
},
{
	"word": "compulsory",
	"group": "C",
	"level": "high",
},
{
	"word": "concentrate",
	"group": "C",
	"level": "high",
},
{
	"word": "concept",
	"group": "C",
	"level": "high",
},
{
	"word": "concern",
	"group": "C",
	"level": "high",
},
{
	"word": "conclude",
	"group": "C",
	"level": "high",
},
{
	"word": "conclusion",
	"group": "C",
	"level": "high",
},
{
	"word": "concrete",
	"group": "C",
	"level": "high",
},
{
	"word": "condemn",
	"group": "C",
	"level": "high",
},
{
	"word": "conduct",
	"group": "C",
	"level": "high",
},
{
	"word": "conductor",
	"group": "C",
	"level": "high",
},
{
	"word": "cone",
	"group": "C",
	"level": "high",
},
{
	"word": "conference",
	"group": "C",
	"level": "high",
},
{
	"word": "confident",
	"group": "C",
	"level": "high",
},
{
	"word": "confidential",
	"group": "C",
	"level": "high",
},
{
	"word": "confirm",
	"group": "C",
	"level": "high",
},
{
	"word": "conflict",
	"group": "C",
	"level": "high",
},
{
	"word": "confuse",
	"group": "C",
	"level": "high",
},
{
	"word": "congratulate",
	"group": "C",
	"level": "high",
},
{
	"word": "congratulation",
	"group": "C",
	"level": "high",
},
{
	"word": "connection",
	"group": "C",
	"level": "high",
},
{
	"word": "conscience",
	"group": "C",
	"level": "high",
},
{
	"word": "consensus",
	"group": "C",
	"level": "high",
},
{
	"word": "consequence",
	"group": "C",
	"level": "high",
},
{
	"word": "conservation",
	"group": "C",
	"level": "high",
},
{
	"word": "conservative",
	"group": "C",
	"level": "high",
},
{
	"word": "considerate",
	"group": "C",
	"level": "high",
},
{
	"word": "consideration",
	"group": "C",
	"level": "high",
},
{
	"word": "consist",
	"group": "C",
	"level": "high",
},
{
	"word": "consistent",
	"group": "C",
	"level": "high",
},
{
	"word": "constant",
	"group": "C",
	"level": "high",
},
{
	"word": "constitution",
	"group": "C",
	"level": "high",
},
{
	"word": "construct",
	"group": "C",
	"level": "high",
},
{
	"word": "construction",
	"group": "C",
	"level": "high",
},
{
	"word": "consult",
	"group": "C",
	"level": "high",
},
{
	"word": "consultant",
	"group": "C",
	"level": "high",
},
{
	"word": "consume",
	"group": "C",
	"level": "high",
},
{
	"word": "contain",
	"group": "C",
	"level": "high",
},
{
	"word": "container",
	"group": "C",
	"level": "high",
},
{
	"word": "contemporary",
	"group": "C",
	"level": "high",
},
{
	"word": "content",
	"group": "C",
	"level": "high",
},
{
	"word": "continent",
	"group": "C",
	"level": "high",
},
{
	"word": "contradict",
	"group": "C",
	"level": "high",
},
{
	"word": "contradictory",
	"group": "C",
	"level": "high",
},
{
	"word": "contrary",
	"group": "C",
	"level": "high",
},
{
	"word": "contribute",
	"group": "C",
	"level": "high",
},
{
	"word": "contribution",
	"group": "C",
	"level": "high",
},
{
	"word": "controversial",
	"group": "C",
	"level": "high",
},
{
	"word": "convenience",
	"group": "C",
	"level": "high",
},
{
	"word": "convenient",
	"group": "C",
	"level": "high",
},
{
	"word": "conventional",
	"group": "C",
	"level": "high",
},
{
	"word": "convey",
	"group": "C",
	"level": "high",
},
{
	"word": "convince",
	"group": "C",
	"level": "high",
},
{
	"word": "cooker",
	"group": "C",
	"level": "high",
},
{
	"word": "corporation",
	"group": "C",
	"level": "high",
},
{
	"word": "correction",
	"group": "C",
	"level": "high",
},
{
	"word": "correspond",
	"group": "C",
	"level": "high",
},
{
	"word": "corrupt",
	"group": "C",
	"level": "high",
},
{
	"word": "cottage",
	"group": "C",
	"level": "high",
},
{
	"word": "cotton",
	"group": "C",
	"level": "high",
},
{
	"word": "counter",
	"group": "C",
	"level": "high",
},
{
	"word": "court",
	"group": "C",
	"level": "high",
},
{
	"word": "courtyard",
	"group": "C",
	"level": "high",
},
{
	"word": "cozy",
	"group": "C",
	"level": "high",
},
{
	"word": "crash",
	"group": "C",
	"level": "high",
},
{
	"word": "cream",
	"group": "C",
	"level": "high",
},
{
	"word": "creature",
	"group": "C",
	"level": "high",
},
{
	"word": "credit",
	"group": "C",
	"level": "high",
},
{
	"word": "crew",
	"group": "C",
	"level": "high",
},
{
	"word": "crime",
	"group": "C",
	"level": "high",
},
{
	"word": "criminal",
	"group": "C",
	"level": "high",
},
{
	"word": "criterion",
	"group": "C",
	"level": "high",
},
{
	"word": "crop",
	"group": "C",
	"level": "high",
},
{
	"word": "crossing",
	"group": "C",
	"level": "high",
},
{
	"word": "crossroads",
	"group": "C",
	"level": "high",
},
{
	"word": "crowd",
	"group": "C",
	"level": "high",
},
{
	"word": "cruel",
	"group": "C",
	"level": "high",
},
{
	"word": "cube",
	"group": "C",
	"level": "high",
},
{
	"word": "cubic",
	"group": "C",
	"level": "high",
},
{
	"word": "cuisine",
	"group": "C",
	"level": "high",
},
{
	"word": "cupboard",
	"group": "C",
	"level": "high",
},
{
	"word": "cure",
	"group": "C",
	"level": "high",
},
{
	"word": "curious",
	"group": "C",
	"level": "high",
},
{
	"word": "currency",
	"group": "C",
	"level": "high",
},
{
	"word": "curriculum",
	"group": "C",
	"level": "high",
},
{
	"word": "curtain",
	"group": "C",
	"level": "high",
},
{
	"word": "cushion",
	"group": "C",
	"level": "high",
},
{
	"word": "custom",
	"group": "C",
	"level": "high",
},
{
	"word": "customs",
	"group": "C",
	"level": "high",
},
{
	"word": "cycle",
	"group": "C",
	"level": "high",
},
{
	"word": "cyclist",
	"group": "C",
	"level": "high",
},
{
	"word": "dad",
	"group": "D",
	"level": "high",
},
{
	"word": "daddy",
	"group": "D",
	"level": "high",
},
{
	"word": "dam",
	"group": "D",
	"level": "high",
},
{
	"word": "damage",
	"group": "D",
	"level": "high",
},
{
	"word": "damp",
	"group": "D",
	"level": "high",
},
{
	"word": "dare",
	"group": "D",
	"level": "high",
},
{
	"word": "darkness",
	"group": "D",
	"level": "high",
},
{
	"word": "dash",
	"group": "D",
	"level": "high",
},
{
	"word": "data",
	"group": "D",
	"level": "high",
},
{
	"word": "database",
	"group": "D",
	"level": "high",
},
{
	"word": "dawn",
	"group": "D",
	"level": "high",
},
{
	"word": "deadline",
	"group": "D",
	"level": "high",
},
{
	"word": "death",
	"group": "D",
	"level": "high",
},
{
	"word": "debate",
	"group": "D",
	"level": "high",
},
{
	"word": "debt",
	"group": "D",
	"level": "high",
},
{
	"word": "decade",
	"group": "D",
	"level": "high",
},
{
	"word": "declare",
	"group": "D",
	"level": "high",
},
{
	"word": "decline",
	"group": "D",
	"level": "high",
},
{
	"word": "decorate",
	"group": "D",
	"level": "high",
},
{
	"word": "decoration",
	"group": "D",
	"level": "high",
},
{
	"word": "decrease",
	"group": "D",
	"level": "high",
},
{
	"word": "deed",
	"group": "D",
	"level": "high",
},
{
	"word": "deer",
	"group": "D",
	"level": "high",
},
{
	"word": "defeat",
	"group": "D",
	"level": "high",
},
{
	"word": "defence",
	"group": "D",
	"level": "high",
},
{
	"word": "defend",
	"group": "D",
	"level": "high",
},
{
	"word": "defense",
	"group": "D",
	"level": "high",
},
{
	"word": "delay",
	"group": "D",
	"level": "high",
},
{
	"word": "delete",
	"group": "D",
	"level": "high",
},
{
	"word": "deliberately",
	"group": "D",
	"level": "high",
},
{
	"word": "delicate",
	"group": "D",
	"level": "high",
},
{
	"word": "delight",
	"group": "D",
	"level": "high",
},
{
	"word": "delighted",
	"group": "D",
	"level": "high",
},
{
	"word": "deliver",
	"group": "D",
	"level": "high",
},
{
	"word": "demand",
	"group": "D",
	"level": "high",
},
{
	"word": "dentist",
	"group": "D",
	"level": "high",
},
{
	"word": "department",
	"group": "D",
	"level": "high",
},
{
	"word": "departure",
	"group": "D",
	"level": "high",
},
{
	"word": "deposit",
	"group": "D",
	"level": "high",
},
{
	"word": "depth",
	"group": "D",
	"level": "high",
},
{
	"word": "description",
	"group": "D",
	"level": "high",
},
{
	"word": "desert",
	"group": "D",
	"level": "high",
},
{
	"word": "deserve",
	"group": "D",
	"level": "high",
},
{
	"word": "design",
	"group": "D",
	"level": "high",
},
{
	"word": "desire",
	"group": "D",
	"level": "high",
},
{
	"word": "desperate",
	"group": "D",
	"level": "high",
},
{
	"word": "dessert",
	"group": "D",
	"level": "high",
},
{
	"word": "destination",
	"group": "D",
	"level": "high",
},
{
	"word": "destroy",
	"group": "D",
	"level": "high",
},
{
	"word": "detective",
	"group": "D",
	"level": "high",
},
{
	"word": "determine",
	"group": "D",
	"level": "high",
},
{
	"word": "devote",
	"group": "D",
	"level": "high",
},
{
	"word": "devotion",
	"group": "D",
	"level": "high",
},
{
	"word": "diagram",
	"group": "D",
	"level": "high",
},
{
	"word": "dial",
	"group": "D",
	"level": "high",
},
{
	"word": "dialog",
	"group": "D",
	"level": "high",
},
{
	"word": "diamond",
	"group": "D",
	"level": "high",
},
{
	"word": "dictation",
	"group": "D",
	"level": "high",
},
{
	"word": "did",
	"group": "D",
	"level": "high",
},
{
	"word": "diet",
	"group": "D",
	"level": "high",
},
{
	"word": "differ",
	"group": "D",
	"level": "high",
},
{
	"word": "digest",
	"group": "D",
	"level": "high",
},
{
	"word": "digital",
	"group": "D",
	"level": "high",
},
{
	"word": "dignity",
	"group": "D",
	"level": "high",
},
{
	"word": "dilemma",
	"group": "D",
	"level": "high",
},
{
	"word": "dimension",
	"group": "D",
	"level": "high",
},
{
	"word": "dinosaur",
	"group": "D",
	"level": "high",
},
{
	"word": "dioxide",
	"group": "D",
	"level": "high",
},
{
	"word": "dip",
	"group": "D",
	"level": "high",
},
{
	"word": "diploma",
	"group": "D",
	"level": "high",
},
{
	"word": "directory",
	"group": "D",
	"level": "high",
},
{
	"word": "disability",
	"group": "D",
	"level": "high",
},
{
	"word": "disabled",
	"group": "D",
	"level": "high",
},
{
	"word": "disadvantage",
	"group": "D",
	"level": "high",
},
{
	"word": "disagree",
	"group": "D",
	"level": "high",
},
{
	"word": "disagreement",
	"group": "D",
	"level": "high",
},
{
	"word": "disappear",
	"group": "D",
	"level": "high",
},
{
	"word": "disappoint",
	"group": "D",
	"level": "high",
},
{
	"word": "disappointed",
	"group": "D",
	"level": "high",
},
{
	"word": "disaster",
	"group": "D",
	"level": "high",
},
{
	"word": "disc",
	"group": "D",
	"level": "high",
},
{
	"word": "discount",
	"group": "D",
	"level": "high",
},
{
	"word": "discourage",
	"group": "D",
	"level": "high",
},
{
	"word": "discrimination",
	"group": "D",
	"level": "high",
},
{
	"word": "disease",
	"group": "D",
	"level": "high",
},
{
	"word": "disgusting",
	"group": "D",
	"level": "high",
},
{
	"word": "disk",
	"group": "D",
	"level": "high",
},
{
	"word": "dislike",
	"group": "D",
	"level": "high",
},
{
	"word": "dismiss",
	"group": "D",
	"level": "high",
},
{
	"word": "distance",
	"group": "D",
	"level": "high",
},
{
	"word": "distant",
	"group": "D",
	"level": "high",
},
{
	"word": "distinction",
	"group": "D",
	"level": "high",
},
{
	"word": "distinguish",
	"group": "D",
	"level": "high",
},
{
	"word": "distribute",
	"group": "D",
	"level": "high",
},
{
	"word": "district",
	"group": "D",
	"level": "high",
},
{
	"word": "disturb",
	"group": "D",
	"level": "high",
},
{
	"word": "disturbing",
	"group": "D",
	"level": "high",
},
{
	"word": "dive",
	"group": "D",
	"level": "high",
},
{
	"word": "diverse",
	"group": "D",
	"level": "high",
},
{
	"word": "division",
	"group": "D",
	"level": "high",
},
{
	"word": "divorce",
	"group": "D",
	"level": "high",
},
{
	"word": "dizzy",
	"group": "D",
	"level": "high",
},
{
	"word": "document",
	"group": "D",
	"level": "high",
},
{
	"word": "doll",
	"group": "D",
	"level": "high",
},
{
	"word": "donate",
	"group": "D",
	"level": "high",
},
{
	"word": "done",
	"group": "D",
	"level": "high",
},
{
	"word": "dorm",
	"group": "D",
	"level": "high",
},
{
	"word": "dormitory",
	"group": "D",
	"level": "high",
},
{
	"word": "dot",
	"group": "D",
	"level": "high",
},
{
	"word": "download",
	"group": "D",
	"level": "high",
},
{
	"word": "downstairs",
	"group": "D",
	"level": "high",
},
{
	"word": "downtown",
	"group": "D",
	"level": "high",
},
{
	"word": "dozen",
	"group": "D",
	"level": "high",
},
{
	"word": "Dr",
	"group": "D",
	"level": "high",
},
{
	"word": "draft",
	"group": "D",
	"level": "high",
},
{
	"word": "drag",
	"group": "D",
	"level": "high",
},
{
	"word": "drawback",
	"group": "D",
	"level": "high",
},
{
	"word": "drawer",
	"group": "D",
	"level": "high",
},
{
	"word": "drill",
	"group": "D",
	"level": "high",
},
{
	"word": "drug",
	"group": "D",
	"level": "high",
},
{
	"word": "drum",
	"group": "D",
	"level": "high",
},
{
	"word": "drunk",
	"group": "D",
	"level": "high",
},
{
	"word": "due",
	"group": "D",
	"level": "high",
},
{
	"word": "dull",
	"group": "D",
	"level": "high",
},
{
	"word": "dusk",
	"group": "D",
	"level": "high",
},
{
	"word": "dustbin",
	"group": "D",
	"level": "high",
},
{
	"word": "dusty",
	"group": "D",
	"level": "high",
},
{
	"word": "duty",
	"group": "D",
	"level": "high",
},
{
	"word": "DVD",
	"group": "D",
	"level": "high",
},
{
	"word": "dynamic",
	"group": "D",
	"level": "high",
},
{
	"word": "dynasty",
	"group": "D",
	"level": "high",
},
{
	"word": "eager",
	"group": "E",
	"level": "high",
},
{
	"word": "eagle",
	"group": "E",
	"level": "high",
},
{
	"word": "earn",
	"group": "E",
	"level": "high",
},
{
	"word": "Easter",
	"group": "E",
	"level": "high",
},
{
	"word": "ecology",
	"group": "E",
	"level": "high",
},
{
	"word": "edge",
	"group": "E",
	"level": "high",
},
{
	"word": "edition",
	"group": "E",
	"level": "high",
},
{
	"word": "editor",
	"group": "E",
	"level": "high",
},
{
	"word": "educate",
	"group": "E",
	"level": "high",
},
{
	"word": "educator",
	"group": "E",
	"level": "high",
},
{
	"word": "effect",
	"group": "E",
	"level": "high",
},
{
	"word": "effort",
	"group": "E",
	"level": "high",
},
{
	"word": "eggplant",
	"group": "E",
	"level": "high",
},
{
	"word": "elect",
	"group": "E",
	"level": "high",
},
{
	"word": "electric",
	"group": "E",
	"level": "high",
},
{
	"word": "electrical",
	"group": "E",
	"level": "high",
},
{
	"word": "electricity",
	"group": "E",
	"level": "high",
},
{
	"word": "elegant",
	"group": "E",
	"level": "high",
},
{
	"word": "e-mail",
	"group": "E",
	"level": "high",
},
{
	"word": "embarrass",
	"group": "E",
	"level": "high",
},
{
	"word": "embassy",
	"group": "E",
	"level": "high",
},
{
	"word": "emergency",
	"group": "E",
	"level": "high",
},
{
	"word": "emperor",
	"group": "E",
	"level": "high",
},
{
	"word": "employ",
	"group": "E",
	"level": "high",
},
{
	"word": "encouragement",
	"group": "E",
	"level": "high",
},
{
	"word": "ending",
	"group": "E",
	"level": "high",
},
{
	"word": "endless",
	"group": "E",
	"level": "high",
},
{
	"word": "energetic",
	"group": "E",
	"level": "high",
},
{
	"word": "energy",
	"group": "E",
	"level": "high",
},
{
	"word": "engine",
	"group": "E",
	"level": "high",
},
{
	"word": "enjoyable",
	"group": "E",
	"level": "high",
},
{
	"word": "enlarge",
	"group": "E",
	"level": "high",
},
{
	"word": "enquiry",
	"group": "E",
	"level": "high",
},
{
	"word": "enterprise",
	"group": "E",
	"level": "high",
},
{
	"word": "entertainment",
	"group": "E",
	"level": "high",
},
{
	"word": "enthusiastic",
	"group": "E",
	"level": "high",
},
{
	"word": "entire",
	"group": "E",
	"level": "high",
},
{
	"word": "entrance",
	"group": "E",
	"level": "high",
},
{
	"word": "entry",
	"group": "E",
	"level": "high",
},
{
	"word": "envelope",
	"group": "E",
	"level": "high",
},
{
	"word": "envy",
	"group": "E",
	"level": "high",
},
{
	"word": "equal",
	"group": "E",
	"level": "high",
},
{
	"word": "equality",
	"group": "E",
	"level": "high",
},
{
	"word": "equip",
	"group": "E",
	"level": "high",
},
{
	"word": "equipment",
	"group": "E",
	"level": "high",
},
{
	"word": "error",
	"group": "E",
	"level": "high",
},
{
	"word": "erupt",
	"group": "E",
	"level": "high",
},
{
	"word": "escape",
	"group": "E",
	"level": "high",
},
{
	"word": "essay",
	"group": "E",
	"level": "high",
},
{
	"word": "evaluate",
	"group": "E",
	"level": "high",
},
{
	"word": "event",
	"group": "E",
	"level": "high",
},
{
	"word": "eventually",
	"group": "E",
	"level": "high",
},
{
	"word": "evidence",
	"group": "E",
	"level": "high",
},
{
	"word": "evident",
	"group": "E",
	"level": "high",
},
{
	"word": "evolution",
	"group": "E",
	"level": "high",
},
{
	"word": "exact",
	"group": "E",
	"level": "high",
},
{
	"word": "examination",
	"group": "E",
	"level": "high",
},
{
	"word": "examine",
	"group": "E",
	"level": "high",
},
{
	"word": "exchange",
	"group": "E",
	"level": "high",
},
{
	"word": "excite",
	"group": "E",
	"level": "high",
},
{
	"word": "exhibition",
	"group": "E",
	"level": "high",
},
{
	"word": "exist",
	"group": "E",
	"level": "high",
},
{
	"word": "existence",
	"group": "E",
	"level": "high",
},
{
	"word": "exit",
	"group": "E",
	"level": "high",
},
{
	"word": "expand",
	"group": "E",
	"level": "high",
},
{
	"word": "expectation",
	"group": "E",
	"level": "high",
},
{
	"word": "expense",
	"group": "E",
	"level": "high",
},
{
	"word": "experiment",
	"group": "E",
	"level": "high",
},
{
	"word": "expert",
	"group": "E",
	"level": "high",
},
{
	"word": "explanation",
	"group": "E",
	"level": "high",
},
{
	"word": "explicit",
	"group": "E",
	"level": "high",
},
{
	"word": "explode",
	"group": "E",
	"level": "high",
},
{
	"word": "explore",
	"group": "E",
	"level": "high",
},
{
	"word": "export",
	"group": "E",
	"level": "high",
},
{
	"word": "expose",
	"group": "E",
	"level": "high",
},
{
	"word": "expression",
	"group": "E",
	"level": "high",
},
{
	"word": "extension",
	"group": "E",
	"level": "high",
},
{
	"word": "extra",
	"group": "E",
	"level": "high",
},
{
	"word": "extraordinary",
	"group": "E",
	"level": "high",
},
{
	"word": "extreme",
	"group": "E",
	"level": "high",
},
{
	"word": "eye",
	"group": "E",
	"level": "high",
},
{
	"word": "eyesight",
	"group": "E",
	"level": "high",
},
{
	"word": "face",
	"group": "F",
	"level": "high",
},
{
	"word": "facial",
	"group": "F",
	"level": "high",
},
{
	"word": "fade",
	"group": "F",
	"level": "high",
},
{
	"word": "failure",
	"group": "F",
	"level": "high",
},
{
	"word": "faith",
	"group": "F",
	"level": "high",
},
{
	"word": "False",
	"group": "F",
	"level": "high",
},
{
	"word": "familiar",
	"group": "F",
	"level": "high",
},
{
	"word": "fancy",
	"group": "F",
	"level": "high",
},
{
	"word": "fantasy",
	"group": "F",
	"level": "high",
},
{
	"word": "fare",
	"group": "F",
	"level": "high",
},
{
	"word": "fasten",
	"group": "F",
	"level": "high",
},
{
	"word": "fault",
	"group": "F",
	"level": "high",
},
{
	"word": "favour",
	"group": "F",
	"level": "high",
},
{
	"word": "fax",
	"group": "F",
	"level": "high",
},
{
	"word": "feast",
	"group": "F",
	"level": "high",
},
{
	"word": "feather",
	"group": "F",
	"level": "high",
},
{
	"word": "federal",
	"group": "F",
	"level": "high",
},
{
	"word": "fee",
	"group": "F",
	"level": "high",
},
{
	"word": "fellow",
	"group": "F",
	"level": "high",
},
{
	"word": "female",
	"group": "F",
	"level": "high",
},
{
	"word": "fence",
	"group": "F",
	"level": "high",
},
{
	"word": "ferry",
	"group": "F",
	"level": "high",
},
{
	"word": "fetch",
	"group": "F",
	"level": "high",
},
{
	"word": "fiber",
	"group": "F",
	"level": "high",
},
{
	"word": "fibre",
	"group": "F",
	"level": "high",
},
{
	"word": "fiction",
	"group": "F",
	"level": "high",
},
{
	"word": "fierce",
	"group": "F",
	"level": "high",
},
{
	"word": "figure",
	"group": "F",
	"level": "high",
},
{
	"word": "file",
	"group": "F",
	"level": "high",
},
{
	"word": "filll",
	"group": "F",
	"level": "high",
},
{
	"word": "fim",
	"group": "F",
	"level": "high",
},
{
	"word": "final",
	"group": "F",
	"level": "high",
},
{
	"word": "finance",
	"group": "F",
	"level": "high",
},
{
	"word": "fingernail",
	"group": "F",
	"level": "high",
},
{
	"word": "fireworks",
	"group": "F",
	"level": "high",
},
{
	"word": "firm",
	"group": "F",
	"level": "high",
},
{
	"word": "fist",
	"group": "F",
	"level": "high",
},
{
	"word": "flame",
	"group": "F",
	"level": "high",
},
{
	"word": "flash",
	"group": "F",
	"level": "high",
},
{
	"word": "flashlight",
	"group": "F",
	"level": "high",
},
{
	"word": "flat",
	"group": "F",
	"level": "high",
},
{
	"word": "flee",
	"group": "F",
	"level": "high",
},
{
	"word": "flesh",
	"group": "F",
	"level": "high",
},
{
	"word": "flexible",
	"group": "F",
	"level": "high",
},
{
	"word": "flight",
	"group": "F",
	"level": "high",
},
{
	"word": "float",
	"group": "F",
	"level": "high",
},
{
	"word": "flood",
	"group": "F",
	"level": "high",
},
{
	"word": "flour",
	"group": "F",
	"level": "high",
},
{
	"word": "flow",
	"group": "F",
	"level": "high",
},
{
	"word": "flu",
	"group": "F",
	"level": "high",
},
{
	"word": "fluency",
	"group": "F",
	"level": "high",
},
{
	"word": "fluent",
	"group": "F",
	"level": "high",
},
{
	"word": "focus",
	"group": "F",
	"level": "high",
},
{
	"word": "fog",
	"group": "F",
	"level": "high",
},
{
	"word": "foggy",
	"group": "F",
	"level": "high",
},
{
	"word": "fold",
	"group": "F",
	"level": "high",
},
{
	"word": "folk",
	"group": "F",
	"level": "high",
},
{
	"word": "fond",
	"group": "F",
	"level": "high",
},
{
	"word": "fool",
	"group": "F",
	"level": "high",
},
{
	"word": "foolish",
	"group": "F",
	"level": "high",
},
{
	"word": "forbid",
	"group": "F",
	"level": "high",
},
{
	"word": "forecast",
	"group": "F",
	"level": "high",
},
{
	"word": "forehead",
	"group": "F",
	"level": "high",
},
{
	"word": "foreigner",
	"group": "F",
	"level": "high",
},
{
	"word": "foresee",
	"group": "F",
	"level": "high",
},
{
	"word": "forever",
	"group": "F",
	"level": "high",
},
{
	"word": "forgetful",
	"group": "F",
	"level": "high",
},
{
	"word": "forgive",
	"group": "F",
	"level": "high",
},
{
	"word": "format",
	"group": "F",
	"level": "high",
},
{
	"word": "former",
	"group": "F",
	"level": "high",
},
{
	"word": "fortnight",
	"group": "F",
	"level": "high",
},
{
	"word": "fortunate",
	"group": "F",
	"level": "high",
},
{
	"word": "fortune",
	"group": "F",
	"level": "high",
},
{
	"word": "forward",
	"group": "F",
	"level": "high",
},
{
	"word": "found",
	"group": "F",
	"level": "high",
},
{
	"word": "fountain",
	"group": "F",
	"level": "high",
},
{
	"word": "fox",
	"group": "F",
	"level": "high",
},
{
	"word": "fragile",
	"group": "F",
	"level": "high",
},
{
	"word": "fragrant",
	"group": "F",
	"level": "high",
},
{
	"word": "framework",
	"group": "F",
	"level": "high",
},
{
	"word": "franc",
	"group": "F",
	"level": "high",
},
{
	"word": "freedom",
	"group": "F",
	"level": "high",
},
{
	"word": "freeway",
	"group": "F",
	"level": "high",
},
{
	"word": "freeze",
	"group": "F",
	"level": "high",
},
{
	"word": "freezing",
	"group": "F",
	"level": "high",
},
{
	"word": "frequent",
	"group": "F",
	"level": "high",
},
{
	"word": "friction",
	"group": "F",
	"level": "high",
},
{
	"word": "frighten",
	"group": "F",
	"level": "high",
},
{
	"word": "frog",
	"group": "F",
	"level": "high",
},
{
	"word": "frontier",
	"group": "F",
	"level": "high",
},
{
	"word": "frost",
	"group": "F",
	"level": "high",
},
{
	"word": "fry",
	"group": "F",
	"level": "high",
},
{
	"word": "fuel",
	"group": "F",
	"level": "high",
},
{
	"word": "function",
	"group": "F",
	"level": "high",
},
{
	"word": "fundamental",
	"group": "F",
	"level": "high",
},
{
	"word": "funeral",
	"group": "F",
	"level": "high",
},
{
	"word": "fur",
	"group": "F",
	"level": "high",
},
{
	"word": "furnished",
	"group": "F",
	"level": "high",
},
{
	"word": "furniture",
	"group": "F",
	"level": "high",
},
{
	"word": "gain",
	"group": "G",
	"level": "high",
},
{
	"word": "gallery",
	"group": "G",
	"level": "high",
},
{
	"word": "gallon",
	"group": "G",
	"level": "high",
},
{
	"word": "garage",
	"group": "G",
	"level": "high",
},
{
	"word": "garbage",
	"group": "G",
	"level": "high",
},
{
	"word": "garlic",
	"group": "G",
	"level": "high",
},
{
	"word": "garment",
	"group": "G",
	"level": "high",
},
{
	"word": "gas",
	"group": "G",
	"level": "high",
},
{
	"word": "gather",
	"group": "G",
	"level": "high",
},
{
	"word": "gay",
	"group": "G",
	"level": "high",
},
{
	"word": "generation",
	"group": "G",
	"level": "high",
},
{
	"word": "generous",
	"group": "G",
	"level": "high",
},
{
	"word": "gentle",
	"group": "G",
	"level": "high",
},
{
	"word": "geometry",
	"group": "G",
	"level": "high",
},
{
	"word": "gesture",
	"group": "G",
	"level": "high",
},
{
	"word": "gifted",
	"group": "G",
	"level": "high",
},
{
	"word": "glance",
	"group": "G",
	"level": "high",
},
{
	"word": "glare",
	"group": "G",
	"level": "high",
},
{
	"word": "globe",
	"group": "G",
	"level": "high",
},
{
	"word": "glory",
	"group": "G",
	"level": "high",
},
{
	"word": "goal",
	"group": "G",
	"level": "high",
},
{
	"word": "god",
	"group": "G",
	"level": "high",
},
{
	"word": "golden",
	"group": "G",
	"level": "high",
},
{
	"word": "golf",
	"group": "G",
	"level": "high",
},
{
	"word": "goods",
	"group": "G",
	"level": "high",
},
{
	"word": "goose",
	"group": "G",
	"level": "high",
},
{
	"word": "govern",
	"group": "G",
	"level": "high",
},
{
	"word": "gradual",
	"group": "G",
	"level": "high",
},
{
	"word": "graduate",
	"group": "G",
	"level": "high",
},
{
	"word": "graduation",
	"group": "G",
	"level": "high",
},
{
	"word": "grain",
	"group": "G",
	"level": "high",
},
{
	"word": "gram",
	"group": "G",
	"level": "high",
},
{
	"word": "grand",
	"group": "G",
	"level": "high",
},
{
	"word": "grandchild",
	"group": "G",
	"level": "high",
},
{
	"word": "grandma",
	"group": "G",
	"level": "high",
},
{
	"word": "grandpa",
	"group": "G",
	"level": "high",
},
{
	"word": "grandparents",
	"group": "G",
	"level": "high",
},
{
	"word": "granny",
	"group": "G",
	"level": "high",
},
{
	"word": "graph",
	"group": "G",
	"level": "high",
},
{
	"word": "grasp",
	"group": "G",
	"level": "high",
},
{
	"word": "grateful",
	"group": "G",
	"level": "high",
},
{
	"word": "gravity",
	"group": "G",
	"level": "high",
},
{
	"word": "gray",
	"group": "G",
	"level": "high",
},
{
	"word": "greedy",
	"group": "G",
	"level": "high",
},
{
	"word": "greengrocer",
	"group": "G",
	"level": "high",
},
{
	"word": "greet",
	"group": "G",
	"level": "high",
},
{
	"word": "greeting",
	"group": "G",
	"level": "high",
},
{
	"word": "grill",
	"group": "G",
	"level": "high",
},
{
	"word": "grocer",
	"group": "G",
	"level": "high",
},
{
	"word": "grocery",
	"group": "G",
	"level": "high",
},
{
	"word": "growth",
	"group": "G",
	"level": "high",
},
{
	"word": "guarantee",
	"group": "G",
	"level": "high",
},
{
	"word": "guidance",
	"group": "G",
	"level": "high",
},
{
	"word": "guilty",
	"group": "G",
	"level": "high",
},
{
	"word": "gym",
	"group": "G",
	"level": "high",
},
{
	"word": "gymnastics",
	"group": "G",
	"level": "high",
},
{
	"word": "haircut",
	"group": "H",
	"level": "high",
},
{
	"word": "ham",
	"group": "H",
	"level": "high",
},
{
	"word": "hammer",
	"group": "H",
	"level": "high",
},
{
	"word": "handful",
	"group": "H",
	"level": "high",
},
{
	"word": "handkerchief",
	"group": "H",
	"level": "high",
},
{
	"word": "handle",
	"group": "H",
	"level": "high",
},
{
	"word": "handwriting",
	"group": "H",
	"level": "high",
},
{
	"word": "handy",
	"group": "H",
	"level": "high",
},
{
	"word": "happiness",
	"group": "H",
	"level": "high",
},
{
	"word": "harbour",
	"group": "H",
	"level": "high",
},
{
	"word": "hardship",
	"group": "H",
	"level": "high",
},
{
	"word": "hardworking",
	"group": "H",
	"level": "high",
},
{
	"word": "harm",
	"group": "H",
	"level": "high",
},
{
	"word": "harmony",
	"group": "H",
	"level": "high",
},
{
	"word": "harvest",
	"group": "H",
	"level": "high",
},
{
	"word": "hatch",
	"group": "H",
	"level": "high",
},
{
	"word": "headline",
	"group": "H",
	"level": "high",
},
{
	"word": "headmaster",
	"group": "H",
	"level": "high",
},
{
	"word": "headmistress",
	"group": "H",
	"level": "high",
},
{
	"word": "hearing",
	"group": "H",
	"level": "high",
},
{
	"word": "heaven",
	"group": "H",
	"level": "high",
},
{
	"word": "heel",
	"group": "H",
	"level": "high",
},
{
	"word": "helicopter",
	"group": "H",
	"level": "high",
},
{
	"word": "helmet",
	"group": "H",
	"level": "high",
},
{
	"word": "herb",
	"group": "H",
	"level": "high",
},
{
	"word": "hesitate",
	"group": "H",
	"level": "high",
},
{
	"word": "highway",
	"group": "H",
	"level": "high",
},
{
	"word": "hire",
	"group": "H",
	"level": "high",
},
{
	"word": "holy",
	"group": "H",
	"level": "high",
},
{
	"word": "homeland",
	"group": "H",
	"level": "high",
},
{
	"word": "honey",
	"group": "H",
	"level": "high",
},
{
	"word": "honour",
	"group": "H",
	"level": "high",
},
{
	"word": "hook",
	"group": "H",
	"level": "high",
},
{
	"word": "hopeful",
	"group": "H",
	"level": "high",
},
{
	"word": "hopeless",
	"group": "H",
	"level": "high",
},
{
	"word": "horrible",
	"group": "H",
	"level": "high",
},
{
	"word": "host",
	"group": "H",
	"level": "high",
},
{
	"word": "hostess",
	"group": "H",
	"level": "high",
},
{
	"word": "hotdog",
	"group": "H",
	"level": "high",
},
{
	"word": "housewife",
	"group": "H",
	"level": "high",
},
{
	"word": "howl",
	"group": "H",
	"level": "high",
},
{
	"word": "hug",
	"group": "H",
	"level": "high",
},
{
	"word": "human-being",
	"group": "H",
	"level": "high",
},
{
	"word": "humour",
	"group": "H",
	"level": "high",
},
{
	"word": "hunger",
	"group": "H",
	"level": "high",
},
{
	"word": "hunt",
	"group": "H",
	"level": "high",
},
{
	"word": "hunter",
	"group": "H",
	"level": "high",
},
{
	"word": "hurricane",
	"group": "H",
	"level": "high",
},
{
	"word": "hydrogen",
	"group": "H",
	"level": "high",
},
{
	"word": "identification",
	"group": "I",
	"level": "high",
},
{
	"word": "identity",
	"group": "I",
	"level": "high",
},
{
	"word": "idiom",
	"group": "I",
	"level": "high",
},
{
	"word": "ignore",
	"group": "I",
	"level": "high",
},
{
	"word": "illegal",
	"group": "I",
	"level": "high",
},
{
	"word": "immediately",
	"group": "I",
	"level": "high",
},
{
	"word": "immigration",
	"group": "I",
	"level": "high",
},
{
	"word": "import",
	"group": "I",
	"level": "high",
},
{
	"word": "importance",
	"group": "I",
	"level": "high",
},
{
	"word": "impress",
	"group": "I",
	"level": "high",
},
{
	"word": "impression",
	"group": "I",
	"level": "high",
},
{
	"word": "improve",
	"group": "I",
	"level": "high",
},
{
	"word": "inch",
	"group": "I",
	"level": "high",
},
{
	"word": "incident",
	"group": "I",
	"level": "high",
},
{
	"word": "income",
	"group": "I",
	"level": "high",
},
{
	"word": "indeed",
	"group": "I",
	"level": "high",
},
{
	"word": "independence",
	"group": "I",
	"level": "high",
},
{
	"word": "independent",
	"group": "I",
	"level": "high",
},
{
	"word": "indicate",
	"group": "I",
	"level": "high",
},
{
	"word": "inform",
	"group": "I",
	"level": "high",
},
{
	"word": "initial",
	"group": "I",
	"level": "high",
},
{
	"word": "injure",
	"group": "I",
	"level": "high",
},
{
	"word": "injury",
	"group": "I",
	"level": "high",
},
{
	"word": "ink",
	"group": "I",
	"level": "high",
},
{
	"word": "inn",
	"group": "I",
	"level": "high",
},
{
	"word": "innocent",
	"group": "I",
	"level": "high",
},
{
	"word": "insect",
	"group": "I",
	"level": "high",
},
{
	"word": "insert",
	"group": "I",
	"level": "high",
},
{
	"word": "insist",
	"group": "I",
	"level": "high",
},
{
	"word": "inspect",
	"group": "I",
	"level": "high",
},
{
	"word": "inspire",
	"group": "I",
	"level": "high",
},
{
	"word": "instant",
	"group": "I",
	"level": "high",
},
{
	"word": "institute",
	"group": "I",
	"level": "high",
},
{
	"word": "institution",
	"group": "I",
	"level": "high",
},
{
	"word": "instruct",
	"group": "I",
	"level": "high",
},
{
	"word": "insurance",
	"group": "I",
	"level": "high",
},
{
	"word": "insure",
	"group": "I",
	"level": "high",
},
{
	"word": "intelligence",
	"group": "I",
	"level": "high",
},
{
	"word": "intent",
	"group": "I",
	"level": "high",
},
{
	"word": "intention",
	"group": "I",
	"level": "high",
},
{
	"word": "interpreter",
	"group": "I",
	"level": "high",
},
{
	"word": "interrupt",
	"group": "I",
	"level": "high",
},
{
	"word": "interval",
	"group": "I",
	"level": "high",
},
{
	"word": "invitation",
	"group": "I",
	"level": "high",
},
{
	"word": "iron",
	"group": "I",
	"level": "high",
},
{
	"word": "irrigation",
	"group": "I",
	"level": "high",
},
{
	"word": "is",
	"group": "I",
	"level": "high",
},
{
	"word": "jam",
	"group": "J",
	"level": "high",
},
{
	"word": "jar",
	"group": "J",
	"level": "high",
},
{
	"word": "jaw",
	"group": "J",
	"level": "high",
},
{
	"word": "jazz",
	"group": "J",
	"level": "high",
},
{
	"word": "jeans",
	"group": "J",
	"level": "high",
},
{
	"word": "jeep",
	"group": "J",
	"level": "high",
},
{
	"word": "jet",
	"group": "J",
	"level": "high",
},
{
	"word": "jewllery",
	"group": "J",
	"level": "high",
},
{
	"word": "jog",
	"group": "J",
	"level": "high",
},
{
	"word": "journalist",
	"group": "J",
	"level": "high",
},
{
	"word": "joy",
	"group": "J",
	"level": "high",
},
{
	"word": "judge",
	"group": "J",
	"level": "high",
},
{
	"word": "judgement",
	"group": "J",
	"level": "high",
},
{
	"word": "jungle",
	"group": "J",
	"level": "high",
},
{
	"word": "junior",
	"group": "J",
	"level": "high",
},
{
	"word": "justice",
	"group": "J",
	"level": "high",
},
{
	"word": "kangaroo",
	"group": "K",
	"level": "high",
},
{
	"word": "kettle",
	"group": "K",
	"level": "high",
},
{
	"word": "kilogramme",
	"group": "K",
	"level": "high",
},
{
	"word": "kindergarten",
	"group": "K",
	"level": "high",
},
{
	"word": "kindness",
	"group": "K",
	"level": "high",
},
{
	"word": "kingdom",
	"group": "K",
	"level": "high",
},
{
	"word": "labour",
	"group": "L",
	"level": "high",
},
{
	"word": "lack",
	"group": "L",
	"level": "high",
},
{
	"word": "lamb",
	"group": "L",
	"level": "high",
},
{
	"word": "lame",
	"group": "L",
	"level": "high",
},
{
	"word": "lamp",
	"group": "L",
	"level": "high",
},
{
	"word": "lantern",
	"group": "L",
	"level": "high",
},
{
	"word": "lap",
	"group": "L",
	"level": "high",
},
{
	"word": "latter",
	"group": "L",
	"level": "high",
},
{
	"word": "laughter",
	"group": "L",
	"level": "high",
},
{
	"word": "laundry",
	"group": "L",
	"level": "high",
},
{
	"word": "lawyer",
	"group": "L",
	"level": "high",
},
{
	"word": "league",
	"group": "L",
	"level": "high",
},
{
	"word": "leak",
	"group": "L",
	"level": "high",
},
{
	"word": "leather",
	"group": "L",
	"level": "high",
},
{
	"word": "lecture",
	"group": "L",
	"level": "high",
},
{
	"word": "legal",
	"group": "L",
	"level": "high",
},
{
	"word": "lemonade",
	"group": "L",
	"level": "high",
},
{
	"word": "length",
	"group": "L",
	"level": "high",
},
{
	"word": "liberation",
	"group": "L",
	"level": "high",
},
{
	"word": "liberty",
	"group": "L",
	"level": "high",
},
{
	"word": "librarian",
	"group": "L",
	"level": "high",
},
{
	"word": "license",
	"group": "L",
	"level": "high",
},
{
	"word": "lid",
	"group": "L",
	"level": "high",
},
{
	"word": "lightening",
	"group": "L",
	"level": "high",
},
{
	"word": "likely",
	"group": "L",
	"level": "high",
},
{
	"word": "limit",
	"group": "L",
	"level": "high",
},
{
	"word": "link",
	"group": "L",
	"level": "high",
},
{
	"word": "lip",
	"group": "L",
	"level": "high",
},
{
	"word": "liquid",
	"group": "L",
	"level": "high",
},
{
	"word": "literary",
	"group": "L",
	"level": "high",
},
{
	"word": "literature",
	"group": "L",
	"level": "high",
},
{
	"word": "litre",
	"group": "L",
	"level": "high",
},
{
	"word": "load",
	"group": "L",
	"level": "high",
},
{
	"word": "loaf",
	"group": "L",
	"level": "high",
},
{
	"word": "loose",
	"group": "L",
	"level": "high",
},
{
	"word": "lorry",
	"group": "L",
	"level": "high",
},
{
	"word": "loss",
	"group": "L",
	"level": "high",
},
{
	"word": "lounge",
	"group": "L",
	"level": "high",
},
{
	"word": "luggage",
	"group": "L",
	"level": "high",
},
{
	"word": "lung",
	"group": "L",
	"level": "high",
},
{
	"word": "madam",
	"group": "M",
	"level": "high",
},
{
	"word": "Madame",
	"group": "M",
	"level": "high",
},
{
	"word": "maid",
	"group": "M",
	"level": "high",
},
{
	"word": "mail",
	"group": "M",
	"level": "high",
},
{
	"word": "mailbox",
	"group": "M",
	"level": "high",
},
{
	"word": "mainland",
	"group": "M",
	"level": "high",
},
{
	"word": "major",
	"group": "M",
	"level": "high",
},
{
	"word": "majority",
	"group": "M",
	"level": "high",
},
{
	"word": "male",
	"group": "M",
	"level": "high",
},
{
	"word": "mankind",
	"group": "M",
	"level": "high",
},
{
	"word": "manner",
	"group": "M",
	"level": "high",
},
{
	"word": "maple",
	"group": "M",
	"level": "high",
},
{
	"word": "marathon",
	"group": "M",
	"level": "high",
},
{
	"word": "marble",
	"group": "M",
	"level": "high",
},
{
	"word": "march",
	"group": "M",
	"level": "high",
},
{
	"word": "marriage",
	"group": "M",
	"level": "high",
},
{
	"word": "mask",
	"group": "M",
	"level": "high",
},
{
	"word": "mass",
	"group": "M",
	"level": "high",
},
{
	"word": "master",
	"group": "M",
	"level": "high",
},
{
	"word": "mat",
	"group": "M",
	"level": "high",
},
{
	"word": "material",
	"group": "M",
	"level": "high",
},
{
	"word": "math",
	"group": "M",
	"level": "high",
},
{
	"word": "mathematics",
	"group": "M",
	"level": "high",
},
{
	"word": "mature",
	"group": "M",
	"level": "high",
},
{
	"word": "maximum",
	"group": "M",
	"level": "high",
},
{
	"word": "means",
	"group": "M",
	"level": "high",
},
{
	"word": "meanwhile",
	"group": "M",
	"level": "high",
},
{
	"word": "measure",
	"group": "M",
	"level": "high",
},
{
	"word": "medal",
	"group": "M",
	"level": "high",
},
{
	"word": "media",
	"group": "M",
	"level": "high",
},
{
	"word": "medium",
	"group": "M",
	"level": "high",
},
{
	"word": "melon",
	"group": "M",
	"level": "high",
},
{
	"word": "memorial",
	"group": "M",
	"level": "high",
},
{
	"word": "memory",
	"group": "M",
	"level": "high",
},
{
	"word": "mend",
	"group": "M",
	"level": "high",
},
{
	"word": "mental",
	"group": "M",
	"level": "high",
},
{
	"word": "merchant",
	"group": "M",
	"level": "high",
},
{
	"word": "merciful",
	"group": "M",
	"level": "high",
},
{
	"word": "mercy",
	"group": "M",
	"level": "high",
},
{
	"word": "merely",
	"group": "M",
	"level": "high",
},
{
	"word": "merry",
	"group": "M",
	"level": "high",
},
{
	"word": "messy",
	"group": "M",
	"level": "high",
},
{
	"word": "metal",
	"group": "M",
	"level": "high",
},
{
	"word": "microscope",
	"group": "M",
	"level": "high",
},
{
	"word": "microwave",
	"group": "M",
	"level": "high",
},
{
	"word": "midnight",
	"group": "M",
	"level": "high",
},
{
	"word": "mild",
	"group": "M",
	"level": "high",
},
{
	"word": "millionaire",
	"group": "M",
	"level": "high",
},
{
	"word": "mineral",
	"group": "M",
	"level": "high",
},
{
	"word": "minibus",
	"group": "M",
	"level": "high",
},
{
	"word": "minimum",
	"group": "M",
	"level": "high",
},
{
	"word": "minister",
	"group": "M",
	"level": "high",
},
{
	"word": "ministry",
	"group": "M",
	"level": "high",
},
{
	"word": "minus",
	"group": "M",
	"level": "high",
},
{
	"word": "mirror",
	"group": "M",
	"level": "high",
},
{
	"word": "missile",
	"group": "M",
	"level": "high",
},
{
	"word": "mist",
	"group": "M",
	"level": "high",
},
{
	"word": "mistaken",
	"group": "M",
	"level": "high",
},
{
	"word": "misunderstand",
	"group": "M",
	"level": "high",
},
{
	"word": "mixture",
	"group": "M",
	"level": "high",
},
{
	"word": "mm",
	"group": "M",
	"level": "high",
},
{
	"word": "mobile",
	"group": "M",
	"level": "high",
},
{
	"word": "modem",
	"group": "M",
	"level": "high",
},
{
	"word": "modest",
	"group": "M",
	"level": "high",
},
{
	"word": "mom",
	"group": "M",
	"level": "high",
},
{
	"word": "moment",
	"group": "M",
	"level": "high",
},
{
	"word": "mommy",
	"group": "M",
	"level": "high",
},
{
	"word": "monitor",
	"group": "M",
	"level": "high",
},
{
	"word": "monument",
	"group": "M",
	"level": "high",
},
{
	"word": "mop",
	"group": "M",
	"level": "high",
},
{
	"word": "moral",
	"group": "M",
	"level": "high",
},
{
	"word": "Moslem",
	"group": "M",
	"level": "high",
},
{
	"word": "mosquito",
	"group": "M",
	"level": "high",
},
{
	"word": "motherland",
	"group": "M",
	"level": "high",
},
{
	"word": "motivation",
	"group": "M",
	"level": "high",
},
{
	"word": "motor",
	"group": "M",
	"level": "high",
},
{
	"word": "motorcycle",
	"group": "M",
	"level": "high",
},
{
	"word": "motto",
	"group": "M",
	"level": "high",
},
{
	"word": "mountainous",
	"group": "M",
	"level": "high",
},
{
	"word": "mourn",
	"group": "M",
	"level": "high",
},
{
	"word": "moustache",
	"group": "M",
	"level": "high",
},
{
	"word": "movement",
	"group": "M",
	"level": "high",
},
{
	"word": "Mr.",
	"group": "M",
	"level": "high",
},
{
	"word": "Mrs.",
	"group": "M",
	"level": "high",
},
{
	"word": "Ms.",
	"group": "M",
	"level": "high",
},
{
	"word": "mud",
	"group": "M",
	"level": "high",
},
{
	"word": "muddy",
	"group": "M",
	"level": "high",
},
{
	"word": "multiply",
	"group": "M",
	"level": "high",
},
{
	"word": "mum",
	"group": "M",
	"level": "high",
},
{
	"word": "mummy",
	"group": "M",
	"level": "high",
},
{
	"word": "murder",
	"group": "M",
	"level": "high",
},
{
	"word": "mushroom",
	"group": "M",
	"level": "high",
},
{
	"word": "musical",
	"group": "M",
	"level": "high",
},
{
	"word": "mustard",
	"group": "M",
	"level": "high",
},
{
	"word": "mutton",
	"group": "M",
	"level": "high",
},
{
	"word": "nail",
	"group": "N",
	"level": "high",
},
{
	"word": "narrow",
	"group": "N",
	"level": "high",
},
{
	"word": "nation",
	"group": "N",
	"level": "high",
},
{
	"word": "nationality",
	"group": "N",
	"level": "high",
},
{
	"word": "nationwide",
	"group": "N",
	"level": "high",
},
{
	"word": "native",
	"group": "N",
	"level": "high",
},
{
	"word": "navy",
	"group": "N",
	"level": "high",
},
{
	"word": "nearby",
	"group": "N",
	"level": "high",
},
{
	"word": "neat",
	"group": "N",
	"level": "high",
},
{
	"word": "necklace",
	"group": "N",
	"level": "high",
},
{
	"word": "needle",
	"group": "N",
	"level": "high",
},
{
	"word": "negotiate",
	"group": "N",
	"level": "high",
},
{
	"word": "neighbourhood",
	"group": "N",
	"level": "high",
},
{
	"word": "nephew",
	"group": "N",
	"level": "high",
},
{
	"word": "nest",
	"group": "N",
	"level": "high",
},
{
	"word": "net",
	"group": "N",
	"level": "high",
},
{
	"word": "network",
	"group": "N",
	"level": "high",
},
{
	"word": "newspaper",
	"group": "N",
	"level": "high",
},
{
	"word": "niece",
	"group": "N",
	"level": "high",
},
{
	"word": "No.",
	"group": "N",
	"level": "high",
},
{
	"word": "noble",
	"group": "N",
	"level": "high",
},
{
	"word": "nod",
	"group": "N",
	"level": "high",
},
{
	"word": "normal",
	"group": "N",
	"level": "high",
},
{
	"word": "northeast",
	"group": "N",
	"level": "high",
},
{
	"word": "northwest",
	"group": "N",
	"level": "high",
},
{
	"word": "novel",
	"group": "N",
	"level": "high",
},
{
	"word": "novelist",
	"group": "N",
	"level": "high",
},
{
	"word": "nowadays",
	"group": "N",
	"level": "high",
},
{
	"word": "nowhere",
	"group": "N",
	"level": "high",
},
{
	"word": "nuclear",
	"group": "N",
	"level": "high",
},
{
	"word": "numb",
	"group": "N",
	"level": "high",
},
{
	"word": "nursery",
	"group": "N",
	"level": "high",
},
{
	"word": "nut",
	"group": "N",
	"level": "high",
},
{
	"word": "nutrition",
	"group": "N",
	"level": "high",
},
{
	"word": "O.K.",
	"group": "O",
	"level": "high",
},
{
	"word": "obey",
	"group": "O",
	"level": "high",
},
{
	"word": "observe",
	"group": "O",
	"level": "high",
},
{
	"word": "obtain",
	"group": "O",
	"level": "high",
},
{
	"word": "obvious",
	"group": "O",
	"level": "high",
},
{
	"word": "occupation",
	"group": "O",
	"level": "high",
},
{
	"word": "occupy",
	"group": "O",
	"level": "high",
},
{
	"word": "occur",
	"group": "O",
	"level": "high",
},
{
	"word": "ocean",
	"group": "O",
	"level": "high",
},
{
	"word": "Oceania",
	"group": "O",
	"level": "high",
},
{
	"word": "offence",
	"group": "O",
	"level": "high",
},
{
	"word": "official",
	"group": "O",
	"level": "high",
},
{
	"word": "offshore",
	"group": "O",
	"level": "high",
},
{
	"word": "oh",
	"group": "O",
	"level": "high",
},
{
	"word": "oilfield",
	"group": "O",
	"level": "high",
},
{
	"word": "oneself",
	"group": "O",
	"level": "high",
},
{
	"word": "onion",
	"group": "O",
	"level": "high",
},
{
	"word": "onto",
	"group": "O",
	"level": "high",
},
{
	"word": "opening",
	"group": "O",
	"level": "high",
},
{
	"word": "opera",
	"group": "O",
	"level": "high",
},
{
	"word": "operate",
	"group": "O",
	"level": "high",
},
{
	"word": "operation",
	"group": "O",
	"level": "high",
},
{
	"word": "operator",
	"group": "O",
	"level": "high",
},
{
	"word": "opinion",
	"group": "O",
	"level": "high",
},
{
	"word": "oppose",
	"group": "O",
	"level": "high",
},
{
	"word": "optimistic",
	"group": "O",
	"level": "high",
},
{
	"word": "optional",
	"group": "O",
	"level": "high",
},
{
	"word": "oral",
	"group": "O",
	"level": "high",
},
{
	"word": "orbit",
	"group": "O",
	"level": "high",
},
{
	"word": "ordinary",
	"group": "O",
	"level": "high",
},
{
	"word": "organ",
	"group": "O",
	"level": "high",
},
{
	"word": "organise",
	"group": "O",
	"level": "high",
},
{
	"word": "organization",
	"group": "O",
	"level": "high",
},
{
	"word": "origin",
	"group": "O",
	"level": "high",
},
{
	"word": "otherwise",
	"group": "O",
	"level": "high",
},
{
	"word": "ought",
	"group": "O",
	"level": "high",
},
{
	"word": "outcome",
	"group": "O",
	"level": "high",
},
{
	"word": "outdoors",
	"group": "O",
	"level": "high",
},
{
	"word": "outer",
	"group": "O",
	"level": "high",
},
{
	"word": "outgoing",
	"group": "O",
	"level": "high",
},
{
	"word": "outing",
	"group": "O",
	"level": "high",
},
{
	"word": "outline",
	"group": "O",
	"level": "high",
},
{
	"word": "output",
	"group": "O",
	"level": "high",
},
{
	"word": "outspoken",
	"group": "O",
	"level": "high",
},
{
	"word": "outstanding",
	"group": "O",
	"level": "high",
},
{
	"word": "outwards",
	"group": "O",
	"level": "high",
},
{
	"word": "oval",
	"group": "O",
	"level": "high",
},
{
	"word": "overcoat",
	"group": "O",
	"level": "high",
},
{
	"word": "overcome",
	"group": "O",
	"level": "high",
},
{
	"word": "overhead",
	"group": "O",
	"level": "high",
},
{
	"word": "overlook",
	"group": "O",
	"level": "high",
},
{
	"word": "overweight",
	"group": "O",
	"level": "high",
},
{
	"word": "owe",
	"group": "O",
	"level": "high",
},
{
	"word": "owner",
	"group": "O",
	"level": "high",
},
{
	"word": "ownership",
	"group": "O",
	"level": "high",
},
{
	"word": "ox",
	"group": "O",
	"level": "high",
},
{
	"word": "oxygen",
	"group": "O",
	"level": "high",
},
{
	"word": "P.C.",
	"group": "P",
	"level": "high",
},
{
	"word": "P.E.",
	"group": "P",
	"level": "high",
},
{
	"word": "pace",
	"group": "P",
	"level": "high",
},
{
	"word": "pack",
	"group": "P",
	"level": "high",
},
{
	"word": "package",
	"group": "P",
	"level": "high",
},
{
	"word": "packet",
	"group": "P",
	"level": "high",
},
{
	"word": "paddle",
	"group": "P",
	"level": "high",
},
{
	"word": "painful",
	"group": "P",
	"level": "high",
},
{
	"word": "painter",
	"group": "P",
	"level": "high",
},
{
	"word": "painting",
	"group": "P",
	"level": "high",
},
{
	"word": "pan",
	"group": "P",
	"level": "high",
},
{
	"word": "panic",
	"group": "P",
	"level": "high",
},
{
	"word": "paperwork",
	"group": "P",
	"level": "high",
},
{
	"word": "paragraph",
	"group": "P",
	"level": "high",
},
{
	"word": "parallel",
	"group": "P",
	"level": "high",
},
{
	"word": "parcel",
	"group": "P",
	"level": "high",
},
{
	"word": "parking",
	"group": "P",
	"level": "high",
},
{
	"word": "parrot",
	"group": "P",
	"level": "high",
},
{
	"word": "participate",
	"group": "P",
	"level": "high",
},
{
	"word": "particular",
	"group": "P",
	"level": "high",
},
{
	"word": "partly",
	"group": "P",
	"level": "high",
},
{
	"word": "partner",
	"group": "P",
	"level": "high",
},
{
	"word": "part-time",
	"group": "P",
	"level": "high",
},
{
	"word": "passage",
	"group": "P",
	"level": "high",
},
{
	"word": "passer-by",
	"group": "P",
	"level": "high",
},
{
	"word": "passive",
	"group": "P",
	"level": "high",
},
{
	"word": "patent",
	"group": "P",
	"level": "high",
},
{
	"word": "path",
	"group": "P",
	"level": "high",
},
{
	"word": "patience",
	"group": "P",
	"level": "high",
},
{
	"word": "pattern",
	"group": "P",
	"level": "high",
},
{
	"word": "pause",
	"group": "P",
	"level": "high",
},
{
	"word": "pavement",
	"group": "P",
	"level": "high",
},
{
	"word": "pea",
	"group": "P",
	"level": "high",
},
{
	"word": "peaceful",
	"group": "P",
	"level": "high",
},
{
	"word": "peach",
	"group": "P",
	"level": "high",
},
{
	"word": "pedestrian",
	"group": "P",
	"level": "high",
},
{
	"word": "pence",
	"group": "P",
	"level": "high",
},
{
	"word": "penny",
	"group": "P",
	"level": "high",
},
{
	"word": "pension",
	"group": "P",
	"level": "high",
},
{
	"word": "pepper",
	"group": "P",
	"level": "high",
},
{
	"word": "per",
	"group": "P",
	"level": "high",
},
{
	"word": "percent",
	"group": "P",
	"level": "high",
},
{
	"word": "percentage",
	"group": "P",
	"level": "high",
},
{
	"word": "perform",
	"group": "P",
	"level": "high",
},
{
	"word": "performance",
	"group": "P",
	"level": "high",
},
{
	"word": "performer",
	"group": "P",
	"level": "high",
},
{
	"word": "perfume",
	"group": "P",
	"level": "high",
},
{
	"word": "permanent",
	"group": "P",
	"level": "high",
},
{
	"word": "permission",
	"group": "P",
	"level": "high",
},
{
	"word": "permit",
	"group": "P",
	"level": "high",
},
{
	"word": "personally",
	"group": "P",
	"level": "high",
},
{
	"word": "personnel",
	"group": "P",
	"level": "high",
},
{
	"word": "persuade",
	"group": "P",
	"level": "high",
},
{
	"word": "pest",
	"group": "P",
	"level": "high",
},
{
	"word": "petrol",
	"group": "P",
	"level": "high",
},
{
	"word": "phenomenon",
	"group": "P",
	"level": "high",
},
{
	"word": "photograph",
	"group": "P",
	"level": "high",
},
{
	"word": "photographer",
	"group": "P",
	"level": "high",
},
{
	"word": "phrase",
	"group": "P",
	"level": "high",
},
{
	"word": "physical",
	"group": "P",
	"level": "high",
},
{
	"word": "physician",
	"group": "P",
	"level": "high",
},
{
	"word": "physicist",
	"group": "P",
	"level": "high",
},
{
	"word": "pianist",
	"group": "P",
	"level": "high",
},
{
	"word": "piano",
	"group": "P",
	"level": "high",
},
{
	"word": "pile",
	"group": "P",
	"level": "high",
},
{
	"word": "pill",
	"group": "P",
	"level": "high",
},
{
	"word": "pillow",
	"group": "P",
	"level": "high",
},
{
	"word": "pin",
	"group": "P",
	"level": "high",
},
{
	"word": "pine",
	"group": "P",
	"level": "high",
},
{
	"word": "pineapple",
	"group": "P",
	"level": "high",
},
{
	"word": "ping-pong",
	"group": "P",
	"level": "high",
},
{
	"word": "pint",
	"group": "P",
	"level": "high",
},
{
	"word": "pipe",
	"group": "P",
	"level": "high",
},
{
	"word": "plain",
	"group": "P",
	"level": "high",
},
{
	"word": "plastic",
	"group": "P",
	"level": "high",
},
{
	"word": "plate",
	"group": "P",
	"level": "high",
},
{
	"word": "platform",
	"group": "P",
	"level": "high",
},
{
	"word": "pleasant",
	"group": "P",
	"level": "high",
},
{
	"word": "pleased",
	"group": "P",
	"level": "high",
},
{
	"word": "plot",
	"group": "P",
	"level": "high",
},
{
	"word": "plug",
	"group": "P",
	"level": "high",
},
{
	"word": "plus",
	"group": "P",
	"level": "high",
},
{
	"word": "pm",
	"group": "P",
	"level": "high",
},
{
	"word": "poet",
	"group": "P",
	"level": "high",
},
{
	"word": "poison",
	"group": "P",
	"level": "high",
},
{
	"word": "poisonous",
	"group": "P",
	"level": "high",
},
{
	"word": "pole",
	"group": "P",
	"level": "high",
},
{
	"word": "policy",
	"group": "P",
	"level": "high",
},
{
	"word": "polish",
	"group": "P",
	"level": "high",
},
{
	"word": "political",
	"group": "P",
	"level": "high",
},
{
	"word": "politician",
	"group": "P",
	"level": "high",
},
{
	"word": "politics",
	"group": "P",
	"level": "high",
},
{
	"word": "pond",
	"group": "P",
	"level": "high",
},
{
	"word": "pop",
	"group": "P",
	"level": "high",
},
{
	"word": "popcorn",
	"group": "P",
	"level": "high",
},
{
	"word": "pork",
	"group": "P",
	"level": "high",
},
{
	"word": "porridge",
	"group": "P",
	"level": "high",
},
{
	"word": "port",
	"group": "P",
	"level": "high",
},
{
	"word": "portable",
	"group": "P",
	"level": "high",
},
{
	"word": "porter",
	"group": "P",
	"level": "high",
},
{
	"word": "position",
	"group": "P",
	"level": "high",
},
{
	"word": "positive",
	"group": "P",
	"level": "high",
},
{
	"word": "possess",
	"group": "P",
	"level": "high",
},
{
	"word": "possession",
	"group": "P",
	"level": "high",
},
{
	"word": "possibility",
	"group": "P",
	"level": "high",
},
{
	"word": "postage",
	"group": "P",
	"level": "high",
},
{
	"word": "postcode",
	"group": "P",
	"level": "high",
},
{
	"word": "poster",
	"group": "P",
	"level": "high",
},
{
	"word": "postpone",
	"group": "P",
	"level": "high",
},
{
	"word": "pot",
	"group": "P",
	"level": "high",
},
{
	"word": "potential",
	"group": "P",
	"level": "high",
},
{
	"word": "pour",
	"group": "P",
	"level": "high",
},
{
	"word": "powder",
	"group": "P",
	"level": "high",
},
{
	"word": "power",
	"group": "P",
	"level": "high",
},
{
	"word": "powerful",
	"group": "P",
	"level": "high",
},
{
	"word": "practical",
	"group": "P",
	"level": "high",
},
{
	"word": "practise",
	"group": "P",
	"level": "high",
},
{
	"word": "pray",
	"group": "P",
	"level": "high",
},
{
	"word": "prayer",
	"group": "P",
	"level": "high",
},
{
	"word": "precious",
	"group": "P",
	"level": "high",
},
{
	"word": "precise",
	"group": "P",
	"level": "high",
},
{
	"word": "predict",
	"group": "P",
	"level": "high",
},
{
	"word": "prefer",
	"group": "P",
	"level": "high",
},
{
	"word": "preference",
	"group": "P",
	"level": "high",
},
{
	"word": "pregnant",
	"group": "P",
	"level": "high",
},
{
	"word": "prejudice",
	"group": "P",
	"level": "high",
},
{
	"word": "premier",
	"group": "P",
	"level": "high",
},
{
	"word": "preparation",
	"group": "P",
	"level": "high",
},
{
	"word": "prescription",
	"group": "P",
	"level": "high",
},
{
	"word": "presentation",
	"group": "P",
	"level": "high",
},
{
	"word": "preserve",
	"group": "P",
	"level": "high",
},
{
	"word": "press",
	"group": "P",
	"level": "high",
},
{
	"word": "pressure",
	"group": "P",
	"level": "high",
},
{
	"word": "pretend",
	"group": "P",
	"level": "high",
},
{
	"word": "prevent",
	"group": "P",
	"level": "high",
},
{
	"word": "preview",
	"group": "P",
	"level": "high",
},
{
	"word": "previous",
	"group": "P",
	"level": "high",
},
{
	"word": "primitive",
	"group": "P",
	"level": "high",
},
{
	"word": "principle",
	"group": "P",
	"level": "high",
},
{
	"word": "prison",
	"group": "P",
	"level": "high",
},
{
	"word": "prisoner",
	"group": "P",
	"level": "high",
},
{
	"word": "privilege",
	"group": "P",
	"level": "high",
},
{
	"word": "procedure",
	"group": "P",
	"level": "high",
},
{
	"word": "process",
	"group": "P",
	"level": "high",
},
{
	"word": "production",
	"group": "P",
	"level": "high",
},
{
	"word": "profession",
	"group": "P",
	"level": "high",
},
{
	"word": "professor",
	"group": "P",
	"level": "high",
},
{
	"word": "profit",
	"group": "P",
	"level": "high",
},
{
	"word": "prohibit",
	"group": "P",
	"level": "high",
},
{
	"word": "promote",
	"group": "P",
	"level": "high",
},
{
	"word": "properly",
	"group": "P",
	"level": "high",
},
{
	"word": "protection",
	"group": "P",
	"level": "high",
},
{
	"word": "prove",
	"group": "P",
	"level": "high",
},
{
	"word": "province",
	"group": "P",
	"level": "high",
},
{
	"word": "psychology",
	"group": "P",
	"level": "high",
},
{
	"word": "pub",
	"group": "P",
	"level": "high",
},
{
	"word": "publish",
	"group": "P",
	"level": "high",
},
{
	"word": "pulse",
	"group": "P",
	"level": "high",
},
{
	"word": "pump",
	"group": "P",
	"level": "high",
},
{
	"word": "punctual",
	"group": "P",
	"level": "high",
},
{
	"word": "punctuation",
	"group": "P",
	"level": "high",
},
{
	"word": "punishment",
	"group": "P",
	"level": "high",
},
{
	"word": "purchase",
	"group": "P",
	"level": "high",
},
{
	"word": "pure",
	"group": "P",
	"level": "high",
},
{
	"word": "purse",
	"group": "P",
	"level": "high",
},
{
	"word": "puzzle",
	"group": "P",
	"level": "high",
},
{
	"word": "pyramid",
	"group": "P",
	"level": "high",
},
{
	"word": "quake",
	"group": "Q",
	"level": "high",
},
{
	"word": "qualification",
	"group": "Q",
	"level": "high",
},
{
	"word": "quality",
	"group": "Q",
	"level": "high",
},
{
	"word": "quantity",
	"group": "Q",
	"level": "high",
},
{
	"word": "quarrel",
	"group": "Q",
	"level": "high",
},
{
	"word": "questionnaire",
	"group": "Q",
	"level": "high",
},
{
	"word": "queue",
	"group": "Q",
	"level": "high",
},
{
	"word": "quilt",
	"group": "Q",
	"level": "high",
},
{
	"word": "quit",
	"group": "Q",
	"level": "high",
},
{
	"word": "quiz",
	"group": "Q",
	"level": "high",
},
{
	"word": "racial",
	"group": "R",
	"level": "high",
},
{
	"word": "radiation",
	"group": "R",
	"level": "high",
},
{
	"word": "radioactive",
	"group": "R",
	"level": "high",
},
{
	"word": "radium",
	"group": "R",
	"level": "high",
},
{
	"word": "rag",
	"group": "R",
	"level": "high",
},
{
	"word": "rail",
	"group": "R",
	"level": "high",
},
{
	"word": "rainbow",
	"group": "R",
	"level": "high",
},
{
	"word": "raincoat",
	"group": "R",
	"level": "high",
},
{
	"word": "rainfall",
	"group": "R",
	"level": "high",
},
{
	"word": "random",
	"group": "R",
	"level": "high",
},
{
	"word": "range",
	"group": "R",
	"level": "high",
},
{
	"word": "rank",
	"group": "R",
	"level": "high",
},
{
	"word": "rare",
	"group": "R",
	"level": "high",
},
{
	"word": "rat",
	"group": "R",
	"level": "high",
},
{
	"word": "rate",
	"group": "R",
	"level": "high",
},
{
	"word": "rather",
	"group": "R",
	"level": "high",
},
{
	"word": "raw",
	"group": "R",
	"level": "high",
},
{
	"word": "ray",
	"group": "R",
	"level": "high",
},
{
	"word": "razor",
	"group": "R",
	"level": "high",
},
{
	"word": "react",
	"group": "R",
	"level": "high",
},
{
	"word": "reading",
	"group": "R",
	"level": "high",
},
{
	"word": "reality",
	"group": "R",
	"level": "high",
},
{
	"word": "reasonable",
	"group": "R",
	"level": "high",
},
{
	"word": "rebuild",
	"group": "R",
	"level": "high",
},
{
	"word": "receipt",
	"group": "R",
	"level": "high",
},
{
	"word": "receiver",
	"group": "R",
	"level": "high",
},
{
	"word": "recent",
	"group": "R",
	"level": "high",
},
{
	"word": "reception",
	"group": "R",
	"level": "high",
},
{
	"word": "receptionist",
	"group": "R",
	"level": "high",
},
{
	"word": "recipe",
	"group": "R",
	"level": "high",
},
{
	"word": "recite",
	"group": "R",
	"level": "high",
},
{
	"word": "recognize",
	"group": "R",
	"level": "high",
},
{
	"word": "recommend",
	"group": "R",
	"level": "high",
},
{
	"word": "recorder",
	"group": "R",
	"level": "high",
},
{
	"word": "recover",
	"group": "R",
	"level": "high",
},
{
	"word": "recreation",
	"group": "R",
	"level": "high",
},
{
	"word": "rectangle",
	"group": "R",
	"level": "high",
},
{
	"word": "recycle",
	"group": "R",
	"level": "high",
},
{
	"word": "reduce",
	"group": "R",
	"level": "high",
},
{
	"word": "refer",
	"group": "R",
	"level": "high",
},
{
	"word": "referee",
	"group": "R",
	"level": "high",
},
{
	"word": "reference",
	"group": "R",
	"level": "high",
},
{
	"word": "reflect",
	"group": "R",
	"level": "high",
},
{
	"word": "reform",
	"group": "R",
	"level": "high",
},
{
	"word": "refresh",
	"group": "R",
	"level": "high",
},
{
	"word": "refrigerator",
	"group": "R",
	"level": "high",
},
{
	"word": "regard",
	"group": "R",
	"level": "high",
},
{
	"word": "regardless",
	"group": "R",
	"level": "high",
},
{
	"word": "register",
	"group": "R",
	"level": "high",
},
{
	"word": "regular",
	"group": "R",
	"level": "high",
},
{
	"word": "regulation",
	"group": "R",
	"level": "high",
},
{
	"word": "reject",
	"group": "R",
	"level": "high",
},
{
	"word": "relate",
	"group": "R",
	"level": "high",
},
{
	"word": "relation",
	"group": "R",
	"level": "high",
},
{
	"word": "relay",
	"group": "R",
	"level": "high",
},
{
	"word": "relevant",
	"group": "R",
	"level": "high",
},
{
	"word": "reliable",
	"group": "R",
	"level": "high",
},
{
	"word": "relief",
	"group": "R",
	"level": "high",
},
{
	"word": "religion",
	"group": "R",
	"level": "high",
},
{
	"word": "religious",
	"group": "R",
	"level": "high",
},
{
	"word": "rely",
	"group": "R",
	"level": "high",
},
{
	"word": "remark",
	"group": "R",
	"level": "high",
},
{
	"word": "remind",
	"group": "R",
	"level": "high",
},
{
	"word": "remote",
	"group": "R",
	"level": "high",
},
{
	"word": "remove",
	"group": "R",
	"level": "high",
},
{
	"word": "rent",
	"group": "R",
	"level": "high",
},
{
	"word": "replace",
	"group": "R",
	"level": "high",
},
{
	"word": "reporter",
	"group": "R",
	"level": "high",
},
{
	"word": "represent",
	"group": "R",
	"level": "high",
},
{
	"word": "representative",
	"group": "R",
	"level": "high",
},
{
	"word": "republic",
	"group": "R",
	"level": "high",
},
{
	"word": "reputation",
	"group": "R",
	"level": "high",
},
{
	"word": "request",
	"group": "R",
	"level": "high",
},
{
	"word": "requirement",
	"group": "R",
	"level": "high",
},
{
	"word": "rescue",
	"group": "R",
	"level": "high",
},
{
	"word": "resemble",
	"group": "R",
	"level": "high",
},
{
	"word": "reservation",
	"group": "R",
	"level": "high",
},
{
	"word": "reserve",
	"group": "R",
	"level": "high",
},
{
	"word": "reset",
	"group": "R",
	"level": "high",
},
{
	"word": "resign",
	"group": "R",
	"level": "high",
},
{
	"word": "resist",
	"group": "R",
	"level": "high",
},
{
	"word": "respect",
	"group": "R",
	"level": "high",
},
{
	"word": "respond",
	"group": "R",
	"level": "high",
},
{
	"word": "responsibility",
	"group": "R",
	"level": "high",
},
{
	"word": "restriction",
	"group": "R",
	"level": "high",
},
{
	"word": "retell",
	"group": "R",
	"level": "high",
},
{
	"word": "retire",
	"group": "R",
	"level": "high",
},
{
	"word": "revision",
	"group": "R",
	"level": "high",
},
{
	"word": "revolution",
	"group": "R",
	"level": "high",
},
{
	"word": "reward",
	"group": "R",
	"level": "high",
},
{
	"word": "rewind",
	"group": "R",
	"level": "high",
},
{
	"word": "rhyme",
	"group": "R",
	"level": "high",
},
{
	"word": "rid",
	"group": "R",
	"level": "high",
},
{
	"word": "riddle",
	"group": "R",
	"level": "high",
},
{
	"word": "ridiculous",
	"group": "R",
	"level": "high",
},
{
	"word": "rigid",
	"group": "R",
	"level": "high",
},
{
	"word": "ripe",
	"group": "R",
	"level": "high",
},
{
	"word": "ripen",
	"group": "R",
	"level": "high",
},
{
	"word": "roast",
	"group": "R",
	"level": "high",
},
{
	"word": "rob",
	"group": "R",
	"level": "high",
},
{
	"word": "rocket",
	"group": "R",
	"level": "high",
},
{
	"word": "roll",
	"group": "R",
	"level": "high",
},
{
	"word": "roof",
	"group": "R",
	"level": "high",
},
{
	"word": "rooster",
	"group": "R",
	"level": "high",
},
{
	"word": "root",
	"group": "R",
	"level": "high",
},
{
	"word": "rot",
	"group": "R",
	"level": "high",
},
{
	"word": "rough",
	"group": "R",
	"level": "high",
},
{
	"word": "roundabout",
	"group": "R",
	"level": "high",
},
{
	"word": "routine",
	"group": "R",
	"level": "high",
},
{
	"word": "royal",
	"group": "R",
	"level": "high",
},
{
	"word": "rubber",
	"group": "R",
	"level": "high",
},
{
	"word": "rude",
	"group": "R",
	"level": "high",
},
{
	"word": "rugby",
	"group": "R",
	"level": "high",
},
{
	"word": "ruin",
	"group": "R",
	"level": "high",
},
{
	"word": "sacred",
	"group": "S",
	"level": "high",
},
{
	"word": "sacrifice",
	"group": "S",
	"level": "high",
},
{
	"word": "sadness",
	"group": "S",
	"level": "high",
},
{
	"word": "sail",
	"group": "S",
	"level": "high",
},
{
	"word": "sailor",
	"group": "S",
	"level": "high",
},
{
	"word": "salary",
	"group": "S",
	"level": "high",
},
{
	"word": "salesgirl",
	"group": "S",
	"level": "high",
},
{
	"word": "salesman",
	"group": "S",
	"level": "high",
},
{
	"word": "salty",
	"group": "S",
	"level": "high",
},
{
	"word": "salute",
	"group": "S",
	"level": "high",
},
{
	"word": "satellite",
	"group": "S",
	"level": "high",
},
{
	"word": "satisfaction",
	"group": "S",
	"level": "high",
},
{
	"word": "saucer",
	"group": "S",
	"level": "high",
},
{
	"word": "sausage",
	"group": "S",
	"level": "high",
},
{
	"word": "saying",
	"group": "S",
	"level": "high",
},
{
	"word": "scan",
	"group": "S",
	"level": "high",
},
{
	"word": "scar",
	"group": "S",
	"level": "high",
},
{
	"word": "scare",
	"group": "S",
	"level": "high",
},
{
	"word": "scene",
	"group": "S",
	"level": "high",
},
{
	"word": "scenery",
	"group": "S",
	"level": "high",
},
{
	"word": "sceptical",
	"group": "S",
	"level": "high",
},
{
	"word": "schedule",
	"group": "S",
	"level": "high",
},
{
	"word": "scholar",
	"group": "S",
	"level": "high",
},
{
	"word": "scholarship",
	"group": "S",
	"level": "high",
},
{
	"word": "schoolboy",
	"group": "S",
	"level": "high",
},
{
	"word": "schoolgirl",
	"group": "S",
	"level": "high",
},
{
	"word": "schoolmate",
	"group": "S",
	"level": "high",
},
{
	"word": "scientific",
	"group": "S",
	"level": "high",
},
{
	"word": "scold",
	"group": "S",
	"level": "high",
},
{
	"word": "scratch",
	"group": "S",
	"level": "high",
},
{
	"word": "scream",
	"group": "S",
	"level": "high",
},
{
	"word": "sculpture",
	"group": "S",
	"level": "high",
},
{
	"word": "seagull",
	"group": "S",
	"level": "high",
},
{
	"word": "seal",
	"group": "S",
	"level": "high",
},
{
	"word": "seashell",
	"group": "S",
	"level": "high",
},
{
	"word": "seaside",
	"group": "S",
	"level": "high",
},
{
	"word": "seaweed",
	"group": "S",
	"level": "high",
},
{
	"word": "section",
	"group": "S",
	"level": "high",
},
{
	"word": "secure",
	"group": "S",
	"level": "high",
},
{
	"word": "security",
	"group": "S",
	"level": "high",
},
{
	"word": "seed",
	"group": "S",
	"level": "high",
},
{
	"word": "seek",
	"group": "S",
	"level": "high",
},
{
	"word": "seize",
	"group": "S",
	"level": "high",
},
{
	"word": "select",
	"group": "S",
	"level": "high",
},
{
	"word": "self",
	"group": "S",
	"level": "high",
},
{
	"word": "selfish",
	"group": "S",
	"level": "high",
},
{
	"word": "semicircle",
	"group": "S",
	"level": "high",
},
{
	"word": "seminar",
	"group": "S",
	"level": "high",
},
{
	"word": "senior",
	"group": "S",
	"level": "high",
},
{
	"word": "sensitive",
	"group": "S",
	"level": "high",
},
{
	"word": "separation",
	"group": "S",
	"level": "high",
},
{
	"word": "servant",
	"group": "S",
	"level": "high",
},
{
	"word": "session",
	"group": "S",
	"level": "high",
},
{
	"word": "settle",
	"group": "S",
	"level": "high",
},
{
	"word": "settlement",
	"group": "S",
	"level": "high",
},
{
	"word": "settler",
	"group": "S",
	"level": "high",
},
{
	"word": "severe",
	"group": "S",
	"level": "high",
},
{
	"word": "sew",
	"group": "S",
	"level": "high",
},
{
	"word": "sex",
	"group": "S",
	"level": "high",
},
{
	"word": "shabby",
	"group": "S",
	"level": "high",
},
{
	"word": "shade",
	"group": "S",
	"level": "high",
},
{
	"word": "shadow",
	"group": "S",
	"level": "high",
},
{
	"word": "shallow",
	"group": "S",
	"level": "high",
},
{
	"word": "shark",
	"group": "S",
	"level": "high",
},
{
	"word": "sharp",
	"group": "S",
	"level": "high",
},
{
	"word": "sharpen",
	"group": "S",
	"level": "high",
},
{
	"word": "sharpener",
	"group": "S",
	"level": "high",
},
{
	"word": "shave",
	"group": "S",
	"level": "high",
},
{
	"word": "shaver",
	"group": "S",
	"level": "high",
},
{
	"word": "shelf",
	"group": "S",
	"level": "high",
},
{
	"word": "shelter",
	"group": "S",
	"level": "high",
},
{
	"word": "shock",
	"group": "S",
	"level": "high",
},
{
	"word": "shoot",
	"group": "S",
	"level": "high",
},
{
	"word": "shopkeeper",
	"group": "S",
	"level": "high",
},
{
	"word": "shoppping",
	"group": "S",
	"level": "high",
},
{
	"word": "shore",
	"group": "S",
	"level": "high",
},
{
	"word": "shortcoming",
	"group": "S",
	"level": "high",
},
{
	"word": "shortly",
	"group": "S",
	"level": "high",
},
{
	"word": "shot",
	"group": "S",
	"level": "high",
},
{
	"word": "shrink",
	"group": "S",
	"level": "high",
},
{
	"word": "shuttle",
	"group": "S",
	"level": "high",
},
{
	"word": "sickness",
	"group": "S",
	"level": "high",
},
{
	"word": "sideroad",
	"group": "S",
	"level": "high",
},
{
	"word": "sidewalk",
	"group": "S",
	"level": "high",
},
{
	"word": "sideway",
	"group": "S",
	"level": "high",
},
{
	"word": "sideways",
	"group": "S",
	"level": "high",
},
{
	"word": "sigh",
	"group": "S",
	"level": "high",
},
{
	"word": "sight",
	"group": "S",
	"level": "high",
},
{
	"word": "sightseeing",
	"group": "S",
	"level": "high",
},
{
	"word": "signal",
	"group": "S",
	"level": "high",
},
{
	"word": "signature",
	"group": "S",
	"level": "high",
},
{
	"word": "significance",
	"group": "S",
	"level": "high",
},
{
	"word": "simplify",
	"group": "S",
	"level": "high",
},
{
	"word": "sincerely",
	"group": "S",
	"level": "high",
},
{
	"word": "sink",
	"group": "S",
	"level": "high",
},
{
	"word": "skateboard",
	"group": "S",
	"level": "high",
},
{
	"word": "skeptical",
	"group": "S",
	"level": "high",
},
{
	"word": "ski",
	"group": "S",
	"level": "high",
},
{
	"word": "skillful",
	"group": "S",
	"level": "high",
},
{
	"word": "skin",
	"group": "S",
	"level": "high",
},
{
	"word": "skip",
	"group": "S",
	"level": "high",
},
{
	"word": "skyscraper",
	"group": "S",
	"level": "high",
},
{
	"word": "slat",
	"group": "S",
	"level": "high",
},
{
	"word": "slave",
	"group": "S",
	"level": "high",
},
{
	"word": "slavery",
	"group": "S",
	"level": "high",
},
{
	"word": "sleeve",
	"group": "S",
	"level": "high",
},
{
	"word": "slice",
	"group": "S",
	"level": "high",
},
{
	"word": "slide",
	"group": "S",
	"level": "high",
},
{
	"word": "slight",
	"group": "S",
	"level": "high",
},
{
	"word": "slim",
	"group": "S",
	"level": "high",
},
{
	"word": "slip",
	"group": "S",
	"level": "high",
},
{
	"word": "smog",
	"group": "S",
	"level": "high",
},
{
	"word": "smoker",
	"group": "S",
	"level": "high",
},
{
	"word": "sneaker",
	"group": "S",
	"level": "high",
},
{
	"word": "sneeze",
	"group": "S",
	"level": "high",
},
{
	"word": "sniff",
	"group": "S",
	"level": "high",
},
{
	"word": "soap",
	"group": "S",
	"level": "high",
},
{
	"word": "sob",
	"group": "S",
	"level": "high",
},
{
	"word": "soccer",
	"group": "S",
	"level": "high",
},
{
	"word": "socialism",
	"group": "S",
	"level": "high",
},
{
	"word": "socialist",
	"group": "S",
	"level": "high",
},
{
	"word": "socket",
	"group": "S",
	"level": "high",
},
{
	"word": "software",
	"group": "S",
	"level": "high",
},
{
	"word": "soil",
	"group": "S",
	"level": "high",
},
{
	"word": "solar",
	"group": "S",
	"level": "high",
},
{
	"word": "soldier",
	"group": "S",
	"level": "high",
},
{
	"word": "solid",
	"group": "S",
	"level": "high",
},
{
	"word": "somehow",
	"group": "S",
	"level": "high",
},
{
	"word": "sorrow",
	"group": "S",
	"level": "high",
},
{
	"word": "sort",
	"group": "S",
	"level": "high",
},
{
	"word": "soul",
	"group": "S",
	"level": "high",
},
{
	"word": "sour",
	"group": "S",
	"level": "high",
},
{
	"word": "southeast",
	"group": "S",
	"level": "high",
},
{
	"word": "southwest",
	"group": "S",
	"level": "high",
},
{
	"word": "souvenir",
	"group": "S",
	"level": "high",
},
{
	"word": "sow",
	"group": "S",
	"level": "high",
},
{
	"word": "spaceship",
	"group": "S",
	"level": "high",
},
{
	"word": "spade",
	"group": "S",
	"level": "high",
},
{
	"word": "sparrow",
	"group": "S",
	"level": "high",
},
{
	"word": "spear",
	"group": "S",
	"level": "high",
},
{
	"word": "specialist",
	"group": "S",
	"level": "high",
},
{
	"word": "specific",
	"group": "S",
	"level": "high",
},
{
	"word": "spelling",
	"group": "S",
	"level": "high",
},
{
	"word": "spin",
	"group": "S",
	"level": "high",
},
{
	"word": "spiritual",
	"group": "S",
	"level": "high",
},
{
	"word": "spit",
	"group": "S",
	"level": "high",
},
{
	"word": "splendid",
	"group": "S",
	"level": "high",
},
{
	"word": "split",
	"group": "S",
	"level": "high",
},
{
	"word": "spoken",
	"group": "S",
	"level": "high",
},
{
	"word": "spokesman",
	"group": "S",
	"level": "high",
},
{
	"word": "sponsor",
	"group": "S",
	"level": "high",
},
{
	"word": "spoonful",
	"group": "S",
	"level": "high",
},
{
	"word": "spot",
	"group": "S",
	"level": "high",
},
{
	"word": "spray",
	"group": "S",
	"level": "high",
},
{
	"word": "spy",
	"group": "S",
	"level": "high",
},
{
	"word": "squeeze",
	"group": "S",
	"level": "high",
},
{
	"word": "squirrel",
	"group": "S",
	"level": "high",
},
{
	"word": "stable",
	"group": "S",
	"level": "high",
},
{
	"word": "stadium",
	"group": "S",
	"level": "high",
},
{
	"word": "staff",
	"group": "S",
	"level": "high",
},
{
	"word": "stage",
	"group": "S",
	"level": "high",
},
{
	"word": "stain",
	"group": "S",
	"level": "high",
},
{
	"word": "stainless",
	"group": "S",
	"level": "high",
},
{
	"word": "stair",
	"group": "S",
	"level": "high",
},
{
	"word": "stare",
	"group": "S",
	"level": "high",
},
{
	"word": "starvation",
	"group": "S",
	"level": "high",
},
{
	"word": "starve",
	"group": "S",
	"level": "high",
},
{
	"word": "statement",
	"group": "S",
	"level": "high",
},
{
	"word": "statesman",
	"group": "S",
	"level": "high",
},
{
	"word": "statistics",
	"group": "S",
	"level": "high",
},
{
	"word": "statue",
	"group": "S",
	"level": "high",
},
{
	"word": "status",
	"group": "S",
	"level": "high",
},
{
	"word": "steady",
	"group": "S",
	"level": "high",
},
{
	"word": "steak",
	"group": "S",
	"level": "high",
},
{
	"word": "steam",
	"group": "S",
	"level": "high",
},
{
	"word": "steel",
	"group": "S",
	"level": "high",
},
{
	"word": "steep",
	"group": "S",
	"level": "high",
},
{
	"word": "steward",
	"group": "S",
	"level": "high",
},
{
	"word": "stewardess",
	"group": "S",
	"level": "high",
},
{
	"word": "sting",
	"group": "S",
	"level": "high",
},
{
	"word": "stocking",
	"group": "S",
	"level": "high",
},
{
	"word": "storage",
	"group": "S",
	"level": "high",
},
{
	"word": "stout",
	"group": "S",
	"level": "high",
},
{
	"word": "stove",
	"group": "S",
	"level": "high",
},
{
	"word": "straightforward",
	"group": "S",
	"level": "high",
},
{
	"word": "strait",
	"group": "S",
	"level": "high",
},
{
	"word": "straw",
	"group": "S",
	"level": "high",
},
{
	"word": "stream",
	"group": "S",
	"level": "high",
},
{
	"word": "strength",
	"group": "S",
	"level": "high",
},
{
	"word": "strengthen",
	"group": "S",
	"level": "high",
},
{
	"word": "stress",
	"group": "S",
	"level": "high",
},
{
	"word": "strike",
	"group": "S",
	"level": "high",
},
{
	"word": "struggle",
	"group": "S",
	"level": "high",
},
{
	"word": "stubborn",
	"group": "S",
	"level": "high",
},
{
	"word": "studio",
	"group": "S",
	"level": "high",
},
{
	"word": "style",
	"group": "S",
	"level": "high",
},
{
	"word": "subjective",
	"group": "S",
	"level": "high",
},
{
	"word": "submit",
	"group": "S",
	"level": "high",
},
{
	"word": "subscribe",
	"group": "S",
	"level": "high",
},
{
	"word": "substitute",
	"group": "S",
	"level": "high",
},
{
	"word": "suck",
	"group": "S",
	"level": "high",
},
{
	"word": "suffer",
	"group": "S",
	"level": "high",
},
{
	"word": "suffering",
	"group": "S",
	"level": "high",
},
{
	"word": "suit",
	"group": "S",
	"level": "high",
},
{
	"word": "suitable",
	"group": "S",
	"level": "high",
},
{
	"word": "suitcase",
	"group": "S",
	"level": "high",
},
{
	"word": "suite",
	"group": "S",
	"level": "high",
},
{
	"word": "summary",
	"group": "S",
	"level": "high",
},
{
	"word": "sunburnt",
	"group": "S",
	"level": "high",
},
{
	"word": "sunlight",
	"group": "S",
	"level": "high",
},
{
	"word": "sunshine",
	"group": "S",
	"level": "high",
},
{
	"word": "super",
	"group": "S",
	"level": "high",
},
{
	"word": "superb",
	"group": "S",
	"level": "high",
},
{
	"word": "superior",
	"group": "S",
	"level": "high",
},
{
	"word": "supper",
	"group": "S",
	"level": "high",
},
{
	"word": "supply",
	"group": "S",
	"level": "high",
},
{
	"word": "supreme",
	"group": "S",
	"level": "high",
},
{
	"word": "surgeon",
	"group": "S",
	"level": "high",
},
{
	"word": "surplus",
	"group": "S",
	"level": "high",
},
{
	"word": "surround",
	"group": "S",
	"level": "high",
},
{
	"word": "surrounding",
	"group": "S",
	"level": "high",
},
{
	"word": "survival",
	"group": "S",
	"level": "high",
},
{
	"word": "survive",
	"group": "S",
	"level": "high",
},
{
	"word": "suspect",
	"group": "S",
	"level": "high",
},
{
	"word": "suspension",
	"group": "S",
	"level": "high",
},
{
	"word": "swallow",
	"group": "S",
	"level": "high",
},
{
	"word": "swap",
	"group": "S",
	"level": "high",
},
{
	"word": "swear",
	"group": "S",
	"level": "high",
},
{
	"word": "sweat",
	"group": "S",
	"level": "high",
},
{
	"word": "sweep",
	"group": "S",
	"level": "high",
},
{
	"word": "swell",
	"group": "S",
	"level": "high",
},
{
	"word": "swift",
	"group": "S",
	"level": "high",
},
{
	"word": "swing",
	"group": "S",
	"level": "high",
},
{
	"word": "switch",
	"group": "S",
	"level": "high",
},
{
	"word": "sword",
	"group": "S",
	"level": "high",
},
{
	"word": "symbol",
	"group": "S",
	"level": "high",
},
{
	"word": "sympathy",
	"group": "S",
	"level": "high",
},
{
	"word": "symphony",
	"group": "S",
	"level": "high",
},
{
	"word": "symptom",
	"group": "S",
	"level": "high",
},
{
	"word": "system",
	"group": "S",
	"level": "high",
},
{
	"word": "systematic",
	"group": "S",
	"level": "high",
},
{
	"word": "tablet",
	"group": "T",
	"level": "high",
},
{
	"word": "table-tennis",
	"group": "T",
	"level": "high",
},
{
	"word": "tailor",
	"group": "T",
	"level": "high",
},
{
	"word": "tale",
	"group": "T",
	"level": "high",
},
{
	"word": "talent",
	"group": "T",
	"level": "high",
},
{
	"word": "tam",
	"group": "T",
	"level": "high",
},
{
	"word": "tank",
	"group": "T",
	"level": "high",
},
{
	"word": "tap",
	"group": "T",
	"level": "high",
},
{
	"word": "target",
	"group": "T",
	"level": "high",
},
{
	"word": "tasteless",
	"group": "T",
	"level": "high",
},
{
	"word": "tasty",
	"group": "T",
	"level": "high",
},
{
	"word": "tax",
	"group": "T",
	"level": "high",
},
{
	"word": "taxpayer",
	"group": "T",
	"level": "high",
},
{
	"word": "teamwork",
	"group": "T",
	"level": "high",
},
{
	"word": "teapot",
	"group": "T",
	"level": "high",
},
{
	"word": "tear",
	"group": "T",
	"level": "high",
},
{
	"word": "tease",
	"group": "T",
	"level": "high",
},
{
	"word": "technical",
	"group": "T",
	"level": "high",
},
{
	"word": "technique",
	"group": "T",
	"level": "high",
},
{
	"word": "teenager",
	"group": "T",
	"level": "high",
},
{
	"word": "telescope",
	"group": "T",
	"level": "high",
},
{
	"word": "temple",
	"group": "T",
	"level": "high",
},
{
	"word": "temporary",
	"group": "T",
	"level": "high",
},
{
	"word": "tend",
	"group": "T",
	"level": "high",
},
{
	"word": "tendency",
	"group": "T",
	"level": "high",
},
{
	"word": "tense",
	"group": "T",
	"level": "high",
},
{
	"word": "tension",
	"group": "T",
	"level": "high",
},
{
	"word": "tent",
	"group": "T",
	"level": "high",
},
{
	"word": "tentative",
	"group": "T",
	"level": "high",
},
{
	"word": "terminal",
	"group": "T",
	"level": "high",
},
{
	"word": "terrify",
	"group": "T",
	"level": "high",
},
{
	"word": "terror",
	"group": "T",
	"level": "high",
},
{
	"word": "textbook",
	"group": "T",
	"level": "high",
},
{
	"word": "thankful",
	"group": "T",
	"level": "high",
},
{
	"word": "theft",
	"group": "T",
	"level": "high",
},
{
	"word": "theirs",
	"group": "T",
	"level": "high",
},
{
	"word": "theme",
	"group": "T",
	"level": "high",
},
{
	"word": "theoretical",
	"group": "T",
	"level": "high",
},
{
	"word": "theory",
	"group": "T",
	"level": "high",
},
{
	"word": "therefore",
	"group": "T",
	"level": "high",
},
{
	"word": "thermos",
	"group": "T",
	"level": "high",
},
{
	"word": "thief",
	"group": "T",
	"level": "high",
},
{
	"word": "thinking",
	"group": "T",
	"level": "high",
},
{
	"word": "thirst",
	"group": "T",
	"level": "high",
},
{
	"word": "thorough",
	"group": "T",
	"level": "high",
},
{
	"word": "thread",
	"group": "T",
	"level": "high",
},
{
	"word": "thrill",
	"group": "T",
	"level": "high",
},
{
	"word": "thriller",
	"group": "T",
	"level": "high",
},
{
	"word": "throat",
	"group": "T",
	"level": "high",
},
{
	"word": "throughout",
	"group": "T",
	"level": "high",
},
{
	"word": "throw",
	"group": "T",
	"level": "high",
},
{
	"word": "thunder",
	"group": "T",
	"level": "high",
},
{
	"word": "thunderstorm",
	"group": "T",
	"level": "high",
},
{
	"word": "thus",
	"group": "T",
	"level": "high",
},
{
	"word": "tick",
	"group": "T",
	"level": "high",
},
{
	"word": "tight",
	"group": "T",
	"level": "high",
},
{
	"word": "till",
	"group": "T",
	"level": "high",
},
{
	"word": "timetable",
	"group": "T",
	"level": "high",
},
{
	"word": "tin",
	"group": "T",
	"level": "high",
},
{
	"word": "tip",
	"group": "T",
	"level": "high",
},
{
	"word": "tire",
	"group": "T",
	"level": "high",
},
{
	"word": "tiresome",
	"group": "T",
	"level": "high",
},
{
	"word": "tissue",
	"group": "T",
	"level": "high",
},
{
	"word": "title",
	"group": "T",
	"level": "high",
},
{
	"word": "toast",
	"group": "T",
	"level": "high",
},
{
	"word": "tobacco",
	"group": "T",
	"level": "high",
},
{
	"word": "tolerate",
	"group": "T",
	"level": "high",
},
{
	"word": "tomb",
	"group": "T",
	"level": "high",
},
{
	"word": "tongue",
	"group": "T",
	"level": "high",
},
{
	"word": "toothbrush",
	"group": "T",
	"level": "high",
},
{
	"word": "toothpaste",
	"group": "T",
	"level": "high",
},
{
	"word": "topic",
	"group": "T",
	"level": "high",
},
{
	"word": "tortoise",
	"group": "T",
	"level": "high",
},
{
	"word": "tough",
	"group": "T",
	"level": "high",
},
{
	"word": "tourism",
	"group": "T",
	"level": "high",
},
{
	"word": "tournament",
	"group": "T",
	"level": "high",
},
{
	"word": "towel",
	"group": "T",
	"level": "high",
},
{
	"word": "track",
	"group": "T",
	"level": "high",
},
{
	"word": "tractor",
	"group": "T",
	"level": "high",
},
{
	"word": "tradition",
	"group": "T",
	"level": "high",
},
{
	"word": "transform",
	"group": "T",
	"level": "high",
},
{
	"word": "translation",
	"group": "T",
	"level": "high",
},
{
	"word": "translator",
	"group": "T",
	"level": "high",
},
{
	"word": "transparent",
	"group": "T",
	"level": "high",
},
{
	"word": "transport",
	"group": "T",
	"level": "high",
},
{
	"word": "trap",
	"group": "T",
	"level": "high",
},
{
	"word": "traveler",
	"group": "T",
	"level": "high",
},
{
	"word": "treatment",
	"group": "T",
	"level": "high",
},
{
	"word": "tremble",
	"group": "T",
	"level": "high",
},
{
	"word": "trend",
	"group": "T",
	"level": "high",
},
{
	"word": "trial",
	"group": "T",
	"level": "high",
},
{
	"word": "triangle",
	"group": "T",
	"level": "high",
},
{
	"word": "trick",
	"group": "T",
	"level": "high",
},
{
	"word": "trolleybus",
	"group": "T",
	"level": "high",
},
{
	"word": "troop",
	"group": "T",
	"level": "high",
},
{
	"word": "troublesome",
	"group": "T",
	"level": "high",
},
{
	"word": "truly",
	"group": "T",
	"level": "high",
},
{
	"word": "trunk",
	"group": "T",
	"level": "high",
},
{
	"word": "tube",
	"group": "T",
	"level": "high",
},
{
	"word": "tune",
	"group": "T",
	"level": "high",
},
{
	"word": "turkey",
	"group": "T",
	"level": "high",
},
{
	"word": "turning",
	"group": "T",
	"level": "high",
},
{
	"word": "tutor",
	"group": "T",
	"level": "high",
},
{
	"word": "TV",
	"group": "T",
	"level": "high",
},
{
	"word": "twin",
	"group": "T",
	"level": "high",
},
{
	"word": "twist",
	"group": "T",
	"level": "high",
},
{
	"word": "type",
	"group": "T",
	"level": "high",
},
{
	"word": "typewriter",
	"group": "T",
	"level": "high",
},
{
	"word": "typhoon",
	"group": "T",
	"level": "high",
},
{
	"word": "typical",
	"group": "T",
	"level": "high",
},
{
	"word": "typist",
	"group": "T",
	"level": "high",
},
{
	"word": "tyre",
	"group": "T",
	"level": "high",
},
{
	"word": "unable",
	"group": "U",
	"level": "high",
},
{
	"word": "unbearable",
	"group": "U",
	"level": "high",
},
{
	"word": "unbelievable",
	"group": "U",
	"level": "high",
},
{
	"word": "uncertain",
	"group": "U",
	"level": "high",
},
{
	"word": "uncomfortable",
	"group": "U",
	"level": "high",
},
{
	"word": "unconditional",
	"group": "U",
	"level": "high",
},
{
	"word": "unconscious",
	"group": "U",
	"level": "high",
},
{
	"word": "underline",
	"group": "U",
	"level": "high",
},
{
	"word": "undertake",
	"group": "U",
	"level": "high",
},
{
	"word": "underwear",
	"group": "U",
	"level": "high",
},
{
	"word": "unemployment",
	"group": "U",
	"level": "high",
},
{
	"word": "unfair",
	"group": "U",
	"level": "high",
},
{
	"word": "unfit",
	"group": "U",
	"level": "high",
},
{
	"word": "unfortunate",
	"group": "U",
	"level": "high",
},
{
	"word": "uniform",
	"group": "U",
	"level": "high",
},
{
	"word": "union",
	"group": "U",
	"level": "high",
},
{
	"word": "unique",
	"group": "U",
	"level": "high",
},
{
	"word": "unite",
	"group": "U",
	"level": "high",
},
{
	"word": "universal",
	"group": "U",
	"level": "high",
},
{
	"word": "universe",
	"group": "U",
	"level": "high",
},
{
	"word": "unlike",
	"group": "U",
	"level": "high",
},
{
	"word": "unrest",
	"group": "U",
	"level": "high",
},
{
	"word": "unusual",
	"group": "U",
	"level": "high",
},
{
	"word": "unwilling",
	"group": "U",
	"level": "high",
},
{
	"word": "update",
	"group": "U",
	"level": "high",
},
{
	"word": "upper",
	"group": "U",
	"level": "high",
},
{
	"word": "upset",
	"group": "U",
	"level": "high",
},
{
	"word": "upstairs",
	"group": "U",
	"level": "high",
},
{
	"word": "upwards",
	"group": "U",
	"level": "high",
},
{
	"word": "urban",
	"group": "U",
	"level": "high",
},
{
	"word": "urge",
	"group": "U",
	"level": "high",
},
{
	"word": "urgent",
	"group": "U",
	"level": "high",
},
{
	"word": "useless",
	"group": "U",
	"level": "high",
},
{
	"word": "user",
	"group": "U",
	"level": "high",
},
{
	"word": "vacant",
	"group": "V",
	"level": "high",
},
{
	"word": "vague",
	"group": "V",
	"level": "high",
},
{
	"word": "vain",
	"group": "V",
	"level": "high",
},
{
	"word": "valid",
	"group": "V",
	"level": "high",
},
{
	"word": "valley",
	"group": "V",
	"level": "high",
},
{
	"word": "variety",
	"group": "V",
	"level": "high",
},
{
	"word": "various",
	"group": "V",
	"level": "high",
},
{
	"word": "vase",
	"group": "V",
	"level": "high",
},
{
	"word": "vast",
	"group": "V",
	"level": "high",
},
{
	"word": "VCD",
	"group": "V",
	"level": "high",
},
{
	"word": "vehicle",
	"group": "V",
	"level": "high",
},
{
	"word": "version",
	"group": "V",
	"level": "high",
},
{
	"word": "vertical",
	"group": "V",
	"level": "high",
},
{
	"word": "vest",
	"group": "V",
	"level": "high",
},
{
	"word": "via",
	"group": "V",
	"level": "high",
},
{
	"word": "vice",
	"group": "V",
	"level": "high",
},
{
	"word": "victim",
	"group": "V",
	"level": "high",
},
{
	"word": "videophone",
	"group": "V",
	"level": "high",
},
{
	"word": "view",
	"group": "V",
	"level": "high",
},
{
	"word": "villager",
	"group": "V",
	"level": "high",
},
{
	"word": "vinegar",
	"group": "V",
	"level": "high",
},
{
	"word": "violate",
	"group": "V",
	"level": "high",
},
{
	"word": "violence",
	"group": "V",
	"level": "high",
},
{
	"word": "violent",
	"group": "V",
	"level": "high",
},
{
	"word": "violinist",
	"group": "V",
	"level": "high",
},
{
	"word": "virtue",
	"group": "V",
	"level": "high",
},
{
	"word": "virus",
	"group": "V",
	"level": "high",
},
{
	"word": "visa",
	"group": "V",
	"level": "high",
},
{
	"word": "visual",
	"group": "V",
	"level": "high",
},
{
	"word": "vital",
	"group": "V",
	"level": "high",
},
{
	"word": "vivid",
	"group": "V",
	"level": "high",
},
{
	"word": "vocabulary",
	"group": "V",
	"level": "high",
},
{
	"word": "volcano",
	"group": "V",
	"level": "high",
},
{
	"word": "volleyballl",
	"group": "V",
	"level": "high",
},
{
	"word": "voluntary",
	"group": "V",
	"level": "high",
},
{
	"word": "volunteer",
	"group": "V",
	"level": "high",
},
{
	"word": "vote",
	"group": "V",
	"level": "high",
},
{
	"word": "voyage",
	"group": "V",
	"level": "high",
},
{
	"word": "wag",
	"group": "W",
	"level": "high",
},
{
	"word": "wage",
	"group": "W",
	"level": "high",
},
{
	"word": "waist",
	"group": "W",
	"level": "high",
},
{
	"word": "waiter",
	"group": "W",
	"level": "high",
},
{
	"word": "waiting-room",
	"group": "W",
	"level": "high",
},
{
	"word": "waitress",
	"group": "W",
	"level": "high",
},
{
	"word": "walnut",
	"group": "W",
	"level": "high",
},
{
	"word": "wander",
	"group": "W",
	"level": "high",
},
{
	"word": "ward",
	"group": "W",
	"level": "high",
},
{
	"word": "warehouse",
	"group": "W",
	"level": "high",
},
{
	"word": "warmth",
	"group": "W",
	"level": "high",
},
{
	"word": "washroom",
	"group": "W",
	"level": "high",
},
{
	"word": "wave",
	"group": "W",
	"level": "high",
},
{
	"word": "wax",
	"group": "W",
	"level": "high",
},
{
	"word": "weakness",
	"group": "W",
	"level": "high",
},
{
	"word": "wealthy",
	"group": "W",
	"level": "high",
},
{
	"word": "web",
	"group": "W",
	"level": "high",
},
{
	"word": "wedding",
	"group": "W",
	"level": "high",
},
{
	"word": "weed",
	"group": "W",
	"level": "high",
},
{
	"word": "weekly",
	"group": "W",
	"level": "high",
},
{
	"word": "weep",
	"group": "W",
	"level": "high",
},
{
	"word": "welfare",
	"group": "W",
	"level": "high",
},
{
	"word": "westwards",
	"group": "W",
	"level": "high",
},
{
	"word": "whale",
	"group": "W",
	"level": "high",
},
{
	"word": "wheat",
	"group": "W",
	"level": "high",
},
{
	"word": "wherever",
	"group": "W",
	"level": "high",
},
{
	"word": "wrestle",
	"group": "W",
	"level": "high",
},
{
	"word": "wrinkle",
	"group": "W",
	"level": "high",
},
{
	"word": "wrist",
	"group": "W",
	"level": "high",
},
{
	"word": "yawn",
	"group": "Y",
	"level": "high",
},
{
	"word": "yell",
	"group": "Y",
	"level": "high",
},
{
	"word": "yoghurt",
	"group": "Y",
	"level": "high",
},
{
	"word": "youth",
	"group": "Y",
	"level": "high",
},
{
	"word": "yummy",
	"group": "Y",
	"level": "high",
},
{
	"word": "zebra",
	"group": "Z",
	"level": "high",
},
{
	"word": "zip",
	"group": "Z",
	"level": "high",
},
{
	"word": "zipper",
	"group": "Z",
	"level": "high",
},
{
	"word": "zone",
	"group": "Z",
	"level": "high",
},
{
	"word": "zoom",
	"group": "Z",
	"level": "high",
}]

word.insert_many(words_data)

