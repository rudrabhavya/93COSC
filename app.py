'''from PIL import Image
from gtts import gTTS
from pytesseract import image_to_string


def image_to_sound(path_to_image):
    """
    Function for converting an  image to sound
    """
    try:
        loaded_image = Image.open(path_to_image)
        decoded_text = image_to_string(loaded_image)
        cleaned_text = " ".join(decoded_text.split("\n"))
        print(cleaned_text)
        sound = gTTS(cleaned_text, lang="en")
        sound.save("sound.mp3")
        return True
    except Exception as bug:
        print("The bug thrown while excuting the code\n", bug)
        return


if __name__ == "__main__":
  sound_image("image.png")'''
from PIL import Image
#import pytesseract
from pytesseract import image_to_string
from gtts import gTTS
import os

def sound_image(path_to_image):
    try :
        load_image =  image_to_string(Image.open(path_to_image))
        gTTS(load_image,lang='en',tld='co.in').save('gene.mp3')
    except Exception as e:
        print("error : \t", e)

if __name__== "__main__":
    sound_image("image.png")
    
