import os
import time
import _thread
import getpass


class SongNamePicker:
    music_services = ['dubtrack', 'plug.dj', 'winamp']
    current_song_name = ''
    previous_song_name = ''

    sleep_fatique = 0

    def __init__(self):
        os.environ["REQUESTS_CA_BUNDLE"] = 'cacert.pem'
        self.choice = 2

        if os.path.isfile('settings.data'):
            self.load_settings_from_file()
        else:
            self.prompt_user_settings()

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
            self.current_song_name = dubtrack_api.get_current_song_name(self)
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
            print('\tMusic picker by Krysztal [github.com/krysztalzg]\n'
                  '\tAktualnie wybrana usługa {}\n\n'
                  '\tWybierz usługe muzyczną:\n\t\t1. dutrack\n\t\t2. plugdj\n\t\t3. winamp'.
                  format(self.music_services[self.choice]))
            try:
                self.choice = int(input('>')) - 1
                if self.choice >= 3 or self.choice < 0:
                    self.choice = 2
            except:
                self.choice = 2

    def save_settings_to_file(self):
        with open('settings.data', 'w') as f:
            print('plugdj_email:{}\nplugdj_password:{}\nplugdj_room:{}\ndubtrack_room:{}\nchoice:{}'.format(
                self.plugdj_email, self.plugdj_password, self.plugdj_room, self.dubtrack_room, self.choice
            ), file=f)

    def load_settings_from_file(self):
        with open('settings.data', 'r') as f:
            self.plugdj_email = f.readline().replace('\n', '').split(':')[1]
            self.plugdj_password = f.readline().replace('\n', '').split(':')[1]
            self.plugdj_room = f.readline().replace('\n', '').split(':')[1]
            self.dubtrack_room = f.readline().replace('\n', '').split(':')[1]
            self.choice = int(f.readline().replace('\n', '').split(':')[1])

    def prompt_user_settings(self):
        self.plugdj_email = input('Plugdj email: ')
        self.plugdj_password = getpass.getpass('Plugdj password: ')
        self.plugdj_room = input('Plugdj room: ')
        self.dubtrack_room = input('Dubtrack room: ')
        self.save_settings_to_file()


picker = SongNamePicker()
