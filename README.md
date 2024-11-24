# Matches results scraping from Yalla Kora website
[![forthebadge made-with-python](https://ForTheBadge.com/images/badges/made-with-python.svg)](https://www.python.org/)

![coworking_img](https://media.istockphoto.com/id/1355225861/vector/soccer-scoreboard-background-match-team-template-design.jpg?s=612x612&w=0&k=20&c=X72GLWOlQRRtxN616RsT5ibx_TGvSZ_oiNLTvQ1yJHU=)

## 🏢 Description
This project is a Python script designed to scrape daily football match results and timings from [Yalla Kora](https://www.yallakora.com/). The script enables users to input a specific date in the format `YYYY-MM-DD` and retrieves the match details for that day, storing the results in a structured CSV file named `matches_details.csv`.

## Features
- **Dynamic Web Scraping**: Fetches match results and timings from Yalla Kora for a user-specified date.
- **User-Friendly Interface**: Prompts the user to enter a date to retrieve match data.
- **CSV Output**: Saves the extracted data in a well-organized CSV file (`matches_details.csv`) for further analysis or reporting.

## 🛎️ Usage
1. Clone the repository and navigate to the project directory.
2. Install the required modules as mentioned in the Requirements file.
3. Run the script `yalla_koora_scraping.py`.
4. Enter the desired date in the format `YYYY-MM-DD` when prompted.
5. The script will fetch the match details and save them in `matches_details.csv`.

```python

date = input("please enter the data you want in this formate YYYY-MM-DD: ")

page = requests.get(
    f"https://www.yallakora.com/match-center/Match-Center/?date={date}#"
)

        
```


## 📦 Repo structure

```
.
├── matches_details
├── yalla_koora_scraping.py
├──requirements.txt 
└── README.md
```
##  Future Improvements
1.More websites can be added to the code to cover most of sports.


## ⏱️ Timeline

This project took 1 hour and half  for completion.
 

Connect with me on [LinkedIn](https://www.linkedin.com/in/moustafa-gabil-8a4a6bab/).

