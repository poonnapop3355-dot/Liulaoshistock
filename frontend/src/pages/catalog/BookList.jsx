import React from 'react';
import { useQuery } from '@tanstack/react-query';
import api from '../../services/api';

const fetchBooks = async () => {
  const { data } = await api.get('/books');
  return data;
};

const BookList = () => {
  const { data: books, error, isLoading } = useQuery(['books'], fetchBooks);

  const handleImport = async (e) => {
    const file = e.target.files[0];
    const formData = new FormData();
    formData.append('file', file);
    await api.post('/catalog/import', formData, {
      headers: {
        'Content-Type': 'multipart/form-data',
      },
    });
  };

  const handleExport = async () => {
    const { data } = await api.get('/catalog/export');
    const blob = new Blob([data], { type: 'text/csv' });
    const url = window.URL.createObjectURL(blob);
    const a = document.createElement('a');
    a.href = url;
    a.download = 'books.csv';
    a.click();
  };

  if (isLoading) {
    return <div>Loading...</div>;
  }

  if (error) {
    return <div>Error fetching books</div>;
  }

  return (
    <div>
      <div className="flex justify-between items-center mb-4">
        <h2 className="text-2xl">Book Catalog</h2>
        <div>
          <label htmlFor="import-csv" className="p-2 bg-blue-600 rounded cursor-pointer mr-2">
            Import CSV
          </label>
          <input id="import-csv" type="file" onChange={handleImport} className="hidden" />
          <button onClick={handleExport} className="p-2 bg-blue-600 rounded">
            Export CSV
          </button>
        </div>
      </div>
      <table className="w-full text-left">
        <thead>
          <tr>
            <th className="p-2">ISBN</th>
            <th className="p-2">Title</th>
            <th className="p-2">Author</th>
          </tr>
        </thead>
        <tbody>
          {books.map((book) => (
            <tr key={book.id}>
              <td className="p-2">{book.isbn13}</td>
              <td className="p-2">{book.title_th}</td>
              <td className="p-2">{book.authors.join(', ')}</td>
            </tr>
          ))}
        </tbody>
      </table>
    </div>
  );
};

export default BookList;
