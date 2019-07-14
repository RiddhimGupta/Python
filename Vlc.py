import vlc

media = vlc.MediaPlayer("a.mp4")

while True:

    media.play()

    while True:

        keypress = input()

#play and pause
        if keypress == "p":

            if media.play()==0:

                media.pause()

            else:

                media.play()

#mute and unmute
        if keypress == "v":

            if media.audio_get_volume()==0:

                media.audio_set_volume(100)

            else:

                media.audio_set_volume(0)

#forward
        if keypress == "f":

            z=media.get_position()

            print(z)
            q=z+0.15

            if(q<0.80):

                media.set_position(q)

            else:

                media.set_position(0.80)
#backward

        if keypress == "b":

            z=media.get_position()

            q=z-0.15
            if(q>0.00):

                media.set_position(q)

            else:

                media.set_position(0.00)

#stop
        if keypress == "s":

            media.stop()

        if keypress == "q":

            break

    break
