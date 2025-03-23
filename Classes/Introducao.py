class Books:
    def __init__(self, title, author, pub_year, ID):
        self.title = title
        self.author = author
        self.year = pub_year
        self.Id_Livro = ID
        self.checked_out = False

# Criando objetos
book1 = Books("Romeu e Julieta", "William Shakespeare", 1597, "SHA-1597")
book2 = Books("Carros", "Autor Desconhecido", 2006, "CAR-2006")

print(book1.__dict__)  
print(book2)  