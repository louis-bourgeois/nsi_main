export default function Navbar() {
  return (
    <header className="mt-[2vh] flex justify-between items-center w-full px-4 py-3">
      <nav aria-label="Navigation principale" className="flex-grow flex justify-between">
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
        <div className="flex justify-between">
          Louis Bourgeois, la date du jour
        </div>
      </nav>
    </header>
  );
}
