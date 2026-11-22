init -2:
    style ls_button:
        background Solid("#172222")
        hover_background Solid("#293331")
        insensitive_background Solid("#101718")
        padding (18, 13)
        xsize 360
        ysize 52

    style ls_button_text:
        color "#d8d5c6"
        hover_color "#f2cc80"
        insensitive_color "#69736e"
        size 19
        bold True
        font "DejaVuSans.ttf"

    style ls_small_button:
        background Solid("#172222")
        hover_background Solid("#293331")
        padding (15, 10)
        xsize 260
        ysize 44

    style ls_small_button_text:
        color "#e1ddce"
        hover_color "#f2cc80"
        size 16
        bold True
        font "DejaVuSans.ttf"

    style ls_panel:
        background Solid("#091011")
        padding (18, 14)

screen laststand_menu():
    tag menu
    modal True
    add CityMenuBackdrop() xysize (1280, 720)
    add SurvivorBulletinBoard() xalign 0.12 yalign 0.5 xysize (500, 660)
    add CityEvidenceBoard() xpos 732 ypos 188 xysize (520, 410)

    text "BULLETIN BOARD / INCIDENT 09" xpos 770 ypos 208 color "#e3d4aa" size 14 bold True
    text "LAST RADIO CALL" xpos 1010 ypos 281 color "#46382e" size 13 bold True
    text "WEST GATE LOST" xpos 1010 ypos 305 color "#4b372d" size 15 bold True
    text "THREE IN THE RAIN" xpos 1010 ypos 327 color "#4b372d" size 13 bold True
    text "THREATS AHEAD" xpos 1010 ypos 394 color "#45362d" size 13 bold True
    text "RUNNER / BRUTE / SPITTER" xpos 1010 ypos 418 color "#4b372d" size 12 bold True
    text "DO NOT FOLLOW LIGHTS" xpos 1010 ypos 450 color "#8f4239" size 12 bold True

    frame:
        xalign 0.12
        yalign 0.5
        xsize 475
        background Solid("#111513ed")
        padding (34, 30)
        vbox:
            spacing 13
            text "BLACKOUT DISTRICT / FIELD LOG" color "#b2a487" size 14 bold True
            text "LAST" color "#eee8d8" size 62 bold True
            text "STAND" color "#e7b766" size 62 bold True yoffset -18
            text "NO RESCUE IS COMING." color "#d28a63" size 16 bold True
            null height 7
            text "Last transmission ended at 02:13. Keep moving. Ration your rounds. If you hear them, they already heard you." color "#c2beb0" size 17 xmaximum 390
            null height 9
            textbutton "01   START" action Return("play") style "ls_button"
            textbutton "02   HOW TO PLAY" action Return("howto") style "ls_button"
            textbutton "03   SETTINGS" action Return("settings") style "ls_button"
            textbutton "04   QUIT" action Quit(confirm=False) style "ls_button"
            hbox:
                xsize 360
                text "BEST SCORE  " color "#71817b" size 12
                text "[persistent.best_score]" color "#e7b766" size 12 bold True
                null width 70
                text "BUILD 01.05" color "#71817b" size 12

screen how_to_play():
    modal True
    add Solid("#080d0ff0")
    frame:
        xalign 0.5
        yalign 0.5
        xsize 830
        background Solid("#10191a")
        padding (40, 34)
        vbox:
            spacing 18
            text "FIELD MANUAL / 01" color "#98a69e" size 14 bold True
            text "SURVIVE THE NIGHT" color "#e8c47e" size 36 bold True
            text "Keep space between you and the horde. Every round matters." color "#c4c7ba" size 19
            null height 5
            grid 2 7:
                spacing 18
                text "W A S D" color "#f1cb7c" size 18 bold True
                text "Move through the district" color "#d7d7ce" size 17
                text "MOUSE" color "#f1cb7c" size 18 bold True
                text "Aim; hold left click to fire" color "#d7d7ce" size 17
                text "R" color "#f1cb7c" size 18 bold True
                text "Reload from collected reserve ammo" color "#d7d7ce" size 17
                text "SHIFT" color "#f1cb7c" size 18 bold True
                text "Sprint to break contact" color "#d7d7ce" size 17
                text "1 - 5" color "#f1cb7c" size 18 bold True
                text "Switch unlocked weapons" color "#d7d7ce" size 17
                text "E" color "#f1cb7c" size 18 bold True
                text "Release a charged full-circle shockwave" color "#d7d7ce" size 17
                text "ESC" color "#f1cb7c" size 18 bold True
                text "Pause the run" color "#d7d7ce" size 17
            null height 8
            text "Five guns: pistol, shotgun (150), SMG (250), rifle (350), and scout rifle (550). Ammo stays limited, so search the street for supplies." color "#aeb9b0" size 16 xmaximum 740
            textbutton "BACK TO MENU" action Return("back") style "ls_small_button"

