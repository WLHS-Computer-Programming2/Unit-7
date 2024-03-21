from pathlib import Path

# path = Path(r'Period_3\programming.txt')
# message = "I love Python!"
# message += "\nand making games in Pygame!"
# path.write_text(message)

# prompt a user for their full name
# add their full name to a file called
# guest.txt
# path = Path(r'Period_3\guest.txt')
# full_name = input("Enter your full name: ")
# path.write_text(full_name)

# Exception handling
# path = Path(r'Period_3\alice.txt')
# try:
#     path.read_text()
# except FileNotFoundError:
#     print(f"The file {path} does not exist")

file_name = input("Give me a good file name: ")
path = Path(f"{file_name}.txt")
path.write_text("Success!")
print(fr"\nthis is a string")