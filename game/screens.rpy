################################################################################
## Initialization
################################################################################

init offset = -1

################################################################################
## Styles
################################################################################

if renpy.variant("small") or renpy.variant("mobile"):
    define gui.text_size = 10
else:
    define gui.text_size = 23

style default:
    properties gui.text_properties()
    language gui.language

style input:
    properties gui.text_properties("input", accent=True)
    adjust_spacing False

style hyperlink_text:
    properties gui.text_properties("hyperlink", accent=True)
    hover_underline True

style gui_text:
    properties gui.text_properties("interface")

style button:
    properties gui.button_properties("button")

style button_text is gui_text:
    properties gui.text_properties("button")
    yalign 0.5

style label_text is gui_text:
    properties gui.text_properties("label", accent=True)

style prompt_text is gui_text:
    properties gui.text_properties("prompt")

style bar:
    ysize gui.bar_size
    left_bar Frame("gui/bar/left.png", gui.bar_borders, tile=gui.bar_tile)
    right_bar Frame("gui/bar/right.png", gui.bar_borders, tile=gui.bar_tile)

style vbar:
    xsize gui.bar_size
    top_bar Frame("gui/bar/top.png", gui.vbar_borders, tile=gui.bar_tile)
    bottom_bar Frame("gui/bar/bottom.png", gui.vbar_borders, tile=gui.bar_tile)

style scrollbar:
    ysize gui.scrollbar_size
    base_bar Frame("gui/scrollbar/horizontal_[prefix_]bar.png", gui.scrollbar_borders, tile=gui.scrollbar_tile)
    thumb Frame("gui/scrollbar/horizontal_[prefix_]thumb.png", gui.scrollbar_borders, tile=gui.scrollbar_tile)
    unscrollable "hide"

style vscrollbar:
    xsize gui.scrollbar_size
    base_bar Frame("gui/scrollbar/vertical_[prefix_]bar.png", gui.vscrollbar_borders, tile=gui.scrollbar_tile)
    thumb Frame("gui/scrollbar/vertical_[prefix_]thumb.png", gui.vscrollbar_borders, tile=gui.scrollbar_tile)
    unscrollable "hide"

style slider:
    ysize gui.slider_size
    base_bar Frame("gui/slider/horizontal_[prefix_]bar.png", gui.slider_borders, tile=gui.slider_tile)
    thumb "gui/slider/horizontal_[prefix_]thumb.png"

style vslider:
    xsize gui.slider_size
    base_bar Frame("gui/slider/vertical_[prefix_]bar.png", gui.vslider_borders, tile=gui.slider_tile)
    thumb "gui/slider/vertical_[prefix_]thumb.png"

style frame:
    padding gui.frame_borders.padding
    background Frame("gui/frame.png", gui.frame_borders, tile=gui.frame_tile)

################################################################################
## In-game screens
################################################################################


## Say screen ##################################################################
##
## The say screen is used to display dialogue to the player. It takes two
## parameters, who and what, which are the name of the speaking character and
## the text to be displayed, respectively. (The who parameter can be None if no
## name is given.)
##
## This screen must create a text displayable with id "what", as Ren'Py uses
## this to manage text display. It can also create displayables with id "who"
## and id "window" to apply style properties.
##
## https://www.renpy.org/doc/html/screen_special.html#say

screen say(who, what):
    style_prefix "say"

    window:

        background Transform(style.window.background, alpha=persistent.say_window_alpha)
        ### IMPORTANT: The Transform() is holding the window background, and the alpha variable ties to our say window alpha

        id "window"

        if who is not None:

            window:
                id "namebox"
                style "namebox"
                text who id "who"
                background Transform(style.namebox.background, alpha=persistent.say_window_alpha)

        text what id "what"

    ## If there's a side image, display it above the text. Do not display on the
    ## phone variant - there's no room.
    if not renpy.variant("small"):
        add SideImage() xalign 0.0 yalign 1.0

## Make the namebox available for styling through the Character object.
init python:
    config.character_id_prefixes.append('namebox')

style window is default
style say_label is default
style say_dialogue is default
style say_thought is say_dialogue

style namebox is default
style namebox_label is say_label

default persistent.say_window_alpha = 0.75

style window:
    xalign 0.5
    xfill True
    yalign gui.textbox_yalign
    ysize gui.textbox_height

    background gui.preference("ADVtextbox", "gui/textbox_1.png")

style namebox:
    yalign 0.04
    xpos gui.name_xpos
    xanchor gui.name_xalign
    xsize gui.namebox_width
    ypos gui.name_ypos
    ysize gui.namebox_height

    background Frame("gui/namebox.png", gui.namebox_borders, tile=gui.namebox_tile, xalign=gui.name_xalign)
    padding gui.namebox_borders.padding

style say_label:
    properties gui.text_properties("name", accent=True)
    xalign gui.name_xalign
    yalign 0.5

style say_dialogue:
    yalign -0.1
    properties gui.text_properties("dialogue")
    xpos gui.dialogue_xpos
    xsize gui.dialogue_width
    ypos gui.dialogue_ypos
    line_spacing gui.preference("dialogue_spacing", 3)


## Input screen ################################################################
##
## This screen is used to display renpy.input. The prompt parameter is used to
## pass a text prompt in.
##
## This screen must create an input displayable with id "input" to accept the
## various input parameters.
##
## https://www.renpy.org/doc/html/screen_special.html#input

screen input(prompt):
    style_prefix "input"

    window:

        vbox:
            xalign gui.dialogue_text_xalign
            xpos gui.dialogue_xpos
            xsize gui.dialogue_width
            ypos gui.dialogue_ypos

            text prompt style "input_prompt"
            input id "input"

style input_prompt is default

style input_prompt:
    xalign gui.dialogue_text_xalign
    properties gui.text_properties("input_prompt")

style input:
    xalign gui.dialogue_text_xalign
    xmaximum gui.dialogue_width


## Choice screen ###############################################################
##
## This screen is used to display the in-game choices presented by the menu
## statement. The one parameter, items, is a list of objects, each with caption
## and action fields.
##
## https://www.renpy.org/doc/html/screen_special.html#choice

screen choice(items):
    style_prefix "choice"

    vbox:
        for i in items:
            textbutton i.caption action i.action

## When this is true, menu captions will be spoken by the narrator. When false,
## menu captions will be displayed as empty buttons.
define config.narrator_menu = True

style choice_vbox is vbox
style choice_button is button
style choice_button_text is button_text

