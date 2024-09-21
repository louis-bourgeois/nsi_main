import { AnimatePresence, motion } from "framer-motion";
import Image from "next/image";
import { useState } from "react";

export default function Card({
  id,
  imageSrc,
  title,
  subtitle,
  date,
  description,
  impact,
}) {
  const [isHovered, setIsHovered] = useState(false);

  return (
    <motion.div
      whileHover={{ scale: 1.05, zIndex: 30 }}
      onHoverStart={() => setIsHovered(true)}
      onHoverEnd={() => setIsHovered(false)}
      transition={{ duration: 0.3 }}
      className="w-full cursor-pointer flex overflow-hidden flex-col justify-start rounded-[24px] shadow-lg bg-white relative"
    >
      <div className="h-[50vh] relative overflow-hidden">
        <Image src={imageSrc} layout="fill" objectFit="cover" alt={title} />
      </div>
      <motion.div
        className="p-5"
        initial={{ opacity: 0, y: 20 }}
        animate={{ opacity: 1, y: 0 }}
        transition={{ duration: 0.3, delay: 0.1 }}
      >
        <h3 id={id} className="font-bold text-3xl mb-2">
          {title}
        </h3>
        <h4 className="text-xl text-gray-600 mb-2">{date}</h4>
        <p className="text-gray-700">{subtitle}</p>
      </motion.div>

      <AnimatePresence>
        {isHovered && (
          <motion.div
            initial={{ opacity: 0, y: 20 }}
            animate={{ opacity: 1, y: 0 }}
            exit={{ opacity: 0, y: 20 }}
            transition={{ duration: 0.2 }}
            className="absolute inset-0 bg-white bg-opacity-95 p-5 overflow-auto"
          >
            <h3 className="font-bold text-2xl mb-2">{title}</h3>
            <p className="text-gray-800 mb-4">{description}</p>
            <h4 className="font-semibold text-xl mb-2">Impact</h4>
            <p className="text-gray-800">{impact}</p>
          </motion.div>
        )}
      </AnimatePresence>
    </motion.div>
  );
}
