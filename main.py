import tkinter.messagebox, tkinter.ttk, tkinter.scrolledtext, tkinter.font

import content

PROGRAM_NAME = "Simple Stupid";


def start(win, init, deinit):
    def uninstall():
        nonlocal frame, win
        frame.destroy();
        win.protocol("WM_DELETE_WINDOW", lambda : win.destroy());
        init(win);

    

    def display_content(*parg):
        ids = items_listbox.curselection();
        if not ids:
            return
        text_space["state"] = "normal";
        text_space.delete("1.0", "end"); 
        text_space.insert("1.0", content.contents[ids[0]]); 
        text_space["state"] = "disabled";

    deinit();
    items_var = tkinter.StringVar(value = content.items);
    frame = tkinter.ttk.Frame(win, takefocus = 1);
    frame.pack(fill = tkinter.BOTH, expand = True);

    text_space = tkinter.Text(frame, width = 100, height = 100, wrap = "none");
    text_vscrollbar = tkinter.Scrollbar(frame, width = 20, orient = tkinter.VERTICAL, command =
            text_space.yview);
    
    text_space.configure(yscrollcommand = text_vscrollbar.set);

    text_hscrollbar = tkinter.Scrollbar(frame, width = 20, orient = tkinter.HORIZONTAL, command =
            text_space.xview);
    
    text_space.configure(xscrollcommand = text_hscrollbar.set);
    
    text_vscrollbar.grid(row = 3, column = 150, sticky = (tkinter.N, tkinter.S, tkinter.W, tkinter.E));

    text_hscrollbar.grid(row = 0, column = 40, sticky = (tkinter.N, tkinter.S, tkinter.W, tkinter.E))

    items_listbox = tkinter.Listbox(frame, width = 30, height = 30, listvariable = items_var);

    vscrollbar = tkinter.Scrollbar(frame, width = 20, orient = tkinter.VERTICAL, command =
            items_listbox.yview);
    
    items_listbox.configure(yscrollcommand = vscrollbar.set);

    hscrollbar = tkinter.Scrollbar(frame, width = 20, orient = tkinter.HORIZONTAL, command =
            items_listbox.xview);
    
    items_listbox.configure(xscrollcommand = hscrollbar.set);

    hscrollbar.grid(row = 0, column = 0, sticky = (tkinter.N, tkinter.S, tkinter.W, tkinter.E));
    hscrollbar.rowconfigure(0, weight = 1, pad = 5);
    hscrollbar.columnconfigure(0, weight = 1, pad = 5);


    items_listbox.grid(column = 0, row = 3, pady = 5, padx = 5);
    items_listbox.rowconfigure(3, weight = 1, pad = 5);
    items_listbox.columnconfigure(0, weight = 1, pad = 5);

    text_space.insert("1.0", "Select an item and press enter (or double-click) to view content"); 
    text_space.grid(column = 40, row = 3, rowspan = 30, pady = 5, padx = 5);
    text_space["state"] = "disabled";

    #items_listbox.columnconfigure(0, weight = 1, pad = 5);
    #items_listbox.rowconfigure(0, weight = 1, pad = 5);


    vscrollbar.grid(column = 35, row = 3);

    #items_listbox.bind('<<ListboxSelect>>', showPopulation)
    items_listbox.bind('<Double-1>', display_content);
    items_listbox.bind('<Return>', display_content);

    win.protocol("WM_DELETE_WINDOW", uninstall);

def main():
    main_win = tkinter.Tk();
    main_win.title(PROGRAM_NAME);
    main_win.geometry("300x300+200+100");
    main_frame = None;

    def deinit():
        nonlocal main_win, main_frame
        main_frame.destroy();

    def init(win = main_win):
        nonlocal main_win, main_frame
        main_frame = tkinter.ttk.Frame(main_win, takefocus = 1);
        with open("ABOUT.md") as f:
            intro_box = tkinter.ttk.Label(main_frame, text = f.read());

        
        intro_box.pack(fill = tkinter.BOTH, expand = True);

        st_btn = tkinter.Button(main_frame, highlightcolor = "green", text = "Start",
                font = tkinter.font.Font(family="Arial", size = 40, weight =
                    "bold"), command = command);
        st_btn.pack(fill = tkinter.BOTH, expand = True);

        main_frame.pack(fill = tkinter.BOTH, expand = True);
    
    command = lambda : start(main_win, init, deinit)

    init();
    main_win.mainloop();



if __name__ == "__main__":
    main();
