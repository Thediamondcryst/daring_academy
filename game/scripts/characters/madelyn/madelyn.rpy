define m = Character("Madelyn", who_color="#df80bC")
define m_nvl = Character("Madelyn", who_color="#df80bC", kind=nvl)


image blink_random_normal_madelyn:
    "images/sprites/madelyn/normal/assets/opened_eyes_madelyn_normal.png"
    choice:
        4.5
    choice:
        3.5
    choice:
        1.5
    "images/sprites/madelyn/normal/assets/closed_eyes_madelyn_normal.png"
    .15
    repeat
