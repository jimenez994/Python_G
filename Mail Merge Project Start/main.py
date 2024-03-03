#TODO: Create a letter using starting_letter.txt 
#for each name in invited_names.txt

with open("Input/Letters/starting_letter.txt") as letter:
    letter_sample = letter.read()
with open("Input/Names/invited_names.txt") as list_name_file:
    name_list = list_name_file.read().strip().splitlines()

    for name in name_list:
        new_letter = letter_sample.replace("[name]", name)
        with open(f"ReadyToSend/invited_{name}.txt", mode="w") as letter:
            letter.write(new_letter)


    # print(name_list.strip().splitlines())

#Replace the [name] placeholder with the actual name.
#Save the letters in the folder "ReadyToSend".

#Hint1: This method will help you: https://www.w3schools.com/python/ref_file_readlines.asp
    #Hint2: This method will also help you: https://www.w3schools.com/python/ref_string_replace.asp
        #Hint3: THis method will help you: https://www.w3schools.com/python/ref_string_strip.asp