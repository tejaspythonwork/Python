from my_package import use_date_time,generate_note


def write_to_file(self):
    date_1,time_1 = use_date_time.date_and_time(self)
    print(date_1)
    print(time_1)
    generator,title,content = generate_note.generate_note(self)
    # print(generator)
    # print(title)
    # print(content)
    with open(rf'F:\Python\Python\Assessment\my_notes\{title}.txt','w+') as file:
        file.write(f'{date_1} \n{time_1} \n')
        file.write(f'\nE-Note Title = {title}')
        file.write(f'\nE-Note Description = {content}')
        file.write(f'\nE-Note Generator = {generator}')
        file.write(f'\n=================================================')