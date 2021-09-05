import cv2
import numpy as np
import json
import requests


def getJpeg(path, size):

    img = cv2.imread(path, cv2.IMREAD_COLOR)
    # retrieved array has BGR format and 0-255 normalization
    img = cv2.resize(img, (size, size))
    img = img.transpose(2,0,1).reshape(1,3,size,size)
    print(path, img.shape, "; data range:",np.amin(img),":",np.amax(img))
    return img

my_image = getJpeg('age-gender-recognition-retail-0001.jpg',62)


data_obj = {'inputs':  my_image.tolist()}
data_json = json.dumps(data_obj)

result = requests.post("http://localhost:9001/v1/models/age_gender:predict", data=data_json)
result_dict = json.loads(result.text)
print(result_dict)