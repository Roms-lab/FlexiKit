import os
import ctypes
import time
import tkinter as tk
from tkinter import ttk, messagebox, filedialog, simpledialog
from ctypes.wintypes import DWORD, HANDLE


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

class time:
    # 1. Get the absolute directory where your DLL is located
    # This assumes time.dll is in the same folder as FlexiKit.py
    _base_path = os.path.dirname(os.path.abspath(__file__))
    _dll_filename = "time.dll"
    
    # 2. Add the directory to the DLL search path (Required for Python 3.8+)
    try:
        os.add_dll_directory(_base_path)
    except (AttributeError, OSError):
        pass # Not on Windows or directory invalid

    # 3. Load the DLL using an absolute path and winmode=0 for compatibility
    _dll_full_path = os.path.join(_base_path, _dll_filename)
    
    try:
        # winmode=0 allows the DLL to find its own dependencies (like MSVC runtime)
        _lib = ctypes.CDLL(_dll_full_path, winmode=0)
    except FileNotFoundError:
        # Fallback if first attempt fails
        raise RuntimeError(f"Could not find { _dll_filename } at { _dll_full_path }. "
                           "Ensure it is compiled as x64.")

    # 4. Configure function signatures
    _lib.WaitSeconds.argtypes = [ctypes.c_int]
    _lib.WaitMinutes.argtypes = [ctypes.c_int]
    _lib.WaitMiliSeconds.argtypes = [ctypes.c_int]
    _lib.WaitMicroSeconds.argtypes = [ctypes.c_int]
    _lib.WaitNanoSeconds.argtypes = [ctypes.c_int]

    @staticmethod
    def WaitSeconds(s):
        time._lib.WaitSeconds(s)

    @staticmethod
    def WaitMinutes(m):
        time._lib.WaitMinutes(m)

    @staticmethod
    def WaitMiliSeconds(ms):
        time._lib.WaitMiliSeconds(ms)

