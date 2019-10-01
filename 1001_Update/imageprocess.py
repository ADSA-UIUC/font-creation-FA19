import cv2

vecror_i=[]
def main():
    imgpath = "/Users/Henry/Desktop/view.jpg" #put your image path here
    img1 = cv2.imread(imgpath, 0)
    vecror_i.append(img1)



#     print(img1)
#     print(img1.dtype)
#     print(img1.shape)
#     print(img1.ndim)
#     print(img1.size)
#
#
#     cv2.imshow('a',img1)
#     cv2.waitKey(0)
#     cv2.destroyWindow('a')
#
if __name__ == "__main__":
    main()

print(vecror_i)