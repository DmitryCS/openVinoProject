# instance segmention people

docker run --rm -d -it --net=host --privileged \
--name dmitrycs_test \
-v $(pwd)/models:/opt/ml \
openvino/model_server:latest \
--config_path /opt/ml/config.json \
--port 9001 \
--rest_port 8001 
