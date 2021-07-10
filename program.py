from pytube import Playlist, YouTube
from multiprocessing import Pool
import os

# define o local em que os arquivos serão salvos
DOWNLOAD_PATH = './Downloads/'
PLAYLIST_NAME = ''

# define a quantidade de downloads que serão realiados em simultaneo
ACTIVE_THREAD_POOL = 10

# cria um objeto Playlist a partir da url e o retorna


def get_playlist() -> Playlist:
    # Buscando uma playlist com a lista de videos do NX Zero
    pl = Playlist("https://www.youtube.com/playlist?list=PLPwbRa5XTXhMQ_MHiOWqTISJhy1cgELp1")
    print(f'Numero de videos da playlist {pl.title}: {len(pl.video_urls)}')

    PLAYLIST_NAME = pl.title

    # NEW_PATH = DOWNLOAD_PATH + pl.title

    return pl
# recebe o objeto de um video contido no objeto Playlist e faz o download

def create_path():
    new_path  = DOWNLOAD_PATH + PLAYLIST_NAME
    if not os.path.exists(new_path):
        os.mkdir(new_path)


def download_video(video: YouTube):
    print(f'Baixando: {video.vid_info_url}')

    # seleciona os arquivos de audio com a melhor qualidade disponivel
    try:
        stream = video.streams.get_audio_only()
        # realiza o download
        stream.download(DOWNLOAD_PATH)
    except:
        print(f'Erro ao baixar {video.vid_info_url} {video.title}')


if __name__ == '__main__':
    # cria uma lista dos videos na Paylist
    playlist_videos = get_playlist().videos

    # cria a fila de execuções e a executa passando o objeto videos como parametro para a funcao de download
    with Pool(ACTIVE_THREAD_POOL) as p:

        p.map(download_video, playlist_videos)

    print('\\n FIM \\n')
