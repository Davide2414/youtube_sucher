import pytchat, time, os, random, pynput
keyboard = pynput.keyboard.Controller()
def main():
    countdown()
    chatread()


def countdown():
    countdown = 5
    for number in range(countdown):
        print(number)
        time.sleep(0.7)


def chatread():
    e=0
    active_time = time.strftime('%H:%M:%S')
    chat = pytchat.create(video_id="jfKfPfyJRdk")
    while chat.is_alive:
        try:
            for comment in chat.get().sync_items():
                time_msg = comment.datetime.partition(' ')[2]
                if time_msg >= active_time:
                    name = comment.author.name
                    msg = comment.message.upper()
                    analisi(msg)
                    file = "C:/Users\hp\Desktop/full/self_mosco/lab/name.ili"
                    with open(file,'w') as frocio:
                        try:
                            frocio.write(name)
                        except:
                            e+=1
                            print (e,"errore nel nome", name)
                            name = ''.join(char for char in name if char.isascii())
                            if name == "" or name == " ":
                                frocio.write("Utente Frocio")
                            else:
                                try:
                                    frocio.write(name)
                                    print (name, "inserito")
                                except:
                                    print("errore non risolto", name)
                    #keyboard commands based on comments down here
                    #salva i nomi della gente che ha scritto in un file ini
                    #!up W !down S !left A !right D !action E
        except:
            print("messaggio o utente non valido")


def analisi(message):
    porcodio = random.randint(0,1)
    if porcodio == 0:
        if '!up' in message.lower():
            print("W")
            keyboard.press('w')
        if '!down' in message.lower():
            print("S")
            keyboard.press('w')
        if '!left' in message.lower():
            print("A")
            keyboard.press('a')
        if '!right' in message.lower():
            print("D")
            keyboard.press('d')
        if '!action' in message.lower():
            print("E")
            keyboard.press('e')



if __name__ == "__main__":
    main()