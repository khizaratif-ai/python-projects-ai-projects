import customtkinter as ctk
import weather


def start():

    ctk.set_appearance_mode("dark")
    ctk.set_default_color_theme("blue")


    window = ctk.CTk()

    window.title("Weather App")

    window.geometry("500x600")


    title = ctk.CTkLabel(
        window,
        text="Weather App",
        font=("Arial", 32)
    )

    title.pack(pady=30)


    city_entry = ctk.CTkEntry(
        window,
        placeholder_text="Enter city name",
        width=300
    )

    city_entry.pack(pady=15)


    result_label = ctk.CTkLabel(
        window,
        text="",
        font=("Arial", 18)
    )

    result_label.pack(
        pady=40
    )


    def search_weather():

        city = city_entry.get()


        data = weather.get_weather(city)


        if data:


            result = f"""
{data['city']}, {data['country']}


Condition:
{data['condition']}


Temperature:
{data['temperature']} °C


Humidity:
{data['humidity']}%


Wind:
{data['wind']} km/h
"""


        else:

            result = "City not found"


        result_label.configure(
            text=result
        )



    button = ctk.CTkButton(
        window,
        text="Get Weather",
        command=search_weather
    )

    button.pack(
        pady=20
    )


    window.mainloop()