style choice_vbox:
    xalign 0.5
    ypos 405
    yanchor 0.5

    spacing gui.choice_spacing

style choice_button is default:
    properties gui.button_properties("choice_button")

style choice_button_text is default:
    properties gui.button_text_properties("choice_button")


## Quick Menu screen ###########################################################
##
## The quick menu is displayed in-game to provide easy access to the out-of-game
## menus.

screen quick_menu():

    ## Ensure this appears on top of other screens.
    zorder 100

    if quick_menu:

        # Add an in-game quick menu.

        hbox:
            style_group "quick"

            xalign 0.5
            yalign 1.003

            ## https://www.renpy.org/doc/html/self_voicing.html#creator-concerns
            # imagebutton auto "foo.png" action None() alt "foo"
            textbutton _("Back") action Rollback() alt "Back"
            textbutton _("History") action ShowMenu('history') alt "History"
            textbutton _("Skip") action Skip() alternate Skip(fast=True, confirm=True) alt "Skip"
            textbutton _("Auto") action Preference("auto-forward", "toggle") alt "Auto"
            textbutton _("Save") action ShowMenu('save') alt "Save"
            textbutton _("Load") action ShowMenu('load') alt "Load"
            textbutton _("Prefs") action ShowMenu('preferences') alt "Preferences"

## This code ensures that the quick_menu screen is displayed in-game, whenever
## the player has not explicitly hidden the interface.
init python:
    config.overlay_screens.append("quick_menu")

default quick_menu = True

default typeface = "DejaVuSans"

default screenshake = True

## This allows you to hide the quickmenu during certain scenes if desired.
# default show_quick_menu = True

style quick_button is default
style quick_button_text is button_text

style quick_button:
    properties gui.button_properties("quick_button")

style quick_button_text:
    properties gui.button_text_properties("quick_button")


################################################################################
## Main and Game Menu Screens
################################################################################

## Navigation screen ###########################################################
##
## This screen is included in the main and game menus, and provides navigation
## to other menus, and to start the game.

screen navigation():
    vbox:
        style_prefix "navigation"
        xpos gui.navigation_xpos
        yalign 0.5
        spacing gui.navigation_spacing
        if main_menu:
            textbutton _("Start") action Start()
        else:
            textbutton _("Save") action ShowMenu("save")
        textbutton _("Load") action ShowMenu("load")
        textbutton _("About") action ShowMenu("about")
        textbutton _("Preferences") action ShowMenu("preferences")
        if not main_menu:
            textbutton _("Main Menu") action MainMenu()

        if main_menu:
            textbutton _("Extras") action ShowMenu("achievements") alt "Extras"
        if renpy.variant("pc") or (renpy.variant("web") and not renpy.variant("mobile")):
            ## Help isn't necessary or relevant to mobile devices.
            textbutton _("Help") action ShowMenu("help") alt "Help"
        if renpy.variant("pc"):
            ## The quit button is banned on iOS and unnecessary on Android and
            ## Web.
            textbutton _("Quit") action Quit(confirm=not main_menu) alt "Quit"


style navigation_button is gui_button
style navigation_button_text is gui_button_text

style navigation_button:
    size_group "navigation"
    properties gui.button_properties("navigation_button")

style navigation_button_text:
    properties gui.button_text_properties("navigation_button")


## Main Menu screen ############################################################
##
## Used to display the main menu when Ren'Py starts.
##
## https://www.renpy.org/doc/html/screen_special.html#main-menu

screen main_menu():

    ## This ensures that any other menu screen is replaced.
    tag menu

    style_prefix "main_menu"

    add gui.main_menu_background

    ## This empty frame darkens the main menu.
    frame:
        pass

    ## The use statement includes another screen inside this one. The actual
    ## contents of the main menu are in the navigation screen.
    use navigation

    add "daring_academy_logo_alpha_build"

    if gui.show_name:

        vbox:
            text "Version [config.version]":
                style "main_menu_version"



style main_menu_frame is empty
style main_menu_vbox is vbox
style main_menu_text is gui_text
style main_menu_title is main_menu_text
style main_menu_version is main_menu_text

style main_menu_frame:
    xsize 280
    yfill True

    background "gui/overlay/main_menu.png"

style main_menu_vbox:
    xalign 1.0
    xoffset -1100
    xmaximum 800
    yalign 1.0
    yoffset -7

style main_menu_text:
    properties gui.text_properties("main_menu", accent=True)

style main_menu_title:
    properties gui.text_properties("title")

style main_menu_version:
    properties gui.text_properties("version")

## Game Menu screen ############################################################
##
## This lays out the basic common structure of a game menu screen. It's called
## with the screen title, and displays the background, title, and navigation.
##
## The scroll parameter can be None, or one of "viewport" or "vpgrid". When
## this screen is intended to be used with one or more children, which are
## transcluded (placed) inside it.

screen game_menu(title, scroll=None, yinitial=0.0):

    style_prefix "game_menu"

    if main_menu:
        add gui.main_menu_background
    else:
        add gui.game_menu_background

    frame:
        style "game_menu_outer_frame"

        hbox:

            ## Reserve space for the navigation section.
            frame:
                style "game_menu_navigation_frame"

            frame:
                style "game_menu_content_frame"

                if scroll == "viewport":

                    viewport:
                        yinitial yinitial
                        scrollbars "vertical"
                        mousewheel True
                        draggable True
                        pagekeys True

                        side_yfill True

                        vbox:
                            transclude

                elif scroll == "vpgrid":

                    vpgrid:
                        cols 1
                        yinitial yinitial

                        scrollbars "vertical"
                        mousewheel True
                        draggable True
                        pagekeys True

                        side_yfill True

                        transclude

                else:

                    transclude

    use navigation

    textbutton _("Return"):
        style "return_button"

        action Return()

    label title

    if main_menu:
        key "game_menu" action ShowMenu("main_menu")


style game_menu_outer_frame is empty
style game_menu_navigation_frame is empty
style game_menu_content_frame is empty
style game_menu_viewport is gui_viewport
style game_menu_side is gui_side
style game_menu_scrollbar is gui_vscrollbar

style game_menu_label is gui_label
style game_menu_label_text is gui_label_text

style return_button is navigation_button
style return_button_text is navigation_button_text

style game_menu_outer_frame:
    bottom_padding 30
    top_padding 120

    background "gui/overlay/game_menu.png"

style game_menu_navigation_frame:
    xsize 280
    yfill True

