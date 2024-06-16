import sqlite3
import datetime
import socket
from urllib.parse import urlparse
import requests
import pandas as pd

# made by gcc at 16/6/2024 in Chengdu num: 2022141530154
# lib.py

def log_error(message):
    with open('error.log', 'a') as f:
        f.write(f"{datetime.datetime.now()}: {message}\n")

def get_chrome_history(history_path):
    try:
        conn = sqlite3.connect(history_path)
        cursor = conn.cursor()
        query = """
        SELECT urls.url, urls.title, visits.visit_time
        FROM visits
        JOIN urls ON visits.url = urls.id
        ORDER BY visits.visit_time DESC
        """
        cursor.execute(query)
        results = cursor.fetchall()
        conn.close()

        history = []
        for url, title, visit_time in results:
            visit_time = datetime.datetime(1601, 1, 1) + datetime.timedelta(microseconds=visit_time)
            history.append({'url': url, 'title': title, 'visit_time': visit_time})

        return history
    except Exception as e:
        log_error(f"Error getting Chrome history: {e}")
        raise

def get_ip_from_url(url):
    try:
        parsed_url = urlparse(url)
        hostname = parsed_url.hostname
        if hostname:
            ip_address = socket.gethostbyname(hostname)
            return ip_address
    except Exception as e:
        log_error(f"Error getting IP for URL {url}: {e}")
        return None

def get_geo_info(ip):
    try:
        response = requests.get(f"http://ip-api.com/json/{ip}")
        if response.status_code == 200:
            return response.json()
        else:
            log_error(f"Error getting geo info for IP {ip}: HTTP {response.status_code}")
            return None
    except Exception as e:
        log_error(f"Error getting geo info for IP {ip}: {e}")
        return None

def save_to_excel(history, path):
    try:
        df = pd.DataFrame(history)
        df.to_excel(path, index=False)
    except Exception as e:
        log_error(f"Error saving history to Excel: {e}")
        raise

def filter_history(history, start_date=None, end_date=None, keyword=None, ip=None, country=None, city=None):
    try:
        filtered = history
        if start_date and end_date:
            filtered = [entry for entry in filtered if start_date <= entry['visit_time'] <= end_date]
        if keyword:
            filtered = [entry for entry in filtered if keyword.lower() in entry['url'].lower()]
        if ip:
            filtered = [entry for entry in filtered if entry['ip'] == ip]
        if country:
            filtered = [entry for entry in filtered if entry.get('country') and country.lower() in entry['country'].lower()]
        if city:
            filtered = [entry for entry in filtered if entry.get('city') and city.lower() in entry['city'].lower()]
        return filtered
    except Exception as e:
        log_error(f"Error filtering history: {e}")
        raise
