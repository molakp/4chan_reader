import requests
from bs4 import BeautifulSoup

def get_soup(url):
    response = requests.get(url)
    soup = BeautifulSoup(response.content, 'html.parser')
    return soup

def get_threads(board_url):
    soup = get_soup(board_url)
    thread_divs = soup.select('div.thread')
    threads = []

    for div in thread_divs:
        thread = {}
        title_div = div.select_one('.postContainer.opContainer .postInfo.desktop .subject')

        if title_div:
            thread['title'] = title_div.text.strip()
        link = div.select_one('a[href^="//boards.4chan.org"]')
        if link:
            thread['url'] = link.get('href')
            thread['title'] = link.text.strip()

        thumb = div.select_one('.thumb')
        if thumb and 'src' in thumb.attrs:
            thread['image_url'] = thumb['src']

        meta = div.select_one('.meta')
        if meta:
            reply_count = meta.select_one('b')
            if reply_count:
                thread['reply_count'] = reply_count.text.strip()

        teaser = div.select_one('.teaser')
        if teaser:
            thread['teaser'] = teaser.text.strip()


        thread['id'] = div['id'][1:]  # Remove the leading 't' from the ID
        message =  div.select_one('.postContainer.opContainer .postMessage')
        if message:
            thread['message'] = message.text.strip()
            
        thread_image = div.select_one('.fileThumb').find('img')['src']
        if thread_image:
            thread['image'] = thread_image

        threads.append(thread)

    return threads



def get_thread_details(board_url, thread_id):
    thread_url = f'https://boards.4chan.org/{board_url}/thread/{thread_id}'
    soup = get_soup(thread_url)
    thread_details = {}
    thread_details['id'] = thread_id
    thread_details['title'] = soup.find('span', class_='subject').get_text(strip=True)
    post_message_div = soup.find('blockquote', class_='postMessage')
    thread_details['content'] = post_message_div.get_text(strip=True) if post_message_div else ''
    return thread_details

