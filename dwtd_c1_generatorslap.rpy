init:
    find label _call_skiptut_3:
        search say "Shh, be quiet. I'll let you know more as soon as I can. But for now, let's just play along. After all, we already have one of these babies." as dwtd_c1_stopslap_linknode
        search say "God knows we need them."
        callto label dwtd_c1_stopslap from dwtd_c1_stopslap_linknode return here

label dwtd_c1_stopslap:
    m "Reza lifted his hand, seemingly to give the generator a light pat."

    if dwtd.check_keypoint():
        call screen dwtd_qte("Stop him.")
    else:
        play sound "fx/system3.wav"
        s "This timeline is hardcore, pal. You can't reload to fix this."
        $ _return = False
    if not _return:
        $ dwtd.will_die()
        $ renpy.pop_call()
        stop music fadeout 1.0
        play sound "fx/beeps2.ogg"
        $ renpy.pause (0.3)
        play sound "fx/explosion.ogg"
        scene black with Shake ((0, 0, 0, 0), 3.0, dist=50)
        $ renpy.pause (4.0)
        scene dwtdfirecafe with dissolveslow
        $ renpy.pause (2.0)
        $ dwtd.deathsound(5)
        show dwtd_youdied_text at top with easeintop
        $ renpy.pause(4.0)
        call dwtd_youdied("Generator Slap","You didn't stop Reza from slapping the generator and blew up.")
    
    m "I grabbed Reza's wrist moments before his hand made contact with the generator."
    c "Maybe you shouldn't slap it like that, it might be fragile."
    if blood:
        Rz annoyed "Why are you so careful all of a sudden?"
        c "Let's just make sure we don't break any of them before they go through the portal."
        show reza normal with dissolve
    else:
        Rz "Good idea."
    return
