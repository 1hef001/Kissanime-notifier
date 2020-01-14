import cloudscraper
from bs4 import BeautifulSoup


def get_url(url):
    scraper = cloudscraper.create_scraper()
    resp = scraper.get(url)
    if (scraper.get(url).status_code < 400):
        return resp.text
    else:
        print('Server refused to connect')


def get_links(url, content):
    '''
    Scrape all links in the website and return true links from main page or
    relative links from current page
    '''


    soup = BeautifulSoup(content, "lxml")
    links = list()
    for link in soup.findAll('a'):
        if(link.get('href').startswith('/')):
            links.append(link.get('href'))
            continue
        # links.append(link.get('href'))
    return links



def list_titles(links = []):
    '''
    Get all the titles with class bigChar
    '''
    titles = []
    for link in links:
        if '/Anime' in link:
            link = link.replace('/Anime/','')
            if '/' in link:
                pass
            else:
                titles.append(link)

   

    return titles

def list_genres(links=[]):
    '''
    The list of links are surfed through
    and the substring genre is found out for classification
    '''


    genres = []
    for link in links:
        if '/Genre/' in link:
            link = link.replace("/Genre/","")
            genres.append(link)

    return genres



if __name__ == '__main__':
    URL = "https://kissanime.ru/AnimeList/MostPopular"
    d_link = get_links(URL,get_url(URL))
    # print(list_genres(d_link))
    print(list_titles(d_link))

