import random

feet_in_male = 5280
meters_in_kilometer = 1000
beatles = ["John Lennon", "Paul McCartney", "George Harrison", "Ringo Star"]

def get_file_ext(filename):
    return filename[filename.index(".") + 1:] # 得到文件的拓展名

def roll_dice(num):
    return random.randint(1, num) # 随机数,里面填写的是范围