class DLL:
    import os
    import ctypes

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
        self.style = ttk.Style()

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
    
    def DoubleVar(self, value=None):
        return tk.DoubleVar(self.root, value=value)
        
    def BooleanVar(self, value=None):
        return tk.BooleanVar(self.root, value=value)


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
        
    def Grid_configure_row(self, parent, row, **options):
        """Configures row properties for the grid layout."""
        parent.grid_rowconfigure(row, **options)
        
    def Grid_configure_column(self, parent, col, **options):
        """Configures column properties for the grid layout."""
        parent.grid_columnconfigure(col, **options)

    # --- Widget Creation (Tk and Ttk) ---
    def AddLabel(self, parent, text, **options):
        """Creates and returns a Ttk Label."""
        label = ttk.Label(parent, text=text, **options)
        return label

    def AddButton(self, parent, text, command, **options):
        """Creates and returns a Ttk Button."""
        button = ttk.Button(parent, text=text, command=command, **options)
        return button

    def AddEntry(self, parent, **options):
        """Creates and returns a Ttk Entry."""
        entry = ttk.Entry(parent, **options)
        return entry

    def AddText(self, parent, **options):
        """Creates and returns a multi-line Text widget (Tk, no Ttk equivalent)."""
        text_widget = tk.Text(parent, **options)
        return text_widget

    def AddFrame(self, parent, **options):
        """Creates and returns a Ttk Frame."""
        frame = ttk.Frame(parent, **options)
        return frame

    def AddCheckbutton(self, parent, text, variable, **options):
        """Creates and returns a Ttk Checkbutton."""
        checkbutton = ttk.Checkbutton(parent, text=text, variable=variable, **options)
        return checkbutton

    def AddRadiobutton(self, parent, text, variable, value, **options):
        """Creates and returns a Ttk Radiobutton."""
        radiobutton = ttk.Radiobutton(parent, text=text, variable=variable, value=value, **options)
        return radiobutton

    def AddScale(self, parent, **options):
        """Creates and returns a Ttk Scale (slider) widget."""
        scale = ttk.Scale(parent, **options)
        return scale
        
    def AddSpinbox(self, parent, from_value=0, to_value=100, **options):
        """Creates and returns a Ttk Spinbox widget."""
        spinbox = ttk.Spinbox(parent, from_=from_value, to=to_value, **options)
        return spinbox

    def AddCombobox(self, parent, values=None, **options):
        """Creates and returns a Ttk Combobox (dropdown list)."""
        combo = ttk.Combobox(parent, values=values, **options)
        return combo
    
    def AddMenubutton(self, parent, text, **options):
        """Creates and returns a Ttk Menubutton."""
        menubutton = ttk.Menubutton(parent, text=text, **options)
        return menubutton

    def AddMenu(self, parent, **options):
        """Creates and returns a Menu widget (Tk, no Ttk equivalent)."""
        menu = tk.Menu(parent, **options)
        return menu

    def AddMenuBar(self, window):
        """Configures a menu bar for the given window."""
        menu_bar = tk.Menu(window)
        window.config(menu=menu_bar)
        return menu_bar

    def AddListbox(self, parent, **options):
        """Creates and returns a Listbox widget (Tk, no Ttk equivalent)."""
        listbox = tk.Listbox(parent, **options)
        return listbox

    def AddCanvas(self, parent, **options):
        """Creates and returns a Canvas widget (Tk, no Ttk equivalent)."""
        canvas = tk.Canvas(parent, **options)
        return canvas

    def AddLabelFrame(self, parent, text, **options):
        """Creates and returns a Ttk LabelFrame."""
        labelframe = ttk.LabelFrame(parent, text=text, **options)
        return labelframe
    
    def AddPanedWindow(self, parent, orient='horizontal', **options):
        """Creates and returns a Ttk PanedWindow."""
        panedwindow = ttk.PanedWindow(parent, orient=orient, **options)
        return panedwindow

    def AddNotebook(self, parent, **options):
        """Creates and returns a Ttk Notebook (tabbed) widget."""
        notebook = ttk.Notebook(parent, **options)
        return notebook

    def AddScrollbar(self, parent, orient='vertical', **options):
        """Creates and returns a Ttk Scrollbar widget."""
        if orient == 'vertical':
            scrollbar = ttk.Scrollbar(parent, orient=tk.VERTICAL, **options)
        elif orient == 'horizontal':
            scrollbar = ttk.Scrollbar(parent, orient=tk.HORIZONTAL, **options)
        else:
            raise ValueError("Invalid orientation for scrollbar. Use 'vertical' or 'horizontal'.")
        return scrollbar
    
    def AddProgressBar(self, parent, mode='indeterminate', **options):
        """Creates and returns a Ttk Progressbar widget."""
        progressbar = ttk.Progressbar(parent, mode=mode, **options)
        return progressbar
    
    def AddToplevel(self, parent, **options):
        """Creates and returns a Toplevel (sub) window."""
        toplevel = tk.Toplevel(parent, **options)
        return toplevel
    
    def AddSeparator(self, parent, orient='horizontal', **options):
        """Creates and returns a Ttk Separator widget."""
        separator = ttk.Separator(parent, orient=orient, **options)
        return separator
        
    def AddSizegrip(self, parent, **options):
        """Creates and returns a Ttk Sizegrip widget for resizing windows."""
        sizegrip = ttk.Sizegrip(parent, **options)
        return sizegrip
    
    def AddTreeview(self, parent, **options):
        """Creates and returns a Ttk Treeview widget for hierarchical data."""
        treeview = ttk.Treeview(parent, **options)
        return treeview


    # --- Ttk Style and Theme Management ---
    def SetTheme(self, theme_name):
        """Sets the ttk theme for the entire application."""
        self.style.theme_use(theme_name)
    
    def GetThemes(self):
        """Returns a list of all available ttk themes."""
        return self.style.theme_names()

    def ConfigureStyle(self, style_name, **options):
        """Configures a ttk style (e.g., 'TButton')."""
        self.style.configure(style_name, **options)

    # --- Common Dialogs ---
    def ShowMessage(self, title, message):
        """Displays a standard message box."""
        messagebox.showinfo(title, message)

    def AskQuestion(self, title, message):
        """Asks a yes/no question and returns True or False."""
        return messagebox.askyesno(title, message)
    
    def AskYesNoCancel(self, title, message):
        """Asks a yes/no/cancel question and returns True, False, or None."""
        return messagebox.askyesnocancel(title, message)
        
    def AskOpenFile(self, **options):
        """Opens a file selection dialog and returns the file path."""
        return filedialog.askopenfilename(**options)

    def AskSaveFile(self, **options):
        """Opens a save file dialog and returns the file path."""
        return filedialog.asksaveasfilename(**options)

    def AskString(self, title, prompt):
        """Asks the user for a string and returns it."""
        return simpledialog.askstring(title, prompt)