style game_menu_content_frame:
    left_margin 40
    right_margin 20
    top_margin 10

style game_menu_viewport:
    xsize 920

style game_menu_vscrollbar:
    unscrollable gui.unscrollable

style game_menu_side:
    spacing 10

style game_menu_label:
    xpos 50
    ysize 120

style game_menu_label_text:
    size gui.title_text_size
    color gui.accent_color
    yalign 0.5

style return_button:
    xpos gui.navigation_xpos
    yalign 1.0
    yoffset -30

## About screen ################################################################
##
## This screen gives credit and copyright information about the game and Ren'Py.
##
## There's nothing special about this screen, and hence it also serves as an
## example of how to make a custom screen.

screen about():

    tag menu

    ## This use statement includes the game_menu screen inside this one. The
    ## vbox child is then included inside the viewport inside the game_menu
    ## screen.
    use game_menu(_("About"), scroll="viewport"):

        style_prefix "about"

        vbox:

            label "[config.name!t]"
            text _("Version [config.version!t]\n")

            ## gui.about is usually set in options.rpy.
            if gui.about:
                text "[gui.about!t]\n"

            text _("Made with {a=https://www.renpy.org/}Ren'Py{/a} [renpy.version_only].\n\n[renpy.license!t]")


## This is redefined in options.rpy to add text to the about screen.
define gui.about = ""


style about_label is gui_label
style about_label_text is gui_label_text
style about_text is gui_text

style about_label_text:
    size gui.label_text_size


## Load and Save screens #######################################################
##
## These screens are responsible for letting the player save the game and load
## it again. Since they share nearly everything in common, both are implemented
## in terms of a third screen, file_slots.
##
## https://www.renpy.org/doc/html/screen_special.html#save https://
## www.renpy.org/doc/html/screen_special.html#load

screen save():

    tag menu

    use file_slots(_("Save"))


screen load():

    tag menu

    use file_slots(_("Load"))


screen file_slots(title):

    default page_name_value = FilePageNameInputValue(pattern=_("Page {}"), auto=_("Automatic saves"), quick=_("Quick saves"))

    use game_menu(title):

        fixed:

            ## This ensures the input will get the enter event before any of the
            ## buttons do.
            order_reverse True

            ## The page name, which can be edited by clicking on a button.
            button:
                style "page_label"

                key_events True
                xalign 0.5
                action page_name_value.Toggle()

                input:
                    style "page_label_text"
                    value page_name_value

            ## The grid of file slots.
            grid gui.file_slot_cols gui.file_slot_rows:
                style_prefix "slot"

                xalign 0.5
                yalign 0.5

                spacing gui.slot_spacing

                for i in range(gui.file_slot_cols * gui.file_slot_rows):

                    $ slot = i + 1

                    button:
                        action FileAction(slot)

                        has vbox

                        add FileScreenshot(slot) xalign 0.5

                        text FileTime(slot, format=_("{#file_time}%A, %B %d %Y, %H:%M"), empty=_("empty slot")):
                            style "slot_time_text"

                        text FileSaveName(slot):
                            style "slot_name_text"

                        key "save_delete" action FileDelete(slot)

            ## Buttons to access other pages.
            hbox:
                style_prefix "page"

                xalign 0.5
                yalign 1.0

                spacing gui.page_spacing

                textbutton _("<") action FilePagePrevious()

                if config.has_autosave:
                    textbutton _("{#auto_page}A") action FilePage("auto")

                if config.has_quicksave:
                    textbutton _("{#quick_page}Q") action FilePage("quick")

                ## range(1, 10) gives the numbers from 1 to 9.
                for page in range(1, 10):
                    textbutton "[page]" action FilePage(page)

                textbutton _(">") action FilePageNext()


style page_label is gui_label
style page_label_text is gui_label_text
style page_button is gui_button
style page_button_text is gui_button_text

style slot_button is gui_button
style slot_button_text is gui_button_text
style slot_time_text is slot_button_text
style slot_name_text is slot_button_text

style page_label:
    xpadding 75
    ypadding 5

style page_label_text:
    text_align 0.5
    layout "subtitle"
    hover_color gui.hover_color

style page_button:
    properties gui.button_properties("page_button")

style page_button_text:
    properties gui.button_text_properties("page_button")

style slot_button:
    properties gui.button_properties("slot_button")

style slot_button_text:
    properties gui.button_text_properties("slot_button")


## Preferences screen ##########################################################
##
## The preferences screen allows the player to configure the game to better suit
## themselves.
##
## https://www.renpy.org/doc/html/screen_special.html#preferences

