# age-gender-and-person-detection-rest

docker run --rm \
-p 9001:9001 -p 8001:8001 \
-v $(pwd)/models:/opt/ml \
-v $(pwd)/config.json:/opt/ml/config.json \
openvino/model_server:latest \
--config_path /opt/ml/config.json \
--port 9001 \
--rest_port 8001 


##### now works bad