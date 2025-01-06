from ultralytics import YOLO

model = YOLO('yolov8n-cls.pt')  # load a pretrained model (recommended for training)

model.train(data=r"C:\Users\arman\OneDrive\Desktop\YOLO project\data\weather_dataset",
            epochs=20, imgsz=64)