screen preferences():

    tag menu

    use game_menu(_("Preferences"), scroll="viewport"):

        vbox:

            ## Standard Preferences
            hbox:

                box_wrap True

                if renpy.variant("pc"):

                    vbox:
                        style_prefix "radio"
                        label _("Display")
                        textbutton _("Window") action Preference("display", "window") alt "Set Display to Windowed"
                        textbutton _("Fullscreen") action Preference("display", "fullscreen") alt "Set Display to Full Screen"

                vbox:
                    style_prefix "radio"
                    label _("Rollback Side")
                    textbutton _("Disable") action Preference("rollback side", "disable") alt "Disable Rollback Side"
                    textbutton _("Allow") action Preference("rollback side", "right") alt "Allow Rollback Side"

                vbox:
                    style_prefix "check"
                    label _("Skip")
                    textbutton _("Unseen Text") action Preference("skip", "toggle") alt "Skip Unseen Text"
                    textbutton _("After Choices") action Preference("after choices", "toggle") alt "Continue Skipping After Choices"
                    textbutton _("Transitions") action InvertSelected(Preference("transitions", "toggle")) alt "Skip Transitions"

                ## Additional vboxes of type "radio_pref" or "check_pref" can be
                ## added here, to add additional creator-defined preferences.

            hbox:

                box_wrap True
                vbox:

                    ## Change Textbox Background:
                    style_prefix "radio"
                    label _("Color Mode (Not Finished)")

                    if renpy.variant("pc"):

                        textbutton _("Dark Mode") action [gui.SetPreference("ADVtextbox", "gui/textbox_1.png"), gui.SetPreference("color", "#ffffff"), gui.SetPreference("NVLtextbox", "gui/nvl_1.png")] alt "Change to Dark Mode"
                        textbutton _("Light Mode") action [gui.SetPreference("ADVtextbox", "gui/textbox_2.png"), gui.SetPreference("color", "#000000"), gui.SetPreference("NVLtextbox", "gui/nvl_2.png"), gui.SetPreference("main_menu_frame", "gui/overlay/main_menu_light.png")] alt "Change to Light Mode"
                     ## NOTE: At the moment, the NVL textbox option is not being used due
                     ## to an issue with updating both the textbox image and the NVL entry
                     ## if a player switches this preference during NVL mode.
                    ## TODO: Find out a way to prevent issue above.

                vbox:
                ## Toggles
                ## You can also create SetField() buttons with on/off variables if you prefer that look.

                    style_prefix "check"
                    label _("Toggle")

                    #Toggle Screenshake
                    textbutton "Screenshake" action ToggleField(persistent,"screenshake",true_value=True,false_value=False) alt "Toggle Screen Shake"

                    ## Self-voicing does not work on smartphone devices, so this option only shows if the user is playing on a PC.
                    if renpy.variant("pc"):

                        textbutton _("Self-Voicing") action Preference("self voicing", "toggle") alt "Toggle Self-Voicing"

                vbox:

                    style_prefix "check"
                    label _("Captions")

                    textbutton _("Song Titles") action ToggleField(persistent,"audio_cues",true_value=True,false_value=False) alt "Toggle Song Titles"
                    textbutton _("SFX Titles") action ToggleVariable("persistent.sound_captions") alt "Toggle Sound Captions"
                    textbutton _("Image Descriptions") action ToggleVariable("persistent.image_captions") alt "Toggle Image Descriptions"

                    ## This shows Ren'Py's built-in accessibility menu. This can also be displayed by pressing "A" on the keyboard when playing on a PC. As this option can break the way the game is displayed and also does not support translation as of the latest Ren'Py build, you may want to hide the option.
                    # textbutton _("More Options...") action Show("_accessibility")

            null height (4 * gui.pref_spacing)

            hbox:
                style_prefix "slider"
                box_wrap True

                vbox:

                    label _("Text Speed")

                    bar value Preference("text speed")

                    label _("Auto-Forward Time")

                    bar value Preference("auto-forward time")

                vbox:

                    if config.has_music:
                        label _("Music Volume")

                        hbox:
                            bar value Preference("music volume")

                    if config.has_sound:

                        label _("Sound Volume")

                        hbox:
                            bar value Preference("sound volume")

                            if config.sample_sound:
                                textbutton _("Test") action Play("sound", config.sample_sound) alt "Test"


                    if config.has_voice:
                        label _("Voice Volume")

                        hbox:
                            bar value Preference("voice volume")

                            if config.sample_voice:
                                textbutton _("Test") action Play("voice", config.sample_voice) alt "Test"

                    if config.has_music or config.has_sound or config.has_voice:
                        null height gui.pref_spacing

                        textbutton _("Mute All"):
                            action Preference("all mute", "toggle")
                            style "mute_all_button"
                            alt "Mute All"

style pref_label is gui_label
style pref_label_text is gui_label_text
style pref_vbox is vbox

style radio_label is pref_label
style radio_label_text is pref_label_text
style radio_button is gui_button
style radio_button_text is gui_button_text
style radio_vbox is pref_vbox

style check_label is pref_label
style check_label_text is pref_label_text
style check_button is gui_button
style check_button_text is gui_button_text
style check_vbox is pref_vbox

style slider_label is pref_label
style slider_label_text is pref_label_text
style slider_slider is gui_slider
style slider_button is gui_button
style slider_button_text is gui_button_text
style slider_pref_vbox is pref_vbox

style mute_all_button is check_button
style mute_all_button_text is check_button_text

style pref_label:
    top_margin gui.pref_spacing
    bottom_margin 2

style pref_label_text:
    yalign 1.0

style pref_vbox:
    xsize 225

style radio_vbox:
    spacing gui.pref_button_spacing

style radio_button:
    properties gui.button_properties("radio_button")
    foreground "gui/button/radio_[prefix_]foreground.png"

style radio_button_text:
    properties gui.button_text_properties("radio_button")

style check_vbox:
    spacing gui.pref_button_spacing

style check_button:
    properties gui.button_properties("check_button")
    foreground "gui/button/check_[prefix_]foreground.png"

style check_button_text:
    properties gui.button_text_properties("check_button")

style slider_slider:
    xsize 350

style slider_button:
    properties gui.button_properties("slider_button")
    yalign 0.5
    left_margin 10

style slider_button_text:
    properties gui.button_text_properties("slider_button")

style slider_vbox:
    xsize 450

## History screen ##############################################################
##
## This is a screen that displays the dialogue history to the player. While
## there isn't anything special about this screen, it does have to access the
## dialogue history stored in _history_list.
##
## https://www.renpy.org/doc/html/history.html

screen history():

    tag menu

    predict False

    frame:

        style_prefix "history"

        label _("History")

        left_margin 100
        right_margin 100
        top_margin 50
        bottom_margin 50

        left_padding 50
        right_padding 25
        top_padding 75
        bottom_padding 50

        vpgrid:

            cols 1
            yinitial 1.0

            draggable True
            mousewheel True
            scrollbars "vertical"

            for h in _history_list:

                window:

                    ## This lays things out properly if history_height is None.
                    has fixed:
                        yfit True

                    if h.who:

                        label h.who:
                            style "history_name"

                            ## Take the color of the who text from the Character, if
                            ## set.
                            if "color" in h.who_args:
                                text_color h.who_args["color"]

                    $ what = renpy.filter_text_tags(h.what, allow=gui.history_allow_tags)
                    text what

            if not _history_list:

                text "The dialogue history is empty." line_spacing 10
                ## Adding line_spacing prevents the bottom of the text
                ## from getting cut off. Adjust when replacing the
                ## default fonts.

        textbutton _("Return") action Return() yalign 1.1 xalign 1.0 alt "Return"

## The old version of the History screen that's attached to the game menu.
# screen history():

#     tag menu

#     ## Avoid predicting this screen, as it can be very large.
#     predict False

#     use game_menu(_("History"), scroll=("vpgrid" if gui.history_height else "viewport"), yinitial=1.0):

#         style_prefix "history"

#         for h in _history_list:

#             window:

#                 ## This lays things out properly if history_height is None.
#                 has fixed:
#                     yfit True

#                 if h.who:

#                     label h.who:
#                         style "history_name"

#                         ## Take the color of the who text from the Character, if
#                         ## set.
#                         if "color" in h.who_args:
#                             text_color h.who_args["color"]

#                 $ what = renpy.filter_text_tags(h.what, allow=gui.history_allow_tags)
#                 text what

