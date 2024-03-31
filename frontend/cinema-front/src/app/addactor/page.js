"use client";

import { useState, useEffect} from 'react';
import axios from 'axios';
import DatePicker from 'react-datepicker';
import 'react-datepicker/dist/react-datepicker.css';
import makeAnimated from 'react-select/animated';
import styles from  "./page.module.css";
import moment from 'moment';

const animatedComponents = makeAnimated();

export default function AddActorPage() {
  const [name, setName] = useState('');
  const [gender, setGender] = useState('');
  const [birthday, setBirthday] = useState('');
  const [description, setDescription] = useState('');
  const [imgPath, setImgPath] = useState('');
  const [error, setError] = useState('');

  const handleLogin = async (e) => {
    e.preventDefault();
    if (!name || !actors.length || !genre || !description || !imgPath) {
      setError('Заполните все поля');
      return;
    } 
    try {
      const response = await axios.post('http://localhost:8000/actor/',
      {
        actor_id: 0,
        name: name,
        birthday: birthday,
        gender: gender,
        description: description,
        img_path: imgPath
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
        <h2>Добавить актера</h2>
        <form onSubmit={handleLogin}>
          <div className={styles.formGroup}>
            <label>Имя актера</label>
            <input
              type="text"
              id="name"
              value={name}
              className={styles.inputClass}
              onChange={(e) => setName(e.target.value)}
            />
          </div>
          <div className={styles.formGroup}>
            <label>Пол актера</label>
            <input
              type="text"
              id="gender"
              value={gender}
              className={styles.inputClass}
              onChange={(e) => setGender(e.target.value)}
            />
          </div>
          <div className={styles.formGroup}>
            <label>Дата рождения</label>
            <DatePicker
              selected={birthday}
              onChange={(date) => setBirthday(date)}
              dateFormat="dd/MM/yyyy"
            />
          </div>  
          <div className={styles.formGroup}>
            <label>Описание</label>
            <textarea
              type="text"
              id="description"
              value={description}
              className={styles.inputClass}
              onChange={(e) => setDescription(e.target.value)}
            />
          </div>
          <div className={styles.formGroup}>
            <label>Путь до картинки</label>
            <input
              type="text"
              id="img_path"
              value={imgPath}
              className={styles.inputClass}
              onChange={(e) => setImgPath(e.target.value)}
            />
          </div>
          {error && <div className={styles.error}>{error}</div>}
          <div className={styles.buttonContainer}>
            <button type="submit" className={styles.redBtn}>Добавить фильм</button>
          </div>
        </form>
      </div>
    </div>
  )
}