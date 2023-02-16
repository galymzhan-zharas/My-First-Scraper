import requests
from bs4 import BeautifulSoup
# get the HTML of a webpage
# locate the data 
# extract the data 

# request 
# extract 
# transform 
# format and return CSV 

#returns a response object
def request_github_trending(url): 
    return requests.get(url)


def extract(page):
    #creates a Beatiful Soup object, representing the html page as a nested structure 
    soup = BeautifulSoup(page, "html.parser")
    #returns an array 
    return soup.find_all("article")

def transform(html_repos):
    arrayOfhash = []
    for row in html_repos:
        repository_name = "".join(row.select_one("h1.h3.lh-condensed").text.split())
        developerName = row.select_one("img.avatar.mb-1.avatar-user")['alt']
        nbr_stars = " ".join(row.select_one("span.d-inline-block.float-sm-right").text.split())
        arrayOfhash.append({'developer':developerName, 'repository_name': repository_name, 'nbr_stars': nbr_stars})
    return arrayOfhash

def format(repositories_data): 
    array = ["Developer, Repository Name, Number of Stars"]
    for dictionary in repositories_data:
        developerName = dictionary.get("developer")
        repository_name = dictionary.get("repository_name")
        numOfstars = dictionary.get("nbr_stars")
        row = developerName + ", " + repository_name + ", " + numOfstars
        array.append(row)
    formatted_string = "\n".join(array)
    return formatted_string