#         if not _history_list:
#             label _("The dialogue history is empty.")

## This determines what tags are allowed to be displayed on the history screen.

define gui.history_allow_tags = set()


style history_window is empty

style history_name is gui_label
style history_name_text is gui_label_text
style history_text is gui_text

style history_text is gui_text

style history_label is gui_label
style history_label_text is gui_label_text

style history_window:
    xfill True
    ysize gui.history_height

style history_name:
    xpos gui.history_name_xpos
    xanchor gui.history_name_xalign
    ypos gui.history_name_ypos
    xsize gui.history_name_width

style history_name_text:
    min_width gui.history_name_width
    text_align gui.history_name_xalign

style history_text:
    xpos gui.history_text_xpos
    ypos gui.history_text_ypos
    xanchor gui.history_text_xalign
    xsize gui.history_text_width
    min_width gui.history_text_width
    text_align gui.history_text_xalign
    layout ("subtitle" if gui.history_text_xalign else "tex")

style history_label:
    xfill True

style history_label_text:
    xalign 0.5
    ypos -50
    size gui.label_text_size

## Help screen #################################################################
##
## A screen that gives information about key and mouse bindings. It uses other
## screens (keyboard_help, mouse_help, and gamepad_help) to display the actual
## help.

screen help():

    tag menu

    default device = "keyboard"

    use game_menu(_("Help"), scroll="viewport"):

        style_prefix "help"

        vbox:
            spacing 15

            hbox:

                textbutton _("Keyboard") action SetScreenVariable("device", "keyboard") alt "Keyboard"
                textbutton _("Mouse") action SetScreenVariable("device", "mouse") alt "Mouse"

                if GamepadExists():
                    textbutton _("Gamepad") action SetScreenVariable("device", "gamepad") alt "Gamepad"

            if device == "keyboard":
                use keyboard_help
            elif device == "mouse":
                use mouse_help
            elif device == "gamepad":
                use gamepad_help


screen keyboard_help():

    hbox:
        label _("Enter")
        text _("Advances dialogue and activates the interface.")

    hbox:
        label _("Space")
        text _("Advances dialogue without selecting choices.")

    hbox:
        label _("Arrow Keys")
        text _("Navigate the interface.")

    hbox:
        label _("Escape")
        text _("Accesses the game menu.")

    hbox:
        label _("Ctrl")
        text _("Skips dialogue while held down.")

    hbox:
        label _("Tab")
        text _("Toggles dialogue skipping.")

    hbox:
        label _("Page Up")
        text _("Rolls back to earlier dialogue.")

    hbox:
        label _("Page Down")
        text _("Rolls forward to later dialogue.")

    hbox:
        label "H"
        text _("Hides the user interface.")

    hbox:
        label "S"
        text _("Takes a screenshot.")

    hbox:
        label "V"
        text _("Toggles assistive {a=https://www.renpy.org/l/voicing}self-voicing{/a}.")


screen mouse_help():

    hbox:
        label _("Left Click")
        text _("Advances dialogue and activates the interface.")

    hbox:
        label _("Middle Click")
        text _("Hides the user interface.")

    hbox:
        label _("Right Click")
        text _("Accesses the game menu.")

    hbox:
        label _("Mouse Wheel Up\nClick Rollback Side")
        text _("Rolls back to earlier dialogue.")

    hbox:
        label _("Mouse Wheel Down")
        text _("Rolls forward to later dialogue.")


screen gamepad_help():

    hbox:
        label _("Right Trigger\nA/Bottom Button")
        text _("Advances dialogue and activates the interface.")

    hbox:
        label _("Left Trigger\nLeft Shoulder")
        text _("Rolls back to earlier dialogue.")

    hbox:
        label _("Right Shoulder")
        text _("Rolls forward to later dialogue.")


    hbox:
        label _("D-Pad, Sticks")
        text _("Navigate the interface.")

    hbox:
        label _("Start, Guide")
        text _("Accesses the game menu.")

    hbox:
        label _("Y/Top Button")
        text _("Hides the user interface.")

    textbutton _("Calibrate") action GamepadCalibrate() alt "Calibrate Gamepad"


style help_button is gui_button
style help_button_text is gui_button_text
style help_label is gui_label
style help_label_text is gui_label_text
style help_text is gui_text

style help_button:
    properties gui.button_properties("help_button")
    xmargin 8

style help_button_text:
    properties gui.button_text_properties("help_button")

style help_label:
    xsize 250
    right_padding 20

style help_label_text:
    size gui.text_size
    xalign 1.0
    text_align 1.0

################################################################################
## Additional screens
################################################################################


## Confirm screen ##############################################################
##
## The confirm screen is called when Ren'Py wants to ask the player a yes or no
## question.
##
## https://www.renpy.org/doc/html/screen_special.html#confirm

screen confirm(message, yes_action, no_action):

    ## Ensure other screens do not get input while this screen is displayed.
    modal True

    zorder 200

    style_prefix "confirm"

    add "gui/overlay/confirm.png"

    frame:

        vbox:
            xalign .5
            yalign .5
            spacing 45

            label _(message):
                style "confirm_prompt"
                xalign 0.5

            hbox:
                xalign 0.5
                spacing 150

                textbutton _("Yes") action yes_action alt "Yes"
                textbutton _("No") action no_action alt "No"

    ## Right-click and escape answer "no".
    key "game_menu" action no_action

style confirm_frame is gui_frame
style confirm_prompt is gui_prompt
style confirm_prompt_text is gui_prompt_text
style confirm_button is gui_medium_button
style confirm_button_text is gui_medium_button_text

style confirm_frame:
    background Frame([ "gui/confirm_frame.png", "gui/frame.png"], gui.confirm_frame_borders, tile=gui.frame_tile)
    padding gui.confirm_frame_borders.padding
    xalign .5
    yalign .5

style confirm_prompt_text:
    text_align 0.5
    layout "subtitle"
    color gui.accent_color

style confirm_button:
    properties gui.button_properties("confirm_button")

style confirm_button_text:
    properties gui.button_text_properties("confirm_button")


## Skip indicator screen #######################################################
##
## The skip_indicator screen is displayed to indicate that skipping is in
## progress.
##
## https://www.renpy.org/doc/html/screen_special.html#skip-indicator

