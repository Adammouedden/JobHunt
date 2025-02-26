import requests
import re
import csv

#Google API and custom search engine setup
API_KEY = 'AIzaSyAs7w2Q-cSEVtVZMdOu52-v46IHUlwFrY0'
CX = '85342cd3fb7954431'

# Google Custom Search API endpoint
BASE_URL = "https://www.googleapis.com/customsearch/v1"

def fetch_urls(query, start_index = 1):
    params = {
        'key': API_KEY,
        'cx': CX,
        'q': query,
        'start': start_index,
    }

    response = requests.get(BASE_URL, params=params)
    data = response.json()


    # Now to extract the URLs from the responses
    job_urls = []

    if 'items' in data:
        for item in data['items']:
            job_urls.append(item['link'])

    return job_urls


#Now for a function to save the URLs into a csv file

def convert_to_csv(urls, filename='internship_urls.csv'):
    with open(filename, mode='w', newline='', encoding='utf-8') as file:
        writer = csv.writer(file)
        writer.writerow(['Internship URL']) #Column header
        for url in urls:
            writer.writerow([url])

#Main function

def main():
    result_job_urls = []
    query = "Software Engineering Internships near Orlando, FL"
    total_results = 100
    pages = total_results // 10

    for page_num in range (pages):
        print(f"Fetching page {page_num + 1}...")
        start_index = page_num * 10 + 1 #Google custom search uses 1-based index
        job_urls = fetch_urls(query, start_index)
        result_job_urls.extend(job_urls)

    convert_to_csv(result_job_urls)
    print(f"Scraping complete! {len(result_job_urls)} URLs saved to internship_urls.csv.")

main()
