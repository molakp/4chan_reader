import requests
from io import BytesIO
from PIL import Image
import base64


def get_image_from_url(url):
    # Esegui la richiesta HTTP utilizzando il server proxy o l'applicazione backend
    
    response = requests.get(url)
    try:
        if response.status_code == 200:
            # Ottieni il contenuto dell'immagine come byte
            image_data = response.content

            # Crea un oggetto immagine utilizzando i byte dell'immagine
            image = Image.open(BytesIO(image_data))
            
            # Converti l'oggetto Image in una stringa Base64
            image_base64 = base64.b64encode(image_data).decode('utf-8')

            #print("Image Data: " + image_base64)

            return image_base64
        
        elif response.status_code == 404:
                print(f"L'immagine all'URL {url} non è stata trovata.")
    
    except Exception as e:
        print(f"Errore nel recupero dell'immagine: {str(e)}")

    return None