screen skip_indicator():

    zorder 100
    style_prefix "skip"

    frame:

        hbox:
            spacing 9

            text _("Skipping")

            text "▸" at delayed_blink(0.0, 1.0) style "skip_triangle"
            text "▸" at delayed_blink(0.2, 1.0) style "skip_triangle"
            text "▸" at delayed_blink(0.4, 1.0) style "skip_triangle"


## This transform is used to blink the arrows one after another.
transform delayed_blink(delay, cycle):
    alpha .5

    pause delay

    block:
        linear .2 alpha 1.0
        pause .2
        linear .2 alpha 0.5
        pause (cycle - .4)
        repeat


style skip_frame is empty
style skip_text is gui_text
style skip_triangle is skip_text

style skip_frame:
    ypos gui.skip_ypos
    background Frame("gui/skip.png", gui.skip_frame_borders, tile=gui.frame_tile)
    padding gui.skip_frame_borders.padding

style skip_text:
    size gui.notify_text_size

style skip_triangle:
    ## We have to use a font that has the BLACK RIGHT-POINTING SMALL TRIANGLE
    ## glyph in it.
    font "DejaVuSans.ttf"


## Notify screen ###############################################################
##
## The notify screen is used to show the player a message. (For example, when
## the game is quicksaved or a screenshot has been taken.)
##
## https://www.renpy.org/doc/html/screen_special.html#notify-screen

screen notify(message):

    zorder 100
    style_prefix "notify"

    frame at notify_appear:
        text "[message!tq]"

    timer 3.25 action Hide('notify')


screen achievement(img):
    fixed:
        at tf_achievement
        style_prefix "achievement"
        add "achievement/" + img align (0.0, 0.0)
    timer 5 action Hide('achievement')


transform tf_achievement:
  pos (980,-100)
  zoom 1.0
  alpha 0.0
  linear 0.3 alpha 1.0 zoom 1.0 pos (980,0)
  on hide:
    linear 0.5 alpha 0.0

transform notify_appear:
    on show:
        alpha 0
        linear .25 alpha 1.0
    on hide:
        linear .5 alpha 0.0


style notify_frame is empty
style notify_text is gui_text

style notify_frame:
    ypos gui.notify_ypos

    background Frame("gui/notify.png", gui.notify_frame_borders, tile=gui.frame_tile)
    padding gui.notify_frame_borders.padding

style notify_text:
    properties gui.text_properties("notify")
    color gui.accent_color


## NVL screen ##################################################################
##
## This screen is used for NVL-mode dialogue and menus.
##
## https://www.renpy.org/doc/html/screen_special.html#nvl

screen nvl(dialogue, items=None):

    window:

        background Transform(style.nvl_window.background, alpha=persistent.say_window_alpha)

        style "nvl_window"

        has vbox:
            spacing gui.nvl_spacing

        ## Displays dialogue in either a vpgrid or the vbox.
        if gui.nvl_height:

            vpgrid:
                cols 1
                yinitial 1.0

                use nvl_dialogue(dialogue)

        else:

            use nvl_dialogue(dialogue)

        ## Displays the menu, if given. The menu may be displayed incorrectly if
        ## config.narrator_menu is set to True, as it is above.
        for i in items:

            textbutton i.caption:
                action i.action
                style "nvl_button"

    add SideImage() xalign 0.0 yalign 1.0

screen nvl_dialogue(dialogue):

    for d in dialogue:

        window:
            id d.window_id

            fixed:
                yfit gui.nvl_height is None

                if d.who is not None:

                    text d.who:
                        id d.who_id

                text d.what:
                    id d.what_id

## This controls the maximum number of NVL-mode entries that can be displayed at
## once.
define config.nvl_list_length = gui.nvl_list_length

style nvl_window is default
style nvl_entry is default

style nvl_label is say_label
style nvl_dialogue is say_dialogue

style nvl_button is button
style nvl_button_text is button_text

style nvl_window:
    xfill True
    yfill True

    background gui.preference("NVLtextbox", "gui/nvl_1.png") #"gui/nvl.png"
    padding gui.nvl_borders.padding

style nvl_entry:
    xfill True
    ysize gui.nvl_height

style nvl_label:
    xpos gui.nvl_name_xpos
    xanchor gui.nvl_name_xalign
    ypos gui.nvl_name_ypos
    yanchor 0.0
    xsize gui.nvl_name_width
    min_width gui.nvl_name_width
    text_align gui.nvl_name_xalign

style nvl_dialogue:
    xpos gui.nvl_text_xpos
    xanchor gui.nvl_text_xalign
    ypos gui.nvl_text_ypos
    xsize gui.nvl_text_width
    min_width gui.nvl_text_width
    text_align gui.nvl_text_xalign
    layout ("subtitle" if gui.nvl_text_xalign else "tex")

style nvl_thought:
    xpos gui.nvl_thought_xpos
    xanchor gui.nvl_thought_xalign
    ypos gui.nvl_thought_ypos
    xsize gui.nvl_thought_width
    min_width gui.nvl_thought_width
    text_align gui.nvl_thought_xalign
    layout ("subtitle" if gui.nvl_text_xalign else "tex")

style nvl_button:
    properties gui.button_properties("nvl_button")
    xpos gui.nvl_button_xpos
    xanchor gui.nvl_button_xalign

style nvl_button_text:
    properties gui.button_text_properties("nvl_button")

## Extras screens ###########################################
##
## A screen that includes Image Galleries, Music Room, and Dev Notes.
## https://www.renpy.org/doc/html/rooms.html

## We let Ren'Py resize our images so we don't have to make buttons in another
## program.

init python:

    # MusicRoom instance.
    mr = MusicRoom(fadeout=1.0)

    # Add music files.
    mr.add("audio/music/Thediamondcrystal_-_Final_Discoveries.mp3", always_unlocked=True)
    mr.add("audio/music/Alex_The_Hat_-_Spirals.mp3")

## Extras Navigation screen ############################################################
##
## This is the same as the Game Menu Navigation screen, but just for the Extras.

screen extras_navigation():

    vbox:
        style_prefix "navigation"

        xpos gui.navigation_xpos
        yalign 0.5

        spacing gui.navigation_spacing

        textbutton _("Achievements") action ShowMenu("achievements") alt "Achievements"


        if persistent.game_clear:

            textbutton _("Developer Notes") action ShowMenu("dev_notes") alt "Developer Notes"

        else:

            textbutton _("???") action None alt ":Locked Option"

        textbutton _("Return") action Return() alt "Return"

## Extras Menu screen #######################################
##
## This is the same as the Game Menu screen, but just for the Extras.

