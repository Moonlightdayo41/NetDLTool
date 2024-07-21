import yt_dlp
import os
import webbrowser

# Function to display progress
def progress_hook(d):
    if d['status'] == 'downloading':
        print(f"Downloading: {d['_percent_str']} at {d['_speed_str']} ETA: {d['_eta_str']}")

# Display menu
def show_menu():
    print("""
1. Download mp4
""")

# Main function
def main():
    show_menu()

    url = input("Enter URL: ")
    folder = input("Destination Directory: ")

    # Set default download folder if none is provided
    if not folder:
        folder = os.path.join(os.path.expanduser("~"), "Downloads")

    # Execute download
    try:
        # Download video using yt-dlp
        output_template = os.path.join(folder, '%(title)s.%(ext)s')
        ydl_opts = {
            'format': 'bestvideo[ext=mp4]+bestaudio[ext=m4a]/best[ext=mp4]/best',
            'outtmpl': output_template,
            'progress_hooks': [progress_hook],  # 進行状況を表示するフック
            'extractor_args': {'youtube': {'player_client': ['web']}}  # APIの問題回避
        }
        with yt_dlp.YoutubeDL(ydl_opts) as ydl:
            info = ydl.extract_info(url, download=True)
            file_name = info['title']
            print("Success. Convert mp4 to mp3 ==> https://convertio.co/ja/mp4-mp3/")
    except Exception as e:
        print(f"An error occurred: {e}")

if __name__ == "__main__":
    main()
