def main():

    import tkinter as tk
    from tkinter import ttk
    import threading
    import assistant

    VOICE_ENABLED = True

    root = tk.Tk()
    root.title("AI Voice Assistant")
    root.geometry("1200x750")
    root.configure(bg="#202123")

    root.rowconfigure(0, weight=1)
    root.columnconfigure(1, weight=1)

    # ---------- SIDEBAR ----------
    sidebar = tk.Frame(root, bg="#111111", width=250)
    sidebar.grid(row=0, column=0, sticky="ns")

    title = tk.Label(
        sidebar,
        text="Chat History",
        bg="#111111",
        fg="white",
        font=("Segoe UI", 14, "bold")
    )
    title.pack(pady=10)

    history_list = tk.Listbox(
        sidebar,
        bg="#1a1a1a",
        fg="white",
        bd=0,
        font=("Segoe UI", 11),
        highlightthickness=0
    )
    history_list.pack(fill="both", expand=True, padx=10, pady=10)

    # ---------- CHAT AREA ----------
    chat_container = tk.Frame(root, bg="#202123")
    chat_container.grid(row=0, column=1, sticky="nsew")

    chat_container.rowconfigure(0, weight=1)
    chat_container.columnconfigure(0, weight=1)

    canvas = tk.Canvas(chat_container, bg="#202123", highlightthickness=0)
    canvas.grid(row=0, column=0, sticky="nsew")

    style = ttk.Style()
    style.theme_use("default")

    style.configure(
        "Vertical.TScrollbar",
        background="#40414F",
        troughcolor="#202123",
        arrowcolor="white"
    )

    scrollbar = ttk.Scrollbar(chat_container, orient="vertical", command=canvas.yview)
    scrollbar.grid(row=0, column=1, sticky="ns")

    canvas.configure(yscrollcommand=scrollbar.set)

    chat_frame = tk.Frame(canvas, bg="#202123")
    canvas.create_window((0, 0), window=chat_frame, anchor="nw")

    def update_scroll(event):
        canvas.configure(scrollregion=canvas.bbox("all"))

    chat_frame.bind("<Configure>", update_scroll)

    # ---------- MESSAGE ----------
    def add_message(sender, message):

        container = tk.Frame(chat_frame, bg="#202123")

        if sender == "user":
            color = "#4e9af1"
            anchor = "e"
        else:
            color = "#444654"
            anchor = "w"

        bubble = tk.Label(
            container,
            text=message,
            bg=color,
            fg="white",
            font=("Segoe UI", 13),
            wraplength=750,
            justify="left",
            padx=10,
            pady=6
        )

        bubble.pack(anchor=anchor, pady=5)
        container.pack(fill="x", padx=20)

        canvas.update_idletasks()
        canvas.yview_moveto(1)

    # ---------- PROCESS ----------
    def process_message(text):

        response = assistant.process(text)

        if response == "exit":
            root.destroy()
            return

        add_message("assistant", response)

        if VOICE_ENABLED:
            assistant.speak(response)

    # ---------- SEND ----------
    def send_message(event=None):

        text = entry.get()

        if not text.strip():
            return

        add_message("user", text)
        history_list.insert(tk.END, text)

        entry.delete(0, tk.END)

        threading.Thread(
            target=process_message,
            args=(text,),
            daemon=True
        ).start()

    # ---------- VOICE ----------
    def voice_input():

        add_message("assistant", "Listening...")

        command = assistant.listen()

        if command:
            add_message("user", command)

            threading.Thread(
                target=process_message,
                args=(command,),
                daemon=True
            ).start()

    # ---------- TOGGLE VOICE ----------
    def toggle_voice():

        nonlocal VOICE_ENABLED

        VOICE_ENABLED = not VOICE_ENABLED

        if VOICE_ENABLED:
            voice_btn.config(text="Voice ON")
        else:
            voice_btn.config(text="Voice OFF")

    # ---------- CLEAR ----------
    def clear_chat():

        for widget in chat_frame.winfo_children():
            widget.destroy()

        history_list.delete(0, tk.END)

    # ---------- INPUT ----------
    bottom = tk.Frame(root, bg="#202123")
    bottom.grid(row=1, column=1, sticky="ew", padx=10, pady=10)

    bottom.columnconfigure(0, weight=1)

    entry = tk.Entry(
        bottom,
        font=("Segoe UI", 13),
        bg="#40414F",
        fg="white",
        insertbackground="white",
        relief="flat"
    )

    entry.grid(row=0, column=0, sticky="ew", padx=5)
    entry.bind("<Return>", send_message)

    send_btn = tk.Button(
        bottom,
        text="Send",
        command=send_message,
        width=8,
        bg="#10A37F",
        fg="white"
    )
    send_btn.grid(row=0, column=1, padx=5)

    mic_btn = tk.Button(
        bottom,
        text="🎤",
        command=voice_input,
        width=5,
        bg="#10A37F",
        fg="white"
    )
    mic_btn.grid(row=0, column=2, padx=5)

    voice_btn = tk.Button(
        bottom,
        text="Voice ON",
        command=toggle_voice,
        width=10
    )
    voice_btn.grid(row=0, column=3, padx=5)

    clear_btn = tk.Button(
        bottom,
        text="Clear",
        command=clear_chat,
        width=8
    )
    clear_btn.grid(row=0, column=4, padx=5)

    add_message("assistant", "Hello! I am your AI assistant.")

    root.mainloop()


if __name__ == "__main__":
    main()