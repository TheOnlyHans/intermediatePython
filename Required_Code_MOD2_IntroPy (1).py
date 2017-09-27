# [] create list-o-matic
# [] copy and paste in edX assignment page

def list_o_matic(entry):
    if entry == "":
        return ('"' + band_list.pop() + '"' + " Popped from band_list")
    else:
        if entry in band_list:
            band_list.remove(entry)
            return ("One instance of " + '"' + entry + '"' + " Removed from band_list")
        else:
            band_list.append(entry)
            return ("1 instance of " + '"' + entry + '"' + " appended to band_list")
    
band_list = ["Mudvayne", "A7X", "Killswitch", "Disturbed"]
entry = ""
list_entry = ""

while band_list != []:
    print("Look at all the bands!", band_list)
    quit_search = input("Enter a band name or type \"Quit\": ")
    if quit_search.lower() == "quit":
        break
    print(list_o_matic(quit_search))
    print("")

print("\nGoodbye!")
