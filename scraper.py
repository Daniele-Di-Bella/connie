import requests
from bs4 import BeautifulSoup


def scholar_scraper(query, num_pages):
    articles = []
    page = 0
    while page < num_pages:
        # https://scholar.google.com/scholar?as_ylo=2024&q=plankton+community&hl=it&as_sdt=0,5
        url = f"https://scholar.google.com/scholar?start={page * 10}&q={query}&hl=en&as_sdt=0,5"
        response = requests.get(url)
        soup = BeautifulSoup(response.content, "html.parser")
        results = soup.find_all("div", class_="gs_ri")

        for result in results:
            title = result.find("h3", class_="gs_rt").text
            authors = result.find("div", class_="gs_a").text
            link = result.find("a")["href"]
            articles.append({"Title": title, "Authors": authors, "Link": link})

        page += 1

    print(articles)


scholar_scraper("plankton+communities", 1)
