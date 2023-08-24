data = { 
    "students": [ 
        { 
            "name": "Mukhamedzhan",  
            "age": 19, 
            "avg": 85 
        }, 
        { 
            "name": "Dias",  
            "age": 20, 
            "avg": 95 
        }, 
        { 
            "name": "Senimzhan",  
            "age": 18, 
            "avg": 90 
        }, 
    ] 
} 
 
print(data) 
print(type(data)) 
 
list_of_students = data.get("students") 
#print(list_of_students) 
 
for student in list_of_students: 
    print(student["name"]) 
 
summ = 0 
count_of_students = len(data["students"]) 
for student in list_of_students: 
    summ += student["avg"] 
 
print(summ / count_of_students) 
 
data.clear() 
print(data)