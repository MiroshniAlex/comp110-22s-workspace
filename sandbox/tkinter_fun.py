"""Tryin out tkinter."""

import tkinter as tk


def main() -> None:
    """Entrypoint of program."""
    global window
    window = tk.Tk()
    # labels()
    # buttons()
    # basic_entry()
    # multiline_text()
    # frames()
    # frame_border_effects()
    # label_placer()
    # grids()
    address_entry_form()
    window.mainloop()


def labels() -> None:
    """Basic tkinter labels. Shows unchangable text."""
    greeting = tk.Label(
        text="Hello, Tkinter",
        foreground="crimson",  # sets text color white
        background="#34A2FE"   # sets background color to sky blue
    )
    label = tk.Label(
        text="This is a line of text.",
        fg="crimson",
        bg="black",
        width=15,
        height=10    
    )
    greeting.pack()
    label.pack()


def buttons() -> None:
    """Basic button (can have on click effect by calling function)."""
    button = tk.Button(
        text="Click me!",
        width=25,
        height=5,
        bg="lightgreen",
        fg="navy"
    )
    button.pack()


def basic_entry() -> None:
    """Basic entry widget (collects text from user)."""
    label = tk.Label(text="Name")
    global entry
    entry = tk.Entry(fg="Yellow", bg="blue", width=50)
    window.bind('<Return>', return_to_get)
    
    label.pack()
    entry.pack()


def return_to_get(event):
    """Gets an entry, prints it, and deletes it."""
    print(entry.get())
    entry.delete(0, tk.END)
 

def multiline_text() -> None:
    """Using text widget. Similar to entry but multiline."""
    text_box = tk.Text()
    text_box.pack()
    
    # To use text.get("<line>.<character>","<line>.<character>")
    # For all text in a text widget, use text.get("1.0", tk.END)
    # Same concept applies to .delete and .insert


def frames() -> None:
    """Using frame widgets to contain other widgets."""
    frame_a = tk.Frame()
    frame_b = tk.Frame()

    label_a = tk.Label(master=frame_a, text="Frame A")
    label_b = tk.Label(master=frame_b, text="Frame B", fg="crimson", bg="black")

    label_a.pack()
    label_b.pack()

    # Order in which frames are pack is what matters.

    frame_b.pack()
    frame_a.pack()


def frame_border_effects() -> None:
    """Tests different border effects for frams."""
    # Possible relief artibutes
    border_effects: dict[str, tk._Relief] = {
        "flat": tk.FLAT,
        "sunken": tk.SUNKEN,
        "raised": tk.RAISED,
        "groove": tk.GROOVE,
        "ridge": tk.RIDGE,
    }

    for relief_name, relief_type in border_effects.items():
        frame = tk.Frame(master=window, relief=relief_type, borderwidth=5, bg="skyblue")
        frame.pack()
        label = tk.Label(master=frame, text=relief_name, bg="lightblue", fg="black")
        label.pack()


def label_placer() -> None:
    """Creates two labels to place in different locations."""
    frame = tk.Frame(master=window, width=150, height=150, bg="skyblue")
    frame.pack(fill=tk.BOTH, expand=True)

    label1 = tk.Label(master=frame, text="I'm original.", bg="lightgreen")
    label1.place(x=0, y=0)
    
    label2 = tk.Label(master=frame, text="I'm at 75,75", bg="coral")
    label2.place(x=75, y=75)


def grids() -> None:
    """Creates a 3x3 grid of frames."""
    for i in range(3):
        window.columnconfigure(i, weight=1, minsize=75)
        window.rowconfigure(i, weight=1, minsize=50)
        for j in range(3):
            frame = tk.Frame(
                master=window,
                relief=tk.SUNKEN,
                borderwidth=1,
            )
            frame.grid(row=i, column=j)
            label = tk.Label(master=frame, text=f"Row {i}\nColumn {j}")
            label.pack()


def address_entry_form() -> None:
    """Practice creating a fillable form."""
    text_list = [
        "First Name:",
        "Last Name:",
        "Address Line 1:",
        "Address Line 2:",
        "City:",
        "State/Province:",
        "Postal Code:",
        "Country:"
    ]

    # Creates grid of lables in column 0 and entrys in column 1

    window.columnconfigure(0, minsize=20)
    window.columnconfigure(1, weight=1, minsize=100)
    for i in range(7):
        for j in range(2):
            frame = tk.Frame(master=window)
            frame.grid(row=i, column=j)
            if j == 0:
                lbe = tk.Label(master=frame, text=text_list[i])
                lbe.pack(side=tk.RIGHT)
            else:
                entry = tk.Entry(master=frame, width=50)
                entry.pack(anchor='w', side=tk.LEFT, expand=True)

    # Creates buttons

    # submit = tk.Button(master=window, text="Submit", relief=tk.RAISED, borderwidth=1)
    # submit.pack(anchor='se')

    # clear = tk.Button(master=window, text="Clear", relief=tk.RAISED, borderwidth=1)
    # clear.pack(anchor='se')


main()