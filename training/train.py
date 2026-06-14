from ultralytics import YOLO

# Dataset Path
DATASET_PATH = r"D:\PlantImageProcessing\datasets\PlantVillage"

# Load YOLOv8 Classification Model
model = YOLO("yolov8n-cls.pt")

# Train
results = model.train(
    data=DATASET_PATH,
    epochs=20,
    imgsz=224,
    batch=32,
    project=r"D:\PlantImageProcessing\runs",
    name="plant_disease_classifier"
)

print("Training Completed!")