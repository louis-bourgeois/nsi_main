import dynamic from "next/dynamic";

const Tux = dynamic(() => import("./Svg/Tux").then((mod) => mod.Tux), {
  loading: () => <></>,
  ssr: false,
});

const Blender = dynamic(
  () => import("./Svg/Blender").then((mod) => mod.Blender),
  {
    loading: () => <></>,
    ssr: false,
  }
);

const VsCode = dynamic(() => import("./Svg/VsCode").then((mod) => mod.VsCode), {
  loading: () => <></>,
  ssr: false,
});

export default function Heroe({ h1 }) {
  return (
    <section
      id="heroe"
      className="h-screen w-full flex items-center justify-center"
    >
      <a
        href="#gnu"
        className="hover:scale-110 transition-all cursor-pointer absolute right-0 bottom-16"
      >
        <Tux width={375} height={375} />
      </a>
      <a
        href="#netscape"
        className="hover:scale-110 transition-all cursor-pointer absolute top-32 left-1/2 transform -translate-x-1/2"
      >
        <Blender width={64} height={64} />
      </a>
      <a
        href="#react"
        className="hover:scale-110 transition-all cursor-pointer absolute left-48 bottom-48"
      >
        <VsCode width={64} height={64} />
      </a>
      <h1 className="text-7xl font-bold text-center px-4">{h1}</h1>
      <a
        href="#definition"
        className="absolute bottom-8 left-1/2 transform -translate-x-1/2"
      >
        <svg
          width="24"
          height="24"
          viewBox="0 0 24 24"
          fill="none"
          xmlns="http://www.w3.org/2000/svg"
        >
          <path
            d="M12 5V19M12 19L19 12M12 19L5 12"
            stroke="#000000"
            strokeWidth="2"
            strokeLinecap="round"
            strokeLinejoin="round"
          />
        </svg>
      </a>
    </section>
  );
}
