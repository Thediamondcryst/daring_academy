init -20 python:
    import discord_rpc
    import time

    def readyCallback(current_user):
        print('Our user: {}'.format(current_user))

    def disconnectedCallback(codeno, codemsg):
        print('Disconnected from Discord rich presence RPC. Code {}: {}'.format(
            codeno, codemsg
        ))

    def errorCallback(errno, errmsg):
        print('An error occurred! Error {}: {}'.format(
            errno, errmsg
        ))

label before_main_menu:
    python:
        # Note: 'event_name': callback
        callbacks = {
            'ready': readyCallback,
            'disconnected': disconnectedCallback,
            'error': errorCallback,
        }
        discord_rpc.initialize('789321686985736232', callbacks=callbacks, log=False)
        start = time.time()
        print(start)
        discord_rpc.update_connection()
        discord_rpc.run_callbacks()
        discord_rpc.update_presence(
            **{
                'details': 'Main Menu',
                'start_timestamp': start,
                'large_image_key': 'daringacademy'
            }
        )
        discord_rpc.update_connection()
        discord_rpc.run_callbacks()

    return

# The script of the game goes in this file.
# Declare characters used by this game. The color argument colorizes the
# name of the character.
define s = Character("???", who_color="#FFFFFF")
define u = Character("You", who_color="#1CFFEF")
define rp = Character("Receptionist", who_color="#45FFC2")
define wt = Character("Waitress", who_color="#45FF4F")
define au = Character("Amelia & You", who_color="#FFA1FF")
define ch = Character("Cashier", who_color="#7BFF83")
define nar_nvl = nvl_narrator


label start:
    # Developper Testing stuff.
    $ amelia_drunk = 0
    $ y = "Test Name"
    $ nk = "Test Nick"
    # This code controls the discord integration.
    python:
        callbacks = {
            'ready': readyCallback,
            'disconnected': disconnectedCallback,
            'error': errorCallback,
        }
        discord_rpc.initialize('789321686985736232', callbacks=callbacks, log=False)
        start = time.time()
        discord_rpc.update_connection()
        discord_rpc.run_callbacks()
        discord_rpc.update_presence(
            **{
                'details': 'Spirit World',
                'state': 'Customizing their character...',
                'large_image_key': 'spiritworld',
                'small_image_key': 'daringacademy',
                'start_timestamp': start
            }
        )

        discord_rpc.update_connection()
        discord_rpc.run_callbacks()
    # The real start of the game.
    scene spirit_world
    s "This game contains choices that depend on your opinion. In order to actually have a pleasant experience, please help me know you by giving me some information."
    s "What is your gender?"
    menu:
        "Boy":
            $ mainGender = 0
        "Girl":
            $ mainGender = 1
        "Non-Binary":
            $ mainGender = 2
    s "Now, what is your name?"
    if mainGender == 0:
        $ y = renpy.input("What is your name? (If no imputs are entered, it will be defaulted to 'Lee'.)")
        if y == "":
            $ y = "Lee"
    if mainGender == 1:
        $ y = renpy.input("What is your name? (If no imputs are entered, it will be defaulted to 'Layla'.)")
        if y == "":
            $ y = "Layla"
    if mainGender == 2:
        $ y = renpy.input("What is your name? (If no imputs are entered, it will be defaulted to 'Lenny'.)")
        if y == "":
            $ y = "Lenny"
    s "Lovely name! Greetings [y]. Can you also say a nickname too?"
    if mainGender == 0:
        $ nk = renpy.input("What is your nickname? (If no imputs are entered, it will be defaulted to 'Lee'.)")
        if nk == "":
            $ nk = "Lee"
    if mainGender == 1:
        $ nk = renpy.input("What is your nickname? (If no imputs are entered, it will be defaulted to 'Lay'.)")
        if nk == "":
            $ nk = "Lay"
    if mainGender == 2:
        $ nk = renpy.input("What is your nickname? (If no imputs are entered, it will be defaulted to 'Len'.)")
        if nk == "":
            $ nk = "Len"
    s "Thank you for this information! Now, please enjoy the wonderful and crazy world of Daring Academy."
    jump day_1_morning_apartment
    with fade


## Under this is Day 1 (Scene 1-3)
label day_1_morning_apartment:
    python:
        start = time.time()
        discord_rpc.update_connection()
        discord_rpc.run_callbacks()
        discord_rpc.update_presence(
            **{
                'details': 'Day 1',
                'state': 'Morning',
                'large_image_key': 'apartmentmoveinday',
                'small_image_key': 'daringacademy',
                'start_timestamp': start
            }
        )

        discord_rpc.update_connection()
        discord_rpc.run_callbacks()
    # This unlocks the the achievement with the corresponding name
    $ play_sound(notification)
    $ play_music(homeland)
    $ achievement.grant("A New Beginning")
    show screen achievement("a_new_beginning_achievement_pop_up.png")
    scene apartment_moving_in_day with dissolve
    show amelia_base
    show eyebrows_amelia_normal
    show blink_random_normal_amelia
    show talking_amelia_normal
    a "Just here?"
    hide talking_amelia_normal
    show smile_closed_amelia_normal
    u "Yep, just here, mate."
    "This is Amelia Sweet. We met when we were kids at the Shining Diamond Elementary school in Hora. 13 years later and we're still friends."
    "Ever since I met her, she's always here for me. When life's hard, she listens to me, gives advice and just cares for me."
    "{i}Amelia placed the box next to the couch. She sighed.{/i}"
    show talking_amelia_normal
    hide smile_closed_amelia_normal
    a "Man, I'm exhausted!"
    hide talking_amelia_normal
    show smile_closed_amelia_normal
    u "Whatchu wanna get for dinner?"
    show talking_amelia_normal
    hide smile_closed_amelia_normal
    a "What about some Thai Breakers?"
    hide talking_amelia_normal
    show smile_closed_amelia_normal
    "{i}'Thai Breakers' is a big chinese-inspired restaurant in Olis, which uses the fish brought from Pezco, a mainly fishing oriented country.{/i}"
    menu:
        "Yeah!":
            $ ameliatrust =+ 1
            $ thai = 1
            u "Some Thai does sound good right now, yeah!"
            "{i}You increased {b}Amelia{/b}'s Trust: +1 Trust.{/i}"
            jump restaurant_choice_amelia
        "Nah, sorry.":
            $ ameliatrust = 0
            $ thai = 0
            u "Hmm, I'm not sure honestly."
            jump restaurant_choice_amelia

