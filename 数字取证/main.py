import os
import shutil
import argparse
import datetime
from lib import get_chrome_history, get_ip_from_url, get_geo_info, save_to_excel, filter_history

# made by gcc at 16/6/2024 in Chengdu num: 2022141530154
# main.py
def log_error(message):
    with open('error.log', 'a') as f:
        f.write(f"{datetime.datetime.now()}: {message}\n")

def parse_date_range(date_range):
    try:
        start_date_str, end_date_str = date_range.split('-')
        start_date = datetime.datetime.strptime(start_date_str, '%Y/%m/%d')
        end_date = datetime.datetime.strptime(end_date_str, '%Y/%m/%d')
        return start_date, end_date
    except ValueError:
        error_message = "Invalid date range format. Use YYYY/MM/DD-YYYY/MM/DD."
        print(error_message)
        log_error(error_message)
        return None, None

def main():
    parser = argparse.ArgumentParser(description='Process Chrome history.')
    parser.add_argument('-c', '--create', action='store_true', help='Create Excel file with Chrome history.')
    parser.add_argument('-s', '--screen', action='store_true', help='Screen and filter Chrome history.')
    parser.add_argument('-d', '--date', type=str, help='Date range to filter history (YYYY/MM/DD-YYYY/MM/DD).')
    parser.add_argument('-k', '--keyword', type=str, help='Keyword to filter URLs.')
    parser.add_argument('--dip', type=str, help='Destination IP address to filter history.')
    parser.add_argument('--country', type=str, help='Country to filter IP geo-location.')
    parser.add_argument('--city', type=str, help='City to filter IP geo-location.')

    args = parser.parse_args()

    if not (args.create or args.screen):
        parser.print_help()
        return

    original_history_path = r'C:\Users\m1550\AppData\Local\Google\Chrome\User Data\Default\History'
    temp_history_path = r'C:\Users\m1550\AppData\Local\Google\Chrome\User Data\Default\History_copy'

    if not os.path.exists(original_history_path):
        error_message = "Chrome history file not found."
        print(error_message)
        log_error(error_message)
        return

    try:
        shutil.copy2(original_history_path, temp_history_path)

        history = get_chrome_history(temp_history_path)

        os.remove(temp_history_path)

        for entry in history:
            ip = get_ip_from_url(entry['url'])
            entry['ip'] = ip
            if ip:
                geo_info = get_geo_info(ip)
                entry['country'] = geo_info.get('country') if geo_info else None
                entry['city'] = geo_info.get('city') if geo_info else None
            else:
                entry['country'] = None
                entry['city'] = None

        if args.create:
            output_path = 'chrome_history.xlsx'
            save_to_excel(history, output_path)
            print(f"Chrome history saved to {output_path}.")
            print(f"Number of entries saved: {len(history)}")

        if args.screen:
            start_date, end_date = None, None
            if args.date:
                start_date, end_date = parse_date_range(args.date)
            filtered_history = filter_history(history, start_date, end_date, args.keyword, args.dip, args.country, args.city)
            output_path = 'filtered_chrome_history.xlsx'
            save_to_excel(filtered_history, output_path)
            print(f"Filtered Chrome history saved to {output_path}.")
            print(f"Number of entries in filtered history: {len(filtered_history)}")
    except Exception as e:
        error_message = f"An error occurred: {e}"
        log_error(error_message)
        print(error_message)
        print("Please check error.log for details.")

if __name__ == "__main__":
    main()
