import { AnimatePresence, motion } from "framer-motion";
import Image from "next/legacy/image";
import { useState } from "react";

export default function Card({
  id,
  imageSrc,
  title,
  subtitle,
  date,
  description,
  details,
  additionalImages = [],
}) {
  const [isHovered, setIsHovered] = useState(false);

  return (
    <motion.div
      id={id}
      whileHover={{ scale: 1.05, zIndex: 30 }}
      onHoverStart={() => setIsHovered(true)}
      onHoverEnd={() => setIsHovered(false)}
      transition={{ duration: 0.3 }}
      className="w-full cursor-pointer flex overflow-hidden flex-col justify-start rounded-[24px] shadow-lg bg-white relative"
    >
      <div className="h-[55vh] relative overflow-hidden">
        <Image src={imageSrc} layout="fill" objectFit="cover" alt={title} />
      </div>
      <motion.div
        className="p-5"
        initial={{ opacity: 0, y: 20 }}
        animate={{ opacity: 1, y: 0 }}
        transition={{ duration: 0.3, delay: 0.1 }}
      >
        <h3 className="font-bold text-3xl mb-2">{title}</h3>
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
            className="absolute inset-0 bg-white bg-opacity-95 p-5 overflow-auto custom-scrollbar"
          >
            <h3 className="font-bold text-3xl mb-2">{title}</h3>
            <p className="text-gray-800 mb-4 text-xl">{description}</p>
            <h4 className="font-semibold text-3xl mb-2">Impact et détails</h4>
            <p className="text-gray-800 text-lg mb-4">{details}</p>

            {additionalImages && additionalImages.length > 0 && (
              <div className="mt-4">
                <h4 className="font-semibold text-2xl mb-2">
                  Images supplémentaires
                </h4>
                <div className="flex justify-center items-center space-x-4">
                  {additionalImages.slice(0, 2).map((img, index) => (
                    <div
                      key={index}
                      className="relative min-h-[400px] max-h-[500px] w-1/2"
                    >
                      <Image
                        src={img}
                        layout="fill"
                        objectFit="cover"
                        className="rounded-md"
                        alt={`Additional image ${index + 1}`}
                      />
                    </div>
                  ))}
                </div>
              </div>
            )}
          </motion.div>
        )}
      </AnimatePresence>
    </motion.div>
  );
}