label restaurant_choice_amelia:
    if ameliatrust > 0:
        hide smile_closed_amelia_normal
        show talking_amelia_normal
        hide blink_random_normal_amelia
        show closed_eyes_amelia_normal
        a "Well, what are you waiting on man? Let's go!"
        jump dress
    if ameliatrust < 1:
        show talking_amelia_normal
        hide smile_closed_amelia_normal
        a "That's ok. I know that it's very expensive. Anything else you want to do?"
        hide talking_amelia_normal
        show smile_closed_amelia_normal
        menu:
            "Burger":
                nvl clear
                $ ameliafood = 0
                u "Well there's a restaurant called 'Daisy's Tavern' which sells burgers, pizzas, steaks, tacos and more. I thought we could get some burgers. What do you think?"
                show talking_amelia_normal
                hide smile_closed_amelia_normal
                a "Sounds good to me!"
                hide talking_amelia_normal
                show smile_closed_amelia_normal
                u "Well, what are you waiting on girl? Let's go!"
                jump dress
            "Pizza":
                nvl clear
                $ ameliafood = 1
                u "Well there's a restaurant called 'Daisy's Tavern' which sells burgers, pizzas, steaks, tacos and more. I thought we could get some pizza. What do you think?"
                hide smile_closed_amelia_normal
                show talking_amelia_normal
                hide blink_random_normal_amelia
                show closed_eyes_amelia_normal
                $ amelialove =+ 1
                a "Yes, pizza! Well, let's go!"
                "{i}You increased {b}Amelia{/b}'s Love: +1 Love.{/i}"
                hide talking_amelia_normal
                show smile_amelia_normal
                u "Alright!"
                jump dress
            "Steak":
                nvl clear
                $ ameliafood = 2
                u "Well there's a restaurant called 'Daisy's Tavern' which sells burgers, pizzas, steaks, tacos and more. I thought we could get some steak. What do you think?"
                show talking_amelia_normal
                hide smile_closed_amelia_normal
                a "I guess this is fine."
                hide talking_amelia_normal
                show smile_closed_amelia_normal
                u "Well, what are you waiting on girl? Let's go!"
                jump dress
            "Taco":
                nvl clear
                u "Well there's a restaurant called 'Daisy's Tavern' which sells burgers, pizzas, steaks, tacos and more. I thought we could get some tacos. What do you think?"
                show worried_mouth_talking_amelia_normal
                hide smile_closed_amelia_normal
                a "Can I get something else? I don't really like tacos."
                hide amelia_talking
                show worried_mouth_amelia_normal
                menu:
                    "Burgers":
                        $ ameliafood = 0
                        u "Well thought we could get some burgers. What do you think?"
                        show talking_amelia_normal
                        hide smile_closed_amelia_normal
                        a "Sounds good to me!"
                        hide talking_amelia_normal
                        show smile_closed_amelia_normal
                        u "Well, what are you waiting on girl? Let's go!"
                        jump dress
                    "Pizza":
                        nvl clear
                        $ ameliafood = 1
                        u "Well I thought we could get some pizza. What do you think?"
                        hide worried_mouth_amelia_normal
                        show talking_amelia_normal
                        hide blink_random_normal_amelia
                        show closed_eyes_amelia_normal
                        $ amelialove =+ 1
                        a "Yes, pizza! Well, let's go!"
                        "{i}You increased {b}Amelia{/b}'s Love: +1 Love.{/i}"
                        hide talking_amelia_normal
                        show smile_amelia_normal
                        u "Alright!"
                        jump dress
                    "Steak":
                        nvl clear
                        $ ameliafood = 2
                        u "Well, I thought we could get some steak. What do you think?"
                        show talking_amelia_normal
                        hide worried_mouth_amelia_normal
                        a "I guess this is fine."
                        hide talking_amelia_normal
                        show smile_closed_amelia_normal
                        u "Well, what are you waiting on girl? Let's go!"
                        jump dress

label dress:
    show talking_amelia_normal
    hide smile_closed_amelia_normal
    hide smile_amelia_normal
    hide closed_eyes_amelia_normal
    show blink_random_normal_amelia
    a "Wait, should I change into a fancy dress?"
    hide talking_amelia_normal
    show smile_closed_amelia_normal
    menu:
        "Sure thing":
            u "Yeah, why not. Do you have a dress tho?"
            show talking_amelia_normal
            hide smile_closed_amelia_normal
            a "I actually do, but it's my last one. Mind going shopping tomorrow?"
            hide talking_amelia_normal
            show smile_closed_amelia_normal
            "I shrugged."
            hide smile_closed_amelia_normal
            hide smile_amelia_normal
            hide closed_eyes_amelia_normal
            hide blink_random_normal_amelia
            hide eyebrows_amelia_normal
            hide amelia_base
            show amelia_talking
            a "Sounds good to me! Wait here."
            hide amelia_talking with moveoutleft
            "I rose my voice."
            u "I'll get my keys, okay?"
            a "Okay, don't leave me tho!"
            "I looked in my coat: Not there. Under the TV? Negative. Pocket? Yup, found them."
            "I heard Amelia say something."
            a "You found them?"
            u "I did, are you done mate?"
            "She opened the bathroom door dressed in a pink v-neck sweetheart halter and a peony in her hair."
            show amelia_talking_dress with moveinleft
            a "Am I done, you think?"
            hide amelia_talking_dress
            show amelia_base_dress
            show blink_random_normal_amelia
            show eyebrows_amelia_normal
            show smile_closed_amelia_normal
            "I couldn't say anything, her dress just fitted her so much."
            hide smile_closed_amelia_normal
            show worried_mouth_talking_amelia_normal
            a "Hello?"
            hide worried_mouth_talking_amelia_normal
            show worried_mouth_amelia_normal
            u "Oh sorry, couldn't focus. The dress really fits you."
            hide worried_mouth_amelia_normal
            show smile_closed_amelia_normal
            "She blushed."
            hide smile_closed_amelia_normal
            show blush_amelia_normal
            show talking_amelia_normal
            hide blink_random_normal_amelia
            show closed_eyes_amelia_normal
            a "Thank you!"
            hide talking_amelia_normal
            show smile_closed_amelia_normal
            u "Anything you're missing?"
            show blink_random_normal_amelia
            hide closed_eyes_amelia_normal
            hide blush_amelia_normal with dissolve
            "She looked at her purse."
            hide smile_closed_amelia_normal
            show talking_amelia_normal
            a "No, I don't think so."
            hide talking_amelia_normal
            show smile_closed_amelia_normal
            u "Well, let's go then!"
            $ amelia_dress = 1
        "No need":
            u "We're not going for long, you don't need one."
            show talking_amelia_normal
            hide smile_closed_amelia_normal
            a "Yeah, you're right."
            hide talking_amelia_normal
            show smile_closed_amelia_normal
            u "Do you have some stuff to do before we leave?"
            hide smile_closed_amelia_normal
            hide smile_amelia_normal
            hide closed_eyes_amelia_normal
            hide blink_random_normal_amelia
            hide eyebrows_amelia_normal
            hide amelia_base
            show amelia_talking
            a "Oh yeah, I need to go to the bathroom, hold on."
            hide amelia_talking with moveoutleft
            "She started to walk to the bathroom door. I rose my voice."
            u "I'll get my keys, okay?"
            a "Okay, don't leave me tho!"
            "I looked in my coat: Not there. Under the TV? Negative. Pocket? Yup, found them."
            "I heard Amelia say something."
            a "You found them?"
            u "I did, are you done mate?"
            a "Not yet."
            u "Alright."
            "I took out my phone and started up the 'Monster Orb TCG Online' app."
            u "Okay... Hmm. Wait, new ban list? Strike was banned. Interesting. So that means I need to edit my Ignitar altar... Great..."
            "I started up the altar editor. At this point, she opened the bathroom door holding a towel."
            show amelia_talking with moveinleft
            a "I'm done."
            hide amelia_talking
            show amelia_base
            show blink_random_normal_amelia
            show eyebrows_amelia_normal
            show smile_closed_amelia_normal
            u "Well, let's go then!"
            $ amelia_dress = 0
    jump restaurant_scene_amelia
    with fade

