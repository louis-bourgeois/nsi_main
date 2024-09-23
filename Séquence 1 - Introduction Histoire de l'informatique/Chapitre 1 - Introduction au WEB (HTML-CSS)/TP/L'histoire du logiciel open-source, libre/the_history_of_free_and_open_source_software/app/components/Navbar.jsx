"use client";
import Link from "next/link";
import { usePathname } from "next/navigation";

const Navbar = () => {
  const pathname = usePathname();
  const today = new Date().toLocaleDateString("fr-FR", {
    weekday: "long",
    year: "numeric",
    month: "long",
    day: "numeric",
  });

  const navItems = [
    { id: "definition", label: "Définition" },
    { id: "unix", label: "Unix" },
    { id: "gnu", label: "GNU" },
    { id: "linux", label: "Linux" },
    { id: "netscape", label: "Netscape" },
    { id: "blender", label: "Blender" },
    { id: "firefox", label: "Firefox" },
    { id: "chrome", label: "Chrome" },
    { id: "react", label: "React" },
    { id: "vscode", label: "VS Code" },
    { id: "llama", label: "Llama" },
  ];

  const getHref = (id) => {
    return pathname !== "/" ? `/#${id}` : `#${id}`;
  };

  return (
    <header className="fixed z-[99] mt-[2vh] flex justify-between items-center w-full px-[4vw] py-3">
      <nav
        aria-label="Navigation principale"
        className="flex-grow flex justify-between"
      >
        <ul className="flex flex-wrap items-center space-x-1 md:space-x-4">
        <li>
          <Link href={"/"}>Accueil</Link>
        </li>
          {navItems.map((item) => (
            <li key={item.id}>
              <Link
                href={getHref(item.id)}
                className="text-gray-800 hover:text-[#007AFF] px-2 py-1 rounded-md text-xs md:text-sm font-medium"
              >
                {item.label}
              </Link>
            </li>
          ))}
          <li>
            <Link
              href="/biographies/ton-roosendaal"
              className="text-gray-800 hover:text-[#007AFF] px-2 py-1 rounded-md text-xs md:text-sm font-medium"
            >
              Ton Roosendaal
            </Link>
          </li>
          <li>
            <Link
              href="/biographies/linus-torvalds"
              className="text-gray-800 hover:text-[#007AFF] px-2 py-1 rounded-md text-xs md:text-sm font-medium"
            >
              Linus Torvalds
            </Link>
          </li>
        </ul>
        <div className="flex justify-between items-center space-x-1 font-bold">
          <span>Louis Bourgeois, le</span>
          <span>{today}</span>
        </div>
      </nav>
    </header>
  );
};

export default Navbar;
