"use client";

import React, {useEffect} from 'react';
import ReactDOM from 'react-dom';
import Link from 'next/link';
import axios from 'axios';
import Modal from 'react-modal';
import styles from  "./page.module.css";


export default function Home() {
  const [isModalLKOpen, setIsModalLKOpen] = React.useState(false);
  const [username, setUsername] = React.useState('');
  const [role, setRole] = React.useState('');
  const [movies, setMovies] = React.useState([]);

  useEffect(() => {
    const username = localStorage.getItem('username');
    const role = localStorage.getItem('role');

    if (username && role) {
      setUsername(username);
      setRole(role);
    }
    axios.get('http://localhost:8000/cinema')
      .then(response => {
        setMovies(response.data);
      })
      .catch(error => {
        console.error('Error fetching movies: ', error);
      });
  }, []);
  
  const openModal = () => {
    setIsModalLKOpen(true);
  };

  const closeModal = () => {
    setIsModalLKOpen(false);
  };

  return (
    <div>
      <header className={styles.homeHeader}>
        <p className={styles.logo}>КиноTomatoes</p>
        <button className={styles.myBtn} onClick={openModal}>Личный кабинет</button>
      </header>
      <div className={styles.backGrad}>
        <div className={styles.textContainer}>
          <p className={styles.textWhite}>Наши фильмы</p>
        </div>

      </div>
      <Modal
        isOpen={isModalLKOpen}
        onRequestClose={closeModal}
        className={styles.modal}
        overlayClassName={styles.modalOverlay}
      >
        <h2>Личный кабинет</h2>
        <label htmlFor="username">Логин: {username}</label>
        <label htmlFor="role">Роль: {role}</label>

        {
          role === 'admin' && (
          <Link href="/addmovie">
            <button className={styles.blueBtn}>Добавить фильм</button>
          </Link>
          )
        }
        {
          role === 'admin' && (
          <Link href="/addactor">
            <button className={styles.blueBtn}>Добавить актера</button>
          </Link>
          )
        }
        {
          role === 'admin' && (
          <Link href="/addgenre">
            <button className={styles.blueBtn}>Добавить жанр</button>
          </Link>
          )
        }
        <Link href="/home">
          <button className={styles.redBtn}>Выйти</button>
        </Link>
      </Modal>
    </div>
  );
}