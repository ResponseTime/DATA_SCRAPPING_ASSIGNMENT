from bs4 import BeautifulSoup as soup
import requests


if __name__ == "__main__":
    data = requests.get(
        "https://docs.google.com/spreadsheets/d/1MdErotSQunkqyDCjLva3ILExp-UL2RVhNWzybBCqjdI/edit#gid=1046942027")
    data = soup(data.text, "html.parser")
    d = data.find_all("tr")
    for i in d:
        dat = i.text.split(",")
        d = "".join([i for i in dat[0] if i.isalpha() or i.isspace()])
        print(
            f'College Name is {d} Address is {"".join(dat[1:]).replace(" ", " ")}')