## Under this is Scene 2
label restaurant_scene_amelia:
    python:
        start = time.time()
        discord_rpc.update_connection()
        discord_rpc.run_callbacks()
        discord_rpc.update_presence(
            **{
                'details': 'Day 1',
                'state': 'At restaurant',
                'large_image_key': 'restaurantday',
                'small_image_key': 'daringacademy',
                'start_timestamp': start
            }
        )

        discord_rpc.update_connection()
        discord_rpc.run_callbacks()
    scene restaurant with dissolve
    "We arrive at the restaurant."
    if thai > 0:
        "Amelia and I stood in line. Silence grew on us, so I broke it."
        u "Hey man?"
        if amelia_dress == 1:
            show amelia_base_dress
        if amelia_dress == 0:
            show amelia_base
        show blink_random_normal_amelia
        show eyebrows_amelia_normal
        show smile_closed_amelia_normal
        a "Hmm?"
        u "Would you rather be the smartest moron or dumbest genius?"
        show talking_amelia_normal
        hide smile_closed_amelia_normal
        a "Oh man, erm..."
        hide talking_amelia_normal
        show smile_closed_amelia_normal
        "She hesitated for a few seconds."
        show talking_amelia_normal
        hide smile_closed_amelia_normal
        a "I would say... The dumbest moron? Because if I'm a genius I'm still smart and a genius. And wait a minute, did you hit me with a paradox?"
        hide talking_amelia_normal
        show smile_closed_amelia_normal
        u "Yup."
        s "Nah sorry mate, that's not a paradox. Good question tho."
        "I just smiled."
        u "Well I would be..."
        menu:
            "Smartest Moron":
                u "I would be the smartest moron, since I would know I'm a smart moron, but just like everyone, I would make dumb mistakes... Just too frequently."
            "Dumbest Genius":
                u "I would be the dumbest genius, since I would be still above society, above normal people, even if I'm not like, I don't know, a reincarnation of Albert Einstein."
            "None":
                u "Honestly, even if you're the dumbest genius or the smartest moron, everyone makes some sort of dumb actions or are dumb in some ways, but not everyone can be a genius..."
                u "...no matter how long you study to become one."
        show talking_amelia_normal
        hide smile_closed_amelia_normal
        a "Interesting answer man."
        hide talking_amelia_normal
        show smile_closed_amelia_normal
        u "And you know, we're just all-"
        ch "Come here."
        "We looked around a bit. The line has disappeared, only leaving myself, Amelia and the cashier. We walked up to them."
        hide amelia_base
        hide amelia_base_dress
        hide blink_random_normal_amelia
        hide eyebrows_amelia_normal
        hide smile_closed_amelia_normal
        show cashier_frank_talking
        ch "Welcome to Thai Breakers, my name is Frank. What can I do for you?"
        hide cashier_frank_talking
        if amelia_dress == 1:
            show amelia_base_dress
        if amelia_dress == 0:
            show amelia_base
        show blink_random_normal_amelia
        show eyebrows_amelia_normal
        show talking_amelia_normal
        a "Yeah, I would like to take some Khao Pod Tod and some chicken noodle soup please."
        hide talking_amelia_normal
        hide amelia_base
        hide amelia_base_dress
        hide blink_random_normal_amelia
        hide eyebrows_amelia_normal
        show cashier_frank_talking
        ch "That will be $9,78. Any drinks?"
        hide cashier_frank_talking
        if amelia_dress == 1:
            show amelia_base_dress
        if amelia_dress == 0:
            show amelia_base
        show blink_random_normal_amelia
        show eyebrows_amelia_normal
        show talking_amelia_normal
        a "Oh yeah, medium Coke please."
        hide talking_amelia_normal
        hide amelia_base
        hide amelia_base_dress
        hide blink_random_normal_amelia
        hide eyebrows_amelia_normal
        show cashier_frank_talking
        ch "That will be $11,26."
        hide cashier_frank_talking
        show cashier_frank_smiling
        y "I'll just get some red curry soup and a medium Coke."
        hide cashier_frank_smiling
        show cashier_frank_talking
        ch "Okay, that will be $25,69. Will you pay in cash or card?"
        hide cashier_frank_talking
        show cashier_frank_smiling
        "Amelia and I looked at each other."
        hide cashier_frank_smiling
        if amelia_dress == 1:
            show amelia_base_dress
        if amelia_dress == 0:
            show amelia_base
        show blink_random_normal_amelia
        show eyebrows_amelia_normal
        show talking_amelia_normal
        a "So who will pay?"
        hide talking_amelia_normal
        show smile_closed_amelia_normal
        "I decided to stand up (Not physically.)"
        u "I will."
        hide smile_closed_amelia_normal
        hide amelia_base
        hide amelia_base_dress
        hide blink_random_normal_amelia
        hide eyebrows_amelia_normal
        show cashier_frank_talking
        ch "Oh."
        hide cashier_frank_talking
        show cashier_frank_smiling
        "The cashier looked at me."
        hide cashier_frank_smiling
        show cashier_frank_talking
        ch "Will you pay in cash or card?"
        hide cashier_frank_talking
        show cashier_frank_smiling
        u "Card, please."
        "I slid my credit card on the credit card scanner. The transaction went through and was approved with no issues."
        hide cashier_frank_smiling
        show cashier_frank_talking
        ch "Your food will be ready in around 20 minutes. Your drinks are coming really soon."
        hide cashier_frank_talking with dissolve
        "Amelia and I sat down at a table."
    else:
        "We saw a receptionist waiving at us. We decided to see him."
        show receptionist_dave_talking
        rp "Welcome to Daisy's Tavern, my name is Dave. What can I do for you?"
        hide receptionist_dave_talking
        show receptionist_dave_smiling
        u "Uh yeah, I would like to have a table for 2 please?"
        if mainGender == 0:
            hide receptionist_dave_smiling
            show receptionist_dave_talking
            rp "Sure thing. Right this way mister."
            hide receptionist_dave_talking
            show receptionist_dave_smiling
        if mainGender == 1:
            hide receptionist_dave_smiling
            show receptionist_dave_talking
            rp "Sure thing. Right this way ma'am."
            hide receptionist_dave_talking
            show receptionist_dave_smiling
        if mainGender == 2:
            hide receptionist_dave_smiling
            show receptionist_dave_talking
            rp "Sure thing. Right this way."
            hide receptionist_dave_talking
            show receptionist_dave_smiling
        "The receptionist showed us an empty table. Amelia and I sat down at that table."
        hide receptionist_dave_smiling with moveoutleft
        u "Hey man?"
        if amelia_dress == 1:
            show amelia_base_dress
        if amelia_dress == 0:
             show amelia_base
        show blink_random_normal_amelia
        show eyebrows_amelia_normal
        show smile_closed_amelia_normal
        a "Hmm?"
        u "Would you rather be the smartest moron or dumbest genius?"
        show talking_amelia_normal
        hide smile_closed_amelia_normal
        a "Oh man, erm..."
        hide talking_amelia_normal
        show smile_closed_amelia_normal
        "She hesitated for a few seconds."
        show talking_amelia_normal
        hide smile_closed_amelia_normal
        a "I would say... The dumbest moron? Because if I'm a genius I'm still smart and a genius. And wait a minute, did you hit me with a paradox?"
        hide talking_amelia_normal
        show smile_closed_amelia_normal
        u "Yup."
        s "Nah sorry mate, that's not a paradox. Good question tho."
        "I just smiled."
        u "Well I would be..."
        menu:
            "Smartest Moron":
                u "I would be the smartest moron, since I would know I'm a smart moron, but just like everyone, I would make dumb mistakes... Just too frequently."
            "Dumbest Genius":
                u "I would be the dumbest genius, since I would be still above society, above normal people, even if I'm not like, I don't know, a reincarnation of Albert Einstein."
            "None":
                u "Honestly, even if you're the dumbest genius or the smartest moron, everyone makes some sort of dumb actions or are dumb in some ways, but not everyone can be a genius, no matter how long you study to become one."
        show talking_amelia_normal
        hide smile_closed_amelia_normal
        a "Interesting answer man."
        hide talking_amelia_normal
        show smile_closed_amelia_normal
        u "And you know, we're just all-"
        wt "Excuse me, are you guys here to order?"
        "A waitress interrupted us."
        hide smile_closed_amelia_normal
        hide amelia_base
        hide amelia_base_dress
        hide blink_random_normal_amelia
        hide eyebrows_amelia_normal
        show waitress_amora_talking
        wt "Welcome to Daisy's Tavern, my name is Amora. I'll be serving you today. What can I do for you?"
        hide waitress_amora_talking
        if amelia_dress == 1:
            show amelia_base_dress
        if amelia_dress == 0:
            show amelia_base
        show blink_random_normal_amelia
        show eyebrows_amelia_normal
        show talking_amelia_normal
        a "I would like to take one burger."
        hide talking_amelia_normal
        hide amelia_base
        hide amelia_base_dress
        hide blink_random_normal_amelia
        hide eyebrows_amelia_normal
        show waitress_amora_talking
        wt "What type of burger? We have 'The Classic' with a patty, a sauce of your choice, lettuce, tomatoes and all that stuff, we also have 'The Double' and 'The Triple'."
        wt "Or if you wanna go all out, we have 'The One', a bur..."
        hide waitress_amora_talking
        if amelia_dress == 1:
            show amelia_base_dress
        if amelia_dress == 0:
            show amelia_base
        show blink_random_normal_amelia
        show eyebrows_amelia_normal
        show talking_amelia_normal
        a "'The One' sounds like a good one, I'll take that!"
        hide talking_amelia_normal
        hide amelia_base
        hide amelia_base_dress
        hide blink_random_normal_amelia
        hide eyebrows_amelia_normal
        show waitress_amora_talking
        wt "Want fries with it?"
        hide waitress_amora_talking
        if amelia_dress == 1:
            show amelia_base_dress
        if amelia_dress == 0:
            show amelia_base
        show blink_random_normal_amelia
        show eyebrows_amelia_normal
        show talking_amelia_normal
        a "Yes please!"
        hide talking_amelia_normal
        hide amelia_base
        hide amelia_base_dress
        hide blink_random_normal_amelia
        hide eyebrows_amelia_normal
        show waitress_amora_talking
        wt "Drink, ma'am?"
        hide waitress_amora_talking
        if amelia_dress == 1:
            show amelia_base_dress
        if amelia_dress == 0:
            show amelia_base
        show blink_random_normal_amelia
        show eyebrows_amelia_normal
        show talking_amelia_normal
        a "What are the options?"
        hide talking_amelia_normal
        hide amelia_base
        hide amelia_base_dress
        hide blink_random_normal_amelia
        hide eyebrows_amelia_normal
        show waitress_amora_talking
        wt "So we have Coke, Pepsi, and their diet form, water, carbonized water, different types of juices, ice tea, or you could get some of our alcohol, like beer, whisky, etc."
        hide waitress_amora_talking
        if amelia_dress == 1:
            show amelia_base_dress
        if amelia_dress == 0:
            show amelia_base
        show blink_random_normal_amelia
        show eyebrows_amelia_normal
        show talking_amelia_normal
        "Amelia turns to me."
        hide smile_closed_amelia_normal
        show talking_amelia_normal
        a "Should we get a bit of alcohol?"
        hide talking_amelia_normal
        show smile_closed_amelia_normal
        menu:
            "Order alcohol for Amelia":
                $ amelia_drunk = 1
                u "Yeah, why not, right? I mean, we're not driving home, so that's not an issue."
                "Amelia turned to the waiter."
                hide smile_closed_amelia_normal
                show talking_amelia_normal
                a "I will take one medium size beer. You [nk]?"
                hide talking_amelia_normal
                show smile_closed_amelia_normal
                menu:
                    "Do the same":
                        nvl clear
                        u "I'll also get the same thing. One beer for me too."
                        hide smile_closed_amelia_normal
                        hide amelia_base
                        hide amelia_base_dress
                        hide blink_random_normal_amelia
                        hide eyebrows_amelia_normal
                        show waitress_amora_talking
                        wt "What size?"
                        hide waitress_amora_talking
                        show waitress_amora_smiling
                        menu:
                            "Small":
                                u "Small, please."
                            "Medium":
                                u "Medium, like her."
                            "Large":
                                u "A large beer would be appreciated."
                            "Extra Large":
                                u "Why not extra large."
                                hide waitress_amora_smiling
                                if amelia_dress == 1:
                                    show amelia_base_dress
                                if amelia_dress == 0:
                                    show amelia_base
                                show blink_random_normal_amelia
                                show eyebrows_amelia_normal
                                show talking_amelia_normal
                                a "You're really gonna drink all that?"
                                hide talking_amelia_normal
                                show smile_closed_amelia_normal
                                u "Well, we'll see."
                    "Take another drink":
                        u "No, thank you, I'll pass on the alcohol, I'll take..."
                        $ drink = renpy.input("What drink do you want?")
                        if drink == "":
                            "Please enter a drink."
                        u "I'll get some [drink]."
                        if mainGender == 0:
                            hide amelia_base
                            hide amelia_base_dress
                            hide blink_random_normal_amelia
                            hide eyebrows_amelia_normal
                            hide smile_closed_amelia_normal
                            show waitress_amora_talking
                            wt "No problem mister."
                            hide waitress_amora_talking
                            show waitress_amora_smiling
                        if mainGender == 1:
                            hide amelia_base
                            hide amelia_base_dress
                            hide blink_random_normal_amelia
                            hide eyebrows_amelia_normal
                            hide smile_closed_amelia_normal
                            show waitress_amora_talking
                            wt "No problem ma'am."
                            hide waitress_amora_talking
                            show waitress_amora_smiling
                        if mainGender == 2:
                            hide amelia_base
                            hide amelia_base_dress
                            hide blink_random_normal_amelia
                            hide eyebrows_amelia_normal
                            hide smile_closed_amelia_normal
                            show waitress_amora_talking
                            wt "No problem."
                            hide waitress_amora_talking
                            show waitress_amora_smiling
                        hide waitress_amora_smiling
                        show waitress_amora_talking
                        wt "What size?"
                        hide waitress_amora_talking
                        show waitress_amora_smiling
                        menu:
                            "Small":
                                u "Small, please."
                            "Medium":
                                u "Medium, like her."
                            "Large":
                                u "A large [drink] would be appreciated."
                            "Extra Large":
                                u "Why not extra large."
                                hide waitress_amora_smiling
                                if amelia_dress == 1:
                                    show amelia_base_dress
                                if amelia_dress == 0:
                                    show amelia_base
                                show blink_random_normal_amelia
                                show eyebrows_amelia_normal
                                show talking_amelia_normal
                                hide smile_closed_amelia_normal
                                a "You're really gonna drink all that?"
                                hide talking_amelia_normal
                                show smile_closed_amelia_normal
                                u "Well, we'll see."
            "Stay sober":
                $ amelia_drunk = 0
                u "Maybe not Amelia, let's stay sober."
                "I look at her eyes and smiled."
                hide smile_closed_amelia_normal
                show talking_amelia_normal
                a "Yeah, you're right. I'll pass on the alcohol. I'll get some diet Coke instead."
                hide talking_amelia_normal
                hide amelia_base
                hide amelia_base_dress
                hide blink_random_normal_amelia
                hide eyebrows_amelia_normal
                show waitress_amora_talking
                wt "What size?"
                hide waitress_amora_talking
                if amelia_dress == 1:
                    show amelia_base_dress
                if amelia_dress == 0:
                    show amelia_base
                show blink_random_normal_amelia
                show eyebrows_amelia_normal
                show talking_amelia_normal
                a "Big."
                if mainGender == 0:
                    hide talking_amelia_normal
                    hide amelia_base
                    hide amelia_base_dress
                    hide blink_random_normal_amelia
                    hide eyebrows_amelia_normal
                    show waitress_amora_talking
                    wt "And you, mister?"
                if mainGender == 1:
                    hide talking_amelia_normal
                    hide amelia_base
                    hide amelia_base_dress
                    hide blink_random_normal_amelia
                    hide eyebrows_amelia_normal
                    show waitress_amora_talking
                    wt "And you, ma'am?"
                if mainGender == 2:
                    hide talking_amelia_normal
                    hide amelia_base
                    hide amelia_base_dress
                    hide blink_random_normal_amelia
                    hide eyebrows_amelia_normal
                    show waitress_amora_talking
                    wt "And you?"
                hide waitress_amora_talking
                show waitress_amora_smiling
                u "I'll take the same thing."
                hide waitress_amora_smiling
                show waitress_amora_talking
                wt "What size?"
                hide waitress_amora_talking
                show waitress_amora_smiling
                menu:
                    "Small":
                        u "Make it a small drink."
                    "Medium":
                        u "Make it a medium size drink."
                    "Large":
                        u "Make it a large one."
                    "Extra Large":
                        u "Make it an extra large diet Coke."
        "The waitress turned to me."
        hide talking_amelia_normal
        hide smiling
        hide amelia_base
        hide amelia_base_dress
        hide blink_random_normal_amelia
        hide eyebrows_amelia_normal
        hide waitress_amora_smiling
        show waitress_amora_talking
        wt "And you?"
        hide waitress_amora_talking
        show waitress_amora_smiling
        u "I'll take..."
        menu:
            "Burger":
                u "I would like a burger as well, like her."
                if mainGender == 0:
                    hide waitress_amora_smiling
                    show waitress_amora_talking
                    wt "One 'The One' for mister, got it."
                    hide waitress_amora_talking
                    show waitress_amora_smiling
                if mainGender == 1:
                    hide waitress_amora_smiling
                    show waitress_amora_talking
                    wt "One 'The One' for ma'am, got it."
                    hide waitress_amora_talking
                    show waitress_amora_smiling
                if mainGender == 2:
                    hide waitress_amora_smiling
                    show waitress_amora_talking
                    wt "One 'The One' for this person, got it."
                    hide waitress_amora_talking
                    show waitress_amora_smiling
            "Pizza":
                u "I would like to take 2 pizza slices please."
                hide waitress_amora_smiling
                show waitress_amora_talking
                wt "What type of pizza? We have the classic cheese or pepperoni pizzas, Neapolitan pizza, Chicago pizza, Hawaiian pizza, New York-Style pizza and others."
                hide waitress_amora_talking
                show waitress_amora_smiling
                menu:
                    "Cheese Pizza":
                        u "2 cheese pizza slices please."
                        hide waitress_amora_smiling
                        show waitress_amora_talking
                        wt "Cheese pizza, coming right up! Want fries with it?"
                        hide waitress_amora_talking
                        show waitress_amora_smiling
                    "Pepperoni Pizza":
                        u "No one can say anything bad about 2 slices of pepperoni pizza, eh? I'll take 2 of them."
                        hide waitress_amora_smiling
                        show waitress_amora_talking
                        wt "Pepperoni pizza, coming right up! Want fries with it?"
                        hide waitress_amora_talking
                        show waitress_amora_smiling
                    "Neapolitan Pizza":
                        u "The classic Neapolitan pizza, 2 slices please."
                        hide waitress_amora_smiling
                        show waitress_amora_talking
                        wt "Neapolitan pizza, coming right up! Want fries with it?"
                        hide waitress_amora_talking
                        show waitress_amora_smiling
                    "Chicago Pizza":
                        u "Why not Chicago?"
                        hide waitress_amora_smiling
                        show waitress_amora_talking
                        wt "Chicago pizza, coming right up! Want fries with it?"
                        hide waitress_amora_talking
                        show waitress_amora_smiling
                    "Hawaiian Pizza":
                        u "Is the Hawaiian pizza the one with pineapples on top?"
                        hide waitress_amora_smiling
                        show waitress_amora_talking
                        wt "Yes it is."
                        hide waitress_amora_talking
                        show waitress_amora_smiling
                        u "I'll take 2 slices then."
                        hide waitress_amora_smiling
                        show waitress_amora_talking
                        wt "Hawaiian pizza, coming right up! Want fries with it?"
                        hide waitress_amora_talking
                        show waitress_amora_smiling
                    "New York-Style Pizza":
                        u "New York, all the way!"
                        hide waitress_amora_smiling
                        show waitress_amora_talking
                        wt "New York-Style pizza, coming right up! Want fries with it?"
                        hide waitress_amora_talking
                        show waitress_amora_smiling
                u "Totally!"
            "Steak":
                u "One big steak please."
                hide waitress_amora_smiling
                show waitress_amora_talking
                wt "One big steak, coming right up! Want fries with it?"
                hide waitress_amora_talking
                show waitress_amora_smiling
                u "Yup."
            "Taco":
                u "I would like to take 3 tacos please."
                hide waitress_amora_smiling
                show waitress_amora_talking
                wt "Classic tacos?"
                hide waitress_amora_talking
                show waitress_amora_smiling
                u "Yes."
                hide waitress_amora_smiling
                show waitress_amora_talking
                wt "Want chips and salsa with it?"
                hide waitress_amora_talking
                show waitress_amora_smiling
                u "Heck yeah!"
        hide waitress_amora_smiling
        show waitress_amora_talking
        wt "Alright that will be a total of $64,96. Will you pay in cash or card?"
        hide waitress_amora_talking
        hide waitress_amora_smiling
        "Amelia and I looked at each other."
        hide waitress_amora_smiling
        if amelia_dress == 1:
            show amelia_base_dress
        if amelia_dress == 0:
            show amelia_base
        show blink_random_normal_amelia
        show eyebrows_amelia_normal
        show talking_amelia_normal
        a "So who will pay?"
        hide talking_amelia_normal
        show smile_amelia_normal
        "I decided to stand up (Not physically.)"
        u "I will."
        hide smile_closed_amelia_normal
        hide amelia_base
        hide amelia_base_dress
        hide blink_random_normal_amelia
        hide eyebrows_amelia_normal
        show waitress_amora_talking
        wt "Oh."
        hide waitress_amora_talking
        show waitress_amora_smiling
        "The waitress looked at me."
        hide waitress_amora_smiling
        show waitress_amora_talking
        wt "Will you pay in cash or card?"
        hide waitress_amora_talking
        show waitress_amora_smiling
        u "Card, please."
        "I slid my credit card on the credit card scanner. The transaction went through and was approved with no issues."
        hide waitress_amora_smiling
        show waitress_amora_talking
        wt "Your food will be ready in around 20 minutes. Your drinks are coming really soon."
        hide waitress_amora_talking
        if amelia_dress == 1:
            show amelia_base_dress
        if amelia_dress == 0:
            show amelia_base
        show blink_random_normal_amelia
        show eyebrows_amelia_normal
        show talking_amelia_normal
        au "Thank you!"
        hide talking_amelia_normal
        show smile_closed_amelia_normal
        "The waitress walks away."
    if amelia_dress ==1:
        show amelia_base_dress
    else:
        show amelia_base
    show talking_amelia_normal
    show blink_random_normal_amelia
    show eyebrows_amelia_normal
    a "So, you made your college application?"
    hide talking_amelia_normal
    show smile_closed_amelia_normal
    u "Yup, in..."
    "{i}{b}Note{/b}: Any choices you decide here will alter the story to respect your choice. In case you want to go back and choose a different choice, a quick save has automatically been made.{/i}"
    "{i}(Click '{b}Load{/b}' at the bottom of the screen and click the '{b}A{/b}' to see your quick saves.){/i}"
    $ renpy.take_screenshot(scale=None, background=False)
    $ renpy.save(renpy.newest_slot(), save_name)
    menu:
        "Art & Humanities":
            nvl clear
            $ subjects = 1
            hide smile_closed_amelia_normal
            show talking_amelia_normal
            a "Oh nice, I remember you told me so you can become an artist or a musician. I wanna be a teacher."
            hide talking_amelia_normal
            show smile_closed_amelia_normal
        "Business & Economics":
            nvl clear
            $ subjects = 2
            hide smile_closed_amelia_normal
            show talking_amelia_normal
            a "Oh nice, I remember you told me so you can make a successful business. I wanna be a teacher."
            hide talking_amelia_normal
            show smile_closed_amelia_normal
        "Engineering & Technology":
            nvl clear
            $ subjects = 3
            hide smile_closed_amelia_normal
            show talking_amelia_normal
            a "Oh nice, I remember you told me so you can help Needles' Eye Inc with their machines and computers. I wanna be a teacher."
            hide talking_amelia_normal
            show smile_closed_amelia_normal
        "Law":
            nvl clear
            $ subjects = 4
            hide smile_closed_amelia_normal
            show talking_amelia_normal
            a "Oh nice, I remember you told me so you can become a lawyer or an attorney. I wanna be a teacher."
            hide talking_amelia_normal
            show smile_closed_amelia_normal
        "Psychology":
            nvl clear
            $ subjects = 5
            hide smile_closed_amelia_normal
            show talking_amelia_normal
            a "Oh nice, I remember you told me so you can help people a lot more than right now. I wanna be a teacher."
            hide talking_amelia_normal
            show smile_closed_amelia_normal
        "Social Sciences":
            nvl clear
            $ subjects = 6
            hide smile_closed_amelia_normal
            show talking_amelia_normal
            a "Oh nice, I remember you told me so you can become a politician. I wanna be a teacher."
            hide talking_amelia_normal
            show smile_closed_amelia_normal
        nar_nvl"What subject do you want to go in Daring Academy?"
    u "In which subject are you going to, Amelia?"
    hide smile_closed_amelia_normal
    show talking_amelia_normal
    a "Education."
    hide talking_amelia_normal
    show smile_closed_amelia_normal
    "Why didn't I think of that? I mean, it was a pretty obvious answer."
    if thai > 0:
        "I just stared down at my take out box in shame..."
        hide smile_closed_amelia_normal
        show worried_mouth_amelia_normal
    if thai < 1:
        "I just stared down in shame..."
        hide smile_closed_amelia_normal
        show worried_mouth_amelia_normal
    "Finally, Amelia broke the silence."
    hide worried_mouth_amelia_normal
    show worried_mouth_talking_amelia_normal
    a "Is there something wrong [y]?"
    hide worried_mouth_talking_amelia_normal
    show worried_mouth_amelia_normal
    u "Oh no, nothing. I'm just thinking why I asked that question."
    "She held my right hand with both hands."
    hide worried_mouth_amelia_normal
    show talking_amelia_normal
    a "No need to do that [nk], everyone forgets things."
    hide talking_amelia_normal
    show smile_closed_amelia_normal
    "She smiled at me."
    hide smile_closed_amelia_normal
    show talking_amelia_normal
    a "Even if the question was a bit idiotic, it's all fine [nk], I'm here for you."
    hide atalking
    show smile_closed_amelia_normal
    "I managed to get my head straight... I just smiled at her."
    u "Thank you [a]."
    scene illuminated_city with fade
    "We finished our dinner and decided to spend the rest of the day chatting, exploring our brand-new city and pretty much just hanging around."
    jump day_1_night_appartment


