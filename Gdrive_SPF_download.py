import time
import requests
import os
from utilities import logger

MASTER_GSHEET_ID = os.getenv("MASTER_GSHEET_ID", "")
MASTER_GSHEET_SUMMARY_GID = os.getenv("MASTER_GSHEET_SUMMARY_GID", "")

def download_specific_tab(sheet_id: str, gid: str, output_file: str):
    if not sheet_id or not gid:
        logger.error("MASTER_GSHEET_ID or GID is not set.")
        return

    start_time = time.time()
    logger.info(f"Start downloading tab (GID: {gid}) at: {time.ctime(start_time)}")
    
    url = f"https://docs.google.com/spreadsheets/d/{sheet_id}/export?format=csv&gid={gid}"
    resp = requests.get(url, timeout=30)
    resp.raise_for_status()
    
    with open(output_file, 'wb') as f:
        f.write(resp.content)
        
    end_time = time.time()
    logger.info(f"End time: {time.ctime(end_time)} | Duration: {end_time - start_time:.2f} seconds")

if __name__ == "__main__":
    output_path = "summary_sheet.csv"
    download_specific_tab(MASTER_GSHEET_ID, MASTER_GSHEET_SUMMARY_GID, output_path)


'''____________________________________OUTPUT__________________________________________'''

'''2026-08-13 11:24:13 [INFO] Start downloading tab (GID: 345736693) at: Thu Aug 13 11:24:13 2026
2026-08-13 11:24:14 [INFO] End time: Thu Aug 13 11:24:14 2026 | Duration: 1.18 seconds'''
