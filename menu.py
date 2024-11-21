from uuid import uuid1

from library import BooksLibrary
from books import Book


def user_menu():
    """Пользовтельское меню"""
    
    library = BooksLibrary()
    
    while True:
        print("\n Библиотека")
        print("1. Добавить книгу")
        print("2. Удалить книгу")
        print("3. Список всех книг")
        print("4. Поиск книги")
        print("5. Изменить статус книги")
        print("6. Выйти")
        choice = input("Выберите действие: ")

        if choice == '1':
            id = uuid1()
            title = input("Введите название книги: ")
            author = input("Введите автора: ")
            year = input("Введите год издания: ")
            status = "В наличии"
            book = Book(str(id), title, author, year, status)
            library.add_book(book)
        elif choice == '2':
            id = input("Введите id книги: ")
            library.delete_book(id)
        elif choice == '3':
            library.list_all_books()
        elif choice == '4':
            query = input("Введите запрос (название, автор или год издания): ")
            library.search_books(query)
        elif choice == '5':
            id = input("Введите id книги: ")
            new_status = input("Введите новый статус: ")
            library.update_book_status(id, new_status)
        elif choice == '6':
            print("Выход из меню.")
            break
        else:
            print("Повторите попытку")