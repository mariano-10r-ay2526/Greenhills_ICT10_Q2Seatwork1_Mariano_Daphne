# Working with Python Lists
from pyscript import document

# Variables
country = ("Brunei", "Cambodia", "Indonesia", "Laos", "Myanmar", "Philippines", "Singapore", "Thailand", "Timor-Leste", "Vietnam")
nickname = ("")

# Function
def reveal_nickname(e):
    chosen_country = document.getElementById("country").value

    selected_nickname = nickname[int(chosen_country)]

    document.getElementById("result").innerText = selected_nickname