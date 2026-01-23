from FlexiKit import Memory
import os

def main():
    """
    Main function for the terminal-based memory application.
    """
    # Instantiate the Memory class outside the loop to keep the handle open.
    mem = Memory()
    os.system("cls")
    
    print("Memory Terminal Application")
    print("----------------------------")
    print("Available commands:")
    print("  pid <process_name>    - Find and open a process.")
    print("  read <address> <size> - Read raw bytes.")
    print("  write <address> <data> - Write raw bytes.")
    print("  read_int <address>    - Read an integer.")
    print("  write_int <address> <value> - Write an integer.")
    print("  read_float <address>  - Read a float.")
    print("  write_float <address> <value> - Write a float.")
    print("  close                 - Close the current process handle.")
    print("  exit                  - Exit the application.")
    
    current_pid = None

    while True:
        try:
            user_input = input(f"> ")
            parts = user_input.strip().split()
            command = parts[0].lower()
            args = parts[1:]

            if command == "pid":
                if not args:
                    print("Usage: pid <process_name>")
                    continue
                try:
                    mem.open_process(args[0])
                    print(f"Process '{args[0]}' opened. PID: {os.getpid()}")
                except (ValueError, RuntimeError) as e:
                    print(f"Error: {e}")
            
            elif command == "read":
                if len(args) != 2:
                    print("Usage: read <address> <size>")
                    continue
                try:
                    address = int(args[0], 16)
                    size = int(args[1])
                    data = mem.read_memory(address, size)
                    print(f"Read {size} bytes: {data.hex()}")
                except (ValueError, RuntimeError, OSError) as e:
                    print(f"Error: {e}")

            elif command == "write":
                if len(args) != 2:
                    print("Usage: write <address> <data>")
                    continue
                try:
                    address = int(args[0], 16)
                    data = bytes.fromhex(args[1])
                    mem.write_memory(address, data)
                    print("Write successful.")
                except (ValueError, RuntimeError, OSError) as e:
                    print(f"Error: {e}")

            elif command == "read_int":
                if len(args) != 1:
                    print("Usage: read_int <address>")
                    continue
                try:
                    address = int(args[0], 16)
                    value = mem.read_int(address)
                    print(f"Read integer: {value}")
                except (ValueError, RuntimeError, OSError) as e:
                    print(f"Error: {e}")

            elif command == "write_int":
                if len(args) != 2:
                    print("Usage: write_int <address> <value>")
                    continue
                try:
                    address = int(args[0], 16)
                    value = int(args[1])
                    mem.write_int(address, value)
                    print("Write successful.")
                except (ValueError, RuntimeError, OSError) as e:
                    print(f"Error: {e}")

            elif command == "read_float":
                if len(args) != 1:
                    print("Usage: read_float <address>")
                    continue
                try:
                    address = int(args[0], 16)
                    value = mem.read_float(address)
                    print(f"Read float: {value}")
                except (ValueError, RuntimeError, OSError) as e:
                    print(f"Error: {e}")

            elif command == "write_float":
                if len(args) != 2:
                    print("Usage: write_float <address> <value>")
                    continue
                try:
                    address = int(args[0], 16)
                    value = float(args[1])
                    mem.write_float(address, value)
                    print("Write successful.")
                except (ValueError, RuntimeError, OSError) as e:
                    print(f"Error: {e}")

            elif command == "close":
                mem.close_process()
            
            elif command == "exit":
                mem.close_process() # Ensure handle is closed
                break

            else:
                print("Unknown command.")
        
        except IndexError:
            print("Invalid command. Please enter a valid command.")
        except KeyboardInterrupt:
            print("\nExiting...")
            mem.close_process()
            break

if __name__ == "__main__":
    main()