screen laststand_settings():
    modal True
    add Solid("#080d0ff0")
    frame:
        xalign 0.5
        yalign 0.5
        xsize 630
        background Solid("#10191a")
        padding (38, 34)
        vbox:
            spacing 20
            text "FIELD MANUAL / 02" color "#98a69e" size 14 bold True
            text "SETTINGS" color "#e8c47e" size 36 bold True
            hbox:
                spacing 24
                text "SOUND EFFECTS" color "#e2dfd2" size 18 yalign 0.5
                bar value Preference("sound volume") xmaximum 260 yalign 0.5
                text "VOLUME" color "#c1b38f" size 14 yalign 0.5
            hbox:
                spacing 24
                text "BACKGROUND MUSIC" color "#e2dfd2" size 18 yalign 0.5
                bar value Preference("music volume") xmaximum 260 yalign 0.5
                text "VOLUME" color "#c1b38f" size 14 yalign 0.5
            textbutton ("SCREEN SHAKE     " + ("ON" if persistent.screen_shake else "OFF")) action Function(toggle_screen_shake) style "ls_small_button"
            text "Your best score is saved on this device." color "#aeb9b0" size 16
            textbutton "BACK TO MENU" action Return("back") style "ls_small_button"

screen gameplay(run, arena):
    tag game
    modal True
    add arena xysize (1280, 720)
    # Keep the HUD responsive without forcing a full screen interaction twelve times a second.
    timer 0.12 repeat True action Function(renpy.restart_interaction)
    key "game_menu" action Return("pause")

    frame:
        style "ls_panel"
        xpos 34 ypos 28
        xsize 270
        vbox:
            spacing 4
            hbox:
                xfill True
                text "SURVIVOR" color "#9eaaa0" size 13 bold True
                null width 115
                text "[int(run.health)]" color "#f0e8d2" size 21 bold True
            bar value run.health range 100 xmaximum 230 ymaximum 12
            hbox:
                xfill True
                text ("BOOST ACTIVE" if run.speed_timer > 0 else "READY") color "#8eaa9a" size 11
                null width 45
                text "HEALTH" color "#819087" size 11

    vbox:
        xalign 0.5
        ypos 24
        spacing 0
        text "CURRENT WAVE" color "#bdc0b2" size 12 bold True xalign 0.5
        text "[run.wave:02d]" color "#edc46f" size 38 bold True xalign 0.5
        if run.between_waves > 0:
            text "NEXT WAVE IN [int(run.between_waves) + 1]" color "#c3b48f" size 11 xalign 0.5
        else:
            text "HOSTILES [len(run.zombies) + run.spawn_left:02d]" color "#a9b0a4" size 11 xalign 0.5

    frame:
        style "ls_panel"
        xalign 1.0 xoffset -34 ypos 28
        xsize 250
        vbox:
            hbox:
                xfill True
                text "SCORE" color "#9eaaa0" size 13 bold True
                null width 64
                text "KILLS" color "#9eaaa0" size 13 bold True
            hbox:
                xfill True
                text "[run.score:06d]" color "#f0e8d2" size 22 bold True
                null width 50
                text "[run.kills:02d]" color "#f0e8d2" size 22 bold True
            hbox:
                text "BEST [persistent.best_score]" color "#c4aa72" size 11
                null width 38
                text "HOSTILES [len(run.zombies) + run.spawn_left:02d]" color "#839087" size 11

    frame:
        style "ls_panel"
        xpos 34
        yalign 1.0
        yoffset -28
        xsize 410
        hbox:
            spacing 14
            frame:
                background Solid("#c49c5e")
                xsize 42 ysize 42
                text "[WEAPONS[run.weapon]['mark']]" color "#18201d" size 25 bold True xalign 0.5 yalign 0.5
            vbox:
                yalign 0.5
                text "EQUIPPED" color "#9eaaa0" size 11 bold True
                text "[WEAPONS[run.weapon]['name']]" color "#e9e3d1" size 16 bold True
                text "[run.weapon.upper()]" color "#b8b49f" size 11
            null width 16
            hbox:
                yalign 0.5
                text "[run.mag[run.weapon]:02d]" color "#f0e4c3" size 30 bold True
                text " / [run.reserve[run.weapon]:02d]" color "#b5b9ac" size 19 yalign 0.55
            vbox:
                yalign 0.5
                text "MAG" color "#9eaaa0" size 10
                text "RESERVE" color "#9eaaa0" size 10
        if run.reloading:
            text "RELOADING" color "#f0c16b" size 14 bold True xalign 0.5 ypos -46

    hbox:
        xalign 1.0
        yalign 1.0
        xoffset -32
        yoffset -28
        spacing 6
        text "WASD MOVE  |  MOUSE AIM/FIRE  |  SHIFT RUN  |  R RELOAD  |  1-5 WEAPONS  |  E WAVE" color "#c2c3b5" size 12 yalign 0.5
        textbutton "Ⅱ" action Return("pause") style "ls_small_button" xsize 48 ysize 42

    if run.shockwave_ready:
        frame:
            background Solid("#102529ed")
            xalign 0.5
            yalign 1.0
            yoffset -88
            padding (18, 9)
            hbox:
                spacing 10
                text "E" color "#7be1dc" size 18 bold True
                text "SHOCKWAVE READY / RELEASE" color "#f0e8d2" size 14 bold True yalign 0.5

    if run.toast_timer > 0:
        frame:
            background Solid("#11191add")
            xalign 0.5 yalign 0.37
            padding (18, 10)
            text run.toast color "#eed397" size 17 bold True
    if run.banner_timer > 0:
        frame:
            background Solid("#11191abb")
            xalign 0.5 yalign 0.27
            padding (22, 10)
            text run.banner color "#f0c66e" size 26 bold True

