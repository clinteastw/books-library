from uuid import UUID


class Book:
    """Класс для представления объекта книги
    
       Атрибуты:
        - id (UUID): Уникальный идентификатор книги
        - title (str): Название книги
        - author (str): Автор книги
        - year (int): Год издания книги
        - status (str): Текущий статус книги ("В наличии", "Выдана")
          
    """
    def __init__(self, id: UUID, title: str, author: str, year: int, status: str):
        """Инициализация объекта книги"""
        
        self.id = id
        self.title = title
        self.author = author
        self.year = year
        self.status = status
        
    def to_json(self) -> dict:
        """Преобразует объект книги в словарь JSON"""
        
        return {
            "id": self.id,
            "title": self.title,
            "author": self.author,
            "year": self.year,
            "status": self.status
        }
        
    def __str__(self) -> str:
        """Строковое представление объекта книги"""
        
        return f"ID - {self.id}: Книга *{self.title}* от автора *{self.author}*, издана: в {self.year}г. -- {self.status}"
    
    
