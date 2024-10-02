PLACEHOLDER = "[name]"

#TODO: Create a letter using starting_letter.txt
with open("./Input/Names/invited_names.txt") as guests:
    names = guests.readlines()

with open("./Input/Letters/starting_letter.txt") as invite_template:
    invite_content = invite_template.read()
    for name in names:
        stripped_name = name.strip()
        new_letter =invite_content.replace(PLACEHOLDER, stripped_name)
        with open(f"./Output/ReadyToSend/starting_letter_{stripped_name}.txt", mode="w") as completed_invite:
            completed_invite.write(new_letter)

