from downloader import download_media
from gui import start_gui
import threading

def start_download_callback(playlist_url, download_type, resolution, log_callback, stop_flag):
    output_folder = 'downloads'
    download_media(playlist_url, output_folder, download_type, resolution, log_callback, stop_flag)

if __name__ == "__main__":
    threading.Thread(target=start_gui, args=(start_download_callback,)).start()
