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


def getJpeg(path: str, size_h: int, size_w: int) -> type(np.array(1)):
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


def draw_boxes(outputs):
    image = cv2.imread('images/people1.jpeg', cv2.IMREAD_COLOR)
    image = cv2.resize(image, (544, 320))
    for image_id, label, conf, x_min, y_min, x_max, y_max in outputs:
        x_min = int(x_min * 544)
        y_min = int(y_min * 320)
        x_max = int(x_max * 544)
        y_max = int(y_max * 320)
        if int(label) == 1:
            image = cv2.rectangle(cv2.UMat(image), (x_min, y_min), (x_max, y_max), (0, 0, 255), 1)
    output_path = os.path.join(args['output_dir'], 'people1_release.jpg')
    print("saving result to", output_path)
    result_flag = cv2.imwrite(output_path, image)
    print("write success = ", result_flag)

my_image = getJpeg('images/age-gender-recognition-retail-0001.jpg', 62, 62)
my_image2 = getJpeg('images/people1.jpeg', 320, 544)

print(make_post_request("http://localhost:8001/v1/models/age-gender:predict", my_image))
outputs = make_post_request("http://localhost:8001/v1/models/person-detection:predict", my_image2)['outputs'][0][0]

draw_boxes(outputs)
