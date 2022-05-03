from tkinter import *
import appbar as ab
from functools import partial
CL = ab.CL

# main window
root = Tk()
ab.config_window(root, CL[3])

# main frames
title_bar = Frame(root, bg=CL[0], relief='raised', bd=0, highlightthickness=0)
window = Frame(root, bg=CL[1])
title_bar.pack(fill=X)
window.pack(fill=BOTH)

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


# WINDOW CODE HERE #


resize_x_widget = Frame(window, bg=CL[1], cursor='sb_h_double_arrow')
resize_x_widget.pack(side=RIGHT, ipadx=2, fill=Y)
resize_x_widget.bind("<B1-Motion>", partial(ab.resize_x, root))
resize_y_widget = Frame(window, bg=CL[1], cursor='sb_v_double_arrow')
resize_y_widget.pack(side=BOTTOM, ipadx=2, fill=X)
resize_y_widget.bind("<B1-Motion>", partial(ab.resize_y, root))

root.mainloop()
