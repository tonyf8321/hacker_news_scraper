import requests
from bs4 import BeautifulSoup
import pprint


def sort_stories_by_votes(hnlist):
    return sorted(hnlist, key=lambda k: k['votes'], reverse=True)


def create_custom_hn(links, subtext):
    hn = []
    pts_bigger_than = 99
    for idx, item in enumerate(links):
        title = item.getText()
        href = item.get('href', None)
        vote = subtext[idx].select('.score')
        if len(vote):
            points = int(vote[0].getText().replace(' points', ''))
            if points > pts_bigger_than:
                hn.append({'title': title, 'link': href, 'votes': points})
    return sort_stories_by_votes(hn)


def get_hacker_news(pages):
    pages_to_get = pages
    mega_list = []
    for page_num in range(1, pages_to_get + 1):
        if page_num == 1:
            res = requests.get('https://news.ycombinator.com/news')
            soup = BeautifulSoup(res.text, 'html.parser')
            sel_links = soup.select('.storylink')
            sel_subtext = soup.select('.subtext')
            mega_list.extend(create_custom_hn(sel_links, sel_subtext))
        else:
            res = requests.get(
                f'https://news.ycombinator.com/news?p={page_num}')
            soup = BeautifulSoup(res.text, 'html.parser')
            sel_links = soup.select('.storylink')
            sel_subtext = soup.select('.subtext')
            mega_list.extend(create_custom_hn(sel_links, sel_subtext))
    return sort_stories_by_votes(mega_list)


def main():
    pprint.pprint(get_hacker_news(4))


if __name__ == '__main__':
    main()
