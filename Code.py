documents = [
    {"type": "passport", "number": "2207 876234", "name": "Василий Гупкин"},
    {"type": "invoice", "number": "11-2", "name": "Геннадий Покемонов"},
    {"type": "insurance", "number": "10006", "name": "Аристарх Павлов"}
    ]

directories = {
    '1': ['2207 876234', '11-2'],
    '2': ['10006'],
    '3': []
    }


def add_doc(docs, shelfs, shelf, type, number, name):
    doc = {'type': type, 'number': number, 'name': name}
    docs.append(doc)
    shelfs[shelf].append(doc['number'])
    return 'Документ добавлен'
 

def get_list(documents):
    for doc in documents:
        print(doc['type'], doc['number'], doc['name'])

def number_doc(documents):
    nomer = input("Введите номер документа: ")
    for numbers in documents:
        if numbers["number"] == nomer:
            return numbers["name"]

def get_shelf(dirs):
    nomer = input("Введите номер документа: ")
    for k,v in dirs.items():
        if nomer in v:
            return f'Документ находится на {k} полке'
        return 'Такого номера нет.'

def main():
    while True:
        command = input('Введите команду. a - чтобы добавить документ; g - чтобы получить список всех документов; n - чтобы получить имя документа по номеру; s - чтобы получить номер полки на которой лежит документ: ')
        if command == 'a':
            shelf = input('Введите номер полки куда положить документ: ')
            if shelf not in directories:
               print('Ошибка. Такой полки нет')
               return()
            if shelf in directories.keys():
                type = input('Введите тип документа: ')
                number = input('Введите номер документа: ')
                name = input('Введите имя владельца документа: ') 
                document = {'type' : type, 'number': number, 'name': name}
                documents.append(document)       
                directories[shelf].append(number)
                print('Документ успешно добавлен!')
        if command == 'g':
            get_list(documents)

        if command == 'n':
            print(number_doc(documents))

        if command == 's':
            print(get_shelf(directories))


main()
