import numpy as np
from os import listdir
from os.path import join, isdir
import matplotlib.pyplot as plt

def generate_photo_matrix(photo_set_path, height, width, people_amount, per_person_amount):
    photo_area = height * width

    dirs = [f for f in listdir(photo_set_path)
            if isdir(join(photo_set_path, f))]

    people_amount = len(dirs)
    people_area = people_amount * per_person_amount

    photo_matrix = np.zeros([people_area, photo_area])

    people_dict = {}
    people_groups = np.zeros(people_area)
    person_num = 1
    img_num = 0
    for person in dirs:
        people_dict[person_num] = person
        for photo in listdir(photo_set_path + '/' + person):
            photo_path = photo_set_path + '/' + person + '/' + photo
            photo_matrix[img_num, :] = generate_photo_vector(photo_path, height, width)
            people_groups[img_num] = person_num

            img_num += 1
            if img_num % per_person_amount == 0:
                break
        person_num += 1

    return photo_matrix, people_groups, people_dict


def generate_photo_vector(photo_path, height, width):
    photo_area = height * width
    photo = plt.imread(photo_path)
    return np.reshape(photo, [1, photo_area])