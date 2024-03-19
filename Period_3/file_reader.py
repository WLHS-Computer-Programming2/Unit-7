'''
Reads the contents of a text file
From Python Crash Course 3rd edition
'''
from pathlib import Path

def main():

  # # accesses all content in file
  # path = Path('Period_3\pi_digits.txt')
  # contents = path.read_text().rstrip()
  # print(contents)

  # read line by line
  path = Path('Period_3\million_digits_pi.txt')
  contents = path.read_text()

  lines = contents.splitlines()
  pi_string = ''
  for line in lines:
    pi_string += line.strip()
  print(f"{pi_string[:52]}...")
  print(f"This is pi to {len(pi_string)-2} decimal places")


  # Ask a user for their birthday in mmddyy form
  # Tell them if their birthday is in pi_string or not
  while True:
    try:
      user_bday = int(input("Enter your birthday in mmddyy form: "))
    except ValueError:
      print("Incorrect form, try again")
      continue
    if str(user_bday) in pi_string:
      print("Your birthday is in the first million digits of pi!")
    else:
      print("Your birthday is not in the first million digits of pi")
  
if __name__ == '__main__':
  main()
