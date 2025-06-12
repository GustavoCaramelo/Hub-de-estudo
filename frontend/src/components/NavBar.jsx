import React, { useContext } from 'react';
import { AuthContext } from '../context/AuthContext';
import {
  AppBar,
  Toolbar,
  Typography,
  Button,
  Box,
} from '@mui/material';
import { Link } from 'react-router-dom';

const NavBar = () => {
  const { isAuthenticated, logout } = useContext(AuthContext);

  return (
    <AppBar position="static">
      <Toolbar>
        <Typography variant="h6" component="div" sx={{ flexGrow: 1 }}>
          StudyHub
        </Typography>
        {isAuthenticated && (
          <Box>
            <Button color="inherit" component={Link} to="/users">
              Usuários
            </Button>
            <Button color="inherit" component={Link} to="/cadastro">
              Cadastrar
            </Button>
            <Button color="inherit" onClick={logout}>
              Sair
            </Button>
          </Box>
        )}
      </Toolbar>
    </AppBar>
  );
};

export default NavBar;
