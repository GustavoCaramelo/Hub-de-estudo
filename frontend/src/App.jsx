import { Routes, Route, Navigate } from 'react-router-dom';
import Login from './pages/Login';
import UserList from './pages/UserList';
import UserForm from './pages/UserForm';
import NavBar from './components/NavBar';
import { useAuth } from './context/AuthContext';

function App() {
  const { isAuthenticated } = useAuth();

  return (
    <>
      {isAuthenticated && <NavBar />}
      <Routes>
        <Route path="/login" element={<Login />} />
        <Route path="/users" element={isAuthenticated ? <UserList /> : <Navigate to="/login" />} />
        <Route path="/users/new" element={isAuthenticated ? <UserForm /> : <Navigate to="/login" />} />
        <Route path="/users/:id" element={isAuthenticated ? <UserForm /> : <Navigate to="/login" />} />
        <Route path="*" element={<Navigate to="/users" />} />
      </Routes>
    </>
  );
}

export default App;
