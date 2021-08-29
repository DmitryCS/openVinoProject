# openVinoProject

### Age and gender recognition is presented in the [age-gender-recognition](https://github.com/DmitryCS/openVinoProject/tree/master/age-gender-recognition) folder.
### Face and landmarks recognition is presented in the [face-landmarks-detection](https://github.com/DmitryCS/openVinoProject/tree/master/face-landmarks-detection) folder.
### Text to voice translation is presented in the [text-to-speech](https://github.com/DmitryCS/openVinoProject/tree/master/text-to-speech) folder.
#### Tutorial for face_detection here: <br>
Download the Docker* image that contains the OpenVINO Model Server. This image is available from DockerHub:`docker pull openvino/model_server:latest`
<br>Doesn't work: "`curl --create-dirs https://storage.openvinotoolkit.org/repositories/open_model_zoo/2021.4/models_bin/1/age-gender-recognition-retail-0013/FP32/age-gender-recognition-retail-0013.xml https://storage.openvinotoolkit.org/repositories/open_model_zoo/2021.4/models_bin/1/age-gender-recognition-retail-0013/FP32/age-gender-recognition-retail-0013.bin -o model/1/age-gender-recognition-retail-0013.xml -o model/1/age-gender-recognition-retail-0013.bin`"
<br>Download the model components to the model/1 directory. Example command using curl:`curl --create-dirs https://download.01.org/opencv/2021/openvinotoolkit/2021.1/open_model_zoo/models_bin/1/face-detection-retail-0004/FP32/face-detection-retail-0004.xml https://download.01.org/opencv/2021/openvinotoolkit/2021.1/open_model_zoo/models_bin/1/face-detection-retail-0004/FP32/face-detection-retail-0004.bin -o model/1/face-detection-retail-0004.xml -o model/1/face-detection-retail-0004.bin`

<br>Start the Model Server container:`docker run -d -u $(id -u):$(id -g) -v $(pwd)/model:/models/age-gender-recognition -p 9000:9000 openvino/model_server:latest \
--model_path /models/age-gender-recognition --model_name age-gender-recognition --port 9000 --plugin_config '{"CPU_THROUGHPUT_STREAMS":"1"}' --shape auto`
<br>Use this command to download all necessary components:`curl https://raw.githubusercontent.com/openvinotoolkit/model_server/master/example_client/client_utils.py -o client_utils.py https://raw.githubusercontent.com/openvinotoolkit/model_server/master/example_client/face_detection.py -o face_detection.py  https://raw.githubusercontent.com/openvinotoolkit/model_server/master/example_client/client_requirements.txt -o client_requirements.txt`
<br>Put the image in a folder by itself. The script runs inference on all images in the folder.`curl --create-dirs https://raw.githubusercontent.com/openvinotoolkit/model_server/master/example_client/images/people/people1.jpeg -o images/people1.jpeg`
<br>Create a folder in which inference results will be put:`mkdir results`
<br>Run the client script:`python3 face_detection.py --model_name age-gender-recognition --batch_size 1 --width 62 --height 62 --input_images_dir images --output_dir results`
