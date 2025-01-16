"use client";
import { motion, useScroll, useSpring, useTransform } from "framer-motion";
import { useEffect, useRef, useState } from "react";
import Card from "./Card";

const events = [
  {
    id: "unix",
    date: 1969,
    title: "Création d'Unix",
    subtitle:
      "Ken Thompson, Dennis Ritchie et l'équipe des Bell Labs créent Unix",
    description:
      "Unix est développé aux Bell Labs par Ken Thompson, Dennis Ritchie et d'autres. C'est l'un des systèmes d'exploitation les plus influents, ayant un impact profond sur les systèmes modernes, notamment Linux et macOS.",
    details:
      "Unix a été créé en 1969 (et publié pour le grand public en 1971) dans le cadre d'une initiative visant à construire un système d'exploitation multi-utilisateur, portable et flexible. Connu pour son approche simple mais puissante, Unix introduit des concepts fondamentaux comme les fichiers en tant que flux d'octets, les pipelines de commandes, et les permissions de fichiers. Il est écrit principalement en C, un langage développé par Dennis Ritchie spécifiquement pour Unix, ce qui le rend plus portable entre différentes machines. Unix a inspiré de nombreuses variantes et systèmes d'exploitation modernes, dont BSD (Berkeley Software Distribution), Linux, et macOS. Son modèle de développement influencé par la modularité et la philosophie des petits outils interconnectés a façonné la culture du développement logiciel moderne.",
    image: "/unix.jpg",
    additionalImages: ["/unix-terminal.png", "/unix-creators.jpg"],
  },
  {
    id: "gnu",
    date: 1983,
    title: "Projet GNU",
    subtitle: "Richard Stallman lance le projet GNU",
    description:
      "Le projet GNU, initié par Richard Stallman, vise à créer un système d'exploitation entièrement libre. C'est une étape cruciale dans l'histoire du logiciel libre, posant les bases éthiques et pratiques du mouvement.",
    details:
      "Le projet GNU (GNU's Not Unix) a été lancé pour offrir un système d'exploitation libre et gratuit, en réaction aux restrictions imposées par les logiciels propriétaires. Richard Stallman a aussi créé la Free Software Foundation (FSF) pour promouvoir et défendre les libertés des utilisateurs de logiciels. La création de la licence GNU GPL (General Public License) est un autre moment important, car elle garantit que les logiciels dérivés restent libres. Le projet a également influencé la philosophie des hackers et des développeurs en prônant la collaboration et la transparence.",
    image: "/gnu.png",
    additionalImages: ["/richard-stallman.jpg", "/gnu-logo.png"],
  },
  {
    id: "linux",
    date: 1991,
    title: "Noyau Linux",
    subtitle: "Linus Torvalds publie la première version du noyau Linux",
    description:
      "Linus Torvalds développe le noyau Linux, qui, combiné aux outils GNU, forme un système d'exploitation complet. Cet événement marque le début de la popularisation des systèmes d'exploitation libres.",
    details:
      "Torvalds a initialement développé Linux comme un projet personnel pour créer une alternative libre aux systèmes UNIX propriétaires. Le noyau a rapidement attiré l'attention de la communauté open source, qui a commencé à contribuer au projet. Associé aux outils GNU, il forme la base de nombreuses distributions (comme Debian, Ubuntu, Red Hat), popularisant les systèmes d'exploitation basés sur Linux. Aujourd'hui, Linux alimente des millions de serveurs, superordinateurs, et est le noyau dominant des systèmes Android.",
    image: "/linux.webp",
    additionalImages: ["/linus-torvalds.jpg", "/linux-distributions.png"],
  },
  {
    id: "netscape",
    date: 1998,
    title: "Netscape Open Source",
    subtitle: "Netscape publie le code source de son navigateur",
    description:
      "Netscape prend la décision historique de publier le code source de son navigateur. Cette action conduit à la création du projet Mozilla et influence grandement le mouvement open source dans le domaine des navigateurs web.",
    details:
      "Netscape a fait face à une concurrence intense avec l'Internet Explorer de Microsoft, qui dominait le marché des navigateurs. En publiant son code source, Netscape espérait revitaliser le développement de son navigateur via une communauté de développeurs. Cela a conduit à la création du projet Mozilla, dont l'une des plus grandes réussites a été le développement de Firefox. Cette initiative a permis de fixer des normes pour les navigateurs et a favorisé la concurrence, incitant à l'adoption de standards ouverts comme HTML, CSS et JavaScript.",
    image: "/netscape.jpg",
    additionalImages: ["/netscape-navigator.jpg", "/mozilla-project.png"],
  },
  {
    id: "blender",
    date: 2002,
    title: "Blender devient Open Source",
    subtitle: "La Fondation Blender est créée pour rendre Blender open source",
    description:
      "Après une campagne de financement réussie, Blender devient un logiciel open source. C'est un moment crucial pour l'industrie de l'animation 3D et des effets visuels.",
    details:
      "Blender, à l'origine un logiciel propriétaire développé par NeoGeo, une société néerlandaise, a été rendu open source après une levée de fonds communautaire. La Fondation Blender, sous la direction de Ton Roosendaal, a permis de maintenir le développement actif de Blender et de le transformer en l'un des outils d'animation 3D les plus utilisés. Blender est largement apprécié pour ses fonctionnalités puissantes, son absence de frais de licence, et a contribué à rendre les outils d'animation 3D accessibles à une large audience, y compris les créateurs indépendants.",
    image: "/blender.jpg",
    additionalImages: ["/blender-interface.jpeg", "/blender-animation.jpg"],
  },
  {
    id: "firefox",
    date: 2004,
    title: "Firefox",
    subtitle: "Mozilla lance le navigateur Firefox",
    description:
      "Mozilla lance Firefox, un navigateur web libre et open-source. Firefox devient rapidement populaire, offrant une alternative viable aux navigateurs propriétaires et promouvant les standards du web ouvert.",
    details:
      "Mozilla Firefox, initialement appelé Phoenix, a été lancé pour contrecarrer la domination d'Internet Explorer, qui contrôlait plus de 90 % du marché. Firefox a introduit des fonctionnalités innovantes comme la navigation par onglets, les extensions et une meilleure sécurité, ce qui a rapidement attiré les utilisateurs. Il a joué un rôle clé dans la promotion des standards ouverts du web, contribuant à l'émergence d'un internet plus diversifié et compétitif. La montée de Firefox a encouragé Microsoft à réagir en améliorant Internet Explorer.",
    image: "/firefox.png",
    additionalImages: ["/firefox-interface.png", "/firefox-logo-evolution.png"],
  },
  {
    id: "chrome",
    date: 2008,
    title: "Projet Chromium",
    subtitle: "Google lance le projet Chromium",
    description:
      "Google initie le projet Chromium, la base open-source du navigateur Chrome. Ce projet révolutionne la performance des navigateurs et influence considérablement le développement web moderne.",
    details:
      "Le projet Chromium est conçu pour être un navigateur léger, rapide et moderne, basé sur WebKit (remplacé plus tard par Blink). Le succès de Chrome repose sur sa rapidité, son interface minimaliste et son architecture multi-processus, qui améliore la stabilité et la sécurité. Chrome est rapidement devenu le navigateur le plus utilisé au monde et sa base open-source, Chromium, a été adoptée par d'autres projets tels que Microsoft Edge, Brave et Opera. Chromium a également favorisé l'adoption de nouvelles technologies comme le moteur JavaScript V8.",
    image: "/chromium.png",
    additionalImages: ["/chrome-browser.png", "/chromium-architecture.png"],
  },
  {
    id: "react",
    date: 2013,
    title: "Facebook s'investit dans l'Open Source",
    subtitle: "Facebook lance React et s'engage dans l'open source",
    description:
      "Facebook publie React, une bibliothèque JavaScript pour la construction d'interfaces utilisateur. Cette décision marque le début d'un engagement important de Facebook dans l'open source.",
    details:
      "React a introduit une approche innovante dans le développement web frontend avec un modèle basé sur des composants réutilisables et la gestion efficace des changements via un DOM virtuel. Ce paradigme a transformé la manière dont les développeurs construisent des interfaces utilisateur interactives et performantes. React est devenu un standard dans l'industrie du développement web et a conduit à une adoption massive dans la création de sites et d'applications. D'autres contributions open source importantes de Facebook incluent GraphQL, React Native et PyTorch.",
    image: "/react.jpg",
    additionalImages: ["/react-code.png", "/react-ecosystem.png"],
  },
  {
    id: "vscode",
    date: 2014,
    title: "Visual Studio Code",
    subtitle: "Microsoft lance VS Code",
    description:
      "Microsoft surprend la communauté en lançant Visual Studio Code, un éditeur de code open-source. Cet événement marque un changement significatif dans l'approche de Microsoft envers le logiciel libre et open-source.",
    details:
      "Visual Studio Code (VS Code) a été une surprise majeure venant de Microsoft, une entreprise autrefois réticente à l'idée de l'open source. VS Code, avec ses fonctionnalités robustes, son extensibilité via des plugins, et sa légèreté par rapport aux autres IDE (environnements de développement intégrés), a rapidement gagné en popularité. Il est utilisé par des millions de développeurs dans le monde entier et a aidé Microsoft à améliorer son image dans la communauté open source, renforçant leur stratégie basée sur l'intégration des services cloud et l'interopérabilité.",
    image: "/vscode.png",
    additionalImages: ["/vscode-interface.png", "/vscode-extensions.png"],
  },
  {
    id: "llama",
    date: 2022,
    title: "Llama",
    subtitle: "Meta (Facebook) publie Llama en open source",
    description:
      "Meta (anciennement Facebook) publie Llama, un grand modèle de langage, en open source. Cette décision permet à la communauté de recherche et de développement d'accéder à un modèle de pointe pour l'IA générative.",
    details:
      "La publication de Llama (Large Language Model Meta AI) a marqué une étape importante dans l'accès démocratisé aux grands modèles de langage (LLMs). Contrairement à d'autres modèles propriétaires comme GPT-4o, Llama est librement accessible à des fins de recherche et de développement. Cela a stimulé la créativité dans le domaine de l'IA, permettant à des chercheurs indépendants et à des petites entreprises d'explorer de nouveaux cas d'utilisation, d'améliorer la technologie existante, et de contribuer à une IA plus équitable.",
    image: "/llama.png",
    additionalImages: ["/llama-architecture.png", "/meta-commitment.png"],
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
    stiffness: 100,
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

    const handleClick = (e) => {
      const target = e.target.closest("a[href^='#']");
      if (target) {
        e.preventDefault();
        const id = target.getAttribute("href").slice(1);
        const element = document.getElementById(id);
        if (element) {
          element.scrollIntoView({
            behavior: "smooth",
            block: "center",
          });
        }
      }
    };

    document.addEventListener("click", handleClick);

    return () => {
      unsubscribe();
      document.removeEventListener("click", handleClick);
    };
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
        Un plongeon à travers l&apos;internet libre
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
          className="fixed left-1/2 top-0 bottom-0 w-2 rounded-full bg-black shadow-lg origin-top"
        />

        <div className="w-full max-w-[50vw]">
          {events.map((event, index) => {
            // eslint-disable-next-line react-hooks/rules-of-hooks
            const opacity = useTransform(
              currentEventIndex,
              [index - 1.5, index - 1, index, index + 0.5, index + 1],
              [0, 1, 1, 1, 0]
            );
            // eslint-disable-next-line react-hooks/rules-of-hooks
            const scale = useTransform(
              currentEventIndex,
              [index - 1, index, index + 1],
              [0.9, 1, 0.9]
            );

            return (
              <motion.div
                key={event.id}
                style={{
                  opacity,
                  scale,
                }}
                className="mb-[150vh] first:mt-[75vh]"
              >
                <div className="absolute top-1/2 left-0 transform -translate-y-1/2" />
                <motion.div
                  style={{
                    position: "sticky",
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
                    details={event.details}
                    additionalImages={event.additionalImages}
                  />
                </motion.div>
              </motion.div>
            );
          })}
        </div>
      </div>
      <div className="text-left font-light z-10 bg-black text-white px-10 py-3 rounded-xl">
        <p>
          Certaines animations ont été réalisées à l&apos;aide (de l&apos;api)
          de Claude 3.5 Sonnet et de Gpt-4o-latest (animations framer-motion,
          n&apos;étant pas à l&apos;aise avec cette librairie qui fait gagner du
          temps). Cela permet de gagner du temps et d&apos;améliorer mon niveau
          en prompt-engineering;
        </p>
        <p>
          Certaines phrases des biographies ont été reformulées, améliorées à
          l&apos;aide de chat Gpt-4o;
        </p>
        <p>
          L&apos;ensemble des images sur ce site ont été publiées de manière à
          respecter les licences (attributions...);
        </p>
        <p>
          Certains bugs n&apos;ont pas eu le temps d&apos;être résolus
          (problèmes de scroll sur les anchor points, problèmes de
          positionnement lors du passage de sticky à relative sur la définition
          de l&apos;open source, hover sur les cards).
        </p>
      </div>
    </section>
  );
}
