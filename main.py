import tkinter.messagebox, tkinter.ttk, tkinter.scrolledtext, tkinter.font

import contents

PROGRAM_NAME = "Simple Stupid";

def start(win, prev_frame):
    prev_frame.grid_remove();
    items_var = tkinter.StringVar(value = contents.items);
    frame = tkinter.ttk.Frame(win, takefocus = 1);
    frame.pack(fill = tkinter.BOTH, expand = True);
    items_listbox = tkinter.ListBox(frame, listvariable = items_var);

    vscrollbar = tkinter.Scrollbar(frame, orient = tkinter.VERTICAL, command =
            items_listbox.yview);
    
    items_listbox.configure(yscrollcommand = vscrollbar.set);

    hscrollbar = tkinter.Scrollbar(frame, orient = tkinter.HORIZONTAL, command =
            items_listbox.xview);
    
    items_listbox.configure(xscrollcommand = hscrollbar.set);

    items_listbox.pack(fill = tkinter.BOTH, expand = True);

    win.protocol("WM_DELETE_WINDOW");

def main():
    main_win = tkinter.Tk();
    main_win.title(PROGRAM_NAME);
    main_win.geometry("300x300+200+100");
    
    main_frame = tkinter.ttk.Frame(main_win, takefocus = 1);
    main_frame.pack(fill = tkinter.BOTH, expand = True);
    with open("ABOUT.md") as f:
        intro_box = tkinter.ttk.Label(main_frame, text = f.read());

    
    intro_box.pack(fill = tkinter.BOTH, expand = True);

    st_btn = tkinter.Button(main_frame, highlightcolor = "green", text = "Start",
            font = tkinter.font.Font(family="Arial", size = 40, weight =
                "bold"), command = lambda : start(main_win, main_frame));
    st_btn.pack(fill = tkinter.BOTH, expand = True);

    main_win.mainloop();



if __name__ == "__main__":
    main();
