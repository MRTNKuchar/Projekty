import random
import time
import tkinter as tk

def spin_reels():
    symbols = ["🍒", "🍋", "🍊", "🍉", "⭐", "🔔", "7", "🎁"]  # Přidán bonusový symbol 🎁
    weights = [0.25, 0.2, 0.15, 0.15, 0.1, 0.08, 0.05, 0.02]  # Úprava pravděpodobností podle online automatů
    return random.choices(symbols, weights=weights, k=3)

def check_win(reels):
    return reels[0] == reels[1] == reels[2]

def check_bonus(reels):
    return reels.count("🎁") >= 2  # Bonus při dvou nebo více symbolech 🎁

def animate_reels(reel_labels):
    symbols = ["🍒", "🍋", "🍊", "🍉", "⭐", "🔔", "7", "🎁"]
    for _ in range(10):  # Počet iterací animace
        for label in reel_labels:
            label.config(text=random.choice(symbols))
        root.update()
        time.sleep(0.1)

def play():
    global balance, bet, free_spins
    
    if free_spins > 0:
        free_spins -= 1
    else:
        if balance < bet:
            result_label.config(text="Nemáte dostatek peněz na další otočení.")
            return
        balance -= bet
    
    balance_label.config(text=f"Zůstatek: {balance} Kč")
    result_label.config(text="Točíme válce...")
    root.update()
    
    animate_reels(reel_labels)
    
    reels = spin_reels()
    for i in range(3):
        reel_labels[i].config(text=reels[i], font=("Arial", 48))  # Zvýšení velikosti ikon
    
    if check_win(reels):
        win_amount = bet * random.choice([5, 10, 20])  # Náhodný multiplikátor pro realističtější výhry
        balance += win_amount
        result_label.config(text=f"Gratulujeme! Vyhráli jste {win_amount} Kč!")
    elif check_bonus(reels):
        free_spins += 10
        result_label.config(text="BONUS! Získali jste 10 otočení zdarma!")
    else:
        result_label.config(text="Bohužel, žádná výhra.")
    
    balance_label.config(text=f"Zůstatek: {balance} Kč")
    free_spins_label.config(text=f"Otočení zdarma: {free_spins}")

def change_bet(amount):
    global bet
    bet = amount
    bet_label.config(text=f"Sázka: {bet} Kč")

def start_game():
    global balance, bet, free_spins, root, result_label, balance_label, bet_label, free_spins_label, reel_labels
    balance = 100
    bet = 10
    free_spins = 0
    
    root = tk.Tk()
    root.title("Slotový Automat")
    
    balance_label = tk.Label(root, text=f"Zůstatek: {balance} Kč", font=("Arial", 14))
    balance_label.pack()
    
    bet_label = tk.Label(root, text=f"Sázka: {bet} Kč", font=("Arial", 14))
    bet_label.pack()
    
    free_spins_label = tk.Label(root, text=f"Otočení zdarma: {free_spins}", font=("Arial", 14))
    free_spins_label.pack()
    
    reel_frame = tk.Frame(root)
    reel_frame.pack()
    reel_labels = [tk.Label(reel_frame, text="❓", font=("Arial", 48)) for _ in range(3)]  # Zvýšení velikosti ikon
    for label in reel_labels:
        label.pack(side=tk.LEFT, padx=10)
    
    result_label = tk.Label(root, text="", font=("Arial", 14))
    result_label.pack()
    
    spin_button = tk.Button(root, text="Točit!", font=("Arial", 14), command=play)
    spin_button.pack()
    
    bet_buttons_frame = tk.Frame(root)
    bet_buttons_frame.pack()
    
    tk.Button(bet_buttons_frame, text="Sázka 10 Kč", command=lambda: change_bet(10)).pack(side=tk.LEFT)
    tk.Button(bet_buttons_frame, text="Sázka 20 Kč", command=lambda: change_bet(20)).pack(side=tk.LEFT)
    tk.Button(bet_buttons_frame, text="Sázka 50 Kč", command=lambda: change_bet(50)).pack(side=tk.LEFT)
    
    root.mainloop()

if __name__ == "__main__":
    start_game()
