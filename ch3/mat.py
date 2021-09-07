import cv2 as cv
import numpy as np


def matop_1():
    img1 = cv.imread('source/cat.bmp', cv.IMREAD_GRAYSCALE)

    if img1 is None:
        print('Image load failed')
        return
    print('type(img1):', type(img1))
    print('img1.shape:', img1.shape)

    if len(img1.shape) == 2:
        print('img1 is a grayscale image')
    elif len(img1.shape) == 3:
        print('img1 is a truecolor image')

    cv.imshow('img1', img1)
    cv.waitKey()
    cv.destroyAllWindows()


def matop_2():
    img1 = np.empty((480, 640), np.uint8)  # grayscale
    img2 = np.zeros((480, 640, 3), np.uint8)  # color
    img3 = np.ones((480, 640), np.int32)  # 1's matrix
    img4 = np.full((480, 640), 0, np.float32)  # fill with 0.0

    mat1 = np.array([[11, 12, 13, 14],
                     [21, 22, 23, 24],
                     [31, 32, 33, 34]]).astype(np.uint8)

    mat1[0, 1] = 100
    mat1[2, :] = 200

    print(img1)
    print(img2)
    print(img3)
    print(img4)
    print(mat1)


def matop_3():
    img1 = cv.imread('source/cat.bmp')

    img2 = img1
    img3 = img1.copy()

    img1[:, :] = (0, 255, 255)

    cv.imshow('img1', img1)
    cv.imshow('img2', img2)
    cv.imshow('img3', img3)
    cv.waitKey()
    cv.destroyAllWindows()


def matop_4():
    img1 = cv.imread('source/lenna.bmp', cv.IMREAD_GRAYSCALE)

    img2 = img1[200:400, 200:400]
    img3 = img1[200:400, 200:400].copy()

    img2 += 20

    cv.imshow('img1', img1)
    cv.imshow('img2', img2)
    cv.imshow('img3', img3)
    cv.waitKey()
    cv.destroyAllWindows()


def matop_5():
    mat1 = np.array(np.arange(12)).reshape(3, 4)

    print('mat1:')
    print(mat1)

    h, w = mat1.shape[:2]

    mat2 = np.zeros(mat1.shape, type(mat1))

    for j in range(h):
        for i in range(w):
            mat2[j, i] = mat1[j, i] + 10

    print('mat2:')
    print(mat2)


def matop_6():
    mat1 = np.ones((3, 4), np.int32)
    mat2 = np.arange(12).reshape(3, 4)
    mat3 = mat1 + mat2
    mat4 = mat2 * 2

    print('mat1:', mat1, sep='\n')
    print('mat2:', mat2, sep='\n')
    print('mat3:', mat3, sep='\n')
    print('mat4:', mat4, sep='\n')


if __name__ == '__main__':
    matop_1()
    matop_2()
    matop_3()
    matop_4()
    matop_5()
    matop_6()