screen pause_menu(run):
    modal True
    add Solid("#050909dd")
    frame:
        xalign 0.5 yalign 0.5
        xsize 500
        background Solid("#101819")
        padding (34, 30)
        vbox:
            spacing 15
            text "SIGNAL LOST / RUN PAUSED" color "#91a39b" size 14 bold True
            text "CATCH YOUR BREATH" color "#e8c47e" size 32 bold True
            textbutton "RESUME" action Return("resume") style "ls_button"
            textbutton "RESTART RUN" action Return("restart") style "ls_button"
            textbutton "MAIN MENU" action Return("menu") style "ls_button"
    key "game_menu" action Return("resume")

screen game_over_screen(run, arena):
    modal True
    add arena xysize (1280, 720)
    add Solid("#050909c8")
    frame:
        xalign 0.5 yalign 0.5
        xsize 570
        background Solid("#101819")
        padding (38, 32)
        vbox:
            spacing 16
            text "SIGNAL LOST / SURVIVOR DOWN" color "#91a39b" size 14 bold True
            text "THE NIGHT WINS" color "#e8c47e" size 36 bold True
            hbox:
                spacing 38
                vbox:
                    text "FINAL SCORE" color "#9eaaa0" size 12
                    text "[run.score]" color "#f0e8d2" size 27 bold True
                vbox:
                    text "ZOMBIES DEFEATED" color "#9eaaa0" size 12
                    text "[run.kills]" color "#f0e8d2" size 27 bold True
            hbox:
                spacing 38
                vbox:
                    text "HIGHEST WAVE" color "#9eaaa0" size 12
                    text "[run.wave]" color "#f0e8d2" size 27 bold True
                vbox:
                    text "BEST SCORE" color "#9eaaa0" size 12
                    text "[persistent.best_score]" color "#e7b766" size 27 bold True
            textbutton "TRY AGAIN" action Return("restart") style "ls_button"
            textbutton "MAIN MENU" action Return("menu") style "ls_button"

init -1:
    style prologue_say_window:
        xalign 0.5
        xfill True
        yalign 1.0
        ysize 205
        background Solid("#080d0fec")
        padding (72, 25)

    style prologue_say_who:
        font "DejaVuSans.ttf"
        size 18
        bold True
        color "#e5b76b"

    style prologue_say_what:
        font "DejaVuSans.ttf"
        size 27
        color "#eee9dd"
        line_spacing 6
        xmaximum 1130

screen prologue_say(who, what):
    window:
        id "window"
        style "prologue_say_window"
        vbox:
            spacing 10
            if who is not None:
                text who id "who" style "prologue_say_who"
            text what id "what" style "prologue_say_what"
            text "CLICK TO CONTINUE" xalign 1.0 size 12 color "#89948e"

screen prologue_hud(page, chapter):
    zorder 130
    text "LAST STAND  /  STORY FILE [page]" xpos 48 ypos 32 size 13 bold True color "#e0d6ba"
    text chapter xpos 48 ypos 56 size 12 color "#c89d61"
    textbutton "SKIP STORY  >>":
        action Jump("prologue_skip")
        xalign 0.96
        ypos 28
        text_size 14
        text_color "#d8d5c6"
        text_hover_color "#f2cc80"
        background Solid("#11191acc")
        hover_background Solid("#293331ee")
        padding (16, 10)
    key "K_ESCAPE" action Jump("prologue_skip")
