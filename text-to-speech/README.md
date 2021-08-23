# forward-tacotron
#### You can translate your text to audio by changing input (-i) and output (-o).
Command to run program:<br>`python3  text_to_speech_demo.py -m_duration models/public/forward-tacotron/forward-tacotron-duration-prediction/FP16/forward-tacotron-duration-prediction.xml -m_forward models/public/forward-tacotron/forward-tacotron-regression/FP16/forward-tacotron-regression.xml -m_upsample models/public/wavernn/wavernn-upsampler/FP16/wavernn-upsampler.xml --model_rnn models/public/wavernn/wavernn-rnn/FP16/wavernn-rnn.xml -i text-files/lorem-ipsum.txt -o results/lorem-ipsum.wav`
