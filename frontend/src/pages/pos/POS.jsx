import React, { useState } from 'react';
import { useQuery, useMutation, useQueryClient } from '@tanstack/react-query';
import api from '../../services/api';
import uuid from 'react-uuid';

const fetchBookVariants = async (query) => {
  if (!query) return [];
  const { data } = await api.get(`/book_variants?q=${query}`);
  return data;
};

const createOrder = async (order) => {
  const { data } = await api.post('/pos/orders', order);
  return data;
};

const POS = () => {
  const queryClient = useQueryClient();
  const [cart, setCart] = useState([]);
  const [search, setSearch] = useState('');

  const { data: searchResults } = useQuery(['bookVariants', search], () => fetchBookVariants(search));

  const mutation = useMutation(createOrder, {
    onSuccess: () => {
      setCart([]);
      queryClient.invalidateQueries('orders');
    },
  });

  const addToCart = (variant) => {
    setCart((prev) => [...prev, { ...variant, quantity: 1 }]);
  };

  const handleCheckout = () => {
    const order = {
      id: uuid(),
      order_no: `POS-${Date.now()}`,
      channel: 'pos',
      customer_id: 'walk-in', // In a real app, you'd select a customer
      items: cart.map(item => ({ book_variant_id: item.id, quantity: item.quantity, price: item.price })),
      payment: { method: 'cash', amount: cart.reduce((acc, item) => acc + item.price * item.quantity, 0) },
    };
    mutation.mutate(order);
  };

  return (
    <div className="flex h-full">
      <div className="w-2/3 p-4">
        <input
          type="text"
          placeholder="Scan or search for a book..."
          value={search}
          onChange={(e) => setSearch(e.target.value)}
          className="w-full p-2 rounded bg-gray-800"
        />
        <div className="mt-4">
          {searchResults && searchResults.map((variant) => (
            <div key={variant.id} onClick={() => addToCart(variant)} className="p-2 border-b border-gray-700 cursor-pointer">
              {variant.sku}
            </div>
          ))}
        </div>
      </div>
      <div className="w-1/3 p-4 bg-gray-800">
        <h2 className="text-2xl mb-4">Cart</h2>
        {cart.length === 0 ? (
          <p>Cart is empty</p>
        ) : (
          <ul>
            {cart.map((item) => (
              <li key={item.id} className="flex justify-between mb-2">
                <span>{item.sku}</span>
                <span>{item.price}</span>
              </li>
            ))}
          </ul>
        )}
        <div className="mt-4">
          <button
            onClick={handleCheckout}
            className="w-full p-2 bg-blue-600 rounded"
            disabled={cart.length === 0 || mutation.isLoading}
          >
            {mutation.isLoading ? 'Processing...' : 'Checkout'}
          </button>
        </div>
      </div>
    </div>
  );
};

export default POS;
