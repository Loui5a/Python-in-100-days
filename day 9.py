# silent auction. You enter all the bids you want and the highest bidder is printed to console
from replit import clear
#HINT: You can call clear() to clear the output in the console.
from art import logo
print(logo)
print("Welcome to the secret auction program.");
choice = "yes"
bids = {};
while(True):
    choice = input("Are there any other bidders? Type 'yes' or 'no'.\n")
    if(choice.lower() == "no"):
        break;

    clear()
    name = input("Please enter your name. \n")
    bid = int(input("Please enter your bid. \n"))
    bids[name] = bid



higestbid = 0;
highestbidder = "";
for item in bids:
    if(bids[item] > higestbid):
        higestbid = bids[item];
        highestbidder = item;

print(f"{highestbidder} has the highest bid with {higestbid}$");