import tkinter.messagebox, tkinter.ttk, tkinter.scrolledtext, tkinter.font

import content

PROGRAM_NAME = "Simple Stupid";

WIN_HEIGHT = 400;
WIN_WIDTH = 800;

MAX_LINES = 1000;
MAX_COLS = 200;

SCROLL_GRAN = None;

INTRO = """
Select an item and press enter (or double-click) to view content.
""";

NO_CONTENT = "Content coming soon..."

def start(win, init, deinit):
    def uninstall():
        nonlocal lframe, rframe, win
        lframe.destroy();
        rframe.destroy();
        win.protocol("WM_DELETE_WINDOW", lambda : win.destroy());
        init(win);


    def display_content(*parg):
        nonlocal tid, items_listbox
        ids = items_listbox.curselection();
        if not ids:
            return
        text_space.itemconfigure(
                tid,
                text = content.contents[ids[0]] + ("" if len(content.contents[ids[0]].split("\n")) > 5 else "\n%s" % (NO_CONTENT,)),
                justify = tkinter.LEFT
                );
        text_space.configure(scrollregion = text_space.bbox("all"));
        text_space.xview("scroll", -MAX_COLS, "units");

    def onMouseScroll(e):
        text_space.yview("scroll", -1*(e.delta//SCROLL_GRAN), "units")


    deinit();
    items_var = tkinter.StringVar(value = content.items);
    lframe = tkinter.ttk.Frame(win, height = WIN_HEIGHT);
    lframe.place(x = 0, y = 0, relwidth = 0.2, relheight = 1);

    rframe = tkinter.ttk.Frame(win, height = WIN_HEIGHT);
    rframe.place(relx= 0.3, y = 0, relwidth = 0.7, relheight = 1);

    items_listbox = tkinter.Listbox(lframe, height = WIN_HEIGHT, listvariable = items_var);

    hscrollbar = tkinter.Scrollbar(lframe, orient = tkinter.HORIZONTAL, command =
            items_listbox.xview);

    vscrollbar = tkinter.Scrollbar(lframe, orient = tkinter.VERTICAL, command =
            items_listbox.yview);

    hscrollbar.place(x = 0, y = 0, anchor = tkinter.NW, relwidth = 1);

    vscrollbar.place(x = 0, rely = 0.098, relheight = 0.9, anchor = tkinter.NW);

    items_listbox.place(relx = 0.098, rely = 0.1, relwidth = 0.9);



    items_listbox.configure(yscrollcommand = vscrollbar.set);

    items_listbox.configure(xscrollcommand = hscrollbar.set);

    text_space = tkinter.Canvas(rframe, height = MAX_LINES, width = MAX_COLS);

    tid = text_space.create_text(0, 0, text = INTRO, justify = tkinter.LEFT, font = "courier");

    text_vscrollbar = tkinter.Scrollbar(rframe, width = 20, orient = tkinter.VERTICAL, command =
            text_space.yview);
    
    text_space.configure(yscrollcommand = text_vscrollbar.set);

    text_hscrollbar = tkinter.Scrollbar(rframe, width = 20, orient = tkinter.HORIZONTAL, command =
            text_space.xview);
    
    text_hscrollbar.place(x = 0, y = 0, relwidth = 1);

    text_vscrollbar.place(relx = 0.005, rely = 0.098, relheight = 0.9);

    text_space.place(relx = 0.098, relwidth = 0.9, relheight = 0.9);


    text_space.configure(xscrollcommand = text_hscrollbar.set, scrollregion = text_space.bbox("all"));


    text_space.tag_bind(tid, "<Up>", lambda e: text_space.yview("scroll",
        -1, "units"));

    text_space.tag_bind(tid, "<Down>", lambda e: text_space.yview("scroll",
        1, "units"));

    text_space.tag_bind(tid, "<Right>", lambda e: text_space.xview("scroll",
        1, "units"));

    text_space.tag_bind(tid, "<Left>", lambda e: text_space.xview("scroll",
        -1, "units"));
    
    text_space.focus();

    win.bind("<MouseWheel>", onMouseScroll);

    #items_listbox.bind('<<ListboxSelect>>', showPopulation)
    items_listbox.bind('<Double-1>', display_content);
    items_listbox.bind('<Return>', display_content);

    win.protocol("WM_DELETE_WINDOW", uninstall);

def main():
    global SCROLL_GRAN;

    main_win = tkinter.Tk();
    main_win.title(PROGRAM_NAME);
    main_win.geometry("%sx%s+200+100" % (WIN_WIDTH, WIN_HEIGHT));
    main_frame = None;
    platform = main_win.tk.call('tk', 'windowingsystem');
    SCROLL_GRAN = 120 if platform.startswith("win") else 1;

    def deinit():
        nonlocal main_win, main_frame, st
        st.set("Restart");
        main_frame.destroy();

    def init(win = main_win):
        nonlocal main_win, main_frame, st
        main_frame = tkinter.ttk.Frame(main_win, takefocus = 1);
        intro_box = tkinter.ttk.Label(main_frame, text = content.ABOUT);

        
        intro_box.pack(fill = tkinter.BOTH, expand = True);

        st_btn = tkinter.Button(main_frame, background = "green", textvariable = st,
                font = tkinter.font.Font(family="Arial", size = 40, weight =
                    "bold"), command = command);
        st_btn.pack(fill = tkinter.BOTH, expand = True);

        main_frame.pack(fill = tkinter.BOTH, expand = True);
    
    command = lambda : start(main_win, init, deinit)

    st = tkinter.StringVar();
    st.set("Start");

    init();
    main_win.mainloop();



if __name__ == "__main__":
    main();
