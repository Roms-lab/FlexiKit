import ctypes
import time
import tkinter as tk
from tkinter import ttk, messagebox, filedialog, simpledialog

# Corrected utility classes
class math:
    @staticmethod
    def add(a, b):
        return a + b

    @staticmethod
    def subtract(a, b):
        return a - b

    @staticmethod
    def divide(a, b):
        # Add error handling for division by zero
        if b == 0:
            raise ValueError("Cannot divide by zero")
        return a / b

    @staticmethod
    def multiply(a, b):
        return a * b

# Avoid using a class named "time" as it shadows the built-in module.
# You can use the built-in time module directly or create a utility function.
def sleep(seconds):
    time.sleep(seconds)

class DLL:
    def __init__(self, lib_path):
        """Loads a DLL or shared library and stores it."""
        try:
            self.lib = ctypes.CDLL(lib_path)
        except OSError as e:
            self.lib = None
            print(f"Error loading DLL: {e}")

    def get_function(self, func_name, arg_types=None, rest_type=None):
        """
        Retrieves a function from the loaded DLL and sets its argument and return types.
        Returns None if the library or function is not found.
        """
        if not self.lib:
            return None
        
        try:
            func = getattr(self.lib, func_name)
            if arg_types:
                func.argtypes = arg_types
            if rest_type:
                func.restype = rest_type
            return func
        except AttributeError:
            print(f"Function '{func_name}' not found in the DLL.")
            return None

    def load_library(self, lib_path):
        """
        Loads or reloads a DLL or shared library.
        """
        try:
            self.lib = ctypes.CDLL(lib_path)
            return True
        except OSError as e:
            print(f"Error loading DLL: {e}")
            self.lib = None
            return False

class UI:
    def __init__(self):
        self.root = tk.Tk()

    def InitUI(self):
        self.root.mainloop()

    def Title(self, title):
        self.root.title(title)

    def Size(self, width, height):
        self.root.geometry(f"{width}x{height}")

    def BgColor(self, color):
        self.root.configure(bg=color)

    # --- Tkinter Variables ---
    def StringVar(self, value=None):
        return tk.StringVar(self.root, value=value)
    
    def IntVar(self, value=None):
        return tk.IntVar(self.root, value=value)
    
    # --- Geometry Managers ---
    def Pack(self, widget, **options):
        """Packs a widget into the parent container."""
        widget.pack(**options)

    def Grid(self, widget, **options):
        """Grids a widget into the parent container."""
        widget.grid(**options)
        
    def Place(self, widget, **options):
        """Places a widget at a specific x,y coordinate."""
        widget.place(**options)

    # --- Widget Creation ---
    def AddLabel(self, parent, text, **options):
        """Creates and returns a label."""
        label = tk.Label(parent, text=text, **options)
        return label

    def AddButton(self, parent, text, command, **options):
        """Creates and returns a button."""
        button = tk.Button(parent, text=text, command=command, **options)
        return button

    def AddEntry(self, parent, **options):
        """Creates and returns a single-line entry widget."""
        entry = tk.Entry(parent, **options)
        return entry

    def AddText(self, parent, **options):
        """Creates and returns a multi-line text widget."""
        text_widget = tk.Text(parent, **options)
        return text_widget

    def AddFrame(self, parent, **options):
        """Creates and returns a frame widget."""
        frame = tk.Frame(parent, **options)
        return frame

    def AddCheckbutton(self, parent, text, variable, **options):
        """Creates and returns a checkbutton."""
        checkbutton = tk.Checkbutton(parent, text=text, variable=variable, **options)
        return checkbutton

    def AddRadiobutton(self, parent, text, variable, value, **options):
        """Creates and returns a radiobutton."""
        radiobutton = tk.Radiobutton(parent, text=text, variable=variable, value=value, **options)
        return radiobutton

    def AddScale(self, parent, **options):
        """Creates and returns a scale (slider) widget."""
        scale = tk.Scale(parent, **options)
        return scale

    def AddMenu(self, parent, **options):
        """Creates and returns a Menu widget."""
        menu = tk.Menu(parent, **options)
        return menu

    def AddMenuBar(self, window):
        """Configures a menu bar for the given window."""
        menu_bar = tk.Menu(window)
        window.config(menu=menu_bar)
        return menu_bar

    # --- Common Dialogs ---
    def ShowMessage(self, title, message):
        """Displays a standard message box."""
        messagebox.showinfo(title, message)

    def AskQuestion(self, title, message):
        """Asks a yes/no question and returns True or False."""
        return messagebox.askyesno(title, message)
        
    def AskOpenFile(self):
        """Opens a file selection dialog and returns the file path."""
        return filedialog.askopenfilename()

    def AskSaveFile(self):
        """Opens a save file dialog and returns the file path."""
        return filedialog.asksaveasfilename()

    def AskString(self, title, prompt):
        """Asks the user for a string and returns it."""
        return simpledialog.askstring(title, prompt)