## Under this is Scene 3
label day_1_night_appartment:
    python:
        start = time.time()
        discord_rpc.update_connection()
        discord_rpc.run_callbacks()
        discord_rpc.update_presence(
            **{
                'details': 'Day 1',
                'state': 'Night',
                'large_image_key': 'apartmentmoveinnight',
                'small_image_key': 'daringacademy',
                'start_timestamp': start
            }
        )
    $ play_music(homeland)
    scene apartment_moving_in_night with dissolve
    $ play_sound(door_unlock)
    if amelia_drunk == 0:
        "We came back home at around 2AM really tired."
        "Upon unlocking the door, Amelia started to walk like a zombie."
        if amelia_dress == 1:
            show amelia_base_dress
        if amelia_dress == 0:
            show amelia_base
        show tired_mouth_amelia_normal
        show blink_random_normal_amelia
        show eyebrows_amelia_normal
        u "Man, it's getting late *yawn*, I think we should go to sleep."
        a "*yawn* I guess you're right. Can you carry me, please?"
        u "I guess."
        scene amelia_sleepy_couch with dissolve
        " I took her and carried her to our couch bed. I smiled at her gently."
        a "Good night [y]."
        scene amelia_sleeping_couch with dissolve
        "I gently kiss her forehead."
        scene amelia_sleeping_couch_blushing with dissolve
        u "Good night [a]."
        $ amelialove =+ 2
        "{i}You increased {b}Amelia{/b}'s Love: +2 Love.{/i}"
        $ ameliatrust =+ 1
        "{i}You increased {b}Amelia{/b}'s Trust: +1 Trust.{/i}"
        jump sleep_day1
    elif amelia_drunk == 1:
        "We came back home at around 2AM drunk and really tired."
        "Upon unlocking the door, Amelia started to walk funny, still with her beer bottle in hand."
        show amelia_drunk_smiling
        u "You know, I think we *hiccup* should go to sleep."
        hide amelia_drunk_smiling
        show amelia_drunk_talking
        a "Screw sl- *hiccup* sleep, I just wanna par-"
        hide amelia_drunk_talking with moveoutbottom
        "She fell to the ground, I held her, so she doesn't get hurt."
        scene amelia_sleeping_couch_blushing with dissolve
        "I decided to place her on our couch bed. I smiled at her gently."
        u "You know *hiccup*, she's kinda cute when she's asl- *hiccup* sleep."
        "I gently kissed her forehead."
        u "Good night, sweetie."
        $ amelialove =+ 2
        "{i}You increased {b}Amelia{/b}'s Love: +2 Love.{/i}"
        $ ameliatrust =+ 1
        "{i}You increased {b}Amelia{/b}'s Trust: +1 Trust.{/i}"
        jump sleep_day1

