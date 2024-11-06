import csv
import json
import time
from datetime import datetime, timedelta
import numpy as np
import requests
from dotenv import load_dotenv
import os
from dateutil import parser
from utils.custom_generator import CustomRandomGenerator
load_dotenv()
class problem1:
    def __init__(self):
        self.API_KEY = os.getenv("API_KEY")
        self.NASA_APOD_URL =os.getenv("NASA_APOD_URL")
        self.JSON_FILE_NAME = os.getenv("JSON_FILE_NAME")
    def get_apod_data(self, date):
        response = requests.get(f'{self.NASA_APOD_URL}?api_key={self.API_KEY}&date={date}', auth=('user', 'pass'))
        formatted_response = (response.json())
        return {
            "date": formatted_response['date'] or 'No date',
            "title": formatted_response['title'] or 'No title',
            "url": formatted_response['url'] or 'No url',
            "explanation": formatted_response['explanation'] or 'No explanation',
            "media_type": formatted_response['media_type'] or 'No media_type'
        }
    def fetch_multiple_apod_data(self, start_date, end_date):
        progressive_date = parser.parse(start_date)
        end_date = parser.parse(end_date)
        json_storer = {}
        for _ in range((end_date-progressive_date).days):
            json_storer[str(progressive_date.date())] = self.get_apod_data(progressive_date.date())
            progressive_date += timedelta(days=1)
            # time.sleep(1)
            print(f"Data 📈 fetch completed for {progressive_date} ✅")
        with open(self.JSON_FILE_NAME, mode='w', encoding='utf-8') as feedsjson:
            entry = {str(datetime.now()): json_storer}
            json.dump(entry,feedsjson)
        return True
class problem2:
    def __init__(self):
        self.JSON_FILE_NAME = os.getenv("JSON_FILE_NAME")
        self.CSV_FILE_NAME = os.getenv("CSV_FILE_NAME")
        with open(self.JSON_FILE_NAME, 'r') as file:
            self.json_file_content = json.load(file)
    def read_apod_data(self):
        for each_date in (entry for timestamps in self.json_file_content.values() for entry in timestamps.values()):
            print(each_date['date'], each_date['title'])
        return True
    def analyze_apod_media(self):
        videos = 0
        images = 0
        longest_explanation_text = ""
        for each_date in (entry for timestamps in self.json_file_content.values() for entry in timestamps.values()):
            if each_date['media_type'] == 'image':
                images+=1
            if each_date['media_type'] == 'video':
                videos+=1
            if len(longest_explanation_text) < len(each_date['explanation']):
                longest_explanation_text = each_date["explanation"]
        print("📊 APOD Media Analysis Summary 📊")
        print(f"🖼️ Total Images: {images}")
        print(f"🎥 Total Videos: {videos}")
        print("📜 Longest Explanation:")
        print(f"{longest_explanation_text[:200]}...")
        return
    def write_to_csv_apod_data(self):
        headers = ["date", "title", "url", "explanation", "media_type"]
        csv_data = (entry for timestamps in self.json_file_content.values() for entry in timestamps.values())
        try:
            with open(self.CSV_FILE_NAME, mode='a', newline='', encoding='utf-8') as csvfile:
                writer = csv.DictWriter(csvfile, fieldnames=headers)
                writer.writeheader()
                for row in csv_data:
                    writer.writerow(row)
            print(f"Data successfully written to {self.CSV_FILE_NAME}")
        except IOError as e:
            print(f"Error writing to CSV file: {e}")
        return
class problem3:
    def __init__(self):
        pass
    def numpy_calculations(self):
        bit_generator = np.random.PCG64()
        custom_rng = CustomRandomGenerator(bit_generator)
        array = custom_rng.custom_array(shape=(20, 5))
        print(array)
        print("\nSum of each row:", np.sum(array, axis=1))
        print("\nTotal sum:", np.sum(array))
        divisible_by_3_and_5 = []
        for row in array:
            for element in row:
                if element % 3 == 0 and element % 5 == 0:
                    divisible_by_3_and_5.append(element)

        print("\nElements divisible by both 3 and 5:")
        print(divisible_by_3_and_5)
        mean_value = np.mean(array)
        for i in range(array.shape[0]):
            for j in range(array.shape[1]):
                if array[i, j] > 75:
                    array[i, j] = mean_value
        print("\nArray after replacing elements greater than 75 with the mean:")
        print(array)
        mean_value = np.mean(array)
        print(f"\nMean of all values: {mean_value}")
        std_dev_value = np.std(array)
        print(f"Standard Deviation of all values: {std_dev_value}")
        median_value = np.median(array)
        print(f"Median value of the array: {median_value}")
        variance_per_column = np.var(array, axis=0)
        print(f"Variance for each column: {variance_per_column}")
        return