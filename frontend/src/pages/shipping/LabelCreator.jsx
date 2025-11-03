import React, { useState } from 'react';
import { useQuery } from '@tanstack/react-query';
import api from '../../services/api';

const fetchOrders = async () => {
  const { data } = await api.get('/orders');
  return data;
};

const LabelCreator = () => {
  const [selectedOrders, setSelectedOrders] = useState([]);
  const { data: orders, error, isLoading } = useQuery(['orders'], fetchOrders);

  const handleGenerateLabels = async () => {
    const { data } = await api.post('/shipping/labels', selectedOrders);
    const newWindow = window.open();
    newWindow.document.write(data);
  };

  const handleSelectOrder = (order) => {
    setSelectedOrders((prev) =>
      prev.find((o) => o.id === order.id)
        ? prev.filter((o) => o.id !== order.id)
        : [...prev, order]
    );
  };

  if (isLoading) return <div>Loading...</div>;
  if (error) return <div>Error fetching orders</div>;

  return (
    <div>
      <h2 className="text-2xl mb-4">Create Shipping Labels</h2>
      <div className="mb-4">
        <button
          onClick={handleGenerateLabels}
          className="p-2 bg-blue-600 rounded"
          disabled={selectedOrders.length === 0}
        >
          Generate Labels for Selected ({selectedOrders.length})
        </button>
      </div>
      <div className="grid grid-cols-3 gap-4">
        {orders.map((order) => (
          <div
            key={order.id}
            className={`p-4 rounded border ${
              selectedOrders.find((o) => o.id === order.id)
                ? 'border-blue-500'
                : 'border-gray-700'
            }`}
            onClick={() => handleSelectOrder(order)}
          >
            <h3 className="font-bold">{order.order_no}</h3>
            <p>{order.customer.fullname}</p>
          </div>
        ))}
      </div>
    </div>
  );
};

export default LabelCreator;
