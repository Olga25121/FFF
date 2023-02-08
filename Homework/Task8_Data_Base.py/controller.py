import model 
import view 
import logging

def run():
    start = view.show_menu()
    if start == 1:
        logging.info('Start 1-show all.')
        model.show_all()

    elif start == 2:
        logging.info('Start 2-find employee.')
        key = input('Введите имя, фамилию или должность сотрудника: ')
        model.find_employee(key)

    elif start == 3:
        logging.info('Start 3-add employee.')
        model.add_employee()
        logging.info('Employee has added.')

    elif start == 4:
        view.show_res(model.show_all()) 
        id, tel = model.change_tel()
        model.update_info(id, tel)
    elif start == 5:
        view.show_res(model.show_all()) 
        id, position = view.change_position()
        model.update_info_1(id, position)
    elif start == 6:
        view.show_res(model.show_all()) 
        id, status = view.change_surname()
        model.update_info_2(id, status)
        
        
        
        # elif start == 4: 
    #     logging.info('Start 4-update data base.')
    #     id_employee=int(input("Укажите id сотрудника:"))
    #     model.setSelected(id_employee)  
    #     print("Выберите параметр изменения: ")
    #     print("1. Фамилия")
    #     print("2. Имя")
    #     print("3. Должность")
    #     print("4. Зарплата")
    #     user_choice = int(input())
    #     model.second_select(user_choice)
    #     # input_update=input("Введите новые данные: ")
    #     logging.info('Input new data.')
    #     # model.update_data(input_update)
    #     model.change_data()
    #     logging.info('Base has updated.')


    elif start == 7:
        logging.info('Start 5-delete employee..')
        key = input('Введите id, имя или фамилию: ')
        model.delete_employee(key)
        logging.info('Employee has deleted.')

    elif start == 8:
        logging.info('Start 6-export/import.')
        model.export_import()

    elif start == 9:
        logging.info("Stop program.\n")
        model.finish_work()