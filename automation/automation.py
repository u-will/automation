import re

def find_phone_number(unclean_file_path, clean_file_path):      
  with open("{unclean_file_path}", "r") as file:
    text = file.read()
    unclean_phone_number =re.findall (r"\d{3}.?\d{3}.?\d{4}", text)
    phone_numbers=[]
    for numbers in unclean_phone_number:
      numbers = numbers.replace(')','')
      numbers = numbers.replace('.', '')
      numbers = numbers.replace('-', '')
      numbers = f"{numbers[0:3]}-{numbers[3:6]}-{numbers[6:11]}"
      phone_numbers.append(numbers)
    phone_numbers.sort()
  with open("{clean_file_path}","w") as file:
    for phone_number in phone_numbers:
      file.write(phone_number+'\n')
      

def find_email(unclean_file_path, clean_file_path):
  with open ("{unclean_file_path}","r") as file:
    text = file.read()
    emails = re.findall(r"[_a-z\.\d-]+@[a-z\d-]+\.[a-z]+",text)
    emails.sort()
    # print(emails)
  with open ("{clean_file_path}",'w' ) as file:
    for email in emails:
      file.write(email+'\n')
 
if __name__ == "__main__":
    find_email(assets/potential-contacts.txt assets/email.txt)
    find_phone_number(assets/potential-contacts.txt assets/contacts.txt)
