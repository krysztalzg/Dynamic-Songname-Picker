from clear_song_name import clear_song_name

from ctypes import *
import win32api
import win32con
import win32gui
import win32process
import pywintypes

class WinampAPI:
    class MlQueryStruct(Structure):
        pass

    class ItemRecordList(Structure):
        _fields_ = [("Items", c_void_p),
                    ("Size", c_int),
                    ("Alloc", c_int)]

    # main window IPC
    WM_WA_IPC = win32con.WM_USER
    # media library IPC
    WM_ML_IPC = WM_WA_IPC + 0x1000
    IPC_GET_PLAYING_TITLE = 3034

    def __init__(self):
        try:
            self.mainWindowHWND = self.find_window([("Winamp v1.x", None)])
        except pywintypes.error:
            raise RuntimeError("Cannot find Winamp windows. Is winamp started?")

        self.processID = win32process.GetWindowThreadProcessId(self.mainWindowHWND)[1]

        self.hProcess = windll.kernel32.OpenProcess(win32con.PROCESS_ALL_ACCESS, False, self.processID)

    def init_structures(self):
        try:
            self.MlQueryStruct._fields_ = [("query", c_char_p),
                                      ("max_results", c_int),
                                      ("itemRecordList", self.ItemRecordList)]
        except AttributeError:
            pass

    def find_window(self, window_list):
        current_window = None
        for i in range(len(window_list)):
            if current_window is None:
                current_window = win32gui.FindWindow(window_list[i][0], window_list[i][1])
            else:
                current_window = win32gui.FindWindowEx(current_window, 0, window_list[i][0], window_list[i][1])
        return current_window

    def send_user_message(self, w_param, l_param, hwnd=None):
        if hwnd is None:
            targetHWND = self.mainWindowHWND
        else:
            targetHWND = hwnd

        return win32api.SendMessage(targetHWND, self.WM_WA_IPC, w_param, l_param)

    def read_string_from_memory(self, address):
        bufferLength = win32con.MAX_PATH * 2
        buffer = create_unicode_buffer(bufferLength * 2)
        bytesRead = c_ulong(0)
        windll.kernel32.ReadProcessMemory(self.hProcess, address, buffer, bufferLength, byref(bytesRead))
        return buffer.value

    def get_current_playing_title(self):
        address = self.send_user_message(0, self.IPC_GET_PLAYING_TITLE)
        return self.read_string_from_memory(address)

    def get_current_song_name(self):
            return clear_song_name(self.get_current_playing_title())

