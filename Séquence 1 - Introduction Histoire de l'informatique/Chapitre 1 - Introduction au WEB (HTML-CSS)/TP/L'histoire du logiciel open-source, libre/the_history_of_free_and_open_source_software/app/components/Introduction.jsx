"use client";
import { useEffect, useRef, useState } from "react";

const Introduction = () => {
  const containerRef = useRef(null);
  const text =
    "Les logiciels libres ou open source sont des programmes dont le code source, ouvert à tous, garantit la liberté d'utilisation, de modification, et de partage. Favorisant ainsi une innovation collaborative et une transparence qui enrichissent l'écosystème technologique.";

  const words = text.split(" ");
  const [isSticky, setIsSticky] = useState(true);

  useEffect(() => {
    const container = containerRef.current;

    const handleScroll = () => {
      if (!container) return;

      const wordElements = container.querySelectorAll(".word");
      const scrollTop = window.scrollY;
      const containerOffsetTop = container.offsetTop;
      const containerHeight = container.scrollHeight;
      const windowHeight = window.innerHeight;

      const startRevealAt = containerOffsetTop - windowHeight * 0.5;
      const endRevealAt = containerOffsetTop + containerHeight;

      const progress = Math.min(
        Math.max(
          (scrollTop - startRevealAt) / (endRevealAt - startRevealAt),
          0
        ),
        1
      );

      const wordsToShow = Math.floor(progress * words.length);

      wordElements.forEach((word, index) => {
        word.style.opacity = index < wordsToShow ? "1" : "0";
        word.style.pointerEvents = index < wordsToShow ? "auto" : "none"; // Enable click only on visible words
      });

      setIsSticky(progress < 1);
    };

    window.addEventListener("scroll", handleScroll);
    return () => window.removeEventListener("scroll", handleScroll);
  }, [words.length]);

  return (
    <section
      className={`${
        isSticky ? "sticky-transition" : "non-sticky"
      } min-h-screen flex items-center transition-all pointer-events-none`}
    >
      <div
        className={`relative transition-all w-full ${
          isSticky ? "h-[200vh]" : "h-auto"
        } flex items-left justify-start`}
      >
        <div
          id="definition"
          ref={containerRef}
          className="w-[65%] text-6xl font-bold text-left leading-snug pointer-events-auto"
        >
          {words.map((word, index) => (
            <span
              key={index}
              className="word inline-block opacity-0 transition-opacity duration-500 ease-in-out pointer-events-none"
              style={{ marginRight: "0.5rem" }} // Adding space between words
            >
              {word}
            </span>
          ))}
        </div>
      </div>
    </section>
  );
};

export default Introduction;
