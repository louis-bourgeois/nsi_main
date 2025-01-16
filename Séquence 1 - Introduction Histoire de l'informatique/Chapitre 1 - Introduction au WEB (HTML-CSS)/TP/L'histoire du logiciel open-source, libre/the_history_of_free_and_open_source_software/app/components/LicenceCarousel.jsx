"use client";
import "swiper/css";
import "swiper/css/navigation";
import "swiper/css/pagination";
import { Autoplay, Navigation, Pagination } from "swiper/modules";
import { Swiper, SwiperSlide } from "swiper/react";

const licenses = [
  {
    name: "MIT License",
    description:
      "Une licence permissive qui offre peu de restrictions. Elle permet la réutilisation du code, même dans des projets propriétaires.",
  },
  {
    name: "GNU GPL",
    description:
      "La GPL (General Public License) exige que tout projet dérivé du code soit également open-source sous la même licence.",
  },
  {
    name: "Apache License 2.0",
    description:
      "Permet aux utilisateurs d'utiliser le logiciel pour n'importe quel usage tout en fournissant des protections contre les poursuites en violation de brevets.",
  },
  {
    name: "BSD License",
    description:
      "Une licence permissive similaire à MIT mais avec quelques différences subtiles.",
  },
];

export default function LicenceCarousel() {
  return (
    <section
      className="w-full flex flex-col items-center gap-[5vh]"
      id="licences"
    >
      <h2 className="font-bold cursor-pointer hover:scale-105 transition-transform text-4xl text-center bg-white bg-opacity-80 px-6 py-2 rounded-full shadow-lg">
        Les licenses Open Source
      </h2>
      <div className="w-4/5 h-[500px] mx-auto py-10">
        <Swiper
          modules={[Pagination, Navigation, Autoplay]}
          spaceBetween={50}
          slidesPerView={1}
          navigation
          pagination={{ clickable: true }}
          autoplay={{ delay: 5000 }}
          loop
          className="swiper"
        >
          {licenses.map((license, index) => (
            <SwiperSlide
              key={index}
              className="flex flex-col justify-center items-center rounded-lg p-10 text-center"
            >
              <h2 className="text-4xl font-bold mb-5">{license.name}</h2>
              <p className="text-lg leading-relaxed">{license.description}</p>
            </SwiperSlide>
          ))}
        </Swiper>
      </div>
    </section>
  );
}
