define j = Character("Johnny", who_color="#940000")
define j_nvl = Character("Johnny", who_color="#940000", kind=nvl)


image blink_random_normal_johnny:
    "images/sprites/johnny/assets/opened_eyes_johnny_normal.png"
    choice:
        4.5
    choice:
        3.5
    choice:
        1.5
    "images/sprites/johnny/assets/closed_eyes_johnny_normal.png"
    .15
    repeat
