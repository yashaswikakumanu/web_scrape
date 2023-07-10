from bs4 import BeautifulSoup
import requests
import csv


url = "http://books.toscrape.com/"
response = requests.get(url)
print("hey",response)
csv_file = open('cms_scrape.csv', 'w')
csv_writer = csv.writer(csv_file)
csv_writer.writerow(['book_title', 'book_price'])

if response.status_code == 200:
    soup = BeautifulSoup(response.text, "html.parser")
    books = soup.find_all("h3")  # Finding all h3 tags which contain book titles
    prices = soup.find_all("p", class_="price_color")  # Finding all p tags with class "price_color" which contain book prices

    for book, price in zip(books, prices):
        title = book.a.attrs["title"]  # Extracting the title attribute from the anchor tag
        book_price = price.text.strip()  # Removing any extra spaces from the price text
        print(f"Title: {title}, Price: {book_price}")
        csv_writer.writerow([title,book_price])
else:
    print("Failed to fetch data from the website.")



# source = requests.get('http://books.toscrape.com/').text

# soup = BeautifulSoup(source, 'lxml')
# print(soup.prettify())
# # csv_file = open('cms_scrape.csv', 'w')

# # csv_writer = csv.writer(csv_file)
# # csv_writer.writerow(['headline', 'summary', 'video_link'])
# # article = soup.find_all('article'):
# # for article in soup.find_all('article'):
# #     headline = article.h2.a.text
# #     print(headline)

# #     summary = article.find('div', class_='entry-content').p.text
# #     print(summary)

# #     try:
# #         vid_src = article.find('iframe', class_='youtube-player')['src']

# #         vid_id = vid_src.split('/')[4]
# #         vid_id = vid_id.split('?')[0]

# #         yt_link = f'https://youtube.com/watch?v={vid_id}'
# #     except Exception as e:
# #         yt_link = None

# #     print(yt_link)

# #     print()

# #     csv_writer.writerow([headline, summary, yt_link])

# # csv_file.close()
