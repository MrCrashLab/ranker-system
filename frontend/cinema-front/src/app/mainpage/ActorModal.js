import React from 'react';
import Modal from 'react-modal';
import back_styles from './page.module.css';
import styles from './ActorModal.module.css';

const ActorModal = ({ isOpen, onRequestClose, actor }) => {
  return (
    <Modal isOpen={isOpen} onRequestClose={onRequestClose} className={back_styles.modal} overlayClassName={back_styles.modalOverlay}>
      <div className={styles.actorContainer}>
        <img className={styles.actorImage} src={actor.img_path} alt={actor.name} />
        <div className={styles.actorInfo}>
          <h2>{actor.name}</h2>
          <p>День рождения: {actor.birthday}</p>
          <p>Пол: {actor.gender}</p>
          <p>Описание: {actor.description}</p>
        </div>
      </div>
    </Modal>
  );
};

export default ActorModal;
