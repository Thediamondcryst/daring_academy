## Splashscreen ############################################################
## A portion of the game that plays at launch, before the main menu is shown.

## The animation is kinda tacky so I recommend using something else.
## ATL documentation: https://www.renpy.org/doc/html/atl.html


image splash = "gui/renpy-logo.png"

label splashscreen:

    scene black
    with Pause(1)

    show text "The Monster Orb Team Presents..." with dissolve
    with Pause(2)

    hide text with dissolve
    with Pause(1)

    show splash with dissolve:
        xalign 0.5 yalign 0.39 alpha 1.0 zoom 0.4
        linear 1.0 alpha 1.0
    show text "{size=30}Made with Ren'Py Version [renpy.version_only]{/s}" with dissolve:
        xalign 0.5 yalign 0.73 alpha 0.0
        linear 1.0 alpha 1.0
    with Pause(2)

    scene black with dissolve
    with Pause(1)

    return
