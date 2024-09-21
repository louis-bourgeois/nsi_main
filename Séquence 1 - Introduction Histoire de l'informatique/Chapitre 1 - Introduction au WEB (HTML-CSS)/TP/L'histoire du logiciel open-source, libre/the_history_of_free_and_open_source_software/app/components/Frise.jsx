"use client";
import { motion, useScroll, useSpring, useTransform } from "framer-motion";
import { useEffect, useRef, useState } from "react";
import Card from "./Card";

const events = [
  {
    id: "gnu",
    date: 1983,
    title: "Projet GNU",
    subtitle: "Richard Stallman lance le projet GNU",
    description:
      "Le projet GNU, initié par Richard Stallman, vise à créer un système d'exploitation entièrement libre. C'est une étape cruciale dans l'histoire du logiciel libre, posant les bases éthiques et pratiques du mouvement.",
    impact:
      "Le projet GNU a établi les fondements philosophiques et techniques du logiciel libre, influençant profondément la culture du développement logiciel.",
    image: "/pngegg (1).png",
  },
  {
    id: "linux",
    date: 1991,
    title: "Noyau Linux",
    subtitle: "Linus Torvalds publie la première version du noyau Linux",
    description:
      "Linus Torvalds développe le noyau Linux, qui, combiné aux outils GNU, forme un système d'exploitation complet. Cet événement marque le début de la popularisation des systèmes d'exploitation libres.",
    impact:
      "Linux est devenu le noyau le plus utilisé au monde, propulsant des millions de serveurs, d'appareils embarqués et de smartphones Android.",
    image: "/image-4.webp",
  },
  {
    id: "netscape",
    date: 1998,
    title: "Netscape Open Source",
    subtitle: "Netscape publie le code source de son navigateur",
    description:
      "Netscape prend la décision historique de publier le code source de son navigateur. Cette action conduit à la création du projet Mozilla et influence grandement le mouvement open source dans le domaine des navigateurs web.",
    impact:
      "Cette décision a donné naissance à Firefox et a contribué à la standardisation du web, promouvant l'innovation et la concurrence dans le domaine des navigateurs.",
    image: "/net7.jpg",
  },
  {
    id: "blender",
    date: 2002,
    title: "Blender devient Open Source",
    subtitle: "La Fondation Blender est créée pour rendre Blender open source",
    description:
      "Après une campagne de financement réussie, Blender devient un logiciel open source. C'est un moment crucial pour l'industrie de l'animation 3D et des effets visuels.",
    impact:
      "Blender est devenu l'un des logiciels d'animation 3D et de VFX les plus populaires, démocratisant l'accès aux outils de création 3D de haute qualité.",
    image: "/maxresdefault.jpg",
  },
  {
    id: "firefox",
    date: 2004,
    title: "Firefox",
    subtitle: "Mozilla lance le navigateur Firefox",
    description:
      "Mozilla lance Firefox, un navigateur web libre et open-source. Firefox devient rapidement populaire, offrant une alternative viable aux navigateurs propriétaires et promouvant les standards du web ouvert.",
    impact:
      "Firefox a brisé le monopole d'Internet Explorer, encourageant l'innovation web et l'adhésion aux standards ouverts.",
    image: "/firefox.png",
  },
  {
    id: "chrome",
    date: 2008,
    title: "Projet Chromium",
    subtitle: "Google lance le projet Chromium",
    description:
      "Google initie le projet Chromium, la base open-source du navigateur Chrome. Ce projet révolutionne la performance des navigateurs et influence considérablement le développement web moderne.",
    impact:
      "Chromium a établi de nouvelles normes de performance pour les navigateurs et est devenu la base de nombreux autres navigateurs, dont Microsoft Edge.",
    image: "/chromium.png",
  },
  {
    id: "react",
    date: 2013,
    title: "Facebook s'investit dans l'Open Source",
    subtitle: "Facebook lance React et s'engage dans l'open source",
    description:
      "Facebook publie React, une bibliothèque JavaScript pour la construction d'interfaces utilisateur. Cette décision marque le début d'un engagement important de Facebook dans l'open source.",
    impact:
      "React a révolutionné le développement web frontend. De plus, Facebook a continué à contribuer à l'open source avec des projets comme React Native, GraphQL, et plus récemment, le modèle de langage Llama. Ce site lui-même a été créé avec React et Next.js, tous deux open source.",
    image: "/maxresdefault (1).jpg",
  },
  {
    id: "vscode",
    date: 2014,
    title: "Visual Studio Code",
    subtitle: "Microsoft lance VS Code",
    description:
      "Microsoft surprend la communauté en lançant Visual Studio Code, un éditeur de code open-source. Cet événement marque un changement significatif dans l'approche de Microsoft envers le logiciel libre et open-source.",
    impact:
      "VS Code est devenu l'un des éditeurs de code les plus populaires, démontrant l'engagement croissant des grandes entreprises envers l'open source.",
    image: "/vscode.png",
  },
  {
    id: "llama",
    date: 2022,
    title: "Llama",
    subtitle: "Meta (Facebook) publie Llama en open source",
    description:
      "Meta (anciennement Facebook) publie Llama, un grand modèle de langage, en open source. Cette décision permet à la communauté de recherche et de développement d'accéder à un modèle de pointe pour l'IA générative.",
    impact:
      "La publication de Llama en open source a démocratisé l'accès aux grands modèles de langage, stimulant l'innovation dans le domaine de l'IA et ouvrant de nouvelles possibilités pour la recherche et les applications.",
    image: "/llama.png",
  },
];

