define l = Character("Lily", who_color="#aa029c")
define l_nvl = Character("Lily", who_color="#aa029c", kind=nvl)


image blink_random_normal_lily:
    "images/sprites/lily/normal/assets/opened_eyes_lily_normal.png"
    choice:
        4.5
    choice:
        3.5
    choice:
        1.5
    "images/sprites/lily/normal/assets/closed_eyes_lily_normal.png"
    .15
    repeat


image blink_random_embarrassed_lily:
    "images/sprites/lily/normal/assets/embarrassed_eyes_lily_normal.png"
    choice:
        4.5
    choice:
        3.5
    choice:
        1.5
    "images/sprites/lily/normal/assets/closed_eyes_lily_normal.png"
    .15
    repeat


image blink_random_smug_lily:
    "images/sprites/lily/normal/assets/smug_eyes_lily_normal.png"
    choice:
        4.5
    choice:
        3.5
    choice:
        1.5
    "images/sprites/lily/normal/assets/closed_eyes_lily_normal.png"
    .15
    repeat
