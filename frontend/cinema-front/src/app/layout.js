import { Inter } from "next/font/google";
import "./globals.css";

const inter = Inter({ subsets: ["latin"] });

export const metadata = {
  title: "КиноTomatoes",
  description: "Сервис для поиска кино",
};

export default function RootLayout({ children }) {
  return (
    <html lang="en">
      <body className={inter.className}>{children}
      <div className="content"></div>
        <footer className="footer-bs">
          Copyright © 2024 All Rights Reserved by Dudarev Maksim
        </footer>
      </body>
    </html>
  );
}
