import requests
import vk_api
import json
import os


def download_photo(path, photo):
    max_photo = photo["sizes"][0]
    for size in photo["sizes"]:
        if size["width"] > max_photo["width"]:
            max_photo = size

    ph = requests.get(max_photo["url"])
    with open(f"{path}/photo_{photo['id']}.jpg", "wb") as f:
        f.write(ph.content)


def parsing_one(data, post, posts_one_photo):
    dir_path = f"{data.config['DOWNLOAD_PATH']}/post_{post['id']}"
    try:
        os.mkdir(dir_path)
    except OSError:
        print(f"Warning: post {post['id']} already exists")
        return
    with open(f"{dir_path}/info.json", "w") as f_info:
        json.dump(post, f_info)
    if "attachments" not in post:
        return
    if len(post["attachments"]) == 1 and post["attachments"][0]["type"] == "photo":
        download_photo(dir_path, post["attachments"][0]["photo"])
        posts_one_photo.append(post["id"])
        return
    for media in post["attachments"]:
        if media["type"] == "photo":
            download_photo(dir_path, media["photo"])


class Data:
    def __init__(self):
        f_config = open("config.json", "r")
        self.config = json.load(f_config)

        if not os.path.exists(self.config['DOWNLOAD_PATH']):
            os.mkdir(self.config['DOWNLOAD_PATH'])

        self.posts_info = {}
        if os.path.exists(f"{self.config['DOWNLOAD_PATH']}/posts_info.json"):
            with open(f"{self.config['DOWNLOAD_PATH']}/posts_info.json", "r") as f:
                self.posts_info = json.load(f)
        self.vk_session = vk_api.VkApi(login=self.config["LOGIN"], password=self.config["PASSWORD"])
        self.vk_session.auth()
        self.vk = self.vk_session.get_api()

        f_config.close()

    def dump_posts_info(self):
        with open(f"{self.config['DOWNLOAD_PATH']}/posts_info.json", "w") as f:
            json.dump(self.posts_info, f)
