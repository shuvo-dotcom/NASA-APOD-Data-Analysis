from fetch_data import problem1, problem2, problem3
if __name__ == "__main__":
    apod_fetcher = problem1()
    start_date = '2024-10-01'
    end_date = '2024-10-10'
    print(apod_fetcher.get_apod_data(start_date))
    apod_fetcher.fetch_multiple_apod_data(start_date, end_date)
    apod_processor = problem2()
    apod_processor.read_apod_data()
    apod_processor.analyze_apod_media()
    apod_processor.write_to_csv_apod_data()
    numpy_operations = problem3()
    numpy_operations.numpy_calculations()
