import requests
from bs4 import BeautifulSoup
import csv


date = input("please enter the data you want in this formate YYYY-MM-DD: ")

page = requests.get(
    f"https://www.yallakora.com/match-center/Match-Center/?date={date}#"
)

# page = requests.get(f"https://www.yallakora.com/match-center/Match-Center/?date=2024-10-02#")


def main(page):
    scr = page.content
    soup = BeautifulSoup(scr, "lxml")
    Match_details = []
    championships = soup.find_all(
        "div", {"class": "matchCard"}
    )  # passing the key and the value for the target section (filttering) It has to be wrote as dic

    # championships is a list here.
    def get_match_info(championships):
        championship_title = championships.contents[1].find("h2").text.strip()
        # note the .contents returns everything as a list so we have index it[1]
        # .contents "from the documentation" this can convert the html or... to a list of contents " bt7faz el content bta3 el div bta3i"
        # .text I just want the text inside the h2 without anything else and .strip to remove any spaces

        all_matches = championships.contents[3].find_all("div", {"class": "allData"})
        number_of_matches = len(all_matches)

        for i in range(number_of_matches):
            # get teams names
            team_A = all_matches[i].find("div", {"class": "teamA"}).text.strip()
            team_B = all_matches[i].find("div", {"class": "teamB"}).text.strip()

            # get score
            match_result = (
                all_matches[i]
                .find("div", {"class": "MResult"})
                .find_all("span", {"class": "score"})
            )
            # please note, the upper line will results in a list that contains " spans and 2 integers (please look at the script om the web page)"
            score = f"{match_result[0].text.strip()} - {match_result[1].text.strip()}"
            # get time
            time_lis = (
                all_matches[i]
                .find("div", {"class": "MResult"})
                .find_all("span", {"class": "time"})
            )
            time = time_lis[0].text.strip()

            Match_details.append(
                {
                    "Champion": championship_title,
                    "First Team": team_A,
                    "Second Team": team_B,
                    "Time": time,
                    "Score": score,
                }
            )

    for i in range(len(championships)):
        get_match_info(championships[i])

    keys = Match_details[0].keys()

    with open(
        "C:\\Users\\mgabi\\Desktop\\becode\\practcing outside\\Matchs_Web_Scraping\\matches_details.csv",
        "w",
        encoding="utf-8",
    ) as output_file:
        dict_writer = csv.DictWriter(output_file, keys)
        dict_writer.writeheader()  # read the documentation of csv module and its methods
        dict_writer.writerows(Match_details)
        print("file created")


main(page)
