import sys

import cv2

if __name__ == '__main__':
    img = cv2.imread('source/lenna.bmp')

    if img is None:
        print('Image load failed')
        sys.exit()

    cv2.namedWindow('img')
    cv2.imshow('img', img)

    while True:
        keycode = cv2.waitKey()
        if keycode == ord('i') or keycode == ord('I'):
            img = ~img
            cv2.imshow('img', img)
        elif keycode == 27 or keycode == ord('q') or keycode == ord('Q'):
            break

    cv2.destroyAllWindows()