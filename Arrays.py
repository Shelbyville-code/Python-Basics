courses=["Fullstack","Data Science","Cybersecurity"]
print(courses)

#Accessing an element
print(courses[2])

print()

#Looping through an array
for course in courses:
    print(course)

#Adding a new element
courses.append("UI/UX")
print(courses)

#Removing an element
courses.remove("Data Science")
print(courses)