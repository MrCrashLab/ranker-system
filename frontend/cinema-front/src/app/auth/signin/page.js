"use client";

import { useState } from 'react';
import axios from 'axios';
import Link from 'next/link';
import styles from  "./page.module.css";

export default function SigninPage() {
  const [username, setUsername] = useState('');
  const [password, setPassword] = useState('');
  const [confirmPassword, setConfirmPassword] = useState('');
  const [error, setError] = useState('');
  const handleLogin = async (e) => {
    e.preventDefault();
    
    try {
      if (password === confirmPassword) {
          console.log(username)
          console.log(password)
          const response = await axios.post('http://localhost:8000/users', {
            user_id: 0,
            username: username,
            password: password,
            role: 'user'
        });
          
          // const { access_token, token_type, role, exp } = response.data;

          // Сохраняем token в локальное хранилище
          localStorage.setItem('username', username);
          localStorage.setItem('role', 'user');

          // Перенаправляем пользователя на главную страницу
          window.location.href = '/mainpage';
      } else{
        setError('Пароли не совпадают');
      }
    } catch (error) {
      console.log(error);
      if (error.response && error.response.status === 400) {
        setError('Пользователь уже существует');
      } else {
        setError('Ошибка авторизации');
      }
    }
  };

  return (
    <div className={styles.container}>
      <div className={styles.card}>
        <h2>Регистрация</h2>
        <form onSubmit={handleLogin}>
          <div className={styles.formGroup}>
            <label htmlFor="username">Логин</label>
            <input
              type="text"
              id="username"
              value={username}
              className={styles.inputClass}
              onChange={(e) => setUsername(e.target.value)}
            />
          </div>
          <div className={styles.formGroup}>
            <label htmlFor="password">Пароль</label>
            <input
              type="password"
              id="password"
              value={password}
              className={styles.inputClass}
              onChange={(e) => setPassword(e.target.value)}
            />
          </div>
          <div className={styles.formGroup}>
            <label htmlFor="confirmPassword">Повторите пароль</label>
            <input
              type="password"
              id="confirmPassword"
              value={confirmPassword}
              className={styles.inputClass}
              onChange={(e) => setConfirmPassword(e.target.value)}
            />
          </div>
          {error && <div className={styles.error}>{error}</div>}
          <div className={styles.buttonContainer}>
              <button type="submit" className={styles.blueBtn}>Зарегистрироваться</button>
          </div>
        </form>
      </div>
    </div>
  )
}