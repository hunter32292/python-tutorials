import json
from PersonSimple import People
from PersonComplex import ComplexPeople

def work_on_file(file_name):
    lines = ""
    try:
        with open(file_name) as f_obj:
            lines = f_obj.readlines()
        if len(lines) <= 0:
            print("File is empty")
            return
    except FileNotFoundError:
        print("Cannot access file %s" % file_name)

    if ".json" in file_name:
        return json.load(open(file_name))

    if ".csv" in file_name:
        new_lines = []
        for line in lines:
            line = line.split(',')
            new_lines.append(line)
        return new_lines

    return lines


if __name__ == "__main__":
    people = []
    lines = work_on_file("MOCK_DATA.csv")
    for line in lines:
        people.append(ComplexPeople(line[0],line[1],line[2],line[3],line[4],line[5]))
    print("People: %s" % people)

    people = []
    lines = work_on_file("MOCK_DATA.json")
    for line in lines:
        people.append(ComplexPeople(line['id'],line['city'],line['last_name'],line['first_name'],line['gender'],line['ip_address']))
    print("People: %s" % people)

