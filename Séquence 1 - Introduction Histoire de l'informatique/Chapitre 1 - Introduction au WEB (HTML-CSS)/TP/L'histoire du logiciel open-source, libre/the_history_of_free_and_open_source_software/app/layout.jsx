import "./globals.css";

// const overusedGrotesk = localFont({
//   src: [
//     {
//       path: "./fonts/OverusedGrotesk-Light.woff2",
//       weight: "300",
//       style: "normal",
//     },
//     {
//       path: "./fonts/OverusedGrotesk-Book.woff2",
//       weight: "350",
//       style: "normal",
//     },
//     {
//       path: "./fonts/OverusedGrotesk-Regular.woff2",
//       weight: "400",
//       style: "normal",
//     },
//     {
//       path: "./fonts/OverusedGrotesk-Medium.woff2",
//       weight: "500",
//       style: "normal",
//     },
//     {
//       path: "./fonts/OverusedGrotesk-SemiBold.woff2",
//       weight: "600",
//       style: "normal",
//     },
//     {
//       path: "./fonts/OverusedGrotesk-Bold.woff2",
//       weight: "700",
//       style: "normal",
//     },
//     {
//       path: "./fonts/OverusedGrotesk-ExtraBold.woff2",
//       weight: "800",
//       style: "normal",
//     },
//     {
//       path: "./fonts/OverusedGrotesk-Black.woff2",
//       weight: "900",
//       style: "normal",
//     },
//   ],
//   variable: "--font-overused",
// });

export default function RootLayout({ children }) {
  return (
    <html lang="fr" className="scroll-smooth">
      <body
        className={`min-h-screen flex flex-col items-center justify-start gap-[42vh] mx-[4vw] overflow-x-hidden scroll-smooth custom-scrollbar`}
      >
        <div className="texture-overlay" />
        {children}
      </body>
    </html>
  );
}
