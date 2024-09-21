export default function Navbar() {
  const options = {
    weekday: "long",
    year: "numeric",
    month: "long",
    day: "numeric",
  };
  const today = new Date();

  return (
    <header className="fixed z-[99] mt-[2vh] flex justify-between items-center w-full px-[4vw] py-3 ">
      <nav
        aria-label="Navigation principale"
        className="flex-grow flex justify-between"
      >
        <ul className="flex flex-wrap items-center space-x-1 md:space-x-4">
          <li>
            <a
              href="#definition"
              className="text-gray-800 hover:text-blue-600 px-2 py-1 rounded-md text-xs md:text-sm font-medium"
            >
              Définition
            </a>
          </li>
          <li>
            <a
              href="#gnu"
              className="text-gray-800 hover:text-blue-600 px-2 py-1 rounded-md text-xs md:text-sm font-medium"
            >
              GNU
            </a>
          </li>
          <li>
            <a
              href="#linux"
              className="text-gray-800 hover:text-blue-600 px-2 py-1 rounded-md text-xs md:text-sm font-medium"
            >
              Linux
            </a>
          </li>
          <li>
            <a
              href="#netscape"
              className="text-gray-800 hover:text-blue-600 px-2 py-1 rounded-md text-xs md:text-sm font-medium"
            >
              Netscape
            </a>
          </li>
          <li>
            <a
              href="#blender"
              className="text-gray-800 hover:text-blue-600 px-2 py-1 rounded-md text-xs md:text-sm font-medium"
            >
              The Blender Foundation
            </a>
          </li>
          <li>
            <a
              href="#browsers"
              className="text-gray-800 hover:text-blue-600 px-2 py-1 rounded-md text-xs md:text-sm font-medium"
            >
              Chromium & Firefox
            </a>
          </li>
          <li>
            <a
              href="#contact"
              className="text-gray-800 hover:text-blue-600 px-2 py-1 rounded-md text-xs md:text-sm font-medium"
            >
              Contact
            </a>
          </li>
        </ul>
        <div className="flex justify-between items-center space-x-1 font-bold">
          <span>Louis Bourgeois, le</span>
          <span>{today.toLocaleDateString("fr-FR")}</span>
        </div>
      </nav>
    </header>
  );
}
