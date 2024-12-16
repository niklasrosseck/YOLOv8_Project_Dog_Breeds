# YOLOv8 Dog Breed Detection Project

## **Introduction**

This project focuses on developing a YOLOv8-based object detection model for identifying dog breeds. The journey began with a pre-annotated dataset and expanded to include self-annotated data and advanced preprocessing techniques.

---

## **Project Start**

### **Initial Dataset**

- Found a dataset on [Roboflow](https://universe.roboflow.com/cv-project-v2/6-dog-breeds/dataset/1).
- Dataset was pre-annotated and split into train, test, and validation sets.
- Decided to enhance the project by appending additional data.

---

## **Dataset Expansion**

### **Adding Dog Breeds**

#### **Stanford Dogs Dataset**

- Sourced from Kaggle: [Stanford Dogs Dataset](https://www.kaggle.com/datasets/jessicali9530/stanford-dogs-dataset).
- Contained 120 breeds with 150-200 images per breed.
- Initial plan: Use all 120 breeds.

#### **Preprocessing Challenges**

1. **Renaming Files**:
   - Scripted renaming to include breed names and unique identifiers.
2. **Annotation Issues**:
   - Annotation files were in `set` format.
   - Developed scripts to identify and convert `set` files to `.txt` format.
3. **YOLOv8 Conversion**:
   - Annotations were in Pascal VOC format.
   - Created a script to convert annotations to YOLOv8 format using a class mapping system (ascending order required).
   - Published processed dataset: [Stanford Dog Breeds for YOLOv8](https://www.kaggle.com/datasets/niklasrosseck/stanford-dog-breeds-for-yolov8).
4. **Hardware Limitation**:
   - Dataset was too large for Google Colab.

---

## **Creating a Manageable Dataset**

### **Downsizing the Dataset**

- Selected 20 breeds from the Stanford dataset.
- Added 3 self-annotated breeds.

### **Self-Annotated Data**

- **Image Sourcing**: Downloaded from [Unsplash](https://unsplash.com/).
- **Preprocessing**:
  1. Renamed images to ensure consistency.
  2. Resized images to 640x640 and applied EXIF auto-orientation.
  3. Reduced image quality to 85% to minimize file size.
- **Annotation and Augmentation**:
  - Annotated using Roboflow.
  - Applied data augmentation (horizontal flips, rotations, saturation adjustments) to increase image count from ~150 to ~700 per breed.
  - Augmented each breed individually due to Roboflow free plan limitations.

### **Data Merging**

- Combined augmented data into a single dataset.
- Updated `data.yaml` and corrected class IDs in annotations (Roboflow had assigned all breeds class ID 0).

### **Final Dataset Versions**

1. **Full Dataset**:
   - 23 breeds with data augmentation (~2313 images per breed).
   - Too large for efficient training.
2. **Test Dataset**:
   - 5 breeds without data augmentation (793 images total).

---

## **Model Training**

### **Training Attempts**

#### **Without Pretrained Model**

- Used `yolov8s.yaml` on the 5-breed dataset.
- Ran for 30 epochs but achieved poor results.
- Increased batch size and froze layers, but performance remained unsatisfactory.

#### **Using Pretrained Model**

- Trained with `yolov8m.pt`.
- Ran for 100 epochs (early stopping at 83 epochs).
- Training duration: ~24.9 hours.
- Results saved in `runs/detect/` on [GitHub](https://github.com/niklasrosseck/YOLOv8_Project_Dog_Breeds).

#### **Roboflow Training**

- Used dataset with data augmentation (~2313 images).
- Trained using Roboflow’s built-in tools.

### **Model Comparison**

| Metric                         | My Trained Model | Roboflow Trained Model |
| ------------------------------ | ---------------- | ---------------------- |
| Validation Mean Precision (mP) | **0.9059**       | 0.899                  |
| Validation Mean Recall (mR)    | **0.9199**       | 0.826                  |
| Validation mAP@0.5             | **0.9522**       | 0.917                  |
| Validation mAP@0.5:0.95        | **0.8151**       | -                      |

---

## **Observations and Insights**

- My model outperformed the Roboflow-trained model despite fewer epochs and no data augmentation.
- Pretrained weights (‘yolov8m.pt’) significantly improved performance.
- Data preprocessing and annotation quality were crucial to achieving better results.

---

## **Future Improvements**

1. **Dataset Refinement**:
   - Balance class distribution.
   - Include diverse backgrounds, lighting, and angles.
2. **Hyperparameter Tuning**:
   - Experiment with learning rates, momentum, and weight decay.
   - Use learning rate schedulers.
3. **Infrastructure Optimization**:
   - Leverage high-performance cloud GPUs for larger datasets.

---

## **Resources**

- **GitHub Repository**: [YOLOv8 Dog Breed Detection Project](https://github.com/niklasrosseck/YOLOv8_Project_Dog_Breeds)
- **Kaggle Datasets**:
  - [Stanford Dog Breeds for YOLOv8](https://www.kaggle.com/datasets/niklasrosseck/stanford-dog-breeds-for-yolov8)
  - [Dog Breed Classification YOLOv8](https://www.kaggle.com/datasets/niklasrosseck/dog-breed-classification-yolov8)
  - [Dog Breed Datasets for YOLOv8](https://www.kaggle.com/datasets/niklasrosseck/dog-breed-detection-for-yolov8)
