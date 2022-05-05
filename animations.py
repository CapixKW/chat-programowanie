from functools import partial


add = 1


def users_nav_off(nav, root, count):
    global add

    x, max_x = nav.winfo_x(), root.winfo_width()
    if count >= 8:
        add += 1
        count = 0
    if x <= max_x:
        x += add
        nav.place(relx=x/max_x)

        f = partial(users_nav_off, nav, root, count+1)
        f.__name__ = f.func.__name__
        root.after(2, f)


def users_nav_in(nav, root, count):
    global add

    x, max_x = nav.winfo_x(), root.winfo_width()
    if count >= 8:
        add -= 1
        count = 0
    if x/max_x > 0.85:
        x -= add
        nav.place(relx=x/max_x)

        f = partial(users_nav_in, nav, root, count+1)
        f.__name__ = f.func.__name__
        root.after(2, f)
    else:
        nav.place(relx=0.85)
