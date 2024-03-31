"use client";

import { useState } from 'react';
import axios from 'axios';
import Link from 'next/link';
import styles from  "./page.module.css";

export default function LoginPage() {
  const [username, setUsername] = useState('');
  const [password, setPassword] = useState('');
  const [error, setError] = useState('');
  const formData = new URLSearchParams();
  formData.append('username', username);
  formData.append('password', password);
  const handleLogin = async (e) => {
    e.preventDefault();
    console.log(formData)

    try {
      const response = await axios.post('http://localhost:8000/token', formData, {
        headers: {
        'Content-Type': 'application/x-www-form-urlencoded'
      }
    });
      
      const { access_token, token_type, role, exp } = response.data;

      // Сохраняем token в локальное хранилище
      localStorage.setItem('username', username);
      localStorage.setItem('role', role);
      localStorage.setItem('access_token', access_token);
      localStorage.setItem('token_type', token_type);

      // Перенаправляем пользователя на главную страницу
      window.location.href = '/mainpage';
    } catch (error) {
      console.log(error);
      if (error.response && error.response.status === 401) {
        setError('Невеерный логин или пароль');
      } else {
        setError('Ошибка авторизации');
      }
    }
  };

  return (
    <div className={styles.container}>
      <div className={styles.card}>
        <h2>Авторизация</h2>
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
          {error && <div className={styles.error}>{error}</div>}
          <div className={styles.buttonContainer}>
            <button type="submit" className={styles.redBtn}>Войти</button>
            <Link href="/auth/signin">
              <button type="button" className={styles.blueBtn}>Регистрация</button>
            </Link>
          </div>
        </form>
      </div>
    </div>
  )
}