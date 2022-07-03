import vk_api
import json
import os
import requests


def download_photo(path, photo):
    max_photo = photo["sizes"][0]
    for size in photo["sizes"]:
        if size["width"] > max_photo["width"]:
            max_photo = size

    ph = requests.get(max_photo["url"])
    with open(f"{path}/photo_{photo['id']}.jpg", "wb") as f:
        f.write(ph.content)


def parsing_part(vk, offset, config, posts_info):
    posts = vk_api.tools.VkTools(vk).get_all_iter("wall.get", 100,
                                                    {"owner_id": -config["GROUP_ID"], "offset": offset, "count": 100})
    posts_one_photo = []
    for post in posts:
        dir_path = f"{config['DOWNLOAD_PATH']}/post_{post['id']}"
        try:
            os.mkdir(dir_path)
        except OSError:
            print(f"Warning: post {post['id']} already exists")
            continue
        with open(f"{dir_path}/info.json", "w") as f_info:
            json.dump(post, f_info)
        if "attachments" not in post:
            continue
        if len(post["attachments"]) == 1 and post["attachments"][0]["type"] == "photo":
            download_photo(dir_path, post["attachments"][0]["photo"])
            posts_one_photo.append(post["id"])
            continue
        for media in post["attachments"]:
            if media["type"] == "photo":
                download_photo(dir_path, media["photo"])
    if "posts_one_photo" not in posts_info:
        posts_info["posts_one_photo"] = []
    posts_info["posts_one_photo"] += posts_one_photo


def main():
    f_config = open("config.json", "r")
    config = json.load(f_config)

    if not os.path.exists(config['DOWNLOAD_PATH']):
        os.mkdir(config['DOWNLOAD_PATH'])

    posts_info = {}
    if os.path.exists(f"{config['DOWNLOAD_PATH']}/posts_info.json"):
        with open(f"{config['DOWNLOAD_PATH']}/posts_info.json", "r") as f:
            posts_info = json.load(f)
    f_posts_info = open(f"{config['DOWNLOAD_PATH']}/posts_info.json", "w")
    vk_session = vk_api.VkApi(login=config["LOGIN"], password=config["PASSWORD"])
    vk_session.auth()
    vk = vk_session.get_api()

    count_posts = vk.wall.get(owner_id=-config["GROUP_ID"])["count"]
    for i in range(count_posts // 2500 + 1):
        parsing_part(vk, i*2500, config, posts_info)
    json.dump(posts_info, f_posts_info)
    f_config.close()
    f_posts_info.close()


if __name__ == '__main__':
    main()

