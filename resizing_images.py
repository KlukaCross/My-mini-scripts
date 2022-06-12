import sys, os
from PIL import Image
"""
Changes the size of all pictures of the format .jpg, .png in a folder and saves the new image to the /new_images folder
:param width: width of new pictures
:param height: height of new pictures
:param path: path to the directory with pictures (by default - the current directory)
"""


def main(size, pth="."):
    ress = [".png", ".jpg", ".jpeg"]
    files = list(filter(lambda x: os.path.splitext(x)[-1] in ress, os.listdir(pth)))
    new_dir = pth + "/new_images"
    os.mkdir(new_dir)
    for i in range(len(files)):
        fl = files[i]
        image = Image.open(pth + "/" + fl)
        image = image.resize(size)
        image.save(f"{new_dir}/{fl}")
    print("The program has worked successfully!")


if __name__ == "__main__":
    if len(sys.argv) not in [3, 4]:
        print("Wrong number of arguments")
    else:
        width = sys.argv[1]
        height = sys.argv[2]
        pth = sys.argv[3] if len(sys.argv) == 4 else "."
        try:
            main((int(width), int(height)), pth)
        except Exception as e:
            print(e)