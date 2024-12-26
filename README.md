# YouTube Downloader GUI
![image](https://github.com/user-attachments/assets/570e7340-9754-4338-8770-9168738d5de5)

This project is a Python-based GUI application for downloading YouTube videos and audio. It uses `yt-dlp` for downloading and provides a simple interface for users to interact with. You can choose to download audio or video files in different resolutions and formats.

## Features

- Download audio and video from YouTube playlists.
- Choose between audio (MP3) and video (MP4) formats.
- Select video resolution (480p, 720p, 1080p).
- Real-time logging of the download process.
- Flask and SocketIO integration for real-time updates (optional).

## Prerequisites

Before you run the program, you need to install the following dependencies:

- Python 3.x (preferably 3.13.1 or higher)
- `yt-dlp` for downloading YouTube videos and audio.
- `Flask` and `SocketIO` for server integration (optional).

### Installation Instructions

1. **Clone the repository**:

    ```bash
    git clone https://github.com/Asadullah-nadeem/YouTube-Downloader-GUI.git
    cd YouTube-Downloader-GUI
    ```

2. **Install dependencies**:

    You can install all required dependencies via `pip`. Run the following command in your terminal:

    ```bash
    pip install -r requirements.txt
    ```

    If `requirements.txt` does not exist, run the following:

    ```bash
    pip install yt-dlp Flask python-socketio
    ```

To integrate the steps you provided into a comprehensive guide for installing and configuring FFmpeg for `yt-dlp`, here's how you can include it in your README or instructions:

---

### 3. **Ensure `ffmpeg` is installed**:

`yt-dlp` uses `ffmpeg` for processing video and audio files. Follow the steps below to install and configure FFmpeg on your system:

#### Step-by-Step Installation Guide for FFmpeg on Windows:

1. **Download FFmpeg**:
   - Go to the official FFmpeg builds site: [https://www.gyan.dev/ffmpeg/builds/](https://www.gyan.dev/ffmpeg/builds/).
   - Under **"Windows Builds"**, download the latest **"ffmpeg-release-essentials.zip"** file.

2. **Extract FFmpeg**:
   - Extract the ZIP file to a folder on your system, such as `C:\ffmpeg`.
   - After extraction, the `C:\ffmpeg` folder will contain subfolders like `bin`, `doc`, and `presets`.

3. **Add FFmpeg to System PATH**:
   - Press `Win + R`, type `sysdm.cpl`, and press Enter to open **System Properties**.
   - Go to the **Advanced** tab and click on **Environment Variables**.
   - Under **System Variables**, find the variable **Path** and click **Edit**.
   - Click **New** and add the path to the `bin` folder of your extracted FFmpeg directory (e.g., `C:\ffmpeg\bin`).
   - Click **OK** to close all dialogs.

4. **Verify FFmpeg Installation**:
   - Open a new **Command Prompt** or **terminal**.
   - Run the following command:
     ```bash
     ffmpeg -version
     ```
   - You should see the FFmpeg version details. This confirms that FFmpeg is installed correctly.



#### Alternative Installation (Using Chocolatey):

If you're using Windows and have **Chocolatey** installed, you can install FFmpeg via the following command:

```bash
choco install ffmpeg
```

#### Configure `yt-dlp` with FFmpeg:

Once FFmpeg is installed and added to your system's PATH, you need to specify the location of FFmpeg in `yt-dlp`. Here’s how to do that:

- **Specify the `ffmpeg_location` in your `yt-dlp` options**:
  
  Replace `C:\ffmpeg\bin` with the correct path where you extracted FFmpeg. Ensure that the folder contains both `ffmpeg.exe` and `ffprobe.exe`.

  For example:

  ```python
  ydl_opts = {
      'ffmpeg_location': r'C:\ffmpeg\bin',  # Update this path
  }
  ```

#### Verify Your FFmpeg Installation:

Confirm that the following files exist in your `ffmpeg\bin` folder:

```bash
C:\ffmpeg\bin\ffmpeg.exe
C:\ffmpeg\bin\ffprobe.exe
```

If both files are present, FFmpeg is installed and ready to be used with `yt-dlp`.

---

This will ensure that FFmpeg is installed, configured, and ready to be used by `yt-dlp` for processing videos and audio files.

4. **Directory Structure**:

    The project folder should look like this:

    ```
    YouTube-Downloader-GUI/
    ├── main.py          # Main Python script to run the app
    ├── downloader.py    # Contains the download logic and GUI
    ├── requirements.txt # List of Python dependencies
    ├── README.md        # This file
    └── downloads/        # Folder where downloaded videos will be saved
    ```

## How to Use

1. **Run the application**:

    To start the YouTube downloader GUI, run the `main.py` script:

    ```bash
    python main.py
    ```

2. **Using the GUI**:

    Once the application is running, you will see a GUI window with the following options:

    - **Paste Playlist URL**: Enter the YouTube playlist URL that you want to download.
    - **Audio/Video Selection**: Choose whether you want to download audio (MP3) or video (MP4).
    - **Resolution (only for video)**: If downloading a video, select the desired resolution (480p, 720p, or 1080p).
    - **Download**: Click the 'Download' button to start the download.

3. **Monitoring the progress**:

    As the download progresses, the log section of the GUI will display real-time status updates, such as downloading specific videos and showing any warnings or errors that occur.

4. **Stopping the download**:

    You can stop the download process by clicking the 'Stop' button. This will immediately halt any ongoing downloads.

## Troubleshooting

- If you encounter issues related to missing dependencies, make sure all required libraries are installed using `pip`.
- If `ffmpeg` is not found, verify that it is properly installed and added to your system's PATH.



