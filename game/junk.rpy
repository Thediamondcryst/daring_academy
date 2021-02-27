image blink_random_amelia_player_hug:
    "images/sprites/other/assets/amelia_player_hug_opened_eyes.png"
    choice:
        4.5
    choice:
        3.5
    choice:
        1.5
    "images/sprites/other/assets/amelia_player_hug_closed_eyes.png"
    .15
    repeat



default show_quick_menu = True
default showBg = False
screen achievementButtonSmug:
    button:
        xsize 100
        ysize 100
        if showBg:
            background Null()
            xpos 567
            ypos 233
        else:
            background Null()
            xpos 567
            ypos 233
        xpos 567
        ypos 233

        action Call("lookin_real_smug_here")
        activate_sound(notification)




screen mall_monster_orb_button:
    button:
        xsize 80
        ysize 80
        if showBg:
            background ("images/buttons/mall/focus/mall_monster_orb_icon_activated.png")
            xsize 80
            ysize 80
        else:
            background ("images/buttons/mall/background/mall_monster_orb_icon.png")
            xsize 80
            ysize 80
        xpos 280
        ypos 300

        action Call("motcg_mall")

screen mall_big_store_button:
    button:
        xsize 80
        ysize 80
        if showBg:
            background ("images/buttons/mall/focus/mall_big_store_icon_activated.png")
            xsize 80
            ysize 80
        else:
            background ("images/buttons/mall/background/mall_big_store_icon.png")
            xsize 80
            ysize 80
        xpos 540
        ypos 220

        action Call("store_mall")

screen mall_plaza_button:
    button:
        xsize 80
        ysize 80
        if showBg:
            background ("images/buttons/mall/focus/mall_plaza_icon_activated.png")
            xsize 80
            ysize 80
        else:
            background ("images/buttons/mall/background/mall_plaza_icon.png")
            xsize 80
            ysize 80
        xpos 920
        ypos 380

        action Call("plaza_mall")

screen mall_restaurant_button:
    button:
        xsize 80
        ysize 80
        if showBg:
            background ("images/buttons/mall/focus/mall_restaurant_icon_activated.png")
            xsize 80
            ysize 80
        else:
            background ("images/buttons/mall/background/mall_restaurant_icon.png")
            xsize 80
            ysize 80
        xpos 480
        ypos 500

        action Call("restaurant_mall")

screen mall_outside_button:
    button:
        xsize 80
        ysize 80
        if showBg:
            background ("images/buttons/mall/focus/mall_outside_icon_activated.png")
            xsize 80
            ysize 80
        else:
            background ("images/buttons/mall/background/mall_outside_icon.png")
            xsize 80
            ysize 80
        xpos 850
        ypos 600

        action Call("outside_mall")

screen mall_clothes_button:
    button:
        xsize 80
        ysize 80
        if showBg:
            background ("images/buttons/mall/focus/mall_clothes_icon_activated.png")
            xsize 80
            ysize 80
        else:
            background ("images/buttons/mall/background/mall_clothes_icon.png")
            xsize 80
            ysize 80
        xpos 690
        ypos 520

        action Call("clothes_mall")


screen mall_skip_button:
    button:
        xpos 690
        ypos 520
        if showBg:
            text "Continue" size 100
        else:
            text "Continue" size 100

        action show_screen(dev_room)
label lookin_real_smug_here:
    $ achievement.grant("Lookin' Real Smug Here!")
    $ play_sound(notification)
    show screen achievement("lookin_real_smug_here_achievement_pop_up.png")


# The script of the game goes in this file.
init python:
    ###Screenshake
    # Shakes the screen. To use, put
    # $ shake()
    # inline. For other uses, simply do a check inline for ATL statements, or a ConditionSwitch for shaky images.
    def shake():
        if persistent.screenshake:
            renpy.with_statement(hpunch)
        else:
            renpy.with_statement(fade) ###OPTIONAL: Show a different effect if screenshake is turned off.
define config.mouse = {"default":[ ("cursor_pointer.png", 0, 0) ] , "imagemap":[ ("cursor_pointer_selected.png", 0, 0) ] }


image strike = im.FactorScale("strike_card.png", 0.6)
