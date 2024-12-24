
import csv
import os

def read_csv(fname):
    try:
        with open(fname, 'r', newline="") as file:
            reader = csv.reader(file)
            rows = list(reader)
            #check if rows empty
            if not rows:
                return None
            #extract data
            students = []
            for row in rows:
                name = row[0]
                section = row[1]
                scores = list(map(float, row[2:]))
                average = round(sum(scores) / len(scores), 3)

                student_data = {
                    'name' : name,
                    'section' : section,
                    'scores' : scores,
                    'average' : average
                }
                students.append(student_data)
            return students
    except FileNotFoundError:
        print(f'Error occurred when opening {fname} to read')
        return None
    except Exception:
        print(f'Error occurred when opening {fname} to read')
        return None

def write_csv(fname,student_data):
    try:
        with open(fname, 'w') as file:
            for student in student_data:
                name = student['name']
                section = student['section']
                scores = ','.join(map(str,student['scores']))
                result = f"{name},{section},{scores}\n"
                file.write(result)
    except FileNotFoundError:
        print(f'Error occurred when opening {fname} to write')
        return None
    except IsADirectoryError:
        print(f'Error occurred when opening {fname} to write')
        return None

def filter_section(student_data, section_name):
    student_in_section = [student for student in student_data if student['section'] == section_name]
    return student_in_section # returns a list of dictionaries ---> each dictionary corresponds to a single student and their corresponding data

def filter_average(student_data, min_inc, max_inc):
    student_within_filter = [student for student in student_data if min_inc <= student["average"] < max_inc]
    return student_within_filter

def split_section(fname):
    try:
    #in progress, make sure to not assume that you know the names of the sections that youre gonna filter by
        section_set = set() 
        student_data = read_csv(fname)

        if student_data == None:
            return None

        [section_set.add(line['section']) for line in student_data] #adds individual sections name to section_set
        # --> filter by section and then write student data into corresponding file
        for section in section_set:
            students = filter_section(student_data, section) # returns a list of dictionaries that contain student data relavant to that section
            base_name, _ = os.path.splitext(fname)
            file_name = f'{base_name}_section_{section}.csv' 
            write_csv(file_name,students)
    except Exception:
        print(f'Error occurred when opening {fname} to write')
        return 

def get_stats(nums : list) -> tuple:
    mean = sum(nums) / len(nums)
    minimum = min(nums)
    maximum = max(nums)
    ranges = max(nums) - min(nums)
    std_dev = (sum([(n - mean)**2 for n in nums]) / len(nums)) ** (1/2)
    return mean,minimum,maximum,ranges,std_dev

def tuple_to_stats_dict(tp):
    stats = {
        'mean' : tp[0],
        'min' : tp[1],
        'max' : tp[2],
        'range' : tp[3],
        'std_dev' : tp[4]
    }
    return stats

def get_assignment_stats(student_data):
    return_list = []

    #returns statistics for the average field of all students
    nums = [student['average'] for student in student_data]
    return_list.append(tuple_to_stats_dict(get_stats(nums)))

    #loops and returns all statistics for each assignmet
    number_of_task = len(student_data[0]['scores'])
    for assigment_num in range(number_of_task):
        assigment_scores = [student['scores'][assigment_num] for student in student_data]
        return_list.append(tuple_to_stats_dict(get_stats(assigment_scores)))

    return return_list

    #returns a new list of dictionaries
   

#testing methods    
data = read_csv("./project_5/students.csv")
write_csv('output.csv' , data)
print(filter_section(data, "A"))
print(filter_average(data,80,85))
split_section("./project_5/students.csv")
get_assignment_stats(data)
print(get_assignment_stats(data))

