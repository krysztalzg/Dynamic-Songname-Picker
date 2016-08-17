import requests
import json

from clear_song_name import clear_song_name

# TODO:
#   Login and room joining error handling


def get_current_song_name(music_picker):
    with requests.session() as s:
        r = s.get('https://plug.dj/')
        try:
            csrf = r.text.split('_csrf="')[1].split("\"")[0]
            # print("CSRF: " + csrf)

            r = s.post('https://plug.dj/_/auth/login', json={'csrf': csrf, 'email': music_picker.plugdj_email, 'password': music_picker.plugdj_password})
            # print("Login: \n" + r.text)

            r = s.post('https://plug.dj/_/rooms/join', json={'slug': music_picker.plugdj_room})
            # print("RoomJoin: \n" + r.text)

            r = s.get('https://plug.dj/_/rooms/state')

            response = json.loads(r.text)['data'][0]['playback']['media']
            current_song = '{} - {}'.format(response['author'], response['title'])
            return clear_song_name(current_song)
        except:
            return ''
