#!/usr/bin/env python
# coding: utf-8

# In[8]:


#TASK 3 STUDENT MARKS PROCESSOR
#importing numpy library
import numpy as np
#defing the weightage of exam maek and course work 
EXAM_WEIGHT=0.60
COURSEWORK_WEIGHT=0.40
#defining input( with details) and output file ( for reesults)
INPUT_FILENAME='input_marks.txt' 
OUTPUT_FILENAME='result_report.txt'
#a function is defined to give grade based on overall marrk
def get_grade(overall_mark):
    if overall_mark>=80:
        return 'A'
    elif overall_mark>=70:
        return 'B'
    elif overall_mark>=60:
        return 'C'
    elif overall_mark>=50:
        return 'D'
    else:
        return 'F'
#a function to for statistics for count and total
def display_statistics(counts, total):
    print("\nGRADE STATISTICS")
    #hgiving header with proper allignment
    print(f"{'Grade':<8}{'Count':<8}{'Percentage':<10}")
    # Definig display order 
    grade_order = ['A', 'B', 'C', 'D', 'F']
    #grade inside the loop
    for grade in grade_order:
        count=counts.get(grade, 0)
        percentage=(count / total) * 100 if total > 0 else 0
        print(f"{grade:<8}{count:<8}{percentage:<10.2f}%")
def process_marks():
    #reading the data from the file and inializing in the list
    raw_data_list=[]
    # empty Dictionary to store Grade Statistics 
    grade_counts={} 
    try:
        #open the file in read mode
        with open(INPUT_FILENAME, 'r') as f:
            #loops through each line in the file
            for line in f:
                #removing extra space and splitting by comma
                parts=line.strip().split(',')
                #only three variable in a line
                if len(parts)==3:
                    # Appending data as RegNo, Exam, Coursework with datatype
                    raw_data_list.append([parts[0], int(parts[1]), int(parts[2])])
    except FileNotFoundError:
        # if file not found
        print(f"Error: Input file '{INPUT_FILENAME}' not found. Please create it and try again.")
        return
    # if file is empty
    if not raw_data_list:
        print("Error: Input file is empty or data could not be read.")
        return

    #defining the coulmn and data type for the numpy array
    dtype=[
        ('RegNo', str),      
        ('Exam', int),        
        ('Coursework', int),  
        ('Overall', float),     
        ('Grade', 'U2')        
    ]
    #initializing the NumPy array with the defined structure and size
    student_array=np.zeros(len(raw_data_list), dtype=dtype)
    # Filling the numpy array
    for i, (regno, exam, cw) in enumerate(raw_data_list):
        #overall mark
        overall=(exam * EXAM_WEIGHT) + (cw * COURSEWORK_WEIGHT)
        #Assigning the grade
        grade=get_grade(overall)
        #grade statistics counting
        grade_counts[grade]=grade_counts.get(grade, 0) + 1
        #all results into the NumPy array row
        student_array[i]=(regno, exam, cw, overall, grade)

    #Sorting students by overall marks 
    sorted_indices=np.argsort(student_array['Overall'])[::-1]
    sorted_array=student_array[sorted_indices]
    #Writing results in output file
    with open(OUTPUT_FILENAME, 'w') as f:
        header=f"{'Rank':<5}{'Reg No':<10}{'Exam (60%)':<12}{'CW (40%)':<12}{'Overall Mark':<15}{'Grade':<5}\n"
        f.write("-" * len(header) + "\n")
        f.write(header)
        f.write("-" * len(header) + "\n")
        #looping through rank
        for rank, student in enumerate(sorted_array, 1):
            f.write(f"{rank:<5}{student['RegNo']:<10}{student['Exam']:<12}{student['Coursework']:<12}{student['Overall']:<15.2f}{student['Grade']:<5}\n")
        
        f.write("-" * len(header) + "\n")
        print(f"\nResults written to '{OUTPUT_FILENAME}'")
    # displaying statistics
    display_statistics(grade_counts, len(raw_data_list))

if __name__=="__main__":
    process_marks()
    


# In[ ]:




