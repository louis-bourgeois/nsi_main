"use client";
import { motion, useAnimation } from "framer-motion";
import Image from "next/image";
import Link from "next/link";
import React, { useEffect } from "react";
import { useInView } from "react-intersection-observer";

const LinusTorvalds = () => {
  const controls = useAnimation();
  const { inView } = useInView({
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
          Linus Torvalds
        </motion.h1>

        <motion.div
          className="bg-white bg-opacity-80 backdrop-filter backdrop-blur-lg rounded-3xl shadow-2xl p-8 mb-16 flex flex-col md:flex-row items-center"
          variants={fadeIn}
        >
          <div className="md:w-1/2 mb-8 md:mb-0 relative">
            <Image
              src="/linus-torvalds_02.jpg"
              alt="Linus Torvalds"
              width={600}
              height={400}
              className="rounded-2xl shadow-lg"
            />
            <Link
              href="https://www.deviantart.com/glenn1794"
              className="absolute bottom-5 left-5 bg-white px-2 rounded-full"
            >
              Attributions : Glenn1794
            </Link>
          </div>
          <div className="md:w-1/2 md:pl-8">
            <h2 className="text-3xl font-bold mb-4 text-[#007AFF]">
              Le créateur de Linux
            </h2>
            <p className="text-xl text-gray-700 leading-relaxed">
              Né le 28 décembre 1969 à Helsinki, Finlande, Linus Benedict
              Torvalds est un informaticien américano-finlandais mondialement
              connu pour avoir créé le noyau Linux en 1991, à seulement 21 ans.
              Il continue de diriger le développement de Linux, étant considéré
              comme le {'"'}dictateur bienveillant à vie{'"'} du projet.
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
              "Création du noyau Linux en 1991",
              "Développement du logiciel de gestion de versions Git",
              "Création du logiciel Subsurface pour la plongée",
              "Lauréat du prix Millennium Technology en 2012",
            ].map((achievement, index) => (
              <motion.li
                key={index}
                variants={fadeIn}
                className="bg-blue-100 rounded-xl p-4 text-lg text-[#007AFF] shadow-md"
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
              Linus Torvalds a commencé sa carrière en informatique très jeune.
              Il a étudié à l{"'"}université d{"'"}Helsinki de 1988 à 1996, où
              il a obtenu un master en informatique. C{"'"}est durant ses études
              qu{"'"}il a commencé à développer le noyau Linux, inspiré par le
              système Minix.
            </p>
            <p className="text-xl text-gray-700 leading-relaxed">
              Après ses études, il a travaillé chez Transmeta de 1997 à 2003,
              puis a rejoint l{"'"}Open Source Development Labs. Depuis 2007, il
              travaille pour la Linux Foundation, se consacrant à temps plein au
              développement du noyau Linux.
            </p>
          </div>
        </motion.div>

        <motion.div
          className="bg-white bg-opacity-80 backdrop-filter backdrop-blur-lg rounded-3xl shadow-2xl p-8 mb-16"
          variants={fadeIn}
        >
          <h2 className="text-3xl font-bold mb-6 text-[#007AFF]">
            Contributions majeures
          </h2>
          <div className="grid grid-cols-1 md:grid-cols-2 gap-8">
            {[
              { title: "Linux", year: 1991 },
              { title: "Git", year: 2005 },
              { title: "Subsurface", year: 2011 },
              { title: "Travail continu sur Linux", year: "1991 - présent" },
            ].map((project, index) => (
              <motion.div
                key={index}
                variants={fadeIn}
                className="bg-blue-100 rounded-xl p-6 shadow-lg"
              >
                <h3 className="text-2xl font-semibold mb-2 text-[#007AFF]">
                  {project.title}
                </h3>
                <p className="text-lg text-blue-600">{project.year}</p>
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
            Le travail de Linus Torvalds a été reconnu par de nombreuses
            distinctions. En 2012, il a reçu le prix Millennium Technology de l
            {"'"}académie de technologie de Finlande pour son travail sur Linux.
            En 2014, il a reçu le prix IEEE Computer Society Computer Pioneer
            Award. Son impact sur l{"'"}industrie du logiciel et l{"'"}open
            source est incommensurable.
          </p>
        </motion.div>
      </motion.div>
    </div>
  );
};

export default LinusTorvalds;
