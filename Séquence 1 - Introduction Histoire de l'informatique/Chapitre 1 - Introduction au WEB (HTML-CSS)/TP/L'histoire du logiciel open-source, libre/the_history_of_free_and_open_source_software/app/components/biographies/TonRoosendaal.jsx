"use client";
import { motion, useAnimation } from "framer-motion";
import Image from "next/image";
import React, { useEffect } from "react";
import { useInView } from "react-intersection-observer";

const TonRoosendaal = () => {
  const controls = useAnimation();
  const [inView] = useInView({
    triggerOnce: true,
    threshold: 0.1,
  });

  useEffect(() => {
    if (inView) {
      controls.start("visible");
    }
  }, [controls, inView]);

  const fadeIn = {
    hidden: { opacity: 0, y: 50 },
    visible: {
      opacity: 1,
      y: 0,
      transition: { duration: 0.8, ease: "easeOut" },
    },
  };

  const staggerChildren = {
    hidden: { opacity: 0 },
    visible: {
      opacity: 1,
      transition: {
        staggerChildren: 0.2,
      },
    },
  };

  return (
    <div className="min-h-screen bg-gradient-to-b py-16 px-4 sm:px-6 lg:px-8">
      <motion.div
        className="max-w-7xl mx-auto"
        initial="hidden"
        animate="visible"
        variants={staggerChildren}
      >
        <motion.h1
          className="text-6xl font-extrabold text-center mb-16 text-[#007AFF]"
          variants={fadeIn}
        >
          Ton Roosendaal
        </motion.h1>

        <motion.div
          className="bg-white bg-opacity-80 backdrop-filter backdrop-blur-lg rounded-3xl shadow-2xl p-8 mb-16 flex flex-col md:flex-row items-center"
          variants={fadeIn}
        >
          <div className="md:w-1/2 mb-8 md:mb-0">
            <Image
              src="/ton-roosendaal.jpg"
              alt="Ton Roosendaal"
              width={600}
              height={400}
              className="rounded-2xl shadow-lg"
            />
          </div>
          <div className="md:w-1/2 md:pl-8">
            <h2 className="text-3xl font-bold mb-4 text-[#007AFF]">
              Le visionnaire derrière Blender
            </h2>
            <p className="text-xl text-gray-700 leading-relaxed">
              Ton Roosendaal, né le 20 mars 1960, est le créateur du logiciel
              libre Blender et l{"'"}actuel président de la fondation Blender.
              Son travail a révolutionné l{"'"}industrie de l{"'"}animation 3D
              en rendant les outils professionnels accessibles à tous.
            </p>
          </div>
        </motion.div>

        <motion.div
          className="bg-white bg-opacity-90 backdrop-filter backdrop-blur-lg rounded-3xl shadow-2xl p-8 mb-16"
          variants={fadeIn}
        >
          <h2 className="text-3xl font-bold mb-6 text-[#007AFF]">
            Réalisations majeures
          </h2>
          <motion.ul
            className="grid grid-cols-1 md:grid-cols-2 gap-6"
            variants={staggerChildren}
          >
            {[
              "Création de Blender, logiciel 3D open source",
              "Fondation de l'institut Blender en 2007",
              "Production de courts-métrages révolutionnaires",
              "Promotion de l'open source dans l'industrie créative",
            ].map((achievement, index) => (
              <motion.li
                key={index}
                variants={fadeIn}
                className="bg-indigo-100 rounded-xl p-4 text-lg text-indigo-900 shadow-md"
              >
                {achievement}
              </motion.li>
            ))}
          </motion.ul>
        </motion.div>

        <motion.div
          className="bg-white bg-opacity-80 backdrop-filter backdrop-blur-lg rounded-3xl shadow-2xl p-8 mb-16"
          variants={fadeIn}
        >
          <h2 className="text-3xl font-bold mb-6 text-[#007AFF]">
            Parcours professionnel
          </h2>
          <div className="space-y-6">
            <p className="text-xl text-gray-700 leading-relaxed">
              La carrière de Roosendaal a débuté avec des études en design
              industriel à Eindhoven. Il a ensuite cofondé NeoGeo, qui est
              rapidement devenue l{"'"}une des plus grandes sociétés d{"'"}
              animation 3D des Pays-Bas dans les années 1990.
            </p>
            <p className="text-xl text-gray-700 leading-relaxed">
              En 1998, sa passion pour l{"'"}animation 3D l{"'"}a conduit à
              fonder Not a Number (NaN) dans le but de développer et
              commercialiser Blender. Malgré la fermeture de NaN, Roosendaal a
              persévéré et créé la Blender Foundation en 2002, réussissant l
              {"'"}exploit de libérer le code source de Blender.
            </p>
          </div>
        </motion.div>

        <motion.div
          className="bg-white bg-opacity-80 backdrop-filter backdrop-blur-lg rounded-3xl shadow-2xl p-8 mb-16"
          variants={fadeIn}
        >
          <h2 className="text-3xl font-bold mb-6 text-[#007AFF]">
            Projets emblématiques
          </h2>
          <div className="grid grid-cols-1 md:grid-cols-2 gap-8">
            {[
              { title: "Elephants Dream", year: 2006 },
              { title: "Big Buck Bunny", year: 2008 },
              { title: "Sintel", year: 2010 },
              { title: "Tears of Steel", year: 2012 },
            ].map((project, index) => (
              <motion.div
                key={index}
                variants={fadeIn}
                className="bg-indigo-100 rounded-xl p-6 shadow-lg"
              >
                <h3 className="text-2xl font-semibold mb-2 text-[#007AFF]">
                  {project.title}
                </h3>
                <p className="text-lg text-indigo-600">{project.year}</p>
              </motion.div>
            ))}
          </div>
        </motion.div>

        <motion.div
          className="bg-white bg-opacity-80 backdrop-filter backdrop-blur-lg rounded-3xl shadow-2xl p-8"
          variants={fadeIn}
        >
          <h2 className="text-3xl font-bold mb-6 text-[#007AFF]">
            Reconnaissance
          </h2>
          <p className="text-xl text-gray-700 leading-relaxed">
            Le travail de Ton Roosendaal a été reconnu en 2009 lorsqu{"'"}il a
            reçu le titre honorifique de docteur de la Leeds Metropolitan
            University. Cette distinction souligne l{"'"}impact considérable de
            ses contributions dans le domaine de l{"'"}animation 3D et du
            logiciel libre.
          </p>
        </motion.div>
      </motion.div>
    </div>
  );
};

export default TonRoosendaal;
