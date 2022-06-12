import sys, os

"""
Renames all pictures of the format .jpg, .png in a folder in the format: 000, 001, 002, etc.
:param path: path to the directory with pictures (by default - the current directory)
"""


def main(pth="."):
    ress = [".png", ".jpg", ".jpeg"]
    files = list(filter(lambda x: os.path.splitext(x)[-1] in ress, os.listdir(pth)))
    for i in range(len(files)):
        fl = files[i]
        os.rename(pth + "\\" + fl, pth + "\\" + "{:03d}".format(i) + os.path.splitext(fl)[-1])
    print("The program has worked successfully!")


if __name__ == "__main__":
    pth = sys.argv[1] if len(sys.argv) == 2 else "."
    try:
        main(pth)
    except Exception as e:
        print(e)