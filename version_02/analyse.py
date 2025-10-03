from functions import *
from emotions import *

def analyse_sentence(sentence):
    """Функцию anylyse_sentence анализирует предложение введенное пользователем."""
    words = [w.replace(',', '').lower() if ',' in w else w.lower() for w in sentence.split()]
    
    words = [w.replace('.', '') if '.' in w else w for w in words]
    
    negative = 0; positive = 0
    for word in words:
        for em in get_emotions():
            if word in em:
                if get_emotions().get(em) == '😓':
                    negative += 1
                if get_emotions().get(em) == '🤗':
                    positive += 1
                    
    if negative > positive:
        negative_function()
    elif negative < positive:
        positive_function()
    elif negative == positive:
        normal_function()  
    else:
        normal_function()           
    