﻿## Original file by npckc - https://npckc.site or https://npckc.itch.io
## Download at https://npckc.itch.io/caption-tool-for-renpy

################################################################################
## Caption Tool
################################################################################

# Hello! This is Caption Tool, a simple tool for adding image and sound captions to your Ren'Py game, made by npckc (https://npckc.site)!

# Please copy this file (captiontool.rpy) to the "game" folder of your game. As well, please add the following textbutton to a screen somewhere, like the Preferences screen in your screens.rpy file.

# textbutton _("Accessibility") action ShowMenu("accessibility")
# Remove the # when pasting in the preferences screen. You can also use the code in the "screens.rpy" file of this tool instead.

# Once you've done that, you're OK! Just edit captiontool.rpy to work with your game (e.g., add your own sound captions, change the image caption character name if necessary).

# If you use this tool, I would appreciate it if you can credit npckc (https://npckc.site or https://npckc.itch.io) or the tool in some way, but it isn't required.

################################################################################
## Initialization
################################################################################

# This asks the user whether they want to use image or sound captions the first time they boot the game. It uses Ren'Py's splashscreen function - you can add your own splashscreen to this label as well.

default persistent.sound_captions = False
default persistent.image_captions = False

################################################################################
## Sound Captions
################################################################################

# These are the commands for playing music and sounds, as well as where sound captions are defined. Please change the text to fit your own

init python:

# This is the text that will show whenever you play a sound. The sound description will follow.
    soundtext = _("Sound: ")

# This is the text that will show whenever you play music. The music description will follow.
    musictext = _("Music: ")

# This is where you define the names for the sound files you will be using in the game.
    # example = "audio/examplefile.ogg"
    notification = "audio/sfx/notification_02.wav"
    door_unlock = "audio/sfx/keys_unlocking_door.mp3"

# This is where you define the sound captions for each sound file you will be using in the game. Please make sure the names of the sounds defined above match the ones used for the captions below.
    sound_list = {
    # example: _("Example text here"),
    door_unlock: _("A Door Unlocks"),
    notification: _("New Notification Incoming"),
    }

# This is where you define the names for the music files you will be using in the game. It is recommended to define the main menu BGM as well.
    # example = "audio/examplefile.ogg"
    final_discoveries = "audio/music/Thediamondcrystal_-_Final_Discoveries.mp3"
    spirals = "audio/music/Alex_The_Hat_-_Spirals.mp3"
    spirits = "audio/music/Thediamondcrystal_-_Spirits.mp3"
    tropical_moom = "audio/music/JustLetterH_-_Tropical_Moom.mp3"
    homeland = "audio/music/JustLetterH_-_Homeland.mp3"
    last_dance = "audio/music/Thediamondcrystal_-_Last_Dance.mp3"
    motgwp = "audio/music/lil_wawa_-_motgwp.mp3"
    rise = "audio/music/nt_-_rise.mp3"

# This is where you define the music captions for each music file you will be using in the game. Please make sure the names of the music defined above match the ones used for the captions below.
    music_list = {
    # example: _("Example text here"),
    final_discoveries: _("Thediamondcrystal - Final Discoveries"),
    spirals: _("Alex The Hat - Spirals"),
    spirits: _("Thediamondcrystal - Spirits"),
    tropical_moom: _("JustLetterH - Tropical Mooms"),
    homeland: _("JustLetterH - Homeland"),
    last_dance: _("Thediamondcrystal - Last Dance"),
    motgwp: _("Lil Wawa - Monster Orb, The Game We Play (Full Version) (ft. N.T)"),
    rise: _("N.T - Rise"),
    }

# This is the sound command. It functions the same way as "play sound" normally does. You can change the fadein, fadeout and loop values when you invoke the command. If you do not change the values, the default values are 0.0 fadein, 0.0 fadeout, and no loop. If you change the values below, that will change the default values for every time you invoke the command.
    def play_sound(file,fadein=0.0,fadeout=0.0,loop=False):
        renpy.sound.play(file,fadein=fadein,fadeout=fadeout,loop=loop)
        if persistent.sound_captions:
            renpy.notify(soundtext + sound_list[renpy.sound.get_playing('sound')])

