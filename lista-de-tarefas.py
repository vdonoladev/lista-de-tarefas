import json


def line():
    print('-'*50)


def table():
    print(
        '''
    FOR THE LIST TO BE SAVED, CLOSE THE PROGRAM USING 4

     [1] | Add task
     [2] | List task
     [3] | Undo the last task
     [4] | Go out
    '''
    )


def undo(indice):
    task_list.pop(-1)
    return indice


task_list = []

while True:
    line()
    table()
    line()

    try:
        option = int(input('Type what you want to do: '))
        if option == 1:
            line()
            task = str(input('Which task do you want to add? '))
            task_list.append(task)
            print('Task added!')
            line()

        elif option == 2:
            try:
                file_C_list = 'task_list.json'
                with open(file_C_list) as saved_file:
                    task_list = json.load(saved_file)
                    print(task_list)
            except:
                line()
                print(task_list)
                line()

        elif option == 3:
            try:
                undo(task_list)
                print(task_list)
            except IndexError:
                print(
                    'Empty list, you have to add something to the list in order to use undo.')

        elif option == 4:
            print('Finish your previous list before writing a new one.\n'
                  'because at the end of the program the list being created will overwrite\n'
                  'the previous list has already been saved.')
            file_C_list = 'task_list.json'
            with open(file_C_list, 'w') as saved_file:
                json.dump(task_list, saved_file)

            print(f'Before you leave. Your list is this {task_list}')

            sair = input('Press any key to confirm the end of the program: ')
            print('Program finished!')
            break
    except ValueError:
        print('Enter a number that corresponds to what you want to do: ')
