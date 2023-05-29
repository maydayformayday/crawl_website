# This is a sample Python script.

# Press Shift+F10 to execute it or replace it with your code.
# Press Double Shift to search everywhere for classes, files, tool windows, actions, and settings.

# Press the green button in the gutter to run the script.
if __name__ == '__main__':
    import csv
    import requests
    from bs4 import BeautifulSoup


    def crawl_website(url):
        response = requests.get(url)
        if response.status_code == 200:
            soup = BeautifulSoup(response.content, 'html.parser')
            articles = soup.select('.post.f.list-post')

            # Create a list to store the extracted data
            data = []

            for article in articles:
                title_element = article.select_one('h2 a')
                if title_element:
                    title = title_element.get_text(strip=True)
                    link = title_element['href']

                    date_element = article.select_one('.time_s')
                    if date_element:
                        date = date_element.get_text(strip=True)
                    else:
                        date = ""

                    content_element = article.select_one('.indexs')
                    if content_element:
                        content = content_element.get_text(strip=True)
                    else:
                        content = ""

                    # Add the extracted data to the list
                    data.append([title, link, date, content])

            # Define the path and filename for the CSV file
            csv_file = "extracted_data.csv"

            # Write the data to the CSV file
            with open(csv_file, "w", newline="", encoding="utf-8") as file:
                writer = csv.writer(file)
                writer.writerow(["Title", "Link", "Date", "Content"])  # Write header row
                writer.writerows(data)  # Write data rows

            print("Data saved to", csv_file)
        else:
            print("Failed to retrieve website:", url)


    # Provide the URL of the website to crawl
    url = 'http://jandan.net/'
    crawl_website(url)

# See PyCharm help at https://www.jetbrains.com/help/pycharm/
