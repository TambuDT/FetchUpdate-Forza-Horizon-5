from asyncio.windows_events import NULL
import bs4, requests, webbrowser, notifypy, time



LINKUPDATE = "https://www.skidrowcodex.net/forza-horizon-5-crackfix-codex/"
HEADERS = {
        'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/99.0.4844.51 Safari/537.36 Edg/99.0.1150.30'
    }
with open('versioneGioco.txt', 'r') as file:
        versione = file.read().rstrip()
        file.close()
    #print(versione)

def searchUpdate():
    richiestaHTTP0 = requests.get(LINKUPDATE, headers=HEADERS)
    soup0 = bs4.BeautifulSoup(richiestaHTTP0.text, 'html.parser')
    ul_links=soup0.find('ul', class_='lcp_catlist')
    a_links=ul_links.find_all('a')
    link_updates=[]
    for a_link in a_links:
        link_update = str(a_link.getText())
        link_updates.append(link_update)
    last_update=link_updates[0]
    current_update=last_update[24:33]
    #print(current_update)
    return current_update
   


def updateFound():
    current_update=searchUpdate()
    notifica=notifypy.Notify()
    notifica.title = "Aggiornamento Forza Horizon 5"
    notifica.message = "Nuovo aggiornamento versione: "+str(current_update)+""
    notifica.application_name = "Software Update Forza Horizon 5"
    notifica.icon="icona.ico"
    notifica.send()

    richiestaHTTP1 = requests.get(LINKUPDATE, headers=HEADERS)
    soup1 = bs4.BeautifulSoup(richiestaHTTP1.text, 'html.parser')
    ul_links=soup1.find('ul', class_='lcp_catlist')
    a_links=ul_links.find_all('a')
    link_updates=[]
    for a_link in a_links:
        link_update = str(a_link.get('href'))
        link_updates.append(link_update)

    last_update=link_updates[0]
    #print(last_update)

    
    richiestaHTTP2 = requests.get(last_update, headers=HEADERS)
    soup2 = bs4.BeautifulSoup(richiestaHTTP2.text, 'html.parser')
    link_downlaod=soup2.find('links')
    a_filecrypt=link_downlaod.find_all('a')
    links_filecrypt_list=[]
    for a_link in a_filecrypt:
        link_filecrypty = str(a_link.get('href'))
        links_filecrypt_list.append(link_filecrypty)
    #print(links_filecrypt_list[0])
    current_filecrypt_link=links_filecrypt_list[0]
    time.sleep(3)
    webbrowser.open(current_filecrypt_link)
    f = open("versioneGioco.txt", "w")
    f.write(current_update)
    f.close()


#def no_update():
    #notifica=notifypy.Notify()
    #notifica.title = "Controllo Giornaliero Aggiornamenti Forza Horizon 5"
    #notifica.message = "Hai già la versione più recente "+str(versione)+""
    #notifica.application_name = "Ricerca Aggiornamenti Forza"
    #notifica.icon="icona.ico"
    #notifica.audio="sound.wav"
    #notifica.send()


current_version=searchUpdate()
time.sleep(4)
if versione!=current_version:
    updateFound()
else: NULL