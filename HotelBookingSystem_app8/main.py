import customtkinter as ctk
from tkinter import messagebox
import pandas as pd
from main2 import Hotel


# ---------------- SETTINGS ----------------

ctk.set_appearance_mode("dark")
ctk.set_default_color_theme("blue")


HOTELS_FILE = "hotels.csv"
BOOKINGS_FILE = "bookings.csv"


selected_hotel = None


# ---------------- DATA FUNCTIONS ----------------


def load_hotels():
    return pd.read_csv(
        HOTELS_FILE,
        dtype={"id": str}
    )


def load_bookings():

    try:
        return pd.read_csv(BOOKINGS_FILE)

    except FileNotFoundError:

        df = pd.DataFrame(
            columns=[
                "customer",
                "email",
                "hotel_id",
                "check_in",
                "check_out"
            ]
        )

        df.to_csv(
            BOOKINGS_FILE,
            index=False
        )

        return df



# ---------------- WINDOW ----------------


app = ctk.CTk()

app.title(
    "Hotel Booking System"
)

app.geometry(
    "900x650"
)



def clear():

    for widget in app.winfo_children():
        widget.destroy()



# ---------------- HOME PAGE ----------------


def home_page():

    clear()


    title = ctk.CTkLabel(
        app,
        text="🏨 HOTEL BOOKING SYSTEM",
        font=("Arial",32,"bold")
    )

    title.pack(
        pady=60
    )


    ctk.CTkButton(
        app,
        text="🏨 ROOM CHECK IN",
        width=300,
        height=60,
        font=("Arial",20),
        command=check_in_page
    ).pack(
        pady=20
    )


    ctk.CTkButton(
        app,
        text="🔑 ROOM CHECK OUT",
        width=300,
        height=60,
        font=("Arial",20),
        command=check_out_page
    ).pack(
        pady=20
    )



# ---------------- CHECK IN ----------------


def check_in_page():

    clear()


    title = ctk.CTkLabel(
        app,
        text="Available Hotels",
        font=("Arial",30,"bold")
    )

    title.pack(
        pady=20
    )


    hotels = load_hotels()


    available = hotels[
        hotels["available"] == "yes"
    ]


    if len(available) == 0:

        messagebox.showinfo(
            "No Rooms",
            "Sorry, we can't help you find a room right now."
        )

        home_page()

        return



    frame = ctk.CTkScrollableFrame(
        app,
        width=700,
        height=450
    )

    frame.pack()



    for _,hotel in available.iterrows():


        card = ctk.CTkFrame(
            frame
        )

        card.pack(
            pady=15,
            padx=20,
            fill="x"
        )


        ctk.CTkLabel(
            card,
            text=f"🏨 {hotel['name']}",
            font=("Arial",22,"bold")
        ).pack()


        ctk.CTkLabel(
            card,
            text=
            f"""
City: {hotel['city']}
Capacity: {hotel['capacity']} people
Status: Available
"""
        ).pack()



        ctk.CTkButton(
            card,
            text="Book This Room",
            command=lambda h=hotel: booking_page(h)
        ).pack(
            pady=10
        )



    ctk.CTkButton(
        app,
        text="Back",
        command=home_page
    ).pack(
        pady=10
    )





# ---------------- BOOKING PAGE ----------------


def booking_page(hotel):

    clear()


    title = ctk.CTkLabel(
        app,
        text=f"Booking {hotel['name']}",
        font=("Arial",28,"bold")
    )

    title.pack(
        pady=20
    )



    box = ctk.CTkFrame(app)

    box.pack(
        pady=10
    )


    entries={}



    fields=[
        "Name",
        "Email",
        "Check In Date",
        "Check Out Date"
    ]



    for field in fields:

        ctk.CTkLabel(
            box,
            text=field
        ).pack()


        entry=ctk.CTkEntry(
            box,
            width=350
        )

        entry.pack(
            pady=5
        )


        entries[field]=entry




    def confirm():


        name=entries["Name"].get()
        email=entries["Email"].get()
        checkin=entries["Check In Date"].get()
        checkout=entries["Check Out Date"].get()



        if name=="" or email=="":

            messagebox.showerror(
                "Error",
                "Please enter your details"
            )

            return



        # Update hotel availability

        h=Hotel(
            str(hotel["id"])
        )

        h.book()



        bookings=load_bookings()


        new_booking=pd.DataFrame(
            [{
                "customer":name,
                "email":email,
                "hotel_id":hotel["id"],
                "check_in":checkin,
                "check_out":checkout
            }]
        )


        bookings=pd.concat(
            [
                bookings,
                new_booking
            ],
            ignore_index=True
        )


        bookings.to_csv(
            BOOKINGS_FILE,
            index=False
        )



        messagebox.showinfo(
            "Success",
            "Room booked successfully!"
        )


        home_page()



    ctk.CTkButton(
        app,
        text="CONFIRM BOOKING",
        width=350,
        command=confirm
    ).pack(
        pady=20
    )


    ctk.CTkButton(
        app,
        text="Back",
        command=check_in_page
    ).pack()






# ---------------- CHECK OUT ----------------


def check_out_page():

    clear()


    title=ctk.CTkLabel(
        app,
        text="Checkout Room",
        font=("Arial",30,"bold")
    )

    title.pack(
        pady=20
    )



    hotels=load_hotels()


    booked=hotels[
        hotels["available"]=="no"
    ]



    if len(booked)==0:

        messagebox.showinfo(
            "No Bookings",
            "There are no rooms to checkout."
        )

        home_page()

        return



    selected={}



    for _,hotel in booked.iterrows():

        btn=ctk.CTkButton(
            app,
            text=
            f"{hotel['name']} - {hotel['city']}",
            width=400,
            command=lambda h=hotel: checkout(h)
        )

        btn.pack(
            pady=10
        )



    ctk.CTkButton(
        app,
        text="Back",
        command=home_page
    ).pack(
        pady=20
    )





def checkout(hotel):


    df=load_hotels()


    df.loc[
        df["id"]==str(hotel["id"]),
        "available"
    ]="yes"


    df.to_csv(
        HOTELS_FILE,
        index=False
    )



    messagebox.showinfo(
        "Checkout Complete",
        f"{hotel['name']} is now available again."
    )


    home_page()





# ---------------- START ----------------


home_page()

app.mainloop()