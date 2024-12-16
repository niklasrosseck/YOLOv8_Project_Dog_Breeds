import os
import shutil
import zipfile

def create_folder(path):
    """Create a folder if it doesn't exist."""
    if not os.path.exists(path):
        os.makedirs(path)

def unzip_all_datasets(zip_folder, output_folder):
    """
    Unzips all .zip files in the given folder to separate subfolders.

    Args:
        zip_folder (str): Path to the folder containing .zip files.
        output_folder (str): Path to the folder where datasets will be unzipped.
    """
    create_folder(output_folder)

    for file in os.listdir(zip_folder):
        if file.endswith(".zip"):
            breed_name = os.path.splitext(file)[0]
            zip_path = os.path.join(zip_folder, file)
            breed_output_path = os.path.join(output_folder, breed_name)

            print(f"Unzipping {file} to {breed_output_path}...")
            with zipfile.ZipFile(zip_path, 'r') as zip_ref:
                zip_ref.extractall(breed_output_path)

def merge_datasets(input_folder, output_folder):
    """
    Merges datasets from multiple subfolders into a single dataset with
    train, test, and val folders for images and labels.

    Args:
        input_folder (str): Path to the unzipped datasets.
        output_folder (str): Path to the combined dataset.
    """
    subsets = ["train", "test", "valid"]
    subdirs = ["images", "labels"]

    for subset in subsets:
        for subdir in subdirs:
            create_folder(os.path.join(output_folder, subset, subdir))

    for breed_folder in os.listdir(input_folder):
        breed_path = os.path.join(input_folder, breed_folder)
        if not os.path.isdir(breed_path):
            continue  

        print(f"Processing breed: {breed_folder}")
        for subset in subsets:
            for subdir in subdirs:
                src_folder = os.path.join(breed_path, subset, subdir)
                dest_folder = os.path.join(output_folder, subset, subdir)

                if not os.path.exists(src_folder):
                    print(f"Warning: Missing {subset}/{subdir} in {breed_folder}")
                    continue

                for file in os.listdir(src_folder):
                    src_file = os.path.join(src_folder, file)
                    dest_file = os.path.join(dest_folder, file)

                    if os.path.exists(dest_file):
                        base, ext = os.path.splitext(file)
                        dest_file = os.path.join(dest_folder, f"{base}_{breed_folder}{ext}")

                    shutil.copy(src_file, dest_file)

    print("Merging completed!")


def main():
    zip_folder = "zipped_datasets"  
    unzipped_folder = "unzipped_datasets" 
    combined_folder = "test_dataset"  

    unzip_all_datasets(zip_folder, unzipped_folder)
    
    merge_datasets(unzipped_folder, combined_folder)

    print("All datasets have been unzipped and merged successfully!")

if __name__ == "__main__":
    main()
