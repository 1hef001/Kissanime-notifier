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


def list_anime_uri(links = []):
    '''
    Get all the link with class bigChar
    '''
    urls = []
    for link in links:
        if '/Anime/' in link:
            urls.append(link)
    
    return urls


def list_titles(links = []):
    '''
    Get all the titles with class bigChar
    '''
    titles = []
    for link in links:
        if '/Anime/' in link:
            link = link.replace('/Anime/','')
            link = link.replace('-',' ')
            if '/' in link:
                pass
            else:
                titles.append(link)

   

    return titles

def list_genres(links = []):
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

def get_desc(url, links = []):
    '''
    Get description of Anime from list
    '''


    
    desc = []
    txt = ''
    l = ''
    
    for link in links:

        l = url + link
        soup = BeautifulSoup(get_url(l), 'lxml')
        txt = soup.find('p',{'style':'text-align: justify;'}).get_text()
        desc.append(txt)

    return desc





if __name__ == '__main__':
    URL = "https://kissanime.ru/AnimeList/MostPopular"
    d_link = get_links(URL,get_url(URL))
    # print(list_genres(d_link))
    # print(list_titles(d_link))
    a_link = list_anime_uri(d_link)
    print(get_desc("https://kissanime.ru", a_link))