class Memory:
    """
    A Python wrapper for inter-process memory access using Memorydll.dll.
    """

    def __init__(self, dll_name="Memory.dll"):
        """
        Initializes the Memory class and loads the DLL.
        
        Args:
            dll_name (str): The name of the DLL file.
        """
        dll_path = os.path.join(os.path.dirname(__file__), dll_name)

        if not os.path.exists(dll_path):
            raise FileNotFoundError(f"DLL file not found at: {dll_path}")

        try:
            self._memory_dll = ctypes.cdll.LoadLibrary(dll_path)
            self._setup_function_signatures()
        except OSError as e:
            raise RuntimeError(f"Error loading DLL: {e}")
            
        self._h_process = None

    def _setup_function_signatures(self):
        """
        Defines the function prototypes for the C++ DLL functions.
        """
        self._memory_dll.get_process_id.restype = DWORD
        self._memory_dll.get_process_id.argtypes = [ctypes.c_char_p]
        
        self._memory_dll.open_process_by_id.restype = HANDLE
        self._memory_dll.open_process_by_id.argtypes = [DWORD]
        
        self._memory_dll.close_handle.argtypes = [HANDLE]
        
        self._memory_dll.read_process_memory.argtypes = [HANDLE, ctypes.c_void_p, ctypes.c_void_p, ctypes.c_size_t]
        
        self._memory_dll.write_process_memory.argtypes = [HANDLE, ctypes.c_void_p, ctypes.c_void_p, ctypes.c_size_t]

    def __enter__(self):
        return self

    def __exit__(self, exc_type, exc_val, exc_tb):
        self.close_process()

    def open_process(self, process_name: str):
        """Finds and opens a process by name."""
        pid = self._memory_dll.get_process_id(process_name.encode('utf-8'))
        if pid == 0:
            raise ValueError(f"Process '{process_name}' not found.")
        
        self._h_process = self._memory_dll.open_process_by_id(pid)
        if not self._h_process:
            raise RuntimeError("Could not open process. Try running as administrator.")
        print(f"Successfully attached to PID {pid}")

    def close_process(self):
        """Closes the currently opened process handle."""
        if self._h_process:
            self._memory_dll.close_handle(self._h_process)
            self._h_process = None
            print("Process handle closed.")

    def read_memory(self, address: int, size: int) -> bytes:
        """
        Reads a specified number of bytes from a memory address in the target process.

        Args:
            address (int): The memory address to read from.
            size (int): The number of bytes to read.

        Returns:
            bytes: The raw data read from memory.
        """
        if not self._h_process:
            raise RuntimeError("No process is open.")
        buffer = ctypes.create_string_buffer(size)
        try:
            self._memory_dll.read_process_memory(self._h_process, ctypes.c_void_p(address), ctypes.byref(buffer), size)
            return buffer.raw
        except OSError as e:
            raise OSError(f"Error reading memory at address {hex(address)}: {e}")

    def write_memory(self, address: int, data: bytes):
        """
        Writes a block of bytes to a specified memory address in the target process.

        Args:
            address (int): The memory address to write to.
            data (bytes): The data to write.
        """
        if not self._h_process:
            raise RuntimeError("No process is open.")
        if not isinstance(data, bytes):
            raise TypeError("Data must be a bytes object.")
        
        buffer = ctypes.create_string_buffer(data, len(data))
        try:
            self._memory_dll.write_process_memory(self._h_process, ctypes.c_void_p(address), ctypes.byref(buffer), len(data))
        except OSError as e:
            raise OSError(f"Error writing memory at address {hex(address)}: {e}")

    def read_int(self, address: int) -> int:
        """Reads a 4-byte signed integer from a memory address."""
        data = self.read_memory(address, ctypes.sizeof(ctypes.c_int))
        return int.from_bytes(data, 'little', signed=True)
    
    def write_int(self, address: int, value: int):
        """Writes a 4-byte signed integer to a memory address."""
        data = value.to_bytes(ctypes.sizeof(ctypes.c_int), 'little', signed=True)
        self.write_memory(address, data)

    def read_float(self, address: int) -> float:
        """Reads a 4-byte float from a memory address."""
        data = self.read_memory(address, ctypes.sizeof(ctypes.c_float))
        return ctypes.c_float.from_buffer_copy(data).value

    def write_float(self, address: int, value: float):
        """Writes a 4-byte float to a memory address."""
        self.write_memory(address, ctypes.c_float(value))