label sleep_day1:
    "I decided to go to sleep next to her."
    scene black with fade
    nar_nvl "Only the couch was set up, so I had no choice to sleep with her. It felt cute in a way, but I sure felt embarrassed during the entirety of the night."
    $ achievement.grant("Day One - Moving Day")
    $ play_sound(notification)
    show screen achievement("day_one_-_moving_day_achievement_pop_up.png")
    jump day_divider_1


label day_divider_1:
    scene black
    with Pause(1)

    show text "Day 2" with dissolve
    with Pause(4)

    hide text with dissolve
    with Pause(1)

    jump day_2_morning


## Under this is Day 2 (Scene 4-X)

label day_2_morning:
    nvl clear
    python:
        start = time.time()
        discord_rpc.update_connection()
        discord_rpc.run_callbacks()
        discord_rpc.update_presence(
            **{
                'details': 'Day 2',
                'state': 'Morning',
                'large_image_key': 'apartmentmoveinday',
                'small_image_key': 'daringacademy',
                'start_timestamp': start
            }
        )
    $ play_music(homeland)
    scene apartment_moving_in_day
    if amelia_drunk == 1:
        "I woke up pretty late with a pretty big headache."
        "I decided to check the time: 11:45am. I though to myself: Okay, so I'll stop being a lazy ass and actually make something to eat. I looked around for a second."
    if amelia_drunk == 0:
        "I woke up pretty late, makes sense given the time we went to sleep."
        "I decided to check the time: 11:45am. I though to myself: Okay, so I'll stop being a lazy butt and actually make something to eat. I looked around for a second."
    "It seems that Amelia opened one of the boxes and built a small table, how kind of her! I see my phone's always on display on on that table: It was a text from Amelia... And, breakfast?"
    "I read the text:"
    window hide
    show apartment_ground_blur with dissolve
    show phone_off at truecenter
    with moveinbottom
    show textbox_bottom with dissolve
    with Pause(1)
    show phone_dark_mode at truecenter
    with dissolve
    hide phone_off
    show amelia_phone_name_white at center
    with dissolve
    show amelia_text_day2 at center
    with dissolve
    pause
    show phone_off with dissolve
    hide phone_dark_mode
    hide amelia_phone_name_white with dissolve
    hide amelia_text_day2 with dissolve
    with Pause(1)
    hide phone_off with moveoutbottom
    hide apartment_ground_blur with dissolve
    window show
    hide textbox_bottom
    "Sure enough, I walked around and heard the shower running. I look at the breakfast."
    "Eggs and bacon. A classic."
    "I sat on the couch and ate my plate. A few minutes later, Amelia opens the bathroom door in a green shirt."
    show amelia_talking_day2 with moveinleft
    a "How's breakfast [nk]? Like it?"
    hide amelia_talking_day2
    show amelia_base_day2
    show eyebrows_amelia_normal
    show blink_random_normal_amelia
    show smile_closed_amelia_normal
    menu:
        "Yes":
            u "It's actually really good. The eggs are well cooked, the bacon's crispy and the toasts are warm."
            $ amelialove =+ 1
            "{i}You increased {b}Amelia{/b}'s Love: +1 Love.{/i}"
            $ ameliatrust =+ 1
            "{i}You increased {b}Amelia{/b}'s Trust: +1 Trust.{/i}"
            hide smile_closed_amelia_normal
            hide blink_random_normal_amelia
            show talking_amelia_normal
            show closed_eyes_amelia_normal
            a "Thank you! Made them just for you."
            hide talking_amelia_normal
            hide closed_eyes_amelia_normal
            show smile_closed_amelia_normal
            show wink_amelia_normal
            "She winks at me."
            hide wink_amelia_normal
            show smile_closed_amelia_normal
            show blink_random_normal_amelia
        "No":
            u "They're a bit cold in my opinion, thank you tho."
            hide smile_closed_amelia_normal
            show talking_amelia_normal
            a "Welcome. Yeah, I kinda made them like an hour ago, sorry about that mate."
            hide talking_amelia_normal
            show smile_closed_amelia_normal
            u "All good."
    "She decides to go to the kitchen to make a drink, I'm guessing she's making some coffee, she's a sucker for mild and soft coffee."
    a "Want anything [nk]?"
    menu:
        "Yeah mate!":
            u "I do want something, yeah."
            a "Nice, want coffee?"
            u "You know me far too well Amelia!"
        "No need.":
            u "No need Amelia, thank you tho."
            a "You're welcome."
    scene amelia_sitting_couch_smiling
    "She decides to sit down next to me."
    u "So what did you make, your classic coffee?"
    a "Nope, french vanilla."
    u "Oh. Trying something different?"
    a "Actually, no. I'm used on getting some at Stirling. Man, they do french vanilla very well there!"
    "{i}'Stirling' is a massive coffee store chain around Odorix.{/i}"
    "We decided to chill out a bit, talking and just having a good time. I finish my plate full as ever. Amelia also finished her drink."
    u "You know, we should probably start building some of the furnitures, eh?"
    "{i}Do you want to skip this scene? {b}Note{/b}: the story will alter based on your choices.{/i}"
    menu:
        "Yes":
            scene black with dissolve
            nvl clear
            nar_nvl "We spent 6 hours building furnitures, talking, listening to music and such. (Remember, I need to improve the writing later on.)"
            jump splash_screen
        "No":
            a "I guess so, the sooner we start, the quicker we can finish."
            "She pulled out a pink hair band and attached her hair into a ball, leaving 2 wicks hanging on each side of her face."
            scene amelia_furniture_smiling
            "We sat down on the floor near boxes."
            scene amelia_furniture_talking
            a "Hold on, I'll put some music."
            scene amelia_furniture_phone
            "She takes her phone."
            a "So, we have 'Last Dance', a nice dubstep song. Here's part of it."
            $ play_music(last_dance)
            a "Last Dance is a good song, one of my favorite."
            stop music
            a "We could play 'Monster Orb, The Game We Play' if you want."
            $ play_music(motgwp)
            a "Man, I love that song!"
            stop music
            a "Or, we could just play a deathstep song: Rise."
            $ play_music(rise)
            a "Might be too loud tho. Your choice tho."
            stop music
            menu:
                "Last Dance":
                    u "Honestly, Last Dance fits the mood better."
                    a "I think it does as well. Last dance it is!"
                    $ play_music(last_dance)
                "Monster Orb, The Game We Play":
                    u "A rap would be nice, yeah!"
                    a "Monster Orb, The Game We Play it is then."
                    $ play_music(motgwp)
                "Rise":
                    u "You know what, play Rise."
                    a "You're sure? Like I said, it might be too loud."
                    u "Why not, eh?"
                    a "Alright, Rise it is."
                    $ play_music(rise)
    a "So what should we start first?"
    menu:
        "Footstool":
            u "Maybe the footstool?"
            a "Wait, we have a footstool?"
            u "Yeah, my mother gave it to me."
            a "Alright, I'll get the tools, can you get the box please?"
            "I went to get the box. A footstool from Odea."
            "Amelia came back with the tool box, I came back with the footstool box."
        "Bedside Cabinet":
            u "We could do the bedside cabinet, so we can start storing our clothes."
            a "Alright, I'll get the tools, can you get the box please?"
            "I went to get the box. A small bedside cabinet from Odea."
            "Amelia came back with the tool box, I came back with the cabinet box."
        "Dining Table":
            u "If we wanna start cooking here, we should make our table, eh?"
            a "Alright, I'll get the tools, can you get the box please?"
            "I went to get the box. A nice and big dining table from Odea."
            "Amelia came back with the tool box, I came back with the dining table box."
    u "Did you bring a knife?"
    a "Yeah, I did bring one."
    "We opened the box and took out all the pieces. Amelia took the instruction manual."
    a "Can you mesure the parts? Just so we know we got the right length?"
    u "Oh yeah, sure!"
    "I took a leg and mesured it with my phone. I said the mesurements for that part."
    a "Wait, was that the top right leg?"
    u "Yup."
    a "On the instructions, it's measured wrong. Try the top left leg."
    "I mesured that leg. I said the mesurements."
    a "...It's also wrong. What was the guy who wrote these instructions on?"
    u "Opium?"
    a "Ha ha, very funny [nk], Opium was made illegal a millenium ago, literally. No, but seriously, the legs are mesured wrong. Let's build something else."
    "So we packed the parts, took another box and mesured the parts. I said the mesurements."
    a "Okay, these are not wrong, thankfully."
    "We stayed silent for a minute while Amelia read the instructions in her head."
    u "Hey Amelia?"
    a "Yeah?"
    u "Are you excited for the upcoming Monster Orb tournament?"
    "She was shocked."
    jump strike_lol

