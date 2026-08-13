import time
import requests
import os
from utilities import logger

MASTER_GSHEET_ID = os.getenv("MASTER_GSHEET_ID", "")

def download_sheet_xlsx(sheet_id: str, output_file: str):
    if not sheet_id:
        logger.error("MASTER_GSHEET_ID is not set.")
        return

    start_time = time.time()
    logger.info(f"Start downloading master sheet as XLSX at: {time.ctime(start_time)}")
    
    # format=xlsx downloads the entire workbook containing all tabs
    url = f"https://docs.google.com/spreadsheets/d/{sheet_id}/export?format=xlsx"
    resp = requests.get(url, timeout=60)
    resp.raise_for_status()
    
    with open(output_file, 'wb') as f:
        f.write(resp.content)
        
    end_time = time.time()
    logger.info(f"End time: {time.ctime(end_time)} | Duration: {end_time - start_time:.2f} seconds")

if __name__ == "__main__":
    output_path = "master_sheet.xlsx"
    download_sheet_xlsx(MASTER_GSHEET_ID, output_path)

_______________________________OUTPUT___________________________________________ 

'''2026-08-13 11:29:53 [INFO] Start downloading master sheet as XLSX at: Thu Aug 13 11:29:53 2026
2026-08-13 11:29:55 [INFO] End time: Thu Aug 13 11:29:55 2026 | Duration: 1.75 seconds'''