export default function Frise() {
  const [currentDate, setCurrentDate] = useState(1980);
  const containerRef = useRef(null);
  const { scrollYProgress } = useScroll({
    target: containerRef,
    offset: ["start start", "end end"],
  });

  const currentEventIndex = useTransform(
    scrollYProgress,
    [0, 1],
    [0, events.length - 1]
  );

  const smoothProgress = useSpring(scrollYProgress, {
    stiffness: 20,
    damping: 30,
    restDelta: 0.001,
  });

  const titleScale = useTransform(scrollYProgress, [0, 0.1], [1, 0.8]);

  useEffect(() => {
    const unsubscribe = currentEventIndex.onChange((v) => {
      const index = Math.min(Math.floor(v), events.length - 1);
      if (events[index]) {
        setCurrentDate(events[index].date);
      }
    });
    return () => unsubscribe();
  }, [currentEventIndex]);

  return (
    <section
      ref={containerRef}
      className="w-full min-h-screen flex flex-col justify-start items-center py-20"
    >
      <motion.h2
        style={{
          scale: titleScale,
          position: "sticky",
          top: "5vh",
          zIndex: 20,
        }}
        className="font-bold text-4xl mb-[5vh] text-center bg-white bg-opacity-80 px-6 py-2 rounded-full shadow-lg"
      >
        Un plongeon à travers l'internet libre
      </motion.h2>

      <motion.div
        style={{ position: "sticky", top: "20vh" }}
        className="w-full flex justify-center items-center mb-10 z-20"
      >
        <motion.div
          style={{ scale: smoothProgress }}
          className="text-6xl font-bold bg-white bg-opacity-80 px-6 py-2 rounded-full shadow-lg"
        >
          {currentDate}
        </motion.div>
      </motion.div>

      <div className="relative w-full flex justify-center items-start">
        <motion.div
          style={{ scaleY: smoothProgress }}
          className="fixed left-1/2 top-0 bottom-0 w-2 rounded-full bg-black shadow-lg origin-top z-10"
        />

        <div className="w-full max-w-[50vw]">
          {events.map((event, index) => (
            <motion.div
              key={event.id}
              id={event.id}
              style={{
                opacity: useTransform(
                  currentEventIndex,
                  [index - 1.5, index - 1, index, index + 0.5, index + 1],
                  [0, 1, 1, 1, 0]
                ),
                scale: useTransform(
                  currentEventIndex,
                  [index - 1, index, index + 1],
                  [0.9, 1, 0.9]
                ),
              }}
              className="mb-[150vh] first:mt-[75vh]"
            >
              <motion.div
                style={{
                  position: useTransform(currentEventIndex, (value) =>
                    value >= index - 0.75 && value <= index + 0.75
                      ? "sticky"
                      : "relative"
                  ),
                  top: "50%",
                  translateY: "-50%",
                }}
              >
                <Card
                  id={event.id}
                  title={event.title}
                  subtitle={event.subtitle}
                  imageSrc={event.image}
                  date={event.date}
                  description={event.description}
                  impact={event.impact}
                />
              </motion.div>
            </motion.div>
          ))}
        </div>
      </div>
    </section>
  );
}