# Here are some examples of how to use the play_sound command in your game.
# Put the name for the file that you defined above in the (brackets).
# Add additional values afterwards if you want to change them from the default.
#(Remove the # when using it.)

# $ play_sound(beepbeep)
# $ play_sound(phone,loop=True)

# You can use "stop sound" to stop the sound, just as you would normally.

# This is the music command. It functions the same way as "play music" normally does. You can change the fadein and fadeout values when you invoke the command. If you do not change the values, the default values are 0.0 fadein and 0.0 fadeout. If you change the values below, that will change the default values for every time you invoke the command.
    def play_music(file,fadein=0.0,fadeout=0.0):
        renpy.music.play(file,fadein=fadein,fadeout=fadeout)
        if persistent.sound_captions:
            renpy.notify (musictext + music_list[renpy.music.get_playing('music')])

# Here are some examples of how to use the play_music command in your game.
# Put the name for the file that you defined above in the (brackets).
# Add additional values afterwards if you want to change them from the default.
#(Remove the # when using it.)

# $ play_music(cake)
# $ play_music(cake,fadein=2.0,fadeout=2.0)

# You can use "stop music" to stop the sound, just as you would normally.

################################################################################
## Image Captions
################################################################################

# This character will speak if image captions or self-voicing is on. Ren'Py also has "sv", a built-in character that can be used for self-voicing, but the following character, "ic", will be displayed even if self-voicing if off as long as image captions are set to On in Preferences. The default character name is None - that is, there is no name, like a narrator - but that can be changed.

define ic = Character(_(None),condition="persistent.image_captions or _preferences.self_voicing")

################################################################################
## Accessibility Menu
################################################################################

# This can be used if you want a menu ONLY for accessibility options. You can also copy and paste the buttons into the default Ren'Py preferences screen.

## For our purposes, we will be adding these into the normal Preferences screen. -

# screen accessibility:

#     tag menu

#     use game_menu(_("Preferences"), scroll="viewport"):
#         vbox:
#             style_prefix "check"
#             label _("Accessibility")
#             textbutton _("Sound Captions") action ToggleVariable("persistent.sound_captions")
#             textbutton _("Image Captions") action ToggleVariable("persistent.image_captions")
#             # Self-voicing does not work on smartphone devices, so this option only shows if the user is playing on a PC.
#             if renpy.variant("pc"):
#                 textbutton _("Self-Voicing") action Preference("self voicing", "toggle")
#             # This shows Ren'Py's built-in accessibility menu. This can also be displayed by pressing "A" on the keyboard when playing on a PC. As this option can break the way the game is displayed and also does not support translation as of the latest Ren'Py build, you may want to hide the option.
#             textbutton _("More Options...") action Show("_accessibility")

#             # This button will return the user to the Preferences menu.
#             # It can be removed if it isn't necessary.
#             textbutton ("") #Adds space between accessibility options and return button
#             textbutton _("Return") action ShowMenu("preferences")

################################################################################
## Translating Image Captions
################################################################################

# The python block below is for translating the image captions. Unfortunately, Ren'Py's built-in translation function does not work with image captions, so the text has to be retranslated separately in a python block.
# You can see the translation in the tool by selecting Language > Test. The image captions will show TEST before each text, as they do below.

translate test python:

### SOUND TEXT
    soundtext = ("TEST Sound: ")
### MUSIC TEXT
    musictext = ("TEST Music: ")

### SOUND CAPTION

    sound_list = {
    # example : _("Example text here"),
    door_unlock : _("A Door Unlocks"),
    notification : _("New Notification Incoming"),
    }

### MUSIC CAPTION

    music_list = {
    # example: _("Example text here"),
    final_discoveries: _("Thediamondcrystal - Final Discoveries"),
    alex_spirals: _("Alex The Hat - Spirals")
    }
