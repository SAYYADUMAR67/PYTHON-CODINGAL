student_id = {
    "id1": {"name": "sigma boy", "class": "7", "subject": "Computer Science"},
    "id2": {"name": "sigma girl", "class": "7", "subject": "Computer Science"},
    "id3": {"name": "gogogaga queen", "class": "7", "subject": "Computer Science"},
    "id4": {"name": "sigma boy", "class": "7", "subject": "Computer Science"},
    }

result = {}

seenkeys = []
for student_id,details in student_id.items():
    unique_key = details["name"],details["class"],details["subject"]
    if unique_key not in seenkeys:
        seenkeys.append(unique_key)
        result[student_id] = details

for u, v in result.items():
    print(u,":", v)
