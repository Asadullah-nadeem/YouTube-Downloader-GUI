import threading
from tkinter import Tk, Label, Button, Entry, Text, Scrollbar, Radiobutton, IntVar, END, Frame

def start_gui(start_download_callback):
    download_thread = None  # Global variable to hold the download thread
    stop_flag = threading.Event()  # Event to signal stopping the thread

    def start_download():
        nonlocal download_thread
        stop_flag.clear()  # Clear the stop flag before starting
        url = url_entry.get()
        download_type = 'audio' if download_choice.get() == 1 else 'video'
        resolution = resolution_choice.get() if download_type == 'video' else None
        log_callback = lambda message: update_log(message)

        # Start download in a separate thread
        download_thread = threading.Thread(target=start_download_callback, args=(url, download_type, resolution, log_callback, stop_flag))
        download_thread.start()

    def stop_download():
        stop_flag.set()  # Signal the thread to stop
        if download_thread and download_thread.is_alive():
            update_log("Stopping download...")
        else:
            update_log("No active download to stop.")

    def update_log(message):
        log_area.insert(END, message + "\n")
        log_area.see(END)

    # GUI Layout
    root = Tk()
    root.title("YouTube Downloader")

    # Input Frame
    input_frame = Frame(root)
    input_frame.pack(padx=10, pady=10)

    Label(input_frame, text="Paste Playlist URL:").grid(row=0, column=0, padx=5, pady=5)
    url_entry = Entry(input_frame, width=50)
    url_entry.grid(row=0, column=1, padx=5, pady=5)

    # Download Type Selection
    download_choice = IntVar(value=1)
    Radiobutton(input_frame, text="Audio", variable=download_choice, value=1).grid(row=1, column=0, padx=5, pady=5)
    Radiobutton(input_frame, text="Video", variable=download_choice, value=2).grid(row=1, column=1, padx=5, pady=5)

    # Resolution Selection (only for video)
    resolution_choice = IntVar(value=720)  # Default resolution
    resolution_frame = Frame(root)
    resolution_frame.pack(padx=10, pady=5)

    Label(resolution_frame, text="Select Video Resolution:").pack(anchor='w', padx=5)
    Radiobutton(resolution_frame, text="480p", variable=resolution_choice, value=480).pack(anchor='w')
    Radiobutton(resolution_frame, text="720p", variable=resolution_choice, value=720).pack(anchor='w')
    Radiobutton(resolution_frame, text="1080p", variable=resolution_choice, value=1080).pack(anchor='w')

    # Download and Stop Buttons
    Button(input_frame, text="Download", command=start_download).grid(row=2, column=0, padx=5, pady=10)
    Button(input_frame, text="Stop", command=stop_download).grid(row=2, column=1, padx=5, pady=10)

    # Log Area
    log_frame = Frame(root)
    log_frame.pack(padx=10, pady=10, fill='both', expand=True)

    Label(log_frame, text="Log:").pack(anchor='w', padx=5)
    log_area = Text(log_frame, wrap='word', height=20, state='normal')
    log_area.pack(side='left', fill='both', expand=True)

    scrollbar = Scrollbar(log_frame, command=log_area.yview)
    scrollbar.pack(side='right', fill='y')
    log_area['yscrollcommand'] = scrollbar.set

    root.mainloop()