label strike_lol:
    scene amelia_furniture_talking
    with vpunch
    a "WAIT, A TOURNAMENT IS COMING?!"
    scene amelia_furniture_smiling
    u "Yeah, on Saturday. Did you update your altar?"
    scene amelia_furniture_talking
    a "Let me guess, another ban list came?"
    scene amelia_furniture_smiling
    u "Yup, banning Strike, once it for all."
    scene amelia_furniture_smiling_blur with dissolve
    show strike at truecenter
    with dissolve
    "{i}Strike is a trapped item card, a type of an item card which can be used during your opponent's turn, which says to destroy one monster.{/i}"
    "{i}Previously limited to one copy (Semi-banned), this card still caused tons of issues in the world of Daring Academy.{/i}"
    a "I did have a copy of Strike in my altar, any other cards banned or unbanned?"
    u "Don't think so, in the Monster Orb app, Strike was the big deal, with thousands of comments on the official post."
    a "Dang... People really hated that card, eh?"
    u "It seems so, but I loved it. Killing any monsters at any time during your opponent's turn might be overpowered, but that's good to turn your game in your favor."
    scene amelia_furniture_talking with dissolve
    hide strike
    with dissolve
    a "Can you pass me a screwdriver please?"
    scene amelia_furniture_smiling
    u "Oh yeah, sure."
    "I gave her a scredriver."
    scene amelia_furniture_talking
    a "Thank you!"
    scene amelia_furniture_smiling
    "I smiled."
    scene amelia_furniture_talking
    a "And what about your Ignitar altar mate?"
    scene amelia_furniture_smiling
    u "I only saw the ban list yesterday, so I didn't have time to update it, but I will tomorrow."
    scene amelia_furniture_talking
    a "Weren't we planning on buying clothes tomorrow?"
    scene amelia_furniture_smiling
    u "Oh yeah, true. You said you needed dresses, right?"
    scene amelia_furniture_talking
    a "Yup, but let's plan that either later today or tomorrow."
    scene amelia_furniture_smiling
    u "Alright."
    "We continued building furnitures for a while."
    "A bright white light suddenly appeared for a brief moment. I looked at Amelia, she was holding her phone."
    u "Did you just take a pic of me?"
    "Amelia smiled."
    "I tried snatching her phone, but she pushed it farther."
    u "Amelia, please give me the phone."
    "She stuck her tongue to me."
    u "Amelia, give me the phone now."
    "She wouldn't budge. I jumped on her, trying to get her phone."
    with vpunch
    show amelia_ground_day_2_base
    show blink_random_ground_amelia
    show serious_amelia_ground
    show eyebrows_worried_amelia_ground
    "We fell to the ground. I quickly took her hands so she couldn't escape."
    show blush_amelia_ground with dissolve
    "Suddenly, she became embarrassed and shy."
    menu:
        "Go aggressive":
            u "Delete the picture NOW!"
            "She looked away, sad."
            hide blink_random_ground_amelia
            hide serious_amelia_ground
            hide eyebrows_worried_amelia_ground
            show blink_random_ground_amelia
            show sad_amelia_ground
            show eyebrows_worried_amelia_ground
            $ amelialove =- 1
            "{i}You decreased {b}Amelia{/b}'s Love: -1 Love.{/i}"
            u "You know how I feel about pictures and privacy in general, so please delete it."
            "Amelia complied."
            "Seeing her in this state makes me..."
            menu:
                "Feel good":
                    "Just knowing that the picture was deleted makes me feel like I have a private life again."
                    $ amelia_anger =+ 1
                    hide blush_ground with dissolve
                    jump anger
                "Feel bad":
                    "I can't let her stay like that..."
                    menu:
                        "Hug her and apologize for your behaviour":
                            "Amelia, even tho she's sweet and loves making friend, she can't really handle people yelling at her, so I had to apologize."
                            hide blush_ground with dissolve
                            "I gently let go of her arms. She sat down, still feeling a bit down."
                            # scene amelia_sitting_day_2_closed_mouth
                            u "Look Amelia, I'm sorry for my actions, but you know how I feel about my life."
                            u "From everything I went through: Bullying, Suicide attempts and such, you know how pictures makes me feel when someone takes them without my consent."
                            "I opened my arms, waiting for a hug."
                            u "Come here man."
                            "She looked up at me. Finally, she accepted my offer."
                            # hide amelia_sitting_day_2_closed_mouth
                            scene love_background with dissolve
                            jump amelia_hug_day_2
                            with dissolve
                        "Apologize":
                            "Amelia, even tho she's sweet and loves making friend, she can't really handle people yelling at her, so I had to apologize."
                            hide blush_ground with dissolve
                            "I gently let go of her arms. She sat down, still feeling a bit down."
                            # scene amelia_sitting_day_2_closed_mouth
                            u "Look Amelia, I'm sorry for my actions, but you know how I feel about my life."
                            u "From everything I went through: Bullying, Suicide attempts and such, you know how pictures makes me feel when someone takes them without my consent."
                            "She looked up at me."
                            u "I don't want our friendship to end like this Amelia, I am truely sorry."
                            # show amelia_sitting_day_2_opened_mouth
                            a "It's alright... It was a bit selfish of me... to take a pic, so I'm sorry as well."
                            # hide amelia_sitting_day_2_opened_mouth
                            # show amelia_sitting_day_2_closed_mouth
                            "We stood there awkwardly for a solid 30 seconds, but felt like an hour. Finally, she got her composure back."
                            u "You good?"
                            # show amelia_sitting_day_2_opened_mouth
                            a "Yeah..."
                            # hide
                            $ amelia_anger = 0
                            jump anger
                        "Kiss her on the cheek and apologize":
                            "Amelia, even tho she's sweet and loves making friend, she can't really handle people yelling at her, so I had to apologize."
                            hide blush_ground with dissolve
                            "I gently let go of her arms. She sat down, still feeling a bit down."
                            # scene amelia_sitting_day_2_closed_mouth
                            "She looked up at me."
                            u "Look Amelia, I'm sorry for my actions, but you know how I feel about my life."
                            u "From everything I went through: Bullying, Suicide attempts and such, you know how pictures makes me feel when someone takes them without my consent."
                            "I stood up."
                            # hide amelia_sitting_day_2_closed_mouth
                            # show amelia_sitting_day_2_opened_mouth
                            a "What are you doing?"
                            "Finally, without hesitation, I went in for a kiss on the cheek."
                            "Instantly, she became red like a tomato from shyness. Her voice weekened."
                            a "Why... why...why...why did you do that?"
                            "I smiled."
                            u "You deserved something from all that trouble."
                            "We stood there awkwardly for a solid 30 seconds, but felt like an hour."
                            u "Did... you at least enjoy it."
                            "She jumped."
                            a "Oh jesus! You scared the crap out of me."
                            "I wasn't amused."
                            u "Were you day dreaming again?"
                            "Her face became red again."
                            a "N...No! But, but, but I did enjoy it..."
                            $ amelialove =+ 3
                            "{i}You increased {b}Amelia{/b}'s Love: +3 Love.{/i}"
                            "I gave her time to compose herself."
                            $ amelia_anger = 0
                            jump anger
        "Go gentle":
            "I gently let go of her arms. She sat down, still feeling a bit down."
            u "Look, I know you don't want to, but can you please delete the pic? I'm sorry for what just happened."
            "Amelia complied, still embarassed and shy about this whole ordeal."
            "Seeing her in this state... I can't let her stay like that..."
            menu:
                "Hug her":
                    "Amelia, even tho she's sweet and loves making friend, she can't really handle people yelling at her, so I had to apologize."
                    hide blush_ground with dissolve
                    "I gently let go of her arms. She sat down, still feeling a bit down."
                    # scene amelia_sitting_day_2_closed_mouth
                    u "Look Amelia, I'm sorry for my actions, but you know how I feel about my life."
                    u "From everything I went through: Bullying, Suicide attempts and such, you know how pictures makes me feel when someone takes them without my consent."
                    "I opened my arms, waiting for a hug."
                    u "Come here man."
                    "She looked up at me. Finally, she accepted my offer."
                    # hide amelia_sitting_day_2_closed_mouth
                    scene love_background with dissolve
                    jump amelia_hug_day_2
                    with dissolve
                "Kiss her on the cheek":
                    "I stood up."
                    a "What are you doing?"
                    "Finally, without hesitation, I went in for a kiss on the cheek."
                    "Instantly, she became red like a tomato from shyness. Her voice weekened."
                    a "Why... why...why...why did you do that?"
                    "I smiled."
                    u "You deserved something from all that trouble."
                    "We stood there awkwardly for a solid 30 seconds, but felt like an hour."
                    u "Did... you at least enjoy it."
                    "She jumped."
                    a "Oh jesus! You scared the crap out of me."
                    "I wasn't amused."
                    u "Were you day dreaming again?"
                    "Her face became red again."
                    a "N...No! But, but, but I did enjoy it..."
                    $ amelialove =+ 3
                    "{i}You increased {b}Amelia{/b}'s Love: +3 Love.{/i}"
                    "I gave her time to compose herself."
                    $ amelia_anger = 0
                    jump anger
        "Let it go":
            u "You know what, nevermind. You can keep the picture. I don't want to ruin our friendship over a simple picture."
            a "Are you sure tho, I know how you feel about pictures and privacy, I can just delete it if you want to."
            u "You can keep it. If you like it, that is."
            "She smiled awkwardly."
            "We stood there awkwardly for a solid 30 seconds, but felt like an hour."
            jump anger


