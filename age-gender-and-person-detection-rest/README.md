# age-gender-and-person-detection-rest

docker run --rm \
-p 9001:9001 -p 8001:8001 \
-v $(pwd)/models:/opt/ml \
-v $(pwd)/config.json:/opt/ml/config.json \
openvino/model_server:latest \
--config_path /opt/ml/config.json \
--port 9001 \
--rest_port 8001 

With MYRIAD:
1. 1 model age-gender:
docker run --rm -it --net=host -u root --privileged -v $(pwd)/models/age-gender/FP16:/opt/model -v /dev:/dev -p 9001:9001 -p 8001:8001 openvino/model_server \
--model_path /opt/model --model_name age-gender --port 9001 --rest_port 8001 --target_device MYRIAD
2. Config with 2 models:
docker run --rm -it --net=host -u root --privileged -v $(pwd)/models:/opt/ml -v /dev:/dev -v $(pwd)/config.json:/opt/ml/config.json -p 9001:9001 -p 8001:8001 openvino/model_server \
--config_path /opt/ml/config.json --port 9001 --rest_port 8001



##### now works bad