#LIST OF STUDENT'S NAME
names=["ANKIT","UTKARSH","HIMANSHU","ADITYA"]
print("List of students:",names)

#LIST OF MARKS 
marks=[80,79,85,74]

print("Marks before updation:",marks)
rank_before=dict(zip(names,marks))
a=dict(sorted(rank_before.items(),reverse=True, key=lambda item:item[1]))
before_updates=list(a)

#PRINTING THE LIST OF STUDENTS IN DESCENDING ORDER OF MARKS BEFORE UPDATION
print("list of students in order of marks before updates:",a)


#LIST OF UPDATES IN MARKS
updates=[1,6,-2,14]
print("Updates:",updates)
updated_marks=[]
for i in range(0,len(marks)):
    updated_marks.append(marks[i]+updates[i])
print("updated marks are:",updated_marks)
rank_after=dict(zip(names,updated_marks))


x=dict(sorted(rank_after.items(),reverse=True, key=lambda item:item[1]))


updated_rank=list(x)

#PRINTING LIST OF STUDENTS IN DESCENDING ORDER OF MARKS AFTER UPDATION
print("list of sudents in order of marks after updates:",x)

# maximum marks of the student
max_marks2=max(rank_after,key=rank_after.get)

#Finding jump in rank of student with maximum marks
B=before_updates.index(max_marks2)
C=updated_rank.index(max_marks2)
print("Student with maximum marks:",max_marks2,",","JUMP:",B-C)