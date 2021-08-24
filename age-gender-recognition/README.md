`docker run --rm -d -u $(id -u):$(id -g) -v $(pwd)/model:/models/age_gender -p 9002:9002 -p 9003:9003 openvino/model_server:latest --model_path /models/age_gender --model_name age_gender --port 9002 --rest_port 9003`

