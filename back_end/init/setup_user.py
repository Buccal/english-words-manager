import sys
sys.path.append("../app")

import pymongo
from config import *

client = pymongo.MongoClient(MONGO_URL)
db = client[MONGO_DB]
user = db[USER_DB]

users_data = [
{
    "username": "admin",
    "hashed_password": "$2b$12$DUCt/w8WEXsdS4rgmks9IukhZk9fapBXiQvQS0wA7uT4TCfHIW89W",
    "email": None,
    "words": ["a", "about", "afraid", "after", "afternoon", "again", "all", "also", "always", "and", "angry", "animal", "answer", "any", "apple", "arm", "art", "ask", "at", "aunt", "autumn", "baby", "back", "bad", "bag", "ball", "banana", "basketball", "be", "bear", "beautiful", "bed", "before", "begin", "behind", "beside", "between", "big", "bike", "bird", "birthday", "black", "blackboard", "blue", "boat", "body", "book", "box", "boy", "bread", "breakfast", "bring", "brother", "brown", "bus", "busy", "but", "buy", "by", "cake", "call", "can", "candy", "cap", "car", "card", "cat", "chair", "chicken", "child", "children", "China", "Chinese", "cinema", "city", "class", "clean", "clever", "clock", "close", "clothes", "cloudy", "coat", "cold", "colour", "come", "computer", "cook", "cool", "cousin", "cow", "crayon", "cry", "dad", "dance", "day", "dear", "desk", "difficult", "dinner", "dirty", "do", "doctor", "dog", "door", "down", "draw", "dress", "drink", "driver", "duck", "ear", "early", "easy", "eat", "egg", "elephant", "email", "English", "evening", "every", "exercise", "eye", "face", "family", "fan", "far", "farm", "farmer", "fast", "father", "favourite", "feel", "film", "find", "fine", "fish", "floor", "flower", "fly", "food", "foot", "football", "for", "friend", "from", "fruit", "game", "get", "girl", "give", "go", "good", "goodbye", "grandfather", "grandmother", "grass", "great", "green", "hair", "half", "hand", "happy", "have", "he", "head", "healthy", "hear", "heavy", "hello", "help", "her", "here", "hi", "high", "him", "his", "holiday", "home", "horse", "hospital", "hot", "hour", "house", "how", "hungry", "I", "ice-cream", "idea", "ill", "in", "interesting", "it", "its", "juice", "jump", "kid", "kind", "kitchen", "kite", "know", "lake", "late", "left", "leg", "lesson", "let", "library", "light", "like", "listen", "llittle", "live", "long", "look", "love", "lunch", "make", "man", "many", "map", "maths", "me", "meet", "milk", "minute", "Miss", "monkey", "month", "moon", "morning", "mother", "mouth", "Mr", "Mrs", "Ms", "much", "mum", "music", "my", "name", "near", "new", "next", "nice", "night", "no", "noodle", "nose", "not", "now", "nurse", "of", "often", "old", "on", "open", "or", "orange", "our", "panda", "parent", "park", "party", "PE", "pen", "pencil", "people", "photo", "picture", "pig", "place", "plane", "plant", "play", "playground", "please", "police", "potato", "pupil", "put", "rain", "read", "red", "rice", "right", "river", "room", "ruler", "run", "sad", "say", "school", "schoolbag", "science", "season", "see", "she", "sheep", "ship", "shirt", "shoe", "shop", "short", "shorts", "sing", "sister", "sit", "skirt", "sleep", "slow", "small", "snow", "sock", "some", "sometimes", "song", "sorry", "soup", "speak", "sport", "spring", "stand", "star", "stop", "story", "street", "strong", "study", "subject", "summer", "sun", "sunny", "supermarket", "sweater", "swim", "table", "take", "talk", "tall", "taxi", "tea", "teacher", "tell", "thank", "that", "the", "their", "them", "then", "there", "these", "they", "thin", "think", "this", "those", "tiger", "time", "tired", "to", "today", "toilet", "tomato", "tomorrow", "too", "toy", "train", "travel", "tree", "trousers", "try", "turn", "TV", "umbrella", "uncle", "under", "up", "us", "use", "vegetable", "very", "visit", "wait", "walk", "want", "warm", "wash", "watch", "water", "way", "we", "wear", "weather", "week", "welcome", "well", "what", "when", "where", "white", "who", "whose", "why", "window", "windy", "winter", "with", "woman", "wonderful", "word", "work", "worker", "worry", "write", "wrong", "year", "yellow", "yes", "yesterday", "you", "young", "your", "zoo"],
    "status": 1,
}
]

user.insert_many(users_data)