screen extras_menu(title, scroll=None, yinitial=0.0):

    style_prefix "game_menu"

    if main_menu:
        add gui.main_menu_background
    else:
        add gui.game_menu_background

    frame:
        style "game_menu_outer_frame"

        hbox:

            ## Reserve space for the navigation section.
            frame:
                style "game_menu_navigation_frame"

            frame:
                style "game_menu_content_frame"

                if scroll == "viewport":

                    viewport:
                        yinitial yinitial
                        scrollbars "vertical"
                        mousewheel True
                        draggable True
                        pagekeys True

                        side_yfill True

                        vbox:
                            transclude

                elif scroll == "vpgrid":

                    vpgrid:
                        cols 1
                        yinitial yinitial

                        scrollbars "vertical"
                        mousewheel True
                        draggable True
                        pagekeys True

                        side_yfill True

                        transclude

                else:

                    transclude

    label title

    use extras_navigation

## Music Gallery screen ############################################################
##
## This is a simple screen that shows buttons that play a music track.

screen music_gallery():

    tag menu

    ## This use statement includes the extras_menu screen inside this one.
    use extras_menu("Music Room"):

        vbox:

            xalign 0.5
            yalign 0.5

            # The buttons that play each track.
            textbutton "Final Discoveries" action mr.Play("audio/music/Thediamondcrystal_-_Final_Discoveries.mp3")

            null height 20

            hbox:
            # Buttons that let us advance through tracks.
                textbutton "Previous" action mr.Previous() alt "Previous Song"
                textbutton "Next" action mr.Next() alt "Next Song"

            null height 20

        # Start the music playing on entry to the music room.
        on "replace" action mr.Play()


## Dev Notes screen ########################################
##
## This screen contains a message for players after they beat the entire game.
## We borrowed the base of this screen from the About screen.

screen dev_notes():

    tag menu

    ## This use statement includes the extras_menu screen inside this one. The
    ## vbox child is then included inside the viewport inside the extras_menu
    ## screen.
    use extras_menu(_("Developer's Notes"), scroll="viewport"):

        style_prefix "about"

        vbox:

            ## gui.dev_notes is usually set in options.rpy.
            if gui.dev_notes:
                text "[gui.dev_notes!t]\n"

## Type your special message here.
define gui.dev_notes = _p("""Hello, this is BáiYù of tofurocks here. I want to thank
    you for downloading this All-In-One GUI template to use in your own game. As
    someone who has received support from the visual novel community in the past,
    I wanted to give back something that will benefit other developers for no
    charge neccessary. While the code provided here is almost a straight copy
    from the official documentation, I purposely kept it very bare-bones so that
    you can customize the GUI yourself. I hope that by sharing this with others, the overall quality of all Ren'Py games will improve.
    \n
    Unfortunately, as of this writing, there were a few bumps in the road with some of the features I wanted to add. Different fonts have different line_spacing properties, so in trying to automatically adjust it for each typeface, it caused bugs in the way the radio buttons were being shown. I'll be working on finding a fix for that, but for now I hope this update helps.
    \n
    Thank you for taking the time to read this, and I wish you the best on your
    development adventures to come.""")

## Achievements screen ######################################
##
## This custom screen contains a list of achievements for the game.
## Official Documentation: https://www.renpy.org/doc/html/achievement.html
## Additional writeup by bobcgames:
## Part 1: http://bobcgames.com/blog/archives/48/
## Part 2: http://bobcgames.com/blog/archives/54/
## Roselia Achievements Module: https://github.com/OlegWock/Roselia-achievements/

## List achievements that are either True or False here
python early:
    simple_achievement_list = (
        # ("Achievement Name", "Description when not unlocked", "Description when unlocked"),
        ("A New Beginning", "???", "Enter your new life."),
        ("Day One - Moving Day", "???", "Complete your first day in Olis."),
        #("Day 2 - Bonding Time", "???", "Spend the second day building furniture with Amelia."),
        ("Final Moments", "???", "Watch the sunset and complete the game."),
        ("Lookin' Real Smug Here!", "???", "Why are you looking smug Lily?"),
    )

## Registers your achievements to work on backend systems such as Steam
## Be sure to match the name of the achievement in achievement_list and
## the corresponding achievement.grant or achievement.progress in the script.
## Notes for testing: you need at least 2 achievements for it to work

## Our actual achievements screen
screen achievements():

    tag menu

    ## This use statement includes the extras_menu screen inside this one. The
    ## vbox child is then included inside the viewport inside the extras_menu
    ## screen.
    use extras_menu(_("Achievements"), scroll="viewport"):

        ## This screen doesn't need anything fancy, so we borrow the style
        ## from the About screen, which just displays text.
        style_prefix "about"

        vbox:

            ## This auto-populates our list of simple achievements that will appear
            ## in the screen, so we don't have to manually type each one out.
            for aname, lockdesc, unlockdesc in simple_achievement_list:

                if achievement.has(aname):
                    text "[aname]: [unlockdesc]"
                    add "sans_titre.png"
                else:
                    text "[aname]: [lockdesc]"
                    add "sans_titre.png"

## End Credits Scroll ############################################################
## ATL for scrolling screen object. In this case, credits roll.
## Speed is the time for object to move up from initial ypos to finish ypos.

## Code Source: https://lemmasoft.renai.us/forums/viewtopic.php?t=42667

transform credits_scroll(speed):
    ypos 600
    linear speed ypos -600
    ## Adjust these numbers to be the height of your end credits. Both numbers
    ## should be the same.

## Credits screen.

screen credits():

    ## Ensure that the game_menu screens don't appear and interrupt the credits.
    key "K_ESCAPE" action NullAction()
    key "K_MENU" action NullAction()
    key "mouseup_3" action NullAction()

    style_prefix "credits"

    ## If a player has seen the end credits before, this button appears.
    if persistent.credits_seen:

        textbutton _("Skip Credits") action Jump("skip_credits") xalign 1.0 yalign 1.0

transform credits_scroll(speed):
    ypos 720
    linear speed ypos -720

## Credits screen.

