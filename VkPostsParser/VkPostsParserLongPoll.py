import utils
from vk_api import bot_longpoll


def main():
    data = utils.Data()
    lp = bot_longpoll.VkBotLongPoll(data.vk_session, data.config["GROUP_ID"])
    for event in lp.listen():
        if event.type == bot_longpoll.VkBotEventType.WALL_POST_NEW:
            posts_one_photo = []
            utils.parsing_one(data, event.object, posts_one_photo)
            if "posts_one_photo" not in data.posts_info:
                data.posts_info["posts_one_photo"] = []
            data.posts_info["posts_one_photo"] += posts_one_photo
            data.dump_posts_info()


if __name__ == '__main__':
    main()
