import sys
import socket

# --- Configuration ---
DEFAULT_PORT = 80
TIMEOUT_SECONDS = 5
BUFFER_SIZE = 4096

def diagnose_server():
    """
    Diagnoses the status of an HTTP server based on command-line arguments.
    """
    
    # 1. Argument Handling and Validation
    # argv[0] is the script name. We expect 2 or 3 elements (script + 1 or 2 args).
    
    if len(sys.argv) < 2 or len(sys.argv) > 3:
        # Check if invocation lacks any arguments
        print("Error: Improper invocation.")
        print("Usage: python server_diagnoser.py <server_address> [port]")
        # Returns an exit code equal to 1
        sys.exit(1)

    server_address = sys.argv[1]
    server_port = DEFAULT_PORT

    if len(sys.argv) == 3:
        # Optional port argument is provided
        port_str = sys.argv[2]
        try:
            # Check if it is an integer
            server_port = int(port_str)
            # Check if it is in the range 1..65535
            if not 1 <= server_port <= 65535:
                raise ValueError 
        except ValueError:
            # If the second argument is not a valid port number
            print(f"Error: Invalid port number '{port_str}'. Port must be an integer in range 1..65535.")
            # Returns an exit code equal to 2
            sys.exit(2)

    # 2. Connection and HTTP Request
    
    try:
        # Create a TCP socket
        s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        
        # Set the connection timeout
        s.settimeout(TIMEOUT_SECONDS)
        
        print(f"Attempting to connect to {server_address}:{server_port}...")
        
        # Connect to the server
        s.connect((server_address, server_port))
        
        # Construct the HTTP HEAD request (using HEAD instead of GET)
        # The Host header is required for HTTP/1.1
        request = (
            f"HEAD / HTTP/1.1\r\n"
            f"Host: {server_address}\r\n"
            f"Connection: close\r\n" # Tell the server we will close the connection after the response
            f"\r\n" # Required empty line to end the headers
        ).encode('utf-8')
        
        # Send the request
        s.sendall(request)
        
        # Receive the first part of the response
        response_data = s.recv(BUFFER_SIZE)
        
        # Connection succeeded
        if response_data:
            # Decode and split the response into lines
            response_lines = response_data.decode('utf-8', 'ignore').split('\n')
            
            # Print the very first line of the server’s response (Status Line)
            # The strip() removes leading/trailing whitespace, including '\r'
            print("\nServer is ALIVE. Response Status Line:")
            print(response_lines[0].strip())
            
            # Successful exit
            sys.exit(0)
        else:
            # This case indicates a successful connection but no immediate data, 
            # which is an unexpected failure in a typical HTTP check.
            print("Error: Connection succeeded but received no response data.")
            sys.exit(4)

    except socket.timeout:
        # Handle connection timeout
        print(f"Error: Connection to {server_address}:{server_port} timed out after {TIMEOUT_SECONDS} seconds.")
        # Returns an exit code equal to 3
        sys.exit(3)
        
    except socket.error as e:
        # Handle connection failures due to any other reason (e.g., connection refused, DNS error)
        print(f"Error: Connection to {server_address}:{server_port} failed. Reason: {e}")
        # Returns an exit code equal to 4
        sys.exit(4)
        
    finally:
        # Close the socket connection
        if 's' in locals() and isinstance(s, socket.socket):
            s.close()

if __name__ == "__main__":
    diagnose_server()


# Level of difficulty

# Easy
# Objectives

# Learn how to:

#     use the socket module and its basic functionalities;
#     manage simple http connections.

# Scenario

# We want you to write a simple CLI (Command Line Interface) tool which can be used in order to diagnose the current status of a particular http server. The tool should accept one or two command line arguments:

#     (obligatory) the address (IP or qualified domain name) of the server to be diagnosed (the diagnosis will be extremely simple, we just want to know if the server is dead or alive)
#     (optional) the server's port number (any absence of the argument means that the tool should use port 80)
#     use the HEAD method instead of GET — it forces the server to send the full response header but without any content; it's enough to check if the server is working properly; the rest of the request remains the same as for GET.

# We also assume that:

#     the tool checks if it is invoked properly, and when the invocation lacks any arguments, the tool prints an error message and returns an exit code equal to 1;
#     if there are two arguments in the invocation line and the second one is not an integer number in the range 1..65535, the tool prints an error message and returns an exit code equal to 2;
#     if the tool experiences a timeout during connection, an error message is printed and 3 is returned as the exit code;
#     if the connection fails due to any other reason, an error message appears and 4 is returned as the exit code;
#     if the connection succeeds, the very first line of the server’s response is printed. 

# Hints:

#     to access command line arguments, use the argv variable from the sys module; its length is always one more than the actual number of arguments, as argv[0] stores your script's name; this means that the first argument is at argv[1] and the second at argv[2]; don't forget that the command line arguments are always strings!
#     returning an exit code equal to n can be achieved by invoking the exit(n) function.