screen credits():
    style_prefix "credits"

    add "#000"

    frame at credits_scroll(1.0):
        background None
        xalign 0.5

        vbox:
            label "Credits"

            null height 20

            hbox:
                text "Role 1"
                text "NAME 1"

            hbox:
                text "Role 2"
                text "NAME 2"

            null height 300

            text "Producer" size 70
            null height 50
            text "BáiYù"

            #null height 200

            # text "Logo" size 100
            # null height 50
            # text "Lorem Ipsum"

            #null height 200

            # text "Script" size 100
            # null height 50
            # text "Lorem Ipsum"

            null height 200

            text "Art" size 70
            null height 50

            text "Mannequin by HelloAR14"

            null height 50

            text "Uncle Mugen"

            null height 200

            text "Soundtrack" size 70
            null height 50

            text "Eric Matyas"

            null height 200

            # text "GUI Template" size 100
            text "Programming" size 70
            null height 50

            hbox:

                xalign 0.5
                spacing 200

                text "BáiYù"

                text "bobcgames"

            null height 50

            hbox:

                xalign 0.5
                spacing 200

                text "minute"

                text "npckc"

            null height 200

            # text "Trailer" size 100
            # null height 50
            # text "Lorem Ipsum"

            # null height 200

            # text "Voiceover" size 100
            # null height 50

            # hbox:
            #     xalign 0.5
            #     spacing 250

            #     vbox:

            #         text "Lorem Ipsum"

            #     vbox:

            #         text "Lorem Ipsum"

            # null height 200

            # text "Backers" size 100
            # null height 50

            # hbox:

            #     xalign 0.5
            #     spacing 100
            #     style_prefix "backercredits"

            #     vbox:

            #         text "Lorem Ipsum"

            #     vbox:

            #         text "Lorem Ipsum"

            #     vbox:

            #         text "Lorem Ipsum"

            text "Made with Ren'Py [renpy.version_only]." size 70

            null height 450

            text "Thanks for Playing!" size 70




style credits_hbox:
    spacing 40
    ysize 30

style credits_label:
    xalign 0.5

style credits_text:
    xalign 0.5

## Show credits screen.

style credits_hbox:
    spacing 40
    ysize 30

style credits_label_text:
    xalign 0.5
    size 100
    text_align 0.5

style credits_text:
    xalign 0.5
    size 50
    justify True
    text_align 0.5

style backercredits_text:
    xalign 0.5
    size 35
    justify True
    text_align 0.5


## TODO: Figure out how to get total game time working properly
## https://lemmasoft.renai.us/forums/viewtopic.php?t=40407
## Official Documentation of function: https://www.renpy.org/doc/html/other.html#renpy.get_game_runtime

# default playtime = 0

# init 2 python:

#     def total_playtime(d):
#         renpy.store.playtime += renpy.get_game_runtime()
#         #renpy.clear_game_runtime()
#         d["playtime"] = renpy.store.playtime

    # config.save_json_callbacks = [total_playtime]

################################################################################
## Mobile Variants
################################################################################

style pref_vbox:
    variant "medium"
    xsize 675

## Since a mouse may not be present, we replace the quick menu with a version
## that uses fewer and bigger buttons that are easier to touch.
screen quick_menu():
    variant "touch"

    zorder 100
    # Add an in-game quick menu.
    if quick_menu:

        hbox:
            style_prefix "quick"

            xalign 0.5
            yalign 1.0

            textbutton _("Back") action Rollback()
            textbutton _("Skip") action Skip() alternate Skip(fast=True, confirm=True)
            textbutton _("Auto") action Preference("auto-forward", "toggle")
            textbutton _("Prefs") action ShowMenu("preferences")


style say_dialogue:
    variant "small"
    size gui.preference("phone_size", 40)

style window:
    variant "small"
    background gui.preference("m_ADVtextbox", "gui/phone/textbox_1.png")
    #background "gui/phone/textbox.png"

style radio_button:
    variant "small"
    foreground "gui/phone/button/radio_[prefix_]foreground.png"

style check_button:
    variant "small"
    foreground "gui/phone/button/check_[prefix_]foreground.png"

style nvl_window:
    variant "small"
    background gui.preference("m_NVLtextbox", "gui/phone/nvl_1.png") #"gui/phone/nvl.png"

style main_menu_frame:
    variant "small"
    background "gui/phone/overlay/main_menu.png"

style game_menu_outer_frame:
    variant "small"
    background "gui/phone/overlay/game_menu.png"

style game_menu_navigation_frame:
    variant "small"
    xsize 510

style game_menu_content_frame:
    variant "small"
    top_margin 0

# style game_menu_text:
#     variant "mobile"
#     size 33 #45

# style game_menu_label_text:
#     variant "mobile"
#     size 51
style pref_vbox:
    variant "small"
    xsize 600

# style bar:
#     variant "small"
#     ysize gui.bar_size
#     left_bar Frame("gui/phone/bar/left.png", gui.bar_borders, tile=gui.bar_tile)
#     right_bar Frame("gui/phone/bar/right.png", gui.bar_borders, tile=gui.bar_tile)

# style vbar:
#     variant "small"
#     xsize gui.bar_size
#     top_bar Frame("gui/phone/bar/top.png", gui.vbar_borders, tile=gui.bar_tile)
#     bottom_bar Frame("gui/phone/bar/bottom.png", gui.vbar_borders, tile=gui.bar_tile)

# style scrollbar:
#     variant "small"
#     ysize gui.scrollbar_size
#     base_bar Frame("gui/phone/scrollbar/horizontal_[prefix_]bar.png", gui.scrollbar_borders, tile=gui.scrollbar_tile)
#     thumb Frame("gui/phone/scrollbar/horizontal_[prefix_]thumb.png", gui.scrollbar_borders, tile=gui.scrollbar_tile)

style vscrollbar:
    variant "small"
    xsize gui.scrollbar_size
    base_bar Frame("gui/phone/scrollbar/vertical_[prefix_]bar.png", gui.vscrollbar_borders, tile=gui.scrollbar_tile)
    thumb Frame("gui/phone/scrollbar/vertical_[prefix_]thumb.png", gui.vscrollbar_borders, tile=gui.scrollbar_tile)

# style slider:
    # variant "small"
    # ysize gui.slider_size
    # base_bar Frame("gui/phone/slider/horizontal_[prefix_]bar.png", gui.slider_borders, tile=gui.slider_tile)
    # thumb "gui/phone/slider/horizontal_[prefix_]thumb.png"

style vslider:
    variant "small"
    xsize gui.slider_size
    base_bar Frame("gui/phone/slider/vertical_[prefix_]bar.png", gui.vslider_borders, tile=gui.slider_tile)
    thumb "gui/phone/slider/vertical_[prefix_]thumb.png"

style slider_pref_vbox:
    variant "small"
    xsize None

style slider_pref_slider:
    variant "small"
    xsize 900