label amelia_hug_day_2:
    show amelia_player_hug_base_guy
    show amelia_player_hug_blush
    show blink_random_amelia_player_hug
    show amelia_player_hug_sad_mouth
    $ amelialove =+ 1
    "{i}You increased {b}Amelia{/b}'s Love: +1 Love.{/i}"
    hide blink_random_amelia_player_hug
    show amelia_player_hug_closed_eyes
    "I could tell she really needed one with how much she was shaking and how strong her grip was on me."
    u "I don't want our friendship to end like this Amelia, I am truely sorry."
    "She weakened a little."
    show blink_random_amelia_player_hug
    hide amelia_player_hug_closed_eyes
    hide amelia_player_hug_sad_mouth
    show amelia_player_hug_sad_talking
    a "It's alright... It was a bit selfish of me... to take a pic, so I'm sorry as well."
    hide amelia_player_hug_sad_talking
    show amelia_player_hug_sad_mouth
    hide blink_random_amelia_player_hug
    show amelia_player_hug_closed_eyes
    "We stood there for a solid 30 seconds, but felt like an hour. My heart was pounding. The feel of her chest and her heart pounding against my chest felt like heaven."
    hide amelia_player_hug_sad_mouth
    show amelia_player_hug_happy_mouth
    "Finally, she got her composure back."
    hide amelia_player_hug_happy_mouth
    show amelia_player_hug_happy_talking
    a "Thank you, I needed that."
    show blink_random_amelia_player_hug
    hide amelia_player_hug_closed_eyes
    hide amelia_player_hug_blush with dissolve
    u "Anytime."
    $ amelia_anger = 0
    jump anger

