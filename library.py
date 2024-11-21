import json

from books import Book


class BooksLibrary:
    """Класс управления библиотекой"""
    
    def __init__(self) -> dict:
        self.books = {}
        
        try:
            with open("library.json", "r", encoding="utf-8") as booklib:
                data = json.load(booklib)
                for row in data:
                    book = Book(
                        row["id"],
                        row["title"],
                        row["author"],
                        row["year"],
                        row["status"]
                        )
                    self.books[str(book.id)] = book
        except FileNotFoundError:
            print("Файл не найден")
            
    def save_to_file(self):
        """Сохранение в файл json"""
        
        with open("library.json", "w", encoding="utf-8") as booklib:
            data = [book.to_json() for book in self.books.values()]
            json.dump(data, booklib, indent=2, sort_keys=True, ensure_ascii=False)
        
    def add_book(self, book: Book):
        """Добавление книги"""
        
        if book.title in self.books:
            print("---------------------------------")
            print("Эта книга уже есть в библиотеке")
        else:
            self.books[str(book.id)] = book
            self.save_to_file()
            print("---------------------------------")
            print("Книга добавлена в библиотеку")
            
    def delete_book(self, id: str):
        """Удаление книги по id"""
        
        try:
            if id in self.books:
                del self.books[str(id)]
                self.save_to_file()
                print("---------------------------------")
                print("Книга удалена из библиотеки")
            else:
                print("---------------------------------")
                raise KeyError("Книги с таким id нет в библиотеке")
        except KeyError as e:
            print(f"{e}")
            
    def search_books(self, query: str | int):
        """Поиск книги по названию, автору или году издания"""
        
        books_found = [book for book in self.books.values() \
                       if query.lower() in book.title.lower() \
                       or query.lower() in book.author.lower() \
                       or query == book.year]
        
        if books_found:
            for book in books_found:
                print(book)
        else:
            print("---------------------------------")
            print("Не нашлось книг по вашему запросу")
            
    def list_all_books(self):
        """Получение списка всех книг"""
        
        for book in self.books.values():
            print("---------------------------------")
            print(book)
            
    def update_book_status(self, id: str, new_status: str):
        """Изменение статуса книги: В наличии/Выдана"""
        
        try:
            if str(id) in self.books:
                self.books[str(id)].status = new_status
                self.save_to_file()
                print("---------------------------------")
                print("Статус книги успешно обновлен")
            else:
                print("---------------------------------")
                raise KeyError("Такой книги нет в библиотеке")
        except KeyError as e:
            print(f"{e}")