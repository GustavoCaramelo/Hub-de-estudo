import { createContext, useContext, useState } from 'react';
import { useNavigate } from 'react-router-dom';
import axios from 'axios';

// Cria o contexto
const AuthContext = createContext();

// Hook para consumir o contexto
export const useAuth = () => useContext(AuthContext);

// Provider
export const AuthProvider = ({ children }) => {
  const [user, setUser] = useState(null);         // Nome ou e-mail do usuário
  const [token, setToken] = useState(null);       // JWT token
  const navigate = useNavigate();

  const login = async (email, password) => {
    try {
      const response = await axios.post('http://localhost:8000/login', {
        username: email,
        password,
      });

      const { access_token } = response.data;

      // Armazena no estado e localStorage
      setToken(access_token);
      localStorage.setItem('token', access_token);
      setUser(email); // opcional: obter do backend
      navigate('/users');
    } catch (error) {
      alert('Falha no login. Verifique as credenciais.');
    }
  };

  const logout = () => {
    setToken(null);
    setUser(null);
    localStorage.removeItem('token');
    navigate('/');
  };

  return (
    <AuthContext.Provider value={{ user, token, login, logout }}>
      {children}
    </AuthContext.Provider>
  );
};
