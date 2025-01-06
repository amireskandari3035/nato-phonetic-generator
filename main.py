import pandas

data = pandas.read_csv(".venv/nato_phonetic_alphabet.csv")

phonetic_dict = {row.letter: row.code for (index, row) in data.iterrows()}

is_ok = True
while is_ok:
    name = input("Enter a name: ").upper()
    try:
        output_name = [phonetic_dict[letter] for letter in name]

    except KeyError:
        print("Sorry, only letters in alphabet please!")

    else:
        print("\n",output_name)
        is_ok = False