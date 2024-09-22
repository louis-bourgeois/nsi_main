import Footer from "./components/Footer";
import Frise from "./components/Frise";
import Heroe from "./components/Heroe";
import Introduction from "./components/Introduction";
import LicenceCarousel from "./components/LicenceCarousel";
import Navbar from "./components/Navbar";
export default function Page() {
  const mainTitle = "L'Art des Logiciels Libres et Open-Source";
  return (
    <>
      <Navbar></Navbar>
      <Heroe h1={mainTitle}></Heroe>
      <Introduction></Introduction>
      <LicenceCarousel></LicenceCarousel>
      <Frise></Frise>
      <Footer></Footer>
    </>
  );
}
