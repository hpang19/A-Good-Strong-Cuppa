import tkinter as tk
# from tkinter import font


class Prompts:
    """
    A class to create prompts for user input within a frame.
    """
    def __init__(self, frame):
        """
        Initialize the Prompts class.
        """
        self.frame = frame
        self.entry_value = tk.StringVar()
        self.greeting = None
        self.entry = None
        self.entry_changed = False

    def on_return(self, event):
        """
        Handles the event when the "Return" key is pressed.
        """
        self.entry_changed = True

    def wait_for_change(self):
        """
        Waits for changes in the entry value.
        """
        if not self.entry_changed:
            self.frame.after(100, self.wait_for_change)
        else:
            self.greeting.pack_forget()
            self.entry.pack_forget()

    def prompt(self, message: str) -> str:
        """
        Prompt for input and get the user input value.

        :param message: a string
        :return: a string input from player
        """
        self.greeting = tk.Label(self.frame, text=message, width=50)
        self.greeting.pack()
        self.entry = tk.Entry(self.frame, textvariable=self.entry_value, width=5)
        self.entry.pack()
        self.entry.bind("<Return>", self.on_return)
        self.wait_for_change()
        self.frame.mainloop()
        return self.entry_value.get()


def print_message(message: str, text_area_object=None, clear=False):
    """
    Print a message to a text area object or the console.

    :param message: a string of message to print
    :postcondition: print a message to a text area object or the console
    """
    if text_area_object:
        if clear:
            text_area_object.delete('1.0', tk.END)
        add_lines(message, text_area_object)
    else:
        print(message, end='')


def add_lines(message: str, text_area_object):
    """
    Add lines to a text area object, maintaining a maximum of 15 lines.

    :param message: a string of message to print
    :postcondition: delete older text if more than 15 lines
    """
    text_area_object.insert(tk.END, message)
    lines = text_area_object.get("1.0", tk.END).splitlines()
    if len(lines) > 15:
        lines_to_delete = len(lines) - 15
        text_area_object.delete(1.0, f"{lines_to_delete}.0")  # Delete older lines
