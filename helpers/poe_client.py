import poe
import json

TOKEN = 'BG_HV09HDR6rnpQyUqIpqA%3D%3D'


def censor_offensive_words(text):
    offensive_words = ['dick','pussy','nigger', 'kike','shit','fuck','fucking','shit','shitlib','nigger','niggers','nigga','cunt','bitch','jew' ]  # Aggiungi qui le parole offensive
    
    censored_text = text
    print(text)
    for word in offensive_words:
        censored_text = censored_text.replace(word, '*' * len(word))
    print("CESNORED    " + censored_text)
    return censored_text


def summarize_text(text_to_summarize):
    text_to_summarize=censor_offensive_words(text_to_summarize)
    client = poe.Client(token=TOKEN)
    print(json.dumps(client.bot_names, indent=2))
    #message = "Summarize the GNU GPL v3"
    response=""
    for chunk in client.send_message("textsummarizer1", text_to_summarize):
        print(chunk["text_new"], end="", flush=True)
        response = response + " " + chunk["text_new"]

    
    return response