from tkinter import *
from functools import partial

import appbar as ab
import functions as f

CL = ab.CL

# main window
root = Tk()
ab.config_window(root)

# main frames
title_bar = Frame(root, bg=CL[0], relief='raised', bd=0, highlightthickness=0)
main_frame = Frame(root, bg=CL[3])
title_bar.pack(fill=X)
main_frame.pack(fill=BOTH, expand=True)

# appbar widgets
close_button = Button(title_bar, text=' × ', command=root.destroy, bg=CL[0], padx=2,
                      pady=2, bd=0, fg=CL[1], highlightthickness=0)
expand_button = Button(title_bar, text=' ■ ', bg=CL[0], padx=2,
                       pady=2, bd=0, fg=CL[1], highlightthickness=0)
expand_button.config(command=partial(ab.maximize, root, expand_button))
minimize_button = Button(title_bar, text=' ▁ ', command=partial(ab.minimize, root), bg=CL[0], padx=2,
                         pady=2, bd=0, fg=CL[1], highlightthickness=0)
title_bar_title = Label(title_bar, text='CHAT', bg=CL[0], bd=0, fg=CL[1], highlightthickness=0)

title_bar.pack(fill=X)
close_button.pack(side=RIGHT, ipadx=7, ipady=1)
expand_button.pack(side=RIGHT, ipadx=7, ipady=1)
minimize_button.pack(side=RIGHT, ipadx=7, ipady=1)
title_bar_title.pack(side=LEFT, padx=10)

title_bar.bind('<Button-1>', partial(ab.get_pos, root, expand_button))
close_button.bind('<Enter>', ab.close_hover)
close_button.bind('<Leave>', ab.close_normal)
expand_button.bind('<Enter>', ab.change_hover)
expand_button.bind('<Leave>', ab.change_normal)
minimize_button.bind('<Enter>', ab.change_hover)
minimize_button.bind('<Leave>', ab.change_normal)


# chat screen widgets
main_screen = Frame(main_frame, bg=CL[3])
main_screen.place(x=0, y=0, relwidth=1, relheight=1)

join_nav = Frame(main_frame, bg=CL[1])
add_room_button = Button(join_nav, bd=0, bg=CL[1], fg=CL[0], text="Utwórz pokój", font=f.ft(12), command=None)
add_room_button.place(relx=0, rely=0, relwidth=1, relheight=0.05)
join_room_button = Button(join_nav, bd=0, bg=CL[1], fg=CL[0], text="Dołącz do czatu", font=f.ft(12), command=None)
join_room_button.place(relx=0, rely=0.05, relwidth=1, relheight=0.05)
# TODO: chats list
join_nav.place(x=0, y=0, relwidth=0.2, relheight=1)

users_nav = Frame(main_frame, bg=CL[2])
users_button = Button(users_nav, bd=0, bg=CL[1], fg=CL[0], text="Członkowie", font=f.ft(12), command=None)
users_button.place(relx=0.1, rely=0.025, relwidth=0.8, relheight=0.075)
# TODO: users list
users_nav.place(relx=0.85, rely=0, relwidth=0.15, relheight=1)


# resizing widgets
resize_x_widget = Frame(main_frame, bg=CL[3], cursor='sb_h_double_arrow')
resize_x_widget.pack(side=RIGHT, ipadx=2, fill=Y)
resize_x_widget.bind("<B1-Motion>", partial(ab.resize_x, root))
resize_y_widget = Frame(main_frame, bg=CL[3], cursor='sb_v_double_arrow')
resize_y_widget.pack(side=BOTTOM, ipady=2, fill=X)
resize_y_widget.bind("<B1-Motion>", partial(ab.resize_y, root))

root.mainloop()
