import csv
from datetime import datetime
import requests
from bs4 import BeautifulSoup


def scholar_scraper(keywords: list, num_pages, most_recent="yes"):
    papers = []
    page = 0
    current_dateTime = datetime.now()
    current_year = current_dateTime.year
    query = ""
    for i in keywords:
        query = query + "+" + i

    while page < num_pages:
        if most_recent == "yes":
            url = f"https://scholar.google.com/scholar?start={page * 10}&q={query}&hl=en&as_sdt=0,5&as_ylo={current_year}"
        else:
            url = f"https://scholar.google.com/scholar?start={page * 10}&q={query}&hl=en&as_sdt=0,5"
        response = requests.get(url)
        soup = BeautifulSoup(response.content, "html.parser")
        results = soup.find_all("div", class_="gs_ri")

        for result in results:
            title = result.find("h3", class_="gs_rt").text
            if result.find("span", class_="gs_ct1") is not None:
                doc_type1 = result.find("span", class_="gs_ct1").text
                if doc_type1 == "[BOOK]":
                    continue
                else:
                    title = title.replace(doc_type1, '')
            if result.find("span", class_="gs_ct2") is not None:
                doc_type2 = result.find("span", class_="gs_ct2").text
                if doc_type2 == "[B]":
                    continue
                else:
                    title = title.replace(doc_type2, "")
            title = title.replace("…\xa0and", "")
            title = title.replace("\xa0…", "")
            title = title.rstrip()
            title = title.lstrip()
            title_l = title.lower()
            keywords_l = [element.lower() for element in keywords]
            N = sum(title_l.count(element) for element in keywords_l)
            rating = (N * 5) / len(keywords)
            link = result.find("a")["href"]
            papers.append({"Title": title, "Rating": rating, "Link": link})

        page += 1

    print(papers)

    field_names = ["Title", "Rating", "Link"]
    with open ("csvs/papers.csv", "w", encoding="utf-8") as file:
        writer = csv.DictWriter(file, fieldnames=field_names)
        writer.writeheader()
        writer.writerows(papers)


scholar_scraper(["communities", "planktonic"], 1)
