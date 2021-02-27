
label dev_room:
    python:
        start = time.time()
        discord_rpc.update_connection()
        discord_rpc.run_callbacks()
        discord_rpc.update_presence(
            **{
                'details': 'Spirit World',
                'state': 'Testing...',
                'large_image_key': 'spiritworld',
                'small_image_key': 'daringacademy',
                'start_timestamp': start
            }
        )
    scene spirit_world
    show lily_base_work
    show blink_random_embarrassed_lily
    show embarrassed_mouth_lily_normal
    show blush_lily_normal
    l "Hi, erm... My name is Lily..."
    pause
    hide lily_base_work
    hide blink_random_embarrassed_lily
    hide embarrassed_mouth_lily_normal
    hide blush_lily_normal

    show lily_base
    show smile_lily_normal
    show blush_lily_normal
    show blink_random_normal_lily
    pause
    hide lily_base
    hide smile_lily_normal
    hide blush_lily_normal
    hide blink_random_normal_lily

    show lily_base_work
    show smug_mouth_lily_normal
    show blush_lily_normal
    show blink_random_smug_lily
    show screen achievementButtonSmug
    pause
    hide lily_base_work
    hide smug_mouth_lily_normal
    hide blush_lily_normal
    hide blink_random_smug_lily
    hide screen achievementButtonSmug
    show madelyn_base
    show talking_madelyn_normal
    show blink_random_normal_madelyn
    show eyebrows_madelyn_normal
    m "Hello, my name is Madelyn! Nice to meet you!"
    hide talking_madelyn_normal
    show smile_madelyn_normal
    show madelyn_base
    show blink_random_normal_madelyn
    show eyebrows_madelyn_normal
    a "Hi Madelyn!"
    hide madelyn_base
    hide smile_madelyn_normal
    hide blink_random_normal_madelyn
    hide eyebrows_madelyn_normal
    show rose_base
    show talking_rose_normal
    show blink_random_normal_rose
    r "Let me introduce myself. My name is Rose Wheatley, I'm 19 years old and I love doing Portal 2 references and play the trading card game Monster Orb."
    hide talking_rose_normal
    show smile_rose_normal
    pause
    hide rose_base
    show rose_base_work
    hide blink_random_normal_rose
    show blink_random_normal_rose
    hide smile_rose_normal
    show smile_rose_normal
    pause
    hide smile_rose_normal
    hide blink_random_normal_rose
    hide rose_base_work
    show johnny_base
    show talking_johnny_normal
    show blink_random_normal_johnny
    j "My name is Johnny Cortez, Madelyn's husband. At your service... Erm, what's your name? Oh, [nk]! Hello [nk]!"
    hide talking_johnny_normal
    show smile_johnny_normal
    pause
    jump test_mall_map


label test_mall_map:
    scene mall_map
    window hide
    show screen mall_monster_orb_button
    show screen mall_big_store_button
    show screen mall_plaza_button
    show screen mall_restaurant_button
    show screen mall_outside_button
    show screen mall_clothes_button
    show screen mall_skip_button
    show textbox_bottom
    return

label motcg_mall:
    window show
    "hi"
    jump test_mall_map

label store_mall:
    window show
    "hello"
    jump test_mall_map

label plaza_mall:
    window show
    "howdy"
    jump test_mall_map

label restaurant_mall:
    window show
    "hoi"
    jump test_mall_map

label outside_mall:
    window show
    "hola"
    jump test_mall_map

label clothes_mall:
    window show
    "heya"
    jump test_mall_map

    return
