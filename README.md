# YOLOv8 Dog Breed Detection

This repository contains the implementation and results of training a YOLOv8 model to detect and classify different dog breeds. The project focuses on achieving high accuracy and efficiency using state-of-the-art techniques and optimizations.

## Dataset

The dataset used includes images of five distinct dog breeds, prepared and uploaded to [Kaggle](https://www.kaggle.com/datasets/niklasrosseck/dog-breed-classification-yolov8/data). Due to size constraints, the dataset is not included in this repository.

## Model Training

- **Model**: YOLOv8
- **Task**: Object detection and classification
- **Optimization**: Training results include loss curves, confusion matrices, and validation images stored in the `runs/detect/` folder.
- **Performance**: The model demonstrated strong detection and classification performance for the target breeds.

## Project Highlights

1. **Preprocessing**:

   - Images were resized and augmented to enhance model generalization.
   - Annotations were formatted for YOLOv8 compatibility.

2. **Evaluation Metrics**:

   - Intersection over Union (IoU)
   - Precision and recall scores
   - Confusion matrix and validation performance

3. **Performance**:
   - High accuracy in identifying and distinguishing breeds.
   - Robust performance under varied lighting and background conditions.

## How to Use

1. Clone the repository:

   ```bash
   git clone https://github.com/niklasrosseck/YOLOv8_Project_Dog_Breeds.git
   cd YOLOv8_Project_Dog_Breeds

   ```

2. Download the dataset from Kaggle

3. Include your preferred YOLOv8 model in the yolo.ipynb and run it

4. Explore the results. Outputs are stored in the runs/detect/ folder.

## Other scripts

1. **Data Preprocessing**:

   - Used for resizing the images to 640 \* 640
   - Auto-orient based on EXIF
   - Quality of image can be inputted (higher quality = larger file size)
   - Use batch_preprocess to preprocess all images in a folder

2. **Rename**:

   - Used for renaming images and annotations to include the specific breed and a unique identifier
   - Also has functions to identify file type and change file extension
   - Renames images and annotations by identifying the same name and then renaming both with the same name
   - Also has a function to convert from VOC to YOLOv8 annotations with a class mapping

3. **Merging Datasets**:
   - Merges multiple zip foldes into one
   - Keeps file structure with test, train and valid
