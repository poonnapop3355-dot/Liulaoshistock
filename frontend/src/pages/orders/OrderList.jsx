import React from 'react';
import { useQuery } from '@tanstack/react-query';
import api from '../../services/api';

const fetchOrders = async () => {
  const { data } = await api.get('/orders');
  return data;
};

const OrderList = () => {
  const { data: orders, error, isLoading } = useQuery(['orders'], fetchOrders);

  if (isLoading) {
    return <div>Loading...</div>;
  }

  if (error) {
    return <div>Error fetching orders</div>;
  }

  return (
    <div>
      <h2 className="text-2xl mb-4">Orders Queue</h2>
      <table className="w-full text-left">
        <thead>
          <tr>
            <th className="p-2">Order #</th>
            <th className="p-2">Customer</th>
            <th className="p-2">Status</th>
          </tr>
        </thead>
        <tbody>
          {orders.map((order) => (
            <tr key={order.id}>
              <td className="p-2">{order.order_no}</td>
              <td className="p-2">{order.customer_id}</td>
              <td className="p-2">{order.status || 'pending'}</td>
            </tr>
          ))}
        </tbody>
      </table>
    </div>
  );
};

export default OrderList;
