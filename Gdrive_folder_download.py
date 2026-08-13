import time
import gdown
from utilities import (
    logger,
    SECURITY_TC_DATA_GDRIVE_FOLDER_ID,
    SECURITY_TC_DATA_DIR,
    QUERY_TC_DATA_GDRIVE_FOLDER_ID,
    QUERY_TC_DATA_DIR
)

def download_drive_folder(folder_id: str, output_dir: str):
    if not folder_id:
        logger.warning(f"No folder ID provided for {output_dir}, skipping.")
        return

    start_time = time.time()
    logger.info(f"Start downloading folder {folder_id} to {output_dir} at: {time.ctime(start_time)}")
    
    # Downloads a publicly shared Google Drive folder using its ID
    gdown.download_folder(id=folder_id, output=output_dir, quiet=False, use_cookies=False)
    
    end_time = time.time()
    logger.info(f"Completed downloading folder to {output_dir}. Duration: {end_time - start_time:.2f} seconds")

if __name__ == "__main__":
    logger.info("Downloading Security Test Data Folder...")
    download_drive_folder(SECURITY_TC_DATA_GDRIVE_FOLDER_ID, SECURITY_TC_DATA_DIR)

    logger.info("Downloading Query Test Data Folder...")
    download_drive_folder(QUERY_TC_DATA_GDRIVE_FOLDER_ID, QUERY_TC_DATA_DIR)
