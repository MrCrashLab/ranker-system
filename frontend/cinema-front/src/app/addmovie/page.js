"use client";

import { useState, useEffect} from 'react';
import axios from 'axios';
import Link from 'next/link';
import Select from 'react-select';
import makeAnimated from 'react-select/animated';
import styles from  "./page.module.css";

const animatedComponents = makeAnimated();

export default function AddMoviePage() {
  const [name, setName] = useState('');
  const [password, setPassword] = useState('');
  const [genres, setGenres] = useState([]);
  const [genre, setGenre] = useState('');
  const [actors, setActors] = useState([]);
  const [getActors, setGetActors] = useState([]);
  const [description, setDescription] = useState('');
  const [imgPath, setImgPath] = useState('');
  const [error, setError] = useState('');
  useEffect(() => {
    axios.get('http://localhost:8000/genre')
      .then(response => {
        setGenres(response.data);
      })
      .catch(error => {
        console.error('Error fetching options: ', error);
      });

    axios.get('http://localhost:8000/actor')
      .then(response => {
        setGetActors(response.data);
      })
      .catch(error => {
        console.error('Error fetching options: ', error);
      });
  }, []);


  const handleLogin = async (e) => {
    e.preventDefault();
    if (!name || !actors.length || !genre || !description || !imgPath) {
      setError('Заполните все поля');
      return;
    } 
    console.log({cinema_id: 0,
      name: name,
      rating: 5,
      actors: actors,
      genres: [genre],
      description: description,
      img_path: imgPath})
    try {
      const response = await axios.post('http://localhost:8000/cinema/',
      {
        cinema_id: 0,
        name: name,
        rating: 5,
        actors: actors,
        genres: [genre],
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
    
      
      // const { access_token, token_type, role, exp } = response.data;

      // Сохраняем token в локальное хранилище
      // localStorage.setItem('username', username);
      // localStorage.setItem('role', role);


      // Перенаправляем пользователя на главную страницу
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

  const handleGenreSelected = (event) => {
    const selectedOption = genres.find(genre => genre.genre_id.toString() === event.value.toString());
    setGenre(selectedOption);
  };

  const handleActorSelect = (selectedOptions) => {
    const selectedActors = selectedOptions.map(option => {
      const actor = getActors.find(actor => actor.actor_id === option.value);
      return actor;
    });
    setActors(selectedActors);
  };
  console.log(actors)

  return (
    <div className={styles.container}>
      <div className={styles.card}>
        <h2>Добавить фильм</h2>
        <form onSubmit={handleLogin}>
          <div className={styles.formGroup}>
            <label htmlFor="name">Название фильма</label>
            <input
              type="text"
              id="name"
              value={name}
              className={styles.inputClass}
              onChange={(e) => setName(e.target.value)}
            />
          </div>
          <div className={styles.formGroup}>
            <label>Жанр</label>
            <Select
              components={animatedComponents}
              options={genres.map(genre_v => ({ value: genre_v.genre_id, label: genre_v.name }))}
              value={{ value: genre?.genre_id, label: genre?.name }}
              onChange={handleGenreSelected}
            />
          </div>
          <div className={styles.formGroup}>
            <label>Актеры</label>
            <Select
              isMulti
              components={animatedComponents}
              options={getActors.map(actor => ({ value: actor.actor_id, label: actor.name }))}
              value={actors.map(ac_v => ({value: ac_v.actor_id, label: ac_v.name}))}
              className={styles.actorSelect}
              onChange={handleActorSelect}
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