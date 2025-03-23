'''def __str__(self): # deixa mais bonitin a forma de saida
        return "{} {} ({}): {}".format(self.author[1], self.author[0], self.year, self.title) 
'''

class Books:
    def __init__(self, title, author, pub_year, ID):
        self.title = title
        self.author = author
        self.year = pub_year
        self.Id_Livro = ID
        self.checked_out = False
     def checkout(self):
        
        if not self.checked_out: #SE a saida do livro não esta True:
            self.checked_out = True
            print(f'O livro "{self.title}" foi emprestado.')
        else:
            print(f'O livro "{self.title}" já está emprestado.')

    def return_book(self):
        
        if self.checked_out: #SE a saida do livro está True
            self.checked_out = False
            print(f'O livro "{self.title}" foi devolvido.')
        else:
            print(f'O livro "{self.title}" já estava na biblioteca.')
            
# Criando objetos
book1 = Books("Romeu e Julieta", "William Shakespeare", 1597, "SHA-1597")
book2 = Books("Carros", "Autor Desconhecido", 2006, "CAR-2006")

print(book1.__dict__)  
print(book2)  
