import React from 'react';
import { useDispatch } from 'react-redux';
import { logout } from '../../store/session';

const LogoutButton = () => {
  const dispatch = useDispatch()

  const onLogout = async (e) => {
    await dispatch(logout());
  };

  return <button className="secondary-button" onClick={onLogout}>Log Out</button>;
};

export default LogoutButton;
