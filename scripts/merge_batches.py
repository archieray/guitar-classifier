## This is my fault for not doing it in one batch.

import os
import shutil

# --- Configuration ---
# You MUST verify this is the correct absolute path to your 'data/test' directory
BASE_DIR = r'C:\Users\archi\Data stuff\Guitar classifier\data\test'
START_INDEX = 501  # Files will start numbering from 000501

def merge_and_rename():
    """Merges image batches into final folders, renaming files sequentially."""
    
    # Define the consolidation tasks based on your file system
    # SOURCE (Batch 2 Folder) : DESTINATION (Final Folder)
    consolidation_tasks = {
        'fender_stratocaster_BATCH2': 'stratocaster',
        'gibson_les_paul_BATCH2': 'les paul'  # Note: Merging into 'les paul'
    }

    for source_folder, dest_folder in consolidation_tasks.items():
        source_dir = os.path.join(BASE_DIR, source_folder)
        dest_dir = os.path.join(BASE_DIR, dest_folder) 
        
        print(f"--- Starting merge from {source_folder} to {dest_folder} ---")

        if not os.path.exists(source_dir):
            print(f"Error: Source folder not found at {source_dir}. Skipping.")
            continue

        if not os.path.exists(dest_dir):
            print(f"Error: Destination folder not found at {dest_dir}. Skipping.")
            continue

        current_index = START_INDEX
        
        # Get all image files, sorted to maintain the order from the download
        files_to_process = sorted([f for f in os.listdir(source_dir) if f.lower().endswith(('.jpg', '.jpeg', '.png'))])

        if not files_to_process:
            print(f"No image files found in {source_folder}. Skipping.")
            os.rmdir(source_dir)
            continue

        for filename in files_to_process:
            # Create the new 6-digit padded filename (e.g., 000501.jpg)
            file_extension = os.path.splitext(filename)[1].lower()
            new_filename = f"{current_index:06}{file_extension}" 
            
            source_path = os.path.join(source_dir, filename)
            dest_path = os.path.join(dest_dir, new_filename)
            
            # Move the file (renaming it in the process)
            try:
                shutil.move(source_path, dest_path)
                current_index += 1
            except Exception as e:
                print(f"Critical Error moving {filename}: {e}. Stopping merge.")
                return

        print(f"Successfully merged {current_index - START_INDEX} files. Final count starts at {START_INDEX}.")
        os.rmdir(source_dir)
        print(f"Removed empty source directory: {source_folder}")
    
    print("--- All batch merges complete ---")

if __name__ == "__main__":
    merge_and_rename()
    