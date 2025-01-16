import Footer from "./components/Footer";
import Frise from "./components/Frise";
import Heroe from "./components/Heroe";
import Introduction from "./components/Introduction";
import LicenceCarousel from "./components/LicenceCarousel";

export default function Page() {
  const mainTitle = "L'Art des Logiciels Libres et Open-Source";
  return (
    <>
      <Heroe h1={mainTitle}></Heroe>
      <Introduction></Introduction>
      <LicenceCarousel></LicenceCarousel>
      <Frise></Frise>
      <Footer></Footer>
    </>
  );
}
