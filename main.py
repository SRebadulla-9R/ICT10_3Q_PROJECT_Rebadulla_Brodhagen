from pyscript import document

# --- 1. NAVIGATION (Switching between sections) ---
def show_signup(event):
    clear_all_sections()
    document.querySelector("#section-signup").classList.add("active")

def show_checker(event):
    clear_all_sections()
    document.querySelector("#section-checker").classList.add("active")

def show_players(event):
    clear_all_sections()
    document.querySelector("#section-players").classList.add("active")
    display_player_loop() # Runs the loop automatically when section opens

def clear_all_sections():
    for section in document.querySelectorAll(".page-section"):
        section.classList.remove("active")

# --- 2. SIGN UP LOGIC (Skills Test) ---
def run_signup(event):
    username = document.querySelector("#user").value
    if username:
        document.querySelector("#signup-out").innerText = "Account created. You may now log in using your credentials."
    else:
        document.querySelector("#signup-out").innerText = "Please enter a username."

# --- 3. TEAM CHECKER LOGIC (Seatwork 2) ---
def run_checker(event):
    is_reg = document.querySelector("#reg-yes").checked
    is_med = document.querySelector("#med-yes").checked
    section = document.querySelector("#sect_name").value
    output = document.querySelector("#checker-out")
    
    # Section-to-team mapping with emojis
    teams = {
        "Ruby": ("Blue Bears", "🐻"),
        "Sapphire": ("Red Bulldogs", "🐶"),
        "Emerald": ("Yellow Tigers", "🐯"),
        "Topaz": ("Green Hornets", "🐝")
    }
    
    # Color mapping for each team
    colors = {
        "Blue Bears": "#3498db",
        "Red Bulldogs": "#e74c3c",
        "Yellow Tigers": "#f39c12",
        "Green Hornets": "#27ae60"
    }
    
    if is_reg and is_med and section in teams:
        team_name, emoji = teams[section]
        team_color = colors.get(team_name, "#000")
        output.innerHTML = f"Congratulations! You are part of the <span style='color:{team_color};'>{team_name} {emoji}</span>"
    else:
        output.innerText = "Error: Ensure registration and medical clearance are checked."

# --- 4. PLAYER LIST LOGIC (Requirement #4 - Loops) ---
def display_player_loop():
    # Names of classmates for the Intramurals
    players = [
        "Escudero", "Estrada", "Tolentino", "Pimentel", "Binay",
        "Cayetano", "Dela Rosa", "Ejercito", "Gatchalian", "Go",
        "Hontiveros", "Lapid", "Legarda", "Marcos", "Padilla"
    ]
    
    list_container = document.querySelector("#player-list")
    list_container.innerHTML = "" # Clear previous list
    
    # REQUIREMENT #4: Displaying names using a Python Loop
    for i, name in enumerate(players, 1):
        li_item = document.createElement("li")
        li_item.innerText = f"{i}) {name}"

        list_container.appendChild(li_item)
