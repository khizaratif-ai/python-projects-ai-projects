from reportlab.pdfgen import canvas
import os


folder = "generated_pdfs"


if not os.path.exists(folder):
    os.makedirs(folder)


def create_pdf(filename, title, content):

    path = folder + "/" + filename

    pdf = canvas.Canvas(path)

    pdf.setTitle(title)


    pdf.setFont(
        "Helvetica-Bold",
        20
    )

    pdf.drawString(
        80,
        750,
        title
    )


    pdf.setFont(
        "Helvetica",
        12
    )


    y = 700


    for line in content.split("\n"):

        pdf.drawString(
            80,
            y,
            line
        )

        y -= 25


    pdf.save()

    return path