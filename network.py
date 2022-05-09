from requests import get, post
from requests.exceptions import HTTPError, ConnectionError, ConnectTimeout
from time import sleep
HOST = 'https://najlepszawgalaktyce.000webhostapp.com/chat/'


def messages_thread(root):
    while root.message_get:
        get_messages()
        sleep(2)


def get_messages():
    try:
        messages = get(HOST+'chat.json').json()
        print(messages)
    except (HTTPError, ConnectionError, ConnectTimeout) as e:
        print(f'Nie udało się pobrać wiadomości:  {e}')
