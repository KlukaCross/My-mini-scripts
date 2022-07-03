import vk_api
import utils


def parsing_part(data: utils.Data, offset):
    posts = vk_api.tools.VkTools(data.vk).get_all_iter("wall.get", 100,
                                                    {"owner_id": -data.config["GROUP_ID"], "offset": offset, "count": 100})
    posts_one_photo = []
    for post in posts:
        utils.parsing_one(data, post, posts_one_photo)
    if "posts_one_photo" not in data.posts_info:
        data.posts_info["posts_one_photo"] = []
    data.posts_info["posts_one_photo"] += posts_one_photo


def main():
    data = utils.Data()
    count_posts = data.vk.wall.get(owner_id=-data.config["GROUP_ID"])["count"]
    for i in range(count_posts // 2500 + 1):
        parsing_part(data, i*2500)


if __name__ == '__main__':
    main()

