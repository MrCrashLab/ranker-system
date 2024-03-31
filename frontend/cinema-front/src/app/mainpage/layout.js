import { Inter } from "next/font/google";
import styles from "./page.module.css"
const inter = Inter({ subsets: ["latin"] });

export const metadata = {
  title: "КиноTomatoes",
  description: "Сервис для поиска кино",
};

export default function RootLayout({ children }) {
  return (
      <div className={inter.className}>{children}</div>
  );
}
