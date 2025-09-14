sandwich_orders = ["Tuna sandwich", "Pastrami sandwich", "Avocado sandwich", "Pastrami sandwich", "Egg sandwich", "Chicken sandwich", "Pastrami sandwich"]
finished_sandwichs = []

while "Pastrami sandwich" in sandwich_orders:
    sandwich_orders.remove("Pastrami sandwich")

while sandwich_orders:
    print(f"{sandwich_orders[0]} finished")
    finished_sandwichs.append(sandwich_orders.pop(0))
    
