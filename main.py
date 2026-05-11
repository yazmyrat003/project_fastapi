from fastapi import FastAPI
import uvicorn
app = FastAPI()
from pydantic import BaseModel
books = [
    {
    "id":1,
    "name":"yazmyrat",
    "author":"Book of dragon",
    },
    {
    "id":2,
    "name":"Jemal",
    "author":"Rich Father and poor Father",
    },
    {
    "id":2,
    "name":"Jemal",
    "author":"Rich Father and poor Father",
    }
]
@app.get("/books")
async def read_books():
    return books
@app.get("/books/{book_id}")
def read_book(book_id: int):
    for book in books:
        if book["id"] == book_id:
            return book
class Book(BaseModel):
    name: str
    author: str
@app.post("/books")
def create_book(new_book: Book):
    books.append({
         "id": len(books) + 1,
        "name": new_book.name,
        "author": new_book.author,
    })
    return {"succes" : True,"message":"Book is succesfully added"}
if __name__ == "__main__":
    uvicorn.run("main:app",reload=True)
