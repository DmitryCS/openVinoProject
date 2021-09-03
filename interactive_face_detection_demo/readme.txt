./interactive_face_detection_demo \
    -i children.mp4  \
    -m models/face-detection-adas-0001/FP16/face-detection-adas-0001.xml \
    -m_ag models/age-gender-recognition-retail-0013/FP16/age-gender-recognition-retail-0013.xml \
    -m_hp models/head-pose-estimation-adas-0001/FP16/head-pose-estimation-adas-0001.xml \
    -m_em models/emotions-recognition-retail-0003/FP16/emotions-recognition-retail-0003.xml \
    -m_lm models/facial-landmarks-35-adas-0002/FP16/facial-landmarks-35-adas-0002.xml \
    -m_am models/anti-spoof-mn3/FP16/anti-spoof-mn3.xml \
    -d GPU

./interactive_face_detection_demo    \
 -i children.mp4  \
     -m models/face-detection-retail-0004/FP16/face-detection-retail-0004.xml  \
        -m_ag models/age-gender-recognition-retail-0013/FP16/age-gender-recognition-retail-0013.xml   \
          -m_hp models/head-pose-estimation-adas-0001/FP16/head-pose-estimation-adas-0001.xml   \
            -m_em models/emotions-recognition-retail-0003/FP16/emotions-recognition-retail-0003.xml   \
              -m_lm models/facial-landmarks-35-adas-0002/FP16/facial-landmarks-35-adas-0002.xml     \
                 -no_show -d MYRIAD -d_ag MYRIAD -d_hp MYRIAD -d_em MYRIAD
