import PySimpleGUI as sg
import yt_dlp
from pydub import AudioSegment
import os

# テーマとフォントの設定
sg.theme('DarkBlue')
sg.set_options(font=("Yu Gothic UI", 12))

def convert_to_mp3(video_path):
    audio_output_path = video_path.replace('.mp4', '.mp3')
    AudioSegment.from_file(video_path).export(audio_output_path, format="mp3")
    return audio_output_path

def download_video(url, folder, convert):
    output_template = os.path.join(folder, '%(title)s.%(ext)s')
    ydl_opts = {
        'format': 'bestvideo+bestaudio/best',
        'outtmpl': output_template,
        'merge_output_format': 'mp4',
    }
    with yt_dlp.YoutubeDL(ydl_opts) as ydl:
        info = ydl.extract_info(url, download=True)
        video_path = output_template.replace('%(title)s', info['title']).replace('%(ext)s', 'mp4')
        return convert_to_mp3(video_path) if convert else video_path

layout = [
    [sg.Text("URLを入力してください:")],
    [sg.InputText(key='-URL-')],
    [sg.Text("保存先を選択してください:")],
    [sg.FolderBrowse("保存先", key='-FOLDER-', target='-FOLDER_INPUT-'), sg.InputText(key='-FOLDER_INPUT-')],
    [sg.Checkbox('音声に変換', key='-CONVERT-', default=False)],
    [sg.Button('ダウンロード'), sg.Button('終了')],
    [sg.Text("", size=(40, 1), key='-STATUS-')]
]

window = sg.Window("Internet Downloader", layout, size=(500, 250))

while True:
    event, values = window.read()
    if event in (sg.WIN_CLOSED, '終了'):
        break
    if event == 'ダウンロード':
        url, folder, convert = values['-URL-'], values['-FOLDER_INPUT-'], values['-CONVERT-']
        if not url or not folder:
            window['-STATUS-'].update("URLと保存先を入力してください")
            continue
        try:
            result_path = download_video(url, folder, convert)
            if convert:
                window['-STATUS-'].update("ダウンロードと音声への変換が完了しました")
            else:
                window['-STATUS-'].update("ダウンロードが完了しました")
        except Exception as e:
            window['-STATUS-'].update(f"エラーが発生しました: {e}")

window.close()
