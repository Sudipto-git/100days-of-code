
a = [ """       ___________
                 \         /
                  )_______( 
                  |"""""""|_.-._,.---------.,_.-._
                  |       | | |               | | ''-.
                  |       |_| |_             _| |_..-'
                  |_______| '-' `'---------'` '-'
                  )"""""""(
                 /_________\
                 `'-------'`
                .-------------.
               /_______________\
                          
    """]

print(a[0])

def find_highest_bidder(bidding_dictionary):
    highest_bid = 0
    winner  = ""
    
    # max(bidding_dictionary)
    for bidder in bidding_dictionary: # bidder is the key
        bid_amount = bidding_dictionary[bidder] # bidder is the key and bidding_dictionary[bidder] is the value
        if bid_amount > highest_bid:
            highest_bid = bid_amount
            winner = bidder
            
    
    print(f"The winner is {winner} with a bid of ${highest_bid}")


bids = {} #empthy dictionary to save the bids
continue_bidding = True

while continue_bidding :
    name = input("Enter your name: ")
    price = int(input("Enter your bid :$ "))
    bids[name] = price # add the name and price to the dictionary
    should_continue = input("Are there any other bidders? Type 'yes' or 'no':\n ").lower()
    
    if should_continue == "no":
        continue_bidding = False
        find_highest_bidder(bids) # call the function to find the highest bidder
        
    elif should_continue == "yes":
        continue_bidding = True


        
    
