import argparse
import os

import cv2
import numpy as np
import json
import requests


def load_image(file_path):
    img = cv2.imread(file_path)  # BGR color format, shape HWC
    print(img.shape)
    img = cv2.resize(img, (args['width'], args['height']))
    img = img.transpose(2,0,1).reshape(1,3,args['height'],args['width'])
    # change shape to NCHW
    return img


parser = argparse.ArgumentParser(description='Age/gender recognition requests via REST API.'
                                             'analyses input images and saveswith with detected objects.'
                                             'it relies on model given as parameter...')

parser.add_argument('--model_name', required=False, help='Name of the model to be used', default="age-gender-recognition")
parser.add_argument('--input_images_dir', required=False, help='Directory with input images', default="images")
parser.add_argument('--output_dir', required=False, help='Directory for staring images with detection results', default="results")
parser.add_argument('--batch_size', required=False, help='How many images should be grouped in one batch', default=1, type=int)
parser.add_argument('--width', required=False, help='How the input image width should be resized in pixels', default=62, type=int)
parser.add_argument('--height', required=False, help='How the input image width should be resized in pixels', default=62, type=int)
parser.add_argument('--rest_address',required=False, default='localhost',  help='Specify url to grpc service. default:localhost')
parser.add_argument('--rest_port',required=False, default=8001, help='Specify port to grpc service. default: 9003')

args = vars(parser.parse_args())
files = os.listdir(args['input_images_dir'])
batch_size = args['batch_size']
model_name = args['model_name']
print("Running "+model_name+" on files:" + str(files))

# imgs = np.zeros((0,3,args['height'],args['width']), np.dtype('<f'))
for i in files:
    img = load_image(os.path.join(args['input_images_dir'], i))
    data_obj = {'inputs':  img.tolist()}
    data_json = json.dumps(data_obj)
    result = requests.post("http://localhost:8001/v1/models/age_gender:predict", data=data_json)
    result_dict = json.loads(result.text)
    print(result_dict)
    # result_flag = cv2.imwrite(r'./some_'+str(i), img[0].transpose(1,2,0))
    # print(result_flag)
# def getJpeg(path, size):
#
#     img = cv2.imread(path, cv2.IMREAD_COLOR)
#     # retrieved array has BGR format and 0-255 normalization
#     img = cv2.resize(img, (size, size))
#     img = img.transpose(2,0,1).reshape(1,3,size,size)
#     print(path, img.shape, "; data range:",np.amin(img),":",np.amax(img))
#     return img
#
# my_image = getJpeg('images/age-gender-recognition-retail-0001.jpg', 62)
#
#
# data_obj = {'inputs':  my_image.tolist()}
# data_json = json.dumps(data_obj)
#
# result = requests.post("http://localhost:9003/v1/models/age_gender:predict", data=data_json)
# result_dict = json.loads(result.text)
# print(result_dict)
#
