import copy

import numpy as np
import cv2


def point():
    pt1_x = 5
    pt1_y = 10

    pt1 = np.array([pt1_x, pt1_y])
    pt2 = np.array([10, 30])

    pt3 = pt1 + pt2
    pt4 = pt1 * 2

    d1 = pt1.dot(pt2)
    b1 = (pt1 == pt2)

    print('pt1: ', pt1)
    print('pt2: ', pt2)
    print('pt3: ', pt3)
    print('pt4: ', pt4)
    print('d1: ', d1)
    print('b1: ', b1)


def size():
    sz1 = []
    sz2 = [10, 20]

    sz1.append(5)
    sz1.append(10)

    sz3 = [sz1[i] + sz2[i] for i in range(2)]
    sz4 = [sz1[i] * 2 for i in range(2)]

    area1 = np.prod(sz4)

    print('sz1: ', sz1)
    print('sz2: ', sz2)
    print('sz3: ', sz3)
    print('sz4: ', sz4)
    print('area1: ', area1)


def rect():
    rc1 = [0, 0]
    rc2 = [10, 10, 60, 40]

    rc3 = copy.deepcopy(rc1)
    rc3.extend([50, 40])

    rc4 = [rc2[i] + 10 if i < 2 else rc2[i] for i in range(4)]

    # def intersection_rect(area1, area2):
    #     for i in range(2):
    #         if area[i]

    ## ing...

    print('rc1: ', rc1)
    print('rc2: ', rc2)
    print('rc3: ', rc3)
    print('rc4: ', rc4)


# def rotatedrect():


if __name__ == '__main__':
    # print(point())
    # size()
    rect()
