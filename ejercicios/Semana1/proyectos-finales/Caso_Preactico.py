

def print_header():
    """
    Generate and print a header with a title and the creator's name.

    """
    title = """ 
  ██╗  ██╗ █████╗ ███████╗██╗  ██╗██╗███╗   ██╗ ██████╗ 
  ██║  ██║██╔══██╗██╔════╝██║  ██║██║████╗  ██║██╔════╝ 
  ███████║███████║███████╗███████║██║██╔██╗ ██║██║  ███╗
  ██╔══██║██╔══██║╚════██║██╔══██║██║██║╚██╗██║██║   ██║
  ██║  ██║██║  ██║███████║██║  ██║██║██║ ╚████║╚██████╔╝
  ╚═╝  ╚═╝╚═╝  ╚═╝╚══════╝╚═╝  ╚═╝╚═╝╚═╝  ╚═══╝ ╚═════╝"""
    name_creator = """ 
  ⣇⡀⡀⢀ ⢀⣀⢀⣸⡀⣀⠄⢀⣀⣀⡀
  ⠧⠜⣑⡺ ⠣⠼⠣⠼⠏ ⠇⠣⠼⠇⠸"""
    print(title)
    print(name_creator)

def calculate_hashes(num_hashes):
    """
    Calculate and print the hash value for a given input.
    arg: 
        - num_hashes: The input value to hash, must be a string.
    return: 
        - The hash value of the input string.

    """
    value_hash = hash(num_hashes)
    return value_hash


print_header()
user_input = input("Ingrese un valor para calcular su hash: ")  
result = calculate_hashes(user_input)
print(f"El valor hash de '{user_input}' es: {result}")