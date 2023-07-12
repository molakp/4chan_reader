import poe
import json

TOKEN = 'BG_HV09HDR6rnpQyUqIpqA%3D%3D'

def summarize_text(text_to_summarize):

    client = poe.Client(token=TOKEN)
    print(json.dumps(client.bot_names, indent=2))
    #message = "Summarize the GNU GPL v3"
    response=""
    for chunk in client.send_message("textsummarizer1", text_to_summarize):
        print(chunk["text_new"], end="", flush=True)
        response=response + " " + chunk
    
    return response