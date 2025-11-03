import React from 'react';
import { Link } from 'react-router-dom';

const Layout = ({ children }) => {
  return (
    <div className="flex h-screen bg-gray-900 text-white">
      <aside className="w-64 bg-gray-800 p-4">
        <h1 className="text-2xl font-bold mb-4">Bookstore</h1>
        <nav>
          <ul>
            <li className="mb-2"><Link to="/" className="hover:text-blue-400">Dashboard</Link></li>
            <li className="mb-2"><Link to="/catalog" className="hover:text-blue-400">Catalog</Link></li>
            <li className="mb-2"><Link to="/pos" className="hover:text-blue-400">POS</Link></li>
            <li className="mb-2"><Link to="/orders" className="hover:text-blue-400">Orders</Link></li>
            <li className="mb-2"><Link to="/shipping" className="hover:text-blue-400">Shipping</Link></li>
          </ul>
        </nav>
      </aside>
      <main className="flex-1 p-4">
        <header className="flex justify-between items-center mb-4">
          <input type="text" placeholder="Search..." className="p-2 rounded bg-gray-800" />
          <div>User Menu</div>
        </header>
        {children}
      </main>
    </div>
  );
};

export default Layout;
