import customtkinter as ctk
import news
import email_sender


def start():


    window = ctk.CTk()

    window.title("Email News App")

    window.geometry(
        "600x600"
    )


    topic = ctk.CTkEntry(
        window,
        placeholder_text="Enter news topic"
    )

    topic.pack(
        pady=20
    )


    email = ctk.CTkEntry(
        window,
        placeholder_text="Receiver email"
    )

    email.pack(
        pady=20
    )


    news_box = ctk.CTkTextbox(
        window,
        width=500,
        height=250
    )

    news_box.pack(
        pady=20
    )


    def get_news_button():

        articles = news.get_news(
            topic.get()
        )


        news_box.delete(
            "1.0",
            "end"
        )


        news_box.insert(
            "end",
            articles
        )



    def send_button():


        message = news_box.get(
            "1.0",
            "end"
        )


        email_sender.send_email(
            email.get(),
            message
        )



    ctk.CTkButton(
        window,
        text="Get News",
        command=get_news_button
    ).pack(pady=10)



    ctk.CTkButton(
        window,
        text="Send Email",
        command=send_button
    ).pack(pady=10)



    window.mainloop()