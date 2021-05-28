from pytube import Playlist, YouTube
from multiprocessing import Pool

# define o local em que os arquivos serão salvos
DOWNLOAD_PATH = './Downloads/'

# define a quantidade de downloads que serão realiados em simultaneo
ACTIVE_THREAD_POOL =  10

# cria um objeto Playlist a partir da url e o retorna 
def get_playlist() -> Playlist:
    #Criando uma playlist com a lista de videos do NX Zero
    pl = Playlist('https://www.youtube.com/watch?v=XdglM81b4g8&list=PLPwbRa5XTXhMQ_MHiOWqTISJhy1cgELp1')

    print(f'Numero de videos na playlist: {len(pl.video_urls)}')

    return pl

# recebe o objeto de um video contido no objeto Playlist e faz o download
def download_video(video: YouTube) -> None:
    print(f'Baixando: {video.vid_info_url}')

    # seleciona os arquivos de audio com a melhor qualidade disponivel
    stream = video.streams.get_audio_only()

    # realza o download
    stream.download(DOWNLOAD_PATH)


if __name__ == '__main__':
    # cria uma lista dos videos na Paylist
    playlist_videos = get_playlist().videos
    
    # cria a fila de execuções e a executa passando o objeto videos como parametro para a funcao de download
    with Pool(ACTIVE_THREAD_POOL) as p:
        p.map(download_video, playlist_videos)

    print('\\n FIM \\n')
