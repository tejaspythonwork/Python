def generate_note(self):

    while True:
        try:
                self.generateor_name = input('Please enter note Generator Name: ')
                if not all(char.isalpha() or char.isspace() or char == '-' for char in self.generateor_name):
                    raise ValueError("Please enter a valid string containing only letters, spaces, or hyphens.")
        except ValueError as e:
                print(e)
        else:
                break

    while True:
        try:
                self.e_note_title = input('Please enter e-note title: ')
                if not self.e_note_title.replace(" ","").isalpha():
                    raise ValueError("Please enter a valid string.")
        except ValueError as e:
                print(e)
        else:
                break

    while True:
        try:
                self.e_note_content = input('Please enter e-note Content: ')
                if not isinstance(self.e_note_content, str) or self.e_note_content.strip() == "":
                    raise ValueError("Please enter a valid content.")
        except ValueError as e:
                print(e)
        else:
                break   


    return self.generateor_name,self.e_note_title,self.e_note_content   