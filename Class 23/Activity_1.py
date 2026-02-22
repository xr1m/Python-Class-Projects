# Get rid of the duplicates:

student_data_dict = {

"id": {"name": "Sara", "class": "VIII", "subject": "english, maths, science"},
"id2": {"name": "Surya", "class": "VIII", "subject": "english, maths, science"},
"id3": {"name": "Surya", "class": "VIII", "subject": "english, maths, science"},
"id4": {"name": "Mohit", "class": "VIII", "subject": "english, maths, science"},
}

empty_dict = {}

seen = set()

for student_id, details in student_data_dict.items():
    unique_key = (details["name"], details["class"], details["subject"])
    if unique_key not in seen:
        seen.add(unique_key)
        empty_dict[student_id] = details

for i, j in empty_dict.items():
    print(i, ":", j)