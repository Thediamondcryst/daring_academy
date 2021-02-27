define a = Character("Amelia", who_color="#FF5C7A")
define a_nvl = Character("Amelia", who_color="#FF5C7A", kind=nvl)


image blink_random_normal_amelia:
    "images/sprites/amelia/normal/assets/opened_eyes_amelia_normal.png"
    choice:
        4.5
    choice:
        3.5
    choice:
        1.5
    "images/sprites/amelia/normal/assets/closed_eyes_amelia_normal.png"
    .15
    repeat


image blink_random_ground_amelia:
    "images/sprites/amelia/ground/assets/opened_eyes_amelia_ground.png"
    choice:
        4.5
    choice:
        3.5
    choice:
        1.5
    "images/sprites/amelia/ground/assets/closed_eyes_amelia_ground.png"
    .15
    repeat


image blink_random_ground_cry_amelia:
    "images/sprites/amelia/ground/assets/cry_opened_eyes_amelia_ground.png"
    choice:
        4.5
    choice:
        3.5
    choice:
        1.5
    "images/sprites/amelia/ground/assets/cry_closed_eyes_amelia_ground.png"
    .15
    repeat
