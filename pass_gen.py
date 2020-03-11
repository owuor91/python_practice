import random


def password_gen():
    s = "abcdefghijklmnopqrstuvwxyz01234567890ABCDEFGHIJKLMNOPQRSTUVWXYZ!@#$%^&*()?"
    pass_len = 16
    return "".join(random.sample(s, pass_len))
