import vk_api

"""
Displays the top users by posts in the group
"""

LOGIN = input("Input your login\n")
PASSWORD = input("Input your password\n")
OWNER_ID = input("Input group id (negative)\n")

vk_session = vk_api.VkApi(LOGIN, PASSWORD)
vk_session.auth()

vk = vk_session.get_api()

count_posts = vk.wall.get(owner_id=OWNER_ID)["count"]
dict_id = {}
dict_names = {}
for i in range(count_posts//100+1):
    request = vk.wall.get(owner_id=OWNER_ID, offset=i*100, count=100, extended=1)
    next_posts = request["items"]
    next_profs = request["profiles"]
    for post in next_posts:
        try:
            signer_id = post["signer_id"]
        except Exception:
            signer_id = post["from_id"]
        if signer_id in dict_id:
            dict_id[signer_id] += 1
        else:
            dict_id[signer_id] = 1
    for prof in next_profs:
        if prof["id"] not in dict_names:
            dict_names[prof["id"]] = prof["first_name"] + " " + prof["last_name"]
    print(f"read {i*100+len(next_posts)} entries")

sort_id = sorted(dict_id.keys(), key=lambda x: dict_id[x], reverse=True)
print(f"number of posts - {count_posts}")
print(f"number of authors - {len(sort_id)}")
for i in range(len(sort_id)):
    id_ = sort_id[i]
    if id_ < 0:
        print(f"{i+1}) Without author - {dict_id[id_]} posts")
        continue
    print(f"{i+1}) {dict_names[id_]} - {dict_id[id_]} posts")
