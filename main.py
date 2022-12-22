# TODO: Create a letter using starting_letter.txt
# for each name in invited_names.txt
# Replace the [name] placeholder with the actual name.
# Save the letters in the folder "ReadyToSend".

# Hint1: This method will help you: https://www.w3schools.com/python/ref_file_readlines.asp
# Hint2: This method will also help you: https://www.w3schools.com/python/ref_string_replace.asp
# Hint3: THis method will help you: https://www.w3schools.com/python/ref_string_strip.asp


filepath = "Input/Names/invited_names.txt"


def get_names(filepath):
    name_list = []
    with open(filepath) as namedata:
        content = namedata.readlines()
    for names in content:
        name_list.append(names.replace("\n", ""))
    return name_list


formatted_names = get_names(filepath)


def output_letter(name_list):
    with open("Input/Letters/starting_letter.txt") as starting_letter:
        letter_content = starting_letter.read()

    for name in formatted_names:
        out_letter = open(f"Output/ReadyToSend/{name}.txt", "x")
        out_letter.write(letter_content.replace("[name]", name))

output_letter(formatted_names)
