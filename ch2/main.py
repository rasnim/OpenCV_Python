import cv2

if __name__ == '__main__':
    img = cv2.imread('lenna.bmp', cv2.IMREAD_UNCHANGED)

    cv2.namedWindow('image')
    cv2.imshow('image', img)

    cv2.waitKey()

    cv2.destroyAllWindows()