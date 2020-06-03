from pprint import pprint
import csv
import re


def read_csv(file_path):
    with open(file_path) as f:
        rows = csv.reader(f, delimiter=",")
        return list(rows)

def fix_names_surnames(each_list):
    names = (each_list[0]+' '+ each_list[1] +' '+ each_list[2])
    names_split = re.split(r'\ ', names)
    each_list[0]=names_split[0]
    each_list[1]=names_split[1]
    each_list[2]=names_split[2]

def fix_phone_naumbers(each_list):
    text = each_list[-2]
    pattern = re.compile(r"^((8|\+7))([\- ]?)?(\()?(\d{3})(\)?)([\- ]?)?([\d]{3})([\- ]?)?([\d]{2})([\- ]?)?([\d]{2})(\ )?(\()?(\ *д*о*б*\.*)( *)(\d{0,4})(\)?)?$")
    text_res = pattern.sub(r"+7(\5)\8-\10-\12 \15\17", text)
    each_list[-2] = text_res

def no_dubs(contacts_list):
    for i in contacts_list[1:]:
        for j in contacts_list[1:]:
            if i[0] == j[0]:
                for r in range (7):
                    if j[r] == '':
                        j[r] = i[r]
                
    return [contacts_list[0]]+list(set(map(tuple,contacts_list[1:])))


def write_to(output_path, output_list):
    with open(output_path, "w") as f:
        datawriter = csv.writer(f, delimiter=',')
        datawriter.writerows(output_list)

if __name__ == "__main__":
    contacts_list = read_csv('phonebook_raw.csv')
    for each_list in contacts_list[1:]:
        fix_names_surnames(each_list)
        fix_phone_naumbers(each_list)
    output_list = no_dubs(contacts_list)
    write_to("phonebook.csv", output_list)