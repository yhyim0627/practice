
import pandas as pd
import numpy as np
import cv2
import matplotlib.pyplot as plt
import glob
import time

##############################################################################

start = time.time()

box = pd.read_csv('train_solution_bounding_boxes(1).csv')

# Yolo 로드
net = cv2.dnn.readNet("yolov3.weights", "yolov3.cfg")
classes = []
with open("coco.names", "r") as f:
    classes = [line.strip() for line in f.readlines()]
layer_names = net.getLayerNames()
output_layers = [layer_names[i[0] - 1] for i in net.getUnconnectedOutLayers()]

########################YOLO를 이용하기 위한 함수 정의##########################

def predict_yolo(img_path):
    # 이미지를 Blob으로 변환
    img = cv2.imread(img_path)
    img = cv2.cvtColor(img, cv2.COLOR_BGR2RGB)
    height, width, channels = img.shape
    
    blob = cv2.dnn.blobFromImage(img, 1/256, (320, 320), (0, 0, 0), swapRB=True, crop=False)
    net.setInput(blob)
    
    # outs는 출력으로 탐지된 개체에 대한 모든 정보와 위치를 제공한다.
    outs = net.forward(output_layers)
    
    # 정보를 화면에 표시
    class_ids = []
    confidences = []
    boxes = []
    for out in outs:
        for detection in out:
            scores = detection[5:]
            class_id = np.argmax(scores)
            confidence = scores[class_id]
            if confidence > 0.5:
                # Object detected
                center_x = int(detection[0] * width)
                center_y = int(detection[1] * height)
                w = int(detection[2] * width)
                h = int(detection[3] * height)
                # 좌표
                x = int(center_x - w / 2)
                y = int(center_y - h / 2)
                boxes.append([x, y, w, h])
                confidences.append(float(confidence))
                class_ids.append(class_id)
    
    indexes = cv2.dnn.NMSBoxes(boxes, confidences, 0.5, 0.4)
    
    font = cv2.FONT_HERSHEY_PLAIN
    colors = np.random.uniform(0, 255, size=(len(boxes), 3))
    
    if len(indexes) > 0:
      for i in indexes.flatten():
          x, y, w, h = boxes[i]
          print(x, y, w, h)
          label = str(classes[class_ids[i]])
          confidence = str(round(confidences[i], 2))
          color = colors[i]
          cv2.rectangle(img, (x, y), ((x+w), (y+h)), color, 2)
          cv2.putText(img, label + " " + confidence, (x, y+20), font, 2, (0, 255, 0), 2)
    
      plt.imshow(img)
      plt.axis('off')
      plt.show()
    
    else:
      print('탐지된 물체가 없습니다.')
      plt.imshow(img)
      plt.axis('off')
      plt.show()

###############################################################################

paths = glob.glob('data/testing_images/*.jpg')
img_path = []

for img_path in paths:
    predict_yolo(img_path)

end = time.time()
print("실행시간: {0:.5f}초".format(end - start))
