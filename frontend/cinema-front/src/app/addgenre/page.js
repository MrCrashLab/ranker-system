"use client";

import { useState, useEffect} from 'react';
import axios from 'axios';
import makeAnimated from 'react-select/animated';
import styles from  "./page.module.css";

const animatedComponents = makeAnimated();

export default function AddMoviePage() {
  const [name, setName] = useState('');
  const [error, setError] = useState('');

  const handleLogin = async (e) => {
    e.preventDefault();
    if (!name) {
      setError('Заполните все поля');
      return;
    } 
    try {
      const response = await axios.post('http://localhost:8000/genre/',
      {
        genre_id: 0,
        name: name,
      },
      {
        headers: {
          'Content-Type': 'application/json',
          'Authorization':`Bearer ${localStorage.getItem('access_token')}`,
          'accept': 'application/json'
        }
      }
    );
      window.location.href = '/mainpage';
    } catch (error) {
      console.log(error);
      if (error.response && error.response.status === 401) {
        setError('Неавторизованный пользователь');
      } else {
        setError('Ошибка авторизации');
      }
    }
  };

  return (
    <div className={styles.container}>
      <div className={styles.card}>
        <h2>Добавить жанр</h2>
        <form onSubmit={handleLogin}>
          <div className={styles.formGroup}>
            <label htmlFor="name">Название жанра</label>
            <input
              type="text"
              id="name"
              value={name}
              className={styles.inputClass}
              onChange={(e) => setName(e.target.value)}
            />
          </div>
          {error && <div className={styles.error}>{error}</div>}
          <div className={styles.buttonContainer}>
            <button type="submit" className={styles.redBtn}>Добавить жанр</button>
          </div>
        </form>
      </div>
    </div>
  )
}