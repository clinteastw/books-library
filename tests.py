import unittest
from uuid import uuid1

from books import Book
from library import BooksLibrary


class TestBook(unittest.TestCase):
    
    test_book_1 = Book(str(uuid1()), "Testbook1", "Testauthor1", "2024", "В наличии")
    test_book_2 = Book(str(uuid1()), "Testbook2", "Testauthor2", "1994", "В наличии")
    
    test_data = [test_book_1.to_json(), test_book_2.to_json()]
        
    def test_add_book(self):
        lib = BooksLibrary()
        lib.add_book(self.test_book_1)
        self.assertIn(str(self.test_book_1.id), lib.books)
        
    def test_delete_book(self):
        lib = BooksLibrary()
        lib.add_book(self.test_book_1)
        lib.delete_book(str(self.test_book_1.id))
        self.assertNotIn(str(self.test_book_1.id), lib.books)
        
    def test_search_books_by_title(self):
        lib = BooksLibrary()
        lib.add_book(self.test_book_1)
        results = lib.search_books("Testbook1")
        self.assertEqual(results, [self.test_book_1])
        
    def test_search_books_by_author(self):
        lib = BooksLibrary()
        lib.add_book(self.test_book_1)
        results = lib.search_books("Testauthor1")
        self.assertEqual(results, [self.test_book_1])
    
    def test_search_books_by_year(self):
        lib = BooksLibrary()
        lib.add_book(self.test_book_1)
        results = lib.search_books("2024")
        self.assertEqual(results, [self.test_book_1])
        
    def test_update_book_status(self):
        lib = BooksLibrary()
        lib.add_book(self.test_book_1)
        lib.update_book_status(str(self.test_book_1.id), "Выдана")
        updated_book = lib.books[str(self.test_book_1.id)]
        self.assertEqual(updated_book.status, "Выдана")
        
if __name__ == '__main__':
    unittest.main()