import eel

eel.init("web")

@eel.expose
def check(data: str) -> str:
    correct = ['therewasawoodbefore', 'beforetherewasawood', 'itwasahugevalley', 'therewasahugevalley', 'avalleywasahuge', 'therewasnotanyhill', 'therewasnotahill', 'therewasnothill', 'therewasntanyhill', 'therewasntahill', 'therewasnthill']
    output = 'Great!'
    
    data = data.lower
    #data = data.replace(' ', '')
    #data = data.replace('.', '')
    #data = data.replace("'", '')
    #data = data.replace('`', '')
    if data not in correct:
        output = 'Uncorrectly. Try again.'
    return output




eel.start('main.html', size = (800, 800))