from FlexiKit_Portable.FlexiKit import DLL
import ctypes
import os

# Create DLL instance, loading the library
dll = DLL("FlexiKit_Portable/Time.dll")

# Get the WaitSeconds function, assuming it takes an int and returns void
wait_seconds = dll.get_function("WaitSeconds", arg_types=[ctypes.c_int], rest_type=None)

if wait_seconds:
    os.system("cls")
    print("Calling WaitSeconds(2)...")
    wait_seconds(2)  # Call the function with argument 2 seconds
else:
    print("Function not found or failed to load.")
