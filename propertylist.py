import requests
from bs4 import BeautifulSoup
import pandas, time

# list of all data
l = []
base_ur = "https://www.commonfloor.com/ahmedabad-property/for-sale?page="
for page in range(0, 3):  # looping over pages
    print(base_ur + str(page))
    r = requests.get("https://www.commonfloor.com/ahmedabad-property/for-sale")
    c = r.content
    soup = BeautifulSoup(c, "html.parser")

    divs = soup.find_all("div", {"class": "snb-tile"})
    for div in divs:
        d = {}  # dictonary of each set of data
        title_div = div.find("div", {"class": "st_title"})
        
        d['title'] = title_div.find("a").text.replace("\n", "")

        d['price'] = title_div.find("span", {"class", "s_p"}).text.replace(
            "\n", "").replace(" ", "")

        info_div = div.find("div", {"class": "snb-info-dls"})

        CarpetArea = info_div.find_all(
            "div", {"class": "infodata"})[0].text.replace("\n", "-").replace(
                "--", "-").replace(" ", "")
        d['CarpetArea'] = CarpetArea[1:len(CarpetArea) - 1].split("-")[1]

        Possession = info_div.find_all(
            "div", {"class": "infodata"})[1].text.replace("\n", "-").replace(
                "--", "-").replace(" ", "")
        d['Possession On'] = Possession[1:len(Possession) - 1].split("-")[1]

        Floor = info_div.find_all("div",
                                  {"class": "infodata"})[2].text.replace(
                                      "\n", "-").replace("--", "-").replace(
                                          " ", "")
        d['Floor'] = Floor[1:len(Floor) - 1].split("-")[1]

        Bathrooms = info_div.find_all(
            "div", {"class": "infodata"})[3].text.replace("\n", "-").replace(
                "--", "-").replace(" ", "")
        d['Bathrooms'] = Bathrooms[1:len(Bathrooms) - 1].split("-")[1]

        l.append(d)
    time.sleep(5)  # sleep for 5 seconds

df = pandas.DataFrame(l)
df.to_csv("output.csv")