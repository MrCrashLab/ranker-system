import Link from 'next/link';
import styles from  "./page.module.css";


export default function Home() {
    return (
      <div >
        <header className={styles.homeHeader}>
          <p className={styles.logo}>КиноTomatoes</p>
            <Link href="/auth/login">
              <button className={styles.myBtn}>Войти</button>
            </Link>
        </header>
        <div className={styles.backImg}>
          <div className={styles.centerTextContainer}>
            <h1 className={styles.centerText}>
              КиноTomatoes - место, где вы найдете самые вкусные фильмы!
            </h1>
            <p className={styles.subText}>
              Самые свежие киноновинки и лучшие фильмы всех времен и народов!
            </p>
          </div>
        </div>
        <div className={styles.backGrad}>
        <div className={styles.textContainer}>
            <p className={styles.textWhite}>Только у нас</p>
          </div>
          <div className={styles.cardContainer}> {/* Добавил новый контейнер для карточек */}
            <div className={styles.card}> {/* Карточка с картинкой */}
              <img src='/poster/1.jpg' alt="Постер 1" />
            </div>
            <div className={styles.card}>
              <img src='/poster/2.jpg' alt="Постер 2" />
            </div>
            <div className={styles.card}>
              <img src='/poster/3.png' alt="Постер 3" />
            </div>
            <div className={styles.card}>
              <img src='/poster/4.jpg' alt="Постер 4" />
            </div>
            <div className={styles.card}>
              <img src='/poster/5.jpg' alt="Постер 5" />
            </div>
            <div className={styles.card}>
              <img src='/poster/6.jpg' alt="Постер 6" />
            </div>
            <div className={styles.card}>
              <img src='/poster/7.jpg' alt="Постер 7" />
            </div>
            <div className={styles.card}>
              <img src='/poster/8.jpg' alt="Постер 8" />
            </div>
            <div className={styles.card}>
              <img src='/poster/9.jpg' alt="Постер 9" />
            </div>
            <div className={styles.card}>
              <img src='/poster/10.jpg' alt="Постер 10" />
            </div>
          </div>
          <div className={styles.textContainer}>
            <p className={styles.text}>И многие другие...</p>
          </div>
          <div className={styles.btnContainer}>
            <Link href="/auth/login">
                <button className={styles.redBtn}>Съесть красную таблетку</button>
            </Link>
            <Link href="/auth/login">
                <button className={styles.blueBtn}>Съесть синюю таблетку</button>
            </Link>
          </div>
        </div>
      </div>
    )
}
  
    