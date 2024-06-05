import yt_dlp
import os
import webbrowser

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

    # Execute download
    try:
        # Download video using yt-dlp
        output_template = os.path.join(folder, '%(title)s.%(ext)s')
        ydl_opts = {
            'format': 'bestvideo[ext=mp4]+bestaudio[ext=m4a]/best[ext=mp4]/best',
            'outtmpl': output_template,
            'quiet': True,  # yt-dlpのログを非表示にする
        }
        with yt_dlp.YoutubeDL(ydl_opts) as ydl:
            info = ydl.extract_info(url, download=True)
            file_name = info['title']
            print("Success. Convert mp4 to mp3 ==> https://convertio.co/ja/mp4-mp3/")
    except Exception as e:
        print(f"An error occurred: {e}")

if __name__ == "__main__":
    main()
