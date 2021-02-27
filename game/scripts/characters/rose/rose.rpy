define r = Character("Rose", who_color="#FF007F")
define r_nvl = Character("Rose", who_color="#FF007F", kind=nvl)


image blink_random_normal_rose:
    "images/sprites/rose/assets/opened_eyes_rose_normal.png"
    choice:
        4.5
    choice:
        3.5
    choice:
        1.5
    "images/sprites/rose/assets/closed_eyes_rose_normal.png"
    .15
    repeat
