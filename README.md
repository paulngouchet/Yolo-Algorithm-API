# Yolo-Algorithm-API
Real Time Object Detection based on the state of the art Computer Vision Algorithm YOLO - You only Look Once. YOLO is packaged into an API


You need to download the Weights yolov3.weights using the Machine Learning Mastery Website

Then you need to run the code create_keras_model.py - to create Keras model based on the downloaded yolov3 weights

YOLO First AI Scientific Algorithm

http://157.230.159.18:5003/api/vision

ssh root@157.230.159.18

pip3 install -r requirements.txt


scp /Users/paulngouchet/Desktop/Scientific_Algorithm/Main_Rapid_API_Yolo/Yolo_API.zip root@157.230.159.18:/root/ScientificAlgorithm

sudo ufw allow 5003

ps -fA | grep python3

nohup python3 run.py --daemon &

Yolo V3 using Keras

Will have to redo the algorithm. It is actually than using that borrowed code. i have way more freedom
https://machinelearningmastery.com/how-to-perform-object-detection-with-yolov3-in-keras/


it took 7.469701290130615 seconds.

Current shape is 2vCPUs 4gb, 80gb, 4 TB / $20/month - With this shape it takes about 7.5 s. I will certainly have to reshape to a lot.

Too slow on CPU but GPU are too expensive so it would still be better to have a big CPU shape depending on how many customers.