label anger:
    u "Come on mate, we still have furnitures to finish. Let's go."
    if amelia_anger == 1:
        hide blink_random_ground_amelia
        hide sad_ground
        hide eyebrows_worried_ground
        show blink_random_ground_cry_amelia
        show sad_talking_ground
        show eyebrows_angry_ground
        a "No, leave me alone!"
        "Tears began to fall down her cheeks."
        "I felt bad. Ruining our friendship over a picture is not the way I thought it would end..."
        "I complied and went to my empty bedroom."
    else:
        a "Yeah..."
        "We continued building furnitures for a while until 8pm came around."
        "I looked at the time"
        u "Shit, it's already 8pm?!"
        #show (Something) with vpunch for up and down
        a "ALREADY?!"
    jump shy_amelia


label shy_amelia:
    if amelialove > 10:
        scene black
        with Pause(1)

        show text "Amelia will now be more shy towards you: 10 Love points accumulated." with dissolve
        with Pause(4)

        hide text with dissolve
        with Pause(1)

        jump splash_screen
    else:
        jump splash_screen


label splash_screen:
    scene black
    with Pause(1)

    show text "To be continued in Version 0.0.3" with dissolve
    with Pause(4)

    hide text with dissolve
    with Pause(1)

    jump credits


label day_divider_2:
    scene black
    with Pause(1)

    show text "Day 3" with dissolve
    with Pause(4)

    hide text with dissolve
    with Pause(1)

    jump day_3_morning


label credits:
    $ play_sound(notification)
    $ achievement.grant("Final Moments")
    show screen achievement("final_moments_achievement_pop_up.png")
    $ play_music(spirits)
    $ credits_speed = 40
    scene black
    show credits_image at Move((0.5, 1.1), (0.5, -10.0), credits_speed,
                  xanchor=0.5, yanchor=0)
    with Pause(credits_speed+0)

return
