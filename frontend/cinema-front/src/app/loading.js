import style from './loading.module.css'

export default function NotFound() {
    return (
      <div className={style.back}>
        <div className={style.loader}>
          <span>Загрузка...</span>
        </div>
      </div>
    )
}