class Py2D:
    import pygame as game

    # Wrapper Function For Pygame Window
    @staticmethod
    def CreateWindow(width, height, title="Py2D Window"):
        Py2D.game.init()
        window = Py2D.game.display.set_mode((width, height))
        Py2D.game.display.set_caption(title)
        return window
    
    # Fills Screen
    @staticmethod
    def Fill(surface, r, g, b):
        surface.fill((r, g, b))

    @staticmethod
    def HandleRunTime(update_callback=None, draw_callback=None, event_callback=None):
        running = True

        while running:
            for event in Py2D.game.event.get():
                if event.type == Py2D.game.QUIT:
                    running = False

                if event_callback:
                    event_callback(event)

            if update_callback:
                update_callback()

            if draw_callback:
                draw_callback()

            Py2D.game.display.update()

    # Handles Circle Drawing
    @staticmethod
    def DrawCircle(screen, color, x, y, radius):
        Py2D.game.draw.circle(screen, color, (x, y), radius)

    # Handles Rect Drawing
    @staticmethod
    def DrawRect(screen, color, x, y, width, height):
        Py2D.game.draw.rect(screen, color, (x, y, width, height))
class WinAPI:
    import win32api as _api
    from win32con import (
        MB_OK, MB_OKCANCEL, MB_YESNO, 
        MB_ICONINFORMATION, MB_ICONWARNING, MB_ICONERROR, MB_ICONQUESTION,
        IDYES, IDNO, IDOK, IDCANCEL
    )

    @staticmethod
    def Commands():
        print("--- WinAPI Commands ---")
        print("MessageBox(Message, Window_Title, id)")
        print("Beep(frequency=int, duration=int)")
        print("TypeKey(key_code) -> Hex value for key (e.g. 0x41 for 'A')")
        print("Cmd(Command)")
        print("Powershell(Command)")
        print("Flash(title, count)")
        print("SetTransparency(title, 0-255)")
        print("LockPC() -> Win + L")
        print("ToggleMute()")

    @staticmethod
    def MessageBox(Message, Window_Title, id):
        return WinAPI._api.MessageBox(0, Message, Window_Title, id)
    
    @staticmethod
    def Beep(frequency=440, duration=500):
        import win32api
        return win32api.Beep(frequency, duration)
    
    @staticmethod
    def TypeKey(key_code):
        import win32api
        import win32con
        win32api.keybd_event(key_code, 0, 0, 0)
        win32api.keybd_event(key_code, 0, win32con.KEYEVENTF_KEYUP, 0)

    @staticmethod
    def Cmd(Command):
        import os
        os.system(Command)

    @staticmethod
    def Powershell(Command):
        import os
        os.system(f'powershell -command "{Command}"')

    @staticmethod
    def LockPC():
        import ctypes
        ctypes.windll.user32.LockWorkStation()

    @staticmethod
    def Flash(window_title, count=5):
        import win32gui
        hwnd = win32gui.FindWindow(None, window_title)
        if hwnd:
            # 1 = FLASHW_CAPTION, 2 = FLASHW_TRAY, 3 = BOTH
            import ctypes
            from ctypes import wintypes
            class FLASHWINFO(ctypes.Structure):
                _fields_ = [("cbSize", wintypes.UINT), ("hwnd", wintypes.HWND),
                            ("dwFlags", wintypes.DWORD), ("uCount", wintypes.UINT),
                            ("dwTimeout", wintypes.DWORD)]
            info = FLASHWINFO(ctypes.sizeof(FLASHWINFO), hwnd, 3, count, 0)
            ctypes.windll.user32.FlashWindowEx(ctypes.byref(info))
    
    @staticmethod
    def SetTransparency(window_title, level):
        """level: 0 (invisible) to 255 (opaque)"""
        import win32gui
        import win32con
        hwnd = win32gui.FindWindow(None, window_title)
        if hwnd:
            # Add the 'Layered' attribute to the window
            style = win32gui.GetWindowLong(hwnd, win32con.GWL_EXSTYLE)
            win32gui.SetWindowLong(hwnd, win32con.GWL_EXSTYLE, style | win32con.WS_EX_LAYERED)
            # Set transparency level
            import ctypes
            ctypes.windll.user32.SetLayeredWindowAttributes(hwnd, 0, level, 2)

    @staticmethod
    def ToggleMute():
        import win32api
        import win32con
        # VK_VOLUME_MUTE = 0xAD
        win32api.keybd_event(0xAD, 0, 0, 0)
        win32api.keybd_event(0xAD, 0, win32con.KEYEVENTF_KEYUP, 0)