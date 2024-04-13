import React from 'react';
import Modal from 'react-modal';
import ActorModal from './ActorModal';
import back_styles from './page.module.css';
import styles from './MovieModal.module.css';

const MovieModal = ({ isOpen, onRequestClose, movie, onActorClick }) => {
  return (
    <Modal isOpen={isOpen} onRequestClose={onRequestClose} className={back_styles.modal} overlayClassName={back_styles.modalOverlay}>
      <div className={styles.movieContainer}>
        <img className={styles.movieImage} src={movie.img_path} alt={movie.name} />
        <div className={styles.movieInfo}>
          <h2>{movie.name}</h2>
          <p>Описание: {movie.description}</p>
          <p>Рейтинг: {movie.rating}</p>
          <h3>Актеры:</h3>
          <ul>
            {movie.actors && movie.actors.map((actor, index) => (
              <li key={index} onClick={() => onActorClick(actor)}>{actor.name}</li>
            ))}
          </ul>
        </div>
      </div>
      <ActorModal isOpen={false} onRequestClose={() => {}} actor={{}} />
    </Modal>
  );
};

export default MovieModal;
