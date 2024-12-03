<h1 align="center">Welcome to NASA-APOD-Data-Analysis 👋</h1>
<p>
  <img alt="Version" src="https://img.shields.io/badge/version-1-blue.svg?cacheSeconds=2592000" />
</p>

> Project Description
```
The project tries to resolve all the 4 problems from the assignment. 
1. Fetching data from NASA APOD website using the API Keys provided and loading those Keys using dotenv module.
2. After fetching the data from the API -> data needs to be read from the json format and manupulations needs to be done.
3. Creating Numpy 2d Array based on certain predefined conditions and then appyling filter technique to retrieve the final array.
4. Analytically Observing the Iris dataset and its results over newly generated features using feature enginering.

```
Create a file named .env and place all the keys required in the file.
```
API_KEY=your_key
NASA_APOD_URL=https://api.nasa.gov/planetary/apod
JSON_FILE_NAME=apod_data.json
CSV_FILE_NAME=apod_summary.csv
```

> Project Installation
```
(caenv) caenvapple@Mac NASA-APOD-Data-Analysis % pip install requirements.txt
(caenv) caenvapple@Mac NASA-APOD-Data-Analysis % cd NASA-APOD-Data-Analysis
(caenv) caenvapple@Mac NASA-APOD-Data-Analysis % python src/__init__.py

Note: Make sure to use virtual enviroments for this project.
```

> Project Configurations
```

from dotenv import load_dotenv
load_dotenv()
class problem1:
    def __init__(self):
        self.API_KEY = os.getenv("API_KEY")
        self.NASA_APOD_URL =os.getenv("NASA_APOD_URL")
        self.JSON_FILE_NAME = "src/static_files/"+os.getenv("JSON_FILE_NAME")
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
            time.sleep(1)
            print(f"Data 📈 fetch completed for {progressive_date} ✅")
        with open(self.JSON_FILE_NAME, mode='w', encoding='utf-8') as feedsjson:
            entry = {str(datetime.now()): json_storer}
            json.dump(entry,feedsjson)
        return True

```
In the above code snipet the below mentioned variables are loaded from .env files.
```
self.API_KEY = os.getenv("API_KEY")
self.NASA_APOD_URL =os.getenv("NASA_APOD_URL")
self.JSON_FILE_NAME = "src/static_files/"+os.getenv("JSON_FILE_NAME")
```
Note the names mentioned in the .env file must be matching to when implemented.
## Author

👤 **Suvajit Lodh**

* Github: [@shuvo-dotcom](https://github.com/shuvo-dotcom)
* LinkedIn: [@suvajitlodh](https://linkedin.com/in/suvajitlodh)

## Show your support

Give a ⭐️ if this project helped you!
