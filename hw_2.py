import collections
import csv

FILE_NAME = "Corp_Summary.csv"

def print_menu() -> None:
    """
    Вывод меню для пользователя
    """
    print("Введите номер необходимого действия:\n\
    1.Вывести иерархию команд.\n\
    2.Вывести сводный отчёт по департаментам.\n\
    3.Сохранить сводный отчёт в файл .csv")

def get_request() -> int:
    """
    Получение запроса от пользователя
    """
    print_menu()
    return int(input())

def print_hierarchy(departments: dict = None, indent: int = 0) -> None:
    """
    Вывод иерархии в консоль
    """
    for department, sub_departments in departments.items():
        print(' ' * indent + department)
        if sub_departments:
            print_hierarchy({sub_dept: [] for sub_dept in sub_departments}, indent + 4)

def print_report(data: list = None) -> None:
    """
    Вывод отчёта в консоль
    """
    for item in data:
        print(f"Департамент: {item['Департамент']}")
        print(f"Численность: {item['Численность']}")
        print(f"Вилка зарплат: от {item['Вилка'][0]} до {item['Вилка'][1]}")
        print(f"Средняя зарплата: {item['Средняя зарплата']}")
        print()

def get_fork(salaries_list: list = None) -> list:
    """
    Получение вилки зарплат
    """
    return([min(salaries_list), max(salaries_list)])

def get_hierarchy() -> None: # 1
    """
    Получение иеарархии департаментов
    """
    hierarchy = collections.defaultdict(list)

    with open(FILE_NAME, encoding="utf-8") as r_file:
        file_reader = csv.reader(r_file, delimiter = ";")
        for row in file_reader:
            dept = row[1]
            unit = row[2]
            if dept == "Департамент": # нужно пропустить первую строку
                continue
            if unit not in hierarchy[dept]:
                hierarchy[dept].append(unit)
    return hierarchy

def get_report() -> dict:
    """
    Получение сводного отчёта
    Ключ - название департамента
    Первая значение - численность департамента
    Второе значение - вилка зарплат в департаменте
    Третье значение - средняя зарплата в депаратаменте
    """
    report = collections.defaultdict(list)
    with open(FILE_NAME, encoding="utf-8") as r_file:
        file_reader = csv.reader(r_file, delimiter = ";")
        for row in file_reader:
            dept = row[1]
            if dept == "Департамент": # нужно пропустить первую строку
                continue
            salary = int(row[-1])
            if len(report[dept]) != 3: # при первом появлении нужно создать поля для данных
                report[dept].append(1) # увеличиваем численность
                report[dept].append([salary]) # добавляем список зарплат
                report[dept].append(salary) # добавляем зарплату для поиска средней
            else: # заполняем информацию о департаменте
                report[dept][0] += 1
                report[dept][1].append(salary)
                report[dept][2] += salary

    for dept in report:
        report[dept][1] = get_fork(report[dept][1])
        report[dept][2] = round(report[dept][2]/report[dept][0]) # получаем среднюю зп

    data = []
    for dept in report: # переводим словарь в удобный вид
        data.append({"Департамент": dept, "Численность": report[dept][0], \
                     "Вилка": report[dept][1], "Средняя зарплата": report[dept][2]})
    return data

def get_report_csv() -> None:
    """
    Получение сводного отчёта в формате .csv
    """
    csv_filename = "report.csv"
    report = get_report()

    with open(csv_filename, "w", newline="", encoding="utf-8") as csv_file:
        fieldnames = report[0].keys()
        csv_writer = csv.DictWriter(csv_file, fieldnames=fieldnames, delimiter=";")

        csv_writer.writeheader()

        for row in report:
            csv_writer.writerow(row)

def proccess_request(request: int = None) -> None:
    """
    Обработка запроса от пользователя
    """
    if request == 1:
        hierarchy = get_hierarchy()
        print_hierarchy(dict(hierarchy.items()))
    if request == 2:
        report = get_report()
        print_report(report)
    else:
        get_report_csv()

def programm() -> None:
    """
    Программа
    """
    request = get_request()
    print()
    proccess_request(request)

if __name__ == '__main__':
    programm()
