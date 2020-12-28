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
        nonlocal frame, win
        frame.destroy();
        win.protocol("WM_DELETE_WINDOW", lambda : win.destroy());
        init(win);


    def display_content(*parg):
        nonlocal tid, items_listbox
        ids = items_listbox.curselection();
        if not ids:
            return
        text_space.itemconfigure(tid, state = "normal");
        text_space.delete(tid, "1.0", "end"); 
        text_space.insert(tid, "1.0", content.contents[ids[0]]); 

        if int(text_space.index(tid, 'end - 1 line').split('.')[0]) <= 4:
            text_space.insert(tid, "end", "\n%s" % (NO_CONTENT,)); 

        text_space.itemconfigure(tid, state = "disabled");

    deinit();
    items_var = tkinter.StringVar(value = content.items);
    frame = tkinter.ttk.Frame(win, height = WIN_HEIGHT, width = WIN_WIDTH, takefocus = 1);
    frame.grid(column = 0, row = 0, sticky = (tkinter.N, tkinter.S, tkinter.W, tkinter.E));
    frame.rowconfigure(0, weight = 1, pad = 0);
    frame.columnconfigure(0, weight = 1, pad = 0);

    items_listbox = tkinter.Listbox(frame, width = 30, height = WIN_HEIGHT, listvariable = items_var);
    items_listbox.grid(column = 0, row = 3, pady = 5, padx = 5);
    items_listbox.columnconfigure(0, weight = 1, pad = 5);

    vscrollbar = tkinter.Scrollbar(frame, width = 20, orient = tkinter.VERTICAL, command =
            items_listbox.yview);

    vscrollbar.grid(column = int(items_listbox["width"]) + 5, row = 3, sticky = (tkinter.N, tkinter.S, tkinter.W, tkinter.E));

    vscrollbar.columnconfigure(int(vscrollbar.grid_info()["column"]), weight = 1);

    items_listbox.configure(yscrollcommand = vscrollbar.set);

    hscrollbar = tkinter.Scrollbar(frame, width = 20, background = "black", orient = tkinter.HORIZONTAL, command =
            items_listbox.xview);

    hscrollbar.grid(row = 0, column = 0, sticky = (tkinter.N, tkinter.S, tkinter.W, tkinter.E));
    hscrollbar.rowconfigure(0, weight = 1, pad = 5);
    
    items_listbox.configure(xscrollcommand = hscrollbar.set);

    text_space = tkinter.Canvas(frame, height = MAX_LINES, width = MAX_COLS);

    tid = text_space.create_text(0, 0, text = INTRO, font = "monospace"); 
    text_space.grid(column = items_listbox["width"] + (5 + int(vscrollbar["width"])), row = 3, pady = 5, padx = 5);
    text_space.itemconfigure(tid, state = "disabled");

    text_vscrollbar = tkinter.Scrollbar(frame, width = 20, orient = tkinter.VERTICAL, command =
            text_space.yview);
    
    text_space.configure(yscrollcommand = text_vscrollbar.set);

    text_hscrollbar = tkinter.Scrollbar(frame, width = 20, orient = tkinter.HORIZONTAL, command =
            text_space.xview);
    
    text_space.configure(xscrollcommand = text_hscrollbar.set);
    
    text_vscrollbar.grid(row = 3, column = int(text_space.grid_info()["column"]) + int(text_space["width"]), sticky = (tkinter.N, tkinter.S, tkinter.W, tkinter.E));

    text_hscrollbar.pack(side = tkinter.RIGHT, expand = True, fill = tkinter.Y);
    
    text_space.bind("<Up>", lambda e: text_space.yview("scroll",
        -1, "units"));

    text_space.bind("<Down>", lambda e: text_space.yview("scroll",
        1, "units"));

    text_space.bind("<Right>", lambda e: text_space.xview("scroll",
        1, "units"));

    text_space.bind("<Left>", lambda e: text_space.xview("scroll",
        -1, "units"));


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
        nonlocal main_win, main_frame
        main_frame.destroy();

    def init(win = main_win):
        nonlocal main_win, main_frame
        main_frame = tkinter.ttk.Frame(main_win, takefocus = 1);
        intro_box = tkinter.ttk.Label(main_frame, text = content.ABOUT);

        
        intro_box.pack(fill = tkinter.BOTH, expand = True);

        st_btn = tkinter.Button(main_frame, background = "green", text = "Start",
                font = tkinter.font.Font(family="Arial", size = 40, weight =
                    "bold"), command = command);
        st_btn.pack(fill = tkinter.BOTH, expand = True);

        main_frame.pack(fill = tkinter.BOTH, expand = True);
    
    command = lambda : start(main_win, init, deinit)

    init();
    main_win.mainloop();



if __name__ == "__main__":
    main();
