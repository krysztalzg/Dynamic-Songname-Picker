import os
import time
import _thread


class SongNamePicker:
    music_services = ['dubtrack', 'plug.dj', 'winamp']
    choice = 2
    current_song_name = ''
    previous_song_name = ''

    sleep_fatique = 0

    plugdj_email = ''
    plugdj_password = ''
    plugdj_room = ''

    def __init__(self):
        os.environ["REQUESTS_CA_BUNDLE"] = 'cacert.pem'
        _thread.start_new_thread(self.service_choice, ())

        while True:
            self.get_current_song_name()
            if self.current_song_name != self.previous_song_name:
                with open('song_name.txt', 'w') as f:
                    print(self.current_song_name, file=f)
                self.previous_song_name = self.current_song_name
            time.sleep(1 + self.sleep_fatique)

    def get_current_song_name(self):
        self.sleep_fatique = 0
        if self.choice == 0:
            import dubtrack_api
            self.current_song_name = dubtrack_api.get_current_song_name()
        elif self.choice == 1:
            import plugdj_api
            self.current_song_name = plugdj_api.get_current_song_name(self)
            self.sleep_fatique = 4
        else:
            import winamp_api
            self.current_song_name = winamp_api.WinampAPI().get_current_song_name()

    def service_choice(self):
        while True:
            os.system('cls' if os.name == 'nt' else 'clear')
            print('\tMusic picker by Krysztal [github.com/krysztalzg]'.format(self.music_services[self.choice]))
            print('\n\tAktualnie wybrana usługa {} '.format(self.music_services[self.choice]))
            print('\n\n\tWybierz usługe muzyczną:\n\t\t1. dutrack\n\t\t2. plugdj\n\t\t3. winamp')
            try:
                self.choice = int(input('>')) - 1
                if self.choice >= 3 or self.choice < 0:
                    self.choice = 2
            except:
                self.choice = 2

picker = SongNamePicker()
