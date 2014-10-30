import android

import socket
from contextlib import closing

android_port = 5000
android_backlog = 10
android_bufsize = 4096

sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
sock.bind( ( '', android_port ) )
sock.listen( android_backlog )

if __name__ == '__main__':

    droid = android.Android()
    while True:
        client, address = sock.accept()
        msg = client.recv( android_bufsize )

        if msg == 'recognize':
            speech = droid.recognizeSpeech().result

            if speech == None:
                speech = 'None'

            client.send( speech )

        elif msg == 'terminate':
            break

        else:
            droid.ttsSpeak( msg )




