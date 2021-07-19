# Created by Antonio Di Mariano (antonio.dimariano@gmail.com) at 21/09/2019
import json


def students_generator(qty, initial_balance=600, currency='USD'):
    """
    Appends to a list a dictionary
    :param qty:
    :param initial_balance:
    :param currency:
    :return:
    """
    students = []
    for i in range(0,qty):
        students.append({"name": "student_"+str(i),
                         "balance": initial_balance})
    return students


def write_list_to_file(list_to_write,file_path='students_list.json'):
    """
    writes the given list on the given file
    :param list_to_write:
    :param file_path:
    :return:
    """
    try:
        with open(file_path, 'w') as fout:
            json.dump(list_to_write, fout)
        return 1
    except Exception as file_error:
        print("EXCEPTION Writing to the file:",file_path,file_error)
        exit(-1)