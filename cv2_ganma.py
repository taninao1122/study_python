import cv2
import os
import numpy as np

dir = "./images/data"
 
# ガンマ値を決める。
def change_gamma(image_name,image_list):
    gamma = 0.5
    print(image_list)
    for i in range(0,4):
        # 処理対象の画像をロード
        imgS = cv2.imread(image_list)
        # ガンマ値を使って Look up tableを作成
        lookUpTable = np.empty((1,256), np.uint8)
        for i in range(256):
            lookUpTable[0,i] = np.clip(pow(i / 255.0, gamma) * 255.0, 0, 255)
        
        # Look up tableを使って画像の輝度値を変更
        imgA = cv2.LUT(imgS, lookUpTable)
        
        # 表示実行
        #cv2.namedWindow('image', cv2.WINDOW_AUTOSIZE)
        if gamma == 1:
            print('if')
            cv2.imwrite('./images/result/'+image_name+'/image_ori.jpg', imgA)
        else: 
            print('else')
            cv2.imwrite('./images/result/'+image_name+'/image_gamma'+ str(gamma) + '.jpg', imgA)
        #cv2.imshow('image', imgA)
        print(gamma)
        print('saved')
        gamma += 0.5
        #cv2.waitKey()
if __name__ == '__main__':
    data_dir = sorted(os.listdir(dir))
    image_name_dir = []
    print('data_dir',data_dir)
    for data_label in data_dir:
        image_name_label = dir + '/' + data_label
        image_name_dir = (sorted(os.listdir(image_name_label)))
        for image_label in image_name_dir:
            print('image_label',image_label)
            image_label_dir = dir + '/' + data_label + '/' +image_label
            change_gamma(data_label,image_label_dir)