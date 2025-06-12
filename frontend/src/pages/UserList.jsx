import React, { useEffect, useState } from 'react';
import api from '../services/api';
import { useNavigate } from 'react-router-dom';

const UserList = () => {
  const [users, setUsers] = useState([]);
  const navigate = useNavigate();

  useEffect(() => {
    const fetchUsers = async () => {
      try {
        const response = await api.get('/users');
        setUsers(response.data);
      } catch (error) {
        console.error('Erro ao buscar usuários:', error);
        if (error.response?.status === 401) {
          navigate('/login');
        }
      }
    };
    fetchUsers();
  }, [navigate]);

  return (
    <div className="container">
      <h2>Usuários</h2>
      <button onClick={() => navigate('/users/new')}>Novo Usuário</button>
      <ul>
        {users.map((user) => (
          <li key={user.id}>
            {user.name} ({user.email}){' '}
            <button onClick={() => navigate(`/users/${user.id}`)}>Editar</button>
          </li>
        ))}
      </ul>
    </div>
  );
};

export default UserList;
