def generate_certificate(student, course):
    cert_id = f"CERT-{student['id']}-{course['id']}"

    return {
        "certificate_id": cert_id,
        "student": student["name"],
        "course": course["title"],
        "date": str(date.today())
    }
