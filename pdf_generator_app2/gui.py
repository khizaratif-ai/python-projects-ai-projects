import customtkinter as ctk
import pdf_functions


ctk.set_appearance_mode("dark")
ctk.set_default_color_theme("blue")



def start():


    window = ctk.CTk()

    window.title("PDF Generator App")

    window.geometry("650x600")



    title = ctk.CTkLabel(
        window,
        text="PDF Generator App",
        font=("Arial", 32)
    )

    title.pack(
        pady=30
    )



    def clear():

        for widget in window.winfo_children():

            widget.destroy()



    def resume_page():

        clear()


        ctk.CTkLabel(
            window,
            text="Resume Generator",
            font=("Arial",25)
        ).pack(pady=20)



        name = ctk.CTkEntry(
            window,
            placeholder_text="Name"
        )

        name.pack(pady=10)



        skills = ctk.CTkEntry(
            window,
            placeholder_text="Skills"
        )

        skills.pack(pady=10)



        education = ctk.CTkEntry(
            window,
            placeholder_text="Education"
        )

        education.pack(pady=10)



        def generate():

            content = f"""
Name:
{name.get()}

Skills:
{skills.get()}

Education:
{education.get()}
"""


            pdf_functions.create_pdf(
                "resume.pdf",
                "Resume",
                content
            )

            success_label.configure(
                text="Resume Created!"
            )



        ctk.CTkButton(
            window,
            text="Generate Resume",
            command=generate
        ).pack(pady=20)


        success_label = ctk.CTkLabel(
            window,
            text=""
        )

        success_label.pack()



        back_button()



    def invoice_page():

        clear()


        ctk.CTkLabel(
            window,
            text="Invoice Generator",
            font=("Arial",25)
        ).pack(pady=20)



        customer = ctk.CTkEntry(
            window,
            placeholder_text="Customer Name"
        )

        customer.pack(pady=10)



        item = ctk.CTkEntry(
            window,
            placeholder_text="Item"
        )

        item.pack(pady=10)



        price = ctk.CTkEntry(
            window,
            placeholder_text="Price"
        )

        price.pack(pady=10)



        def generate():

            content=f"""
Customer:
{customer.get()}

Item:
{item.get()}

Price:
{price.get()}
"""


            pdf_functions.create_pdf(
                "invoice.pdf",
                "Invoice",
                content
            )

            message.configure(
                text="Invoice Created!"
            )



        ctk.CTkButton(
            window,
            text="Generate Invoice",
            command=generate
        ).pack(pady=20)


        message=ctk.CTkLabel(
            window,
            text=""
        )

        message.pack()


        back_button()



    def report_page():

        clear()


        ctk.CTkLabel(
            window,
            text="Report Generator",
            font=("Arial",25)
        ).pack(pady=20)


        heading = ctk.CTkEntry(
            window,
            placeholder_text="Report Title"
        )

        heading.pack(pady=10)



        body = ctk.CTkTextbox(
            window,
            width=400,
            height=200
        )

        body.pack(pady=10)



        def generate():

            content = body.get(
                "1.0",
                "end"
            )


            pdf_functions.create_pdf(
                "report.pdf",
                heading.get(),
                content
            )


            message.configure(
                text="Report Created!"
            )



        ctk.CTkButton(
            window,
            text="Generate Report",
            command=generate
        ).pack(pady=20)



        message = ctk.CTkLabel(
            window,
            text=""
        )

        message.pack()


        back_button()



    def certificate_page():

        clear()


        ctk.CTkLabel(
            window,
            text="Certificate Generator",
            font=("Arial",25)
        ).pack(pady=20)


        name = ctk.CTkEntry(
            window,
            placeholder_text="Student Name"
        )

        name.pack(pady=10)



        achievement = ctk.CTkEntry(
            window,
            placeholder_text="Achievement"
        )

        achievement.pack(pady=10)



        def generate():

            content=f"""
This certificate is awarded to

{name.get()}

For:

{achievement.get()}
"""


            pdf_functions.create_pdf(
                "certificate.pdf",
                "Certificate",
                content
            )


            message.configure(
                text="Certificate Created!"
            )


        ctk.CTkButton(
            window,
            text="Generate Certificate",
            command=generate
        ).pack(pady=20)



        message=ctk.CTkLabel(
            window,
            text=""
        )

        message.pack()


        back_button()



    def back_button():

        ctk.CTkButton(
            window,
            text="Back",
            command=home
        ).pack(
            pady=20
        )



    def home():

        clear()

        title = ctk.CTkLabel(
            window,
            text="PDF Generator App",
            font=("Arial",32)
        )

        title.pack(pady=30)


        ctk.CTkButton(
            window,
            text="Resume Generator",
            command=resume_page
        ).pack(pady=10)


        ctk.CTkButton(
            window,
            text="Invoice Generator",
            command=invoice_page
        ).pack(pady=10)


        ctk.CTkButton(
            window,
            text="Report Generator",
            command=report_page
        ).pack(pady=10)


        ctk.CTkButton(
            window,
            text="Certificate Generator",
            command=certificate_page
        ).pack(pady=10)



    home()

    window.mainloop()