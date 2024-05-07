from card import Card
import random
import math
import matplotlib.pyplot as plt
import tkinter as tk
from matplotlib.backends.backend_tkagg import FigureCanvasTkAgg


# Press Shift+F10 to execute it or replace it with your code.
# Press Double Shift to search everywhere for classes, files, tool windows, actions, and settings.

#CONSTANTS
N = 10 # number of times to run draw simulation


def create_deck(*args):  # enter card type and then number of that card ex: copper,7,estate,3
    returndeck = []
    request = [*args]
    while len(request) > 1:
        for i in range(request.pop(1)):
            returndeck.append(request[0])
        request.pop(0)
    return returndeck

def run_simulation():
    sums = []
    average = 0
    N = int(entryN.get())
    #SIMULATE!
    for i in range(N):
        deck = create_deck(copper, int(entry3.get()), silver, int(entry4.get()), gold, int(entry5.get()), estate,
                           int(entry6.get()), laboratory, int(entry7.get()), village, int(entry8.get()), smithy,
                           int(entry9.get()))
        discard = []  # create discard pile
        hand = []
        random.shuffle(deck)
        actions = 1
        for i in range(5):
            hand.append(deck.pop(0))
        while actions > 0:
            if laboratory in hand:
                hand.remove(laboratory) #remove lab from hand
                if deck:
                    hand.append(deck.pop(0)) # pick a card
                if deck:
                    hand.append(deck.pop(0)) # pick another card

                discard.append(laboratory)
            if village in hand:
                hand.remove(village)  # remove lab from hand
                if(deck):
                    hand.append(deck.pop(0))  # pick a card
                actions += 1  # gain an action

                discard.append(village)

            if smithy in hand:
                hand.remove(smithy)  # remove lab from hand
                if deck:
                    hand.append(deck.pop(0))  # pick a card
                if deck:
                    hand.append(deck.pop(0))  # pick another card
                if deck:
                    hand.append(deck.pop(0))  # pick another card
                actions -= 1 # lose an action

                discard.append(smithy)

            no_actions = True
            for card in hand:
                if card.isAction:
                    no_actions = False




            if no_actions:
                break


        total = hand.count(copper) + hand.count(silver) * 2 + hand.count(gold) * 3
        sums.append(total)


    mean = sum(sums)/N

    #expected value
    label10 = tk.Label(root, text="Expected Value:")
    label10.grid(row=10, column=0, padx=10, pady=10)

    output10 = tk.Label(root, text=str(mean))
    output10.grid(row=10, column=1, padx=10, pady=10)

    #make graph
    num_0 = sums.count(0) / N
    num_1 = sums.count(1) / N
    num_2 = sums.count(2) / N
    num_3 = sums.count(3) / N
    num_4 = sums.count(4) / N
    num_5 = sums.count(5) / N
    num_6 = sums.count(6) / N
    num_7 = sums.count(7) / N
    num_8 = sums.count(8) / N
    num_9 = sums.count(9) / N
    num_10 = sums.count(10) / N

    print("Simulated with N = " + str(N) + ":")
    print("Percent of hands with 2 coppers:" + str(num_2))
    print("Percent of hands with 3 coppers:" + str(num_3))
    print("Percent of hands with 4 coppers:" + str(num_4))
    print("Percent of hands with 5 coppers:" + str(num_5))
    print(num_2 + num_3 + num_4 + num_5)

    # make graph
    names = ["0","1","2", "3", "4", "5","6","7","8","9","10"]
    values_simulation = [num_0,num_1,num_2, num_3, num_4,num_5,num_6,num_7,num_8,num_9,num_10]

    # Create the bar graph
    fig, ax = plt.subplots()

    # Plot a bar chart
    ax.grid(axis='y')
    ax.bar(names, values_simulation)

    title = "Simulated Probabilities for drawing x # of Coppers"
    ax.set_title(title)

    # Display the graph
    ax.set_xlabel('# of Coppers drawn')
    ax.set_ylabel("Frequency (%)")


    # Create a canvas to embed Matplotlib figure in Tkinter window
    canvas = FigureCanvasTkAgg(fig, master=root)
    canvas.draw()

    # Add the canvas to the Tkinter window using .grid()
    canvas.get_tk_widget().grid(row=0, column=2)












# Press the green button in the gutter to run the script.
if __name__ == '__main1__':
    #create card types

    # money
    copper = Card("copper",1, 0, 0, 0, False)  # name, coin, actions, draws, vpoints, isAction):
    silver = Card("silver",2, 0, 0, 0, False)
    gold = Card("gold",3, 0, 0, 0, False)

    # VPs
    estate = Card("estate",0, 0, 0, 1, False)

    # Action Cards
    laboratory = Card("laboratory",0, 1, 2, 0, True)
    village = Card("village",0, 2, 1, 0, True)
    smithy = Card("smithy",0, 0, 3, 0, True)

    # CREATE DATA ENTRY WINDOW
    # Create the main window
    root = tk.Tk()
    root.title("Dominion Simulation:")

    # Create a labels
    label1 = tk.Label(root, text="Enter # of Each Type of Card in Deck:")
    label1.grid(row=0, column=0, padx=10, pady=10)

    label2 = tk.Label(root, text="Quantity:")
    label2.grid(row=0, column=1, padx=10, pady=10)

    label3 = tk.Label(root, text="Copper:")
    label3.grid(row=1, column=0, padx=10, pady=10)

    entry3 = tk.Entry(root)
    entry3.insert(0,"7")
    entry3.grid(row=1,column=1,padx=10,pady=10)

    label4 = tk.Label(root, text="Silver:")
    label4.grid(row=2, column=0, padx=10, pady=10)

    entry4 = tk.Entry(root)
    entry4.insert(0, "0")
    entry4.grid(row=2, column=1, padx=10, pady=10)

    label5 = tk.Label(root, text="Gold:")
    label5.grid(row=3, column=0, padx=10, pady=10)

    entry5 = tk.Entry(root)
    entry5.insert(0, "0")
    entry5.grid(row=3, column=1, padx=10, pady=10)

    label6 = tk.Label(root, text="Estate:")
    label6.grid(row=4, column=0, padx=10, pady=10)

    entry6 = tk.Entry(root)
    entry6.insert(0, "0")
    entry6.grid(row=4, column=1, padx=10, pady=10)

    label7 = tk.Label(root, text="Laboratory:")
    label7.grid(row=5, column=0, padx=10, pady=10)

    entry7 = tk.Entry(root)
    entry7.insert(0, "3")
    entry7.grid(row=5, column=1, padx=10, pady=10)

    label8 = tk.Label(root, text="Village:")
    label8.grid(row=6, column=0, padx=10, pady=10)

    entry8 = tk.Entry(root)
    entry8.insert(0, "0")
    entry8.grid(row=6, column=1, padx=10, pady=10)

    label9 = tk.Label(root, text="Smithy:")
    label9.grid(row=7, column=0, padx=10, pady=10)

    entry9 = tk.Entry(root)
    entry9.insert(0, "0")
    entry9.grid(row=7, column=1, padx=10, pady=10)

    labelN = tk.Label(root, text="Number of Trials:")
    labelN.grid(row=8, column=0, padx=10, pady=10)

    entryN = tk.Entry(root)
    entryN.insert(0, "10")
    entryN.grid(row=8, column=1, padx=10, pady=10)

    # Create a button to submit the input
    submit_button = tk.Button(root, text="Run", command=run_simulation)
    submit_button.grid(row=9, column=1, padx=10, pady=10)

    # Run the Tkinter event loop
    root.mainloop()