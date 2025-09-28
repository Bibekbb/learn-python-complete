from ultralytics import YOLO

model = YOLO("B:/Project 0/test/runs/detect/train32/weights/best.pt")
results = model.predict(source="B:/Project 0/model/Project 0/valid/images/IMG_20241224_162158_jpg.rf.1f62db481859ddf4e9f5b3155afc5660.jpg")
results.show()  # This will display the image with predictions
