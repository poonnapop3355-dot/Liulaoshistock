from fastapi import APIRouter, Depends, UploadFile, File
from app.core.rbac import require_role
from app.crud.book import crud_book
from app.schemas.book import Book
import csv
import io
import uuid

router = APIRouter()

@router.post("/import", dependencies=[Depends(require_role(["admin", "manager"]))])
async def import_catalog(file: UploadFile = File(...)):
    """
    Import a catalog of books from a CSV file.
    """
    contents = await file.read()
    csv_file = io.StringIO(contents.decode("utf-8"))
    reader = csv.DictReader(csv_file)
    for row in reader:
        book = Book(
            id=str(uuid.uuid4()),
            isbn13=row["isbn13"],
            title_th=row["title_th"],
            authors=[], # In a real scenario, you would look up or create authors
        )
        crud_book.create(book)
    return {"message": "Catalog imported successfully"}

@router.get("/export", dependencies=[Depends(require_role(["admin", "manager"]))])
def export_catalog():
    """
    Export the catalog of books to a CSV file.
    """
    output = io.StringIO()
    writer = csv.writer(output)
    writer.writerow(["isbn13", "title_th"])
    for book in crud_book.get_multi():
        writer.writerow([book.isbn13, book.title_th])
    return output.getvalue()
