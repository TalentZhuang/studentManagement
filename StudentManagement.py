import os
import re

file_name = 'student_info.txt'


def menu():
    print('''
    ====Student Management System=====
                    Menu
                              
        1: insert new students info   
        2: search students info
        3: delete students info
        4: modify students info
        5: sort students info
        6: count students number
        7: show all students info
        0: exit
    ===================================
    ''')


def show_students(student_list):
    if not student_list:
        print("(o@.@o) no student data, (o@.@o)")
        return
    # define column name format
    title_format = "{:^6}{:^12}\t{:^8}\t{:^10}\t{:^10}\t{:^10}"
    print(title_format.format("ID", "Name", "English", "Python", "C", "Total"))
    data_format = "{:^6}{:^12}\t{:^8}\t{:^10}\t{:^10}\t{:^10}"
    for st in student_list:
        print(data_format.format(st.get('id'), st.get('name'), str(st.get('english')), str(st.get('python')),
                                 str(st.get('c')), str(st.get('english') + st.get('python') + st.get('c'))))


def save(students):
    # try:
    #     st_txt = open(file_name, 'a')
    # except Exception as e:
    #     st_txt = open(file_name, 'w')
    # for student in students:
    #     st_txt.write(str(student) + '\n')
    # st_txt.close()
    if os.path.exists(file_name):
        st_txt = open(file_name, 'a')
    else:
        st_txt = open(file_name, 'w')
    for student in students:
        st_txt.write(str(student) + '\n')
    st_txt.close()


def insert():
    studentList = []
    mark = True
    while mark:
        id = input("please input student id:")
        if not id:
            break
        name = input("please input student name:")
        if not name:
            break
        try:
            english = int(input("please input English score"))
            python = int(input("please input Python score"))
            c = int(input("please input C score"))
        except:
            print("invalid input, please input inter number")
            continue
        student = {'id': id, 'name': name, 'english': english, 'python': python, 'c': c}
        studentList.append(student)
        inputMark = input("continue insert? (y/n)")
        if inputMark == 'y':
            mark = True
        else:
            mark = False
    save(studentList)
    print("insert is done")


def search():
    mark = True
    st_query = []
    while mark:
        id = ''
        name = ''
        if os.path.exists(file_name):
            mode = input('please input search mode, input 1 search by ID: input 2 search by name: ')
            if mode == '1':
                st_id = input('please input student ID: ')
            elif mode == '2':
                name = input('please input student name: ')
            else:
                inputMark = input('invalid input, continue to search y/n: ')
                if inputMark != 'y':
                    mark = False
                continue
            with open(file_name, 'r') as st_txt:
                students = st_txt.readlines()
            for st in students:
                st_dict = eval(st)
                if st_id is not '':
                    if st_dict.get('id') == id:
                        st_query.append(st_dict)
                if name is not '':
                    if st_dict.get('name') == name:
                        st_query.append(st_dict)
            show_students(st_query)
            st_query.clear()
            inputMark = input('continue search? y/n: ')
            if inputMark != 'y':
                mark = False
        else:
            print('no students info inserted')
            return


def delete():
    mark = True
    while mark:
        show()
        st_id = input("please input student id you want to delete: ")
        if st_id is not '':
            if os.path.exists(file_name):
                with open(file_name, 'r') as st_txt:
                    students_old = st_txt.readlines()
            else:
                print("students info file does not exist. please insert student info first")
                break
            ifdel = False
            if students_old:
                with open(file_name, 'w') as wfile:
                    for st in students_old:
                        st_dict = dict(eval(st))
                        if st_dict.get('id') != st_id:
                            wfile.write(st)
                        else:
                            ifdel = True
                    if ifdel:
                        print("ID: %s student is deleted..." % st_id)
                    else:
                        print('no id = %s student is found' % st_id)
            else:
                print("no student info")
                break
            show()
            input_mark = input('do you want continue delete? y/n: ')
            if input_mark != 'y':
                mark = False
        else:
            input_mark = input('you did not input student id, continue to delete y/n?: ')
            if input_mark != 'y':
                mark = False

def modify():
    print('modify')


def sort():
    show()
    if os.path.exists(file_name):
        with open(file_name, 'r') as st_txt:
            students = st_txt.readlines()
        students_dict = []
        for st in students:
            d = dict(eval(st))
            students_dict.append(d)
    else:
        print('there is no students info, back to main menu')
        menu()
        return
    asc_or_desc = input('please input (0: ascent; 1 descent): ')
    if asc_or_desc == '0':
        asc_or_desc = True
    elif asc_or_desc == '1':
        asc_or_desc = False
    else:
        print('Wrong input, please select from main menu')
        menu()
        return
    mode = input('please select sort by (1: Engling, 2: Python, 3: C, 0:total): ')
    if mode == '1':
        students_dict.sort(key=lambda x: x['english'], reverse=asc_or_desc)
    elif mode == '2':
        students_dict.sort(key=lambda x: x['python'], reverse=asc_or_desc)
    elif mode == '3':
        students_dict.sort(key=lambda x: x['c'], reverse=asc_or_desc)
    elif mode == '0':
        students_dict.sort(key=lambda x: x['english']+x['python']+x['c'], reverse=asc_or_desc)
    else:
        print('Wrong input, please select from main menu')
        menu()
        return
    show_students(students_dict)

def count():
    if os.path.exists(file_name):
        with open(file_name, 'r') as st_txt:
            students = st_txt.readlines()
            if students:
                print('there are total %d students' % len(students))
            else:
                print('no students inserted')
    else:
        print('no students info file...')


def show():
    if os.path.exists(file_name):
        student_list = []
        with open(file_name, 'r') as st_txt:
            students = st_txt.readlines()
        [student_list.append(eval(st)) for st in students]
        show_students(student_list)
    else:
        print('there is no student info inserted')


def main():
    ctrl = True
    menu()
    while ctrl:
        option = input('please select:')
        option_str = re.sub("\D", "", option)
        if option_str in [str(x) for x in range(8)]:
            option_int = int(option_str)
            if option_int == 0:
                ctrl = False
            elif option_int == 1:
                insert()
            elif option_int == 2:
                search()
            elif option_int == 3:
                delete()
            elif option_int == 4:
                modify()
            elif option_int == 5:
                sort()
            elif option_int == 6:
                count()
            elif option_int == 7:
                show()
        else:
            print("invalid input")


if __name__ == '__main__':
    main()
