import cv2
import numpy as np 


def rtd():
    # net = cv2.dnn.readNet('realTimeDetector/yolov3.weights','realTimeDetector/yolov3.cfg')
    net = cv2.dnn.readNet('yolov3.weights','yolov3.cfg')
    classes = []
    # with open('realTimeDetector/coco.names','r') as f:
    with open('coco.names','r') as f:
        classes = f.read().splitlines()

    # cap = cv2.VideoCapture('new video.mp4')
    cap = cv2.VideoCapture('traffic.mp4')
    # cap = cv2.VideoCapture(0)
    # img = cv2.imread('image.jpg')

    while True:
        if cap.isOpened():
            _, img = cap.read()
        height, width, _ = img.shape

        blob = cv2.dnn.blobFromImage(img, 1/255, (416, 416), (0,0,0), swapRB=True, crop=False)
        net.setInput(blob)
        output_layers_names = net.getUnconnectedOutLayersNames()
        layersOutput =net.forward(output_layers_names)

        boxes = []
        confidences = []
        class_ids = []

        for output in layersOutput:
            for detection in output:
                scores = detection[5:]
                class_id = np.argmax(scores)
                confidence = scores[class_id]
                if confidence > 0.5:
                    center_x = int(detection[0]*width)
                    center_y = int(detection[1]*height)
                    w = int(detection[2]*width)
                    h = int(detection[3]*height)

                    x = int(center_x - w/2)
                    y = int(center_y - h/2)

                    boxes.append([x, y, w, h])
                    confidences.append((float(confidence)))
                    class_ids.append(class_id)

        #print(len(boxes))
        indexes = cv2.dnn.NMSBoxes(boxes, confidences, 0.5, 0.4)

        font = cv2.FONT_HERSHEY_PLAIN
        colors = np.random.uniform(0,255, size=(len(boxes),3))

        for i in indexes.flatten():
            x, y, w, h = boxes[i]
            label = str(classes[class_ids[i]])
            confidence = str(round(confidences[i],2))
            color = colors[i]
            cv2.rectangle(img, (x,y), (x+w, y+h), color, 2)
            cv2.putText(img, label + " " + confidence, (x,y+20), font, 2, (255,255,255), 2)

        cv2.imshow('RealTimeDetector', img)
        key = cv2.waitKey(1)
        if key == 27:
            break

    cap.release()
    cv2.destroyAllWindows()