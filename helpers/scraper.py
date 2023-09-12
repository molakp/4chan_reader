import requests
from bs4 import BeautifulSoup
from helpers.cors import get_image_from_url
from helpers.poe_client import *
import re

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
            thread['image'] = get_image_from_url("https:" + thread_image) #https://i.4cdn.org/pol/1689142797200819s.jpg
            #thread['image'] = thread_image

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
    thread_details['thread_url'] = thread_url

    # Find all the blockquote elements with class 'postMessage'
    blocks = soup.find_all('blockquote', class_='postMessage')
    conversation = ""
    # Extract the text content from each blockquote element
    for block in blocks:
        text = block.get_text(strip=True)
        cleaned_text = re.sub(r'[^a-zA-Z\s]|(\d+)', '', text)
        conversation = text #conversation + " " + cleaned_text

    # HERE SUMMARIZATION OF THREAD
    thread_details['conversation'] = conversation 
    #summarize_text(conversation[:10000])
    # Definisci replies_divs come una lista vuota all'inizio
    replies_divs = []
    for div in soup.select("div.postContainer.replyContainer"):
        # Codice per ottenere le risposte ai thread
        # Codice per ottenere le risposte ai thread
        replies_divs.extend(div.select('.post.reply'))  # Aggiungi le risposte trovate alla lista


    if replies_divs:
        thread_details['replies'] = []  # Crea una lista per memorizzare le risposte

        for reply_div in replies_divs:
            reply = {}
            # Estrai le informazioni da ciascun post di risposta e aggiungile all'oggetto reply
            # Ad esempio, puoi estrarre il nome, l'ID, il testo del messaggio, ecc.
            reply['name'] = reply_div.select_one('.name').text.strip()
            reply['post_id'] = reply_div.select_one('.postNum a').text.strip()
            br_tags= reply_div.select_one('.postMessage').find_all('br')
            
            print(br_tags)
           
            text = [tag.next_sibling.strip() for tag in br_tags]
            reply['message'] = text
           
            #reply_image = div.select_one('.fileThumb').find('img')['src']
            reply_image_element = div.select_one('.fileThumb')
            if reply_image_element is not None:
                reply_image = reply_image_element.find('img')['src']
                reply['image'] = get_image_from_url("https:" + reply_image)
            else:
                reply_image = None  # o un valore predefinito a tua scelta
                

            thread_details['replies'].append(reply)  # Aggiungi la risposta alla lista delle risposte del thread
            #print(reply)
    return thread_details

