import os
import random

import argparse
import cv2
import numpy as np
import json
import requests

parser = argparse.ArgumentParser(description='')

parser.add_argument('--input_images_dir', required=False, help='Directory with input images', default="images/people")
parser.add_argument('--output_dir', required=False, help='Directory for staring images with detection results', default="results")
args = vars(parser.parse_args())


def getJpeg(path: str, size_h: int, size_w: int) -> np.ndarray:
    img = cv2.imread(path, cv2.IMREAD_COLOR)
    # retrieved array has BGR format and 0-255 normalization
    img = cv2.resize(img, (size_h, size_w))
    img = img.transpose(2,0,1).reshape(1,3,size_h, size_w)
    print(path, img.shape, "; data range:",np.amin(img),":",np.amax(img))
    return img


def make_post_request(url: str, image) -> None:
    data_obj = {'inputs': image.tolist()}
    data_json = json.dumps(data_obj)

    result = requests.post(url, data=data_json)
    result_dict = json.loads(result.text)
    return result_dict


def draw_boxes(outputs, img_w=608, img_h=608):
    image = cv2.imread('images/people1.jpeg', cv2.IMREAD_COLOR)
    image = cv2.resize(image, (img_w, img_h))
    labels = outputs['labels']
    cnt_people = 0
    for label, [x_min, y_min, x_max, y_max, conf] in zip(labels, outputs['boxes']):
        x_min = int(x_min)
        y_min = int(y_min)
        x_max = int(x_max)
        y_max = int(y_max)
        if label == 0 and conf > 0.9:
            image = cv2.rectangle(cv2.UMat(image), (x_min, y_min), (x_max, y_max), \
                                  (random.randint(0, 255), random.randint(0, 255), random.randint(0, 255)), 1)
            cnt_people += 1
    print(cnt_people)
    output_path = os.path.join('results', 'people1_release.jpg')
    print("saving result to", output_path)
    result_flag = cv2.imwrite(output_path, image)
    print("write success = ", result_flag)

my_image = getJpeg('images/age-gender-recognition-retail-0001.jpg', 62, 62)
my_image2 = getJpeg('images/people1.jpeg', 608, 608)

outputs = make_post_request("http://localhost:8001/v1/models/segmentation:predict", my_image2)
with open("results/segm_out.txt", 'w') as f1:
    f1.write(str(outputs))
print(outputs['outputs']['boxes'])
print(make_post_request("http://localhost:8001/v1/models/age-gender:predict", my_image))

#outputs = make_post_request("http://localhost:8001/v1/models/person-detection:predict", my_image2)['outputs'][0][0]

draw_boxes(outputs['outputs'])
