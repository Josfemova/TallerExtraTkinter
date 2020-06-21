import vlc
#pip install python-vlc ---- biblioteca para manejo de sonido
#si usan python 32 bit deben instalar vlc 32 bit, lo mismo para 64 bit
current_ost=vlc.MediaPlayer()

def reproducir_ost(archivoMP3):
    reproductor = vlc.MediaPlayer(archivoMP3))
    Thread(target = reproductor.play, args=()).start()
    setCurrent_ost(reproductor)
    
def detener_ost():
    global current_ost
    if(isinstance(current_ost, vlc.MediaPlayer)):
        current_ost.stop()

def setCurrent_ost(reproductor):
    global current_ost
    current_ost= reproductor

