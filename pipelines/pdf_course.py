from reportlab.lib.pagesizes import A4
from reportlab.pdfgen import canvas
from datetime import date

def generate_course_pdf(course):
    filename = f"{course['title']}.pdf"
    c = canvas.Canvas(filename, pagesize=A4)

    c.setFont("Helvetica-Bold", 20)
    c.drawString(50, 800, course["title"])

    c.setFont("Helvetica", 12)
    y = 760
    for lesson in course["lessons"]:
        c.drawString(50, y, f"Lesson: {lesson}")
        y -= 20

    c.save()
    return filename
