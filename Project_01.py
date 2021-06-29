import csv
def write_into_csv(info_list):
    with open('student_info.csv','a',newline='') as csv_file:
        writer = csv.writer(csv_file)
        if csv_file.tell()==0:
            writer.writerow(['Name','Age','Email_ID','Contact_Number'])
        writer.writerow(info_list)
if __name__ == '__main__':
    condition =True
    student_num = 1
    while(condition):
        student_info = input('Enter information for the student #{} in th following format\n(Name Age Email_ID Contact_Number) :'.format(student_num))
        student_info_list = student_info.split(' ')
        print('\nThe entered information is :\nName: {}\nAge: {}\nEmail_ID: {}\nContact_Number: {}'.format(student_info_list[0],student_info_list[1],student_info_list[2],student_info_list[3]))
        confirmation = input('Is the entered information correct? (yes/no): ')
        if confirmation == 'yes':
            write_into_csv(student_info_list)
            condition_check = input('Enter (yes/no) whether you want to enter information for another student: ')
            if condition_check == 'yes':
                condition = True
                student_num += 1
            elif condition_check == 'no':
                condition = False
        else:
            print('\nPlease re-enter the values!')
