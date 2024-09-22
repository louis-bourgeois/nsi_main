import Navbar from "./components/Navbar";
import "./globals.css";

export default function RootLayout({ children }) {
  return (
    <html lang="fr" className="scroll-smooth">
      <body
        className={`min-h-screen flex flex-col items-center justify-start gap-[25vh] mx-[4vw] overflow-x-hidden scroll-smooth custom-scrollbar`}
      >
        <div className="texture-overlay" />
        <Navbar />
        {children}
      </body>
    </html>
  );
}
