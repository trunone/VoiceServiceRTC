import android
import socket

droid = android.Android()
sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

def eventloop():
    while True:
        event=droid.eventWait().result
        print event
        if event["name"]=="click":
            id=event["data"]["id"]
            if id==4:
                return
            elif id=="recognize":
                speech = droid.recognizeSpeech().result
                droid.fullSetProperty("result","text",speech)
                sock.send(speech)
                sock.recv(4096)
            elif id=="forward":
                sock.send("go forward")
                sock.recv(4096)
            elif id=="backward":
                sock.send("go backward")
                sock.recv(4096)
            elif id=="right":
                sock.send("turn right")
                sock.recv(4096)
            elif id=="left":
                sock.send("turn left")
                sock.recv(4096)
            elif id=="stop":
                sock.send("stop")
                sock.recv(4096)
            elif id=="save":
                sock.send("save the target")
                sock.recv(4096)
            elif id=="go_to":
                sock.send("go to the target")
                sock.recv(4096)

        elif event["name"]=="screen":
            if event["data"]=="destroy":
                return

def main():
    with open ("layout.xml", "r") as layout_file:
        layout = layout_file.read().replace('\n', '')

    print 'Start connection'
    try:
        sock.connect(('192.168.3.168', 8080))
    except:
        droid.fullSetProperty("result","text","No connection")

    droid.fullShow(layout)
    eventloop()
    print droid.fullQuery()
    print "Data entered =",droid.fullQueryDetail("editText1").result
    droid.fullDismiss()

if __name__ == "__main__":
    main()
