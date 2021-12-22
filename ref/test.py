# import pymongo
# from config import *
# import json

# client = pymongo.MongoClient(MONGO_URL)
# db = client[MONGO_DB]
# template_words = db["TEMPLATE_WORDS"]
# user = db["USER"]

# # a = user.find_one()
# # b = user.find()
# # c = user.find({"username": "alice"})

# # def to_list_or_dict(cursor):
# #     new_list = list(cursor)
# #     count = len(new_list)
# #     if(count == 1):
# #         return new_list[0]
# #     else:
# #         return {
# #             "count": count,
# #             "data": new_list
# #         }

# # a1 = to_list_or_dict(a)
# # b1 = to_list_or_dict(b)
# # c1 = to_list_or_dict(c)

# # # print(type(a1))
# # # print(a1)
# # print(type(b1))
# # print(b1)
# # # print(type(c1))
# # # print(c1)

# users_info = [
#     {
#         "username": "alice",
#         "email": "alice@example.com",
#         "hashed_password": "$2b$12$7GVHbbcNTEnxJcnSSShH1O0MsNwwSajCjWnzIJ3TzsMI8E8DRvFPe",
#         "disabled": False,
#     },
#     {
#         "username": "johndoe",
#         "email": "johndoe@example.com",
#         "hashed_password": "$2b$12$UO7uKI/DfBxYy4lKocTSJO75A6D4eVDyDxOCLGnJ2mOpdBH4SoDfG",
#         "disabled": True,
#     }
# ]

# user.insert_many(users_info)

# # from decrypt_data import decrypt_data

# # encode_password = "mO34nsfRHnyKj4tj4Mah4F5AzXRjFHhg/DtacwiJJRdmxyLsECkEKX57e0jaSKZPdFNtgpaW9q0ruODaIKVy8HnUFa2Gk1JwXjR1i1bS0w+CV9Iq2zkgkJkEp5yf/0oM95mkF4MQs/NKaQyEEoedeULghqgw0G+RSuJkK8x8Rm4="
# # print(decrypt_data(encode_password))

a = 1
print("a = %s"%a)