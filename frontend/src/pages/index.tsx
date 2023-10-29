import Container from "@/components/container";
import NavBar from "../components/navbar";


function Homepage() {
  return (
    <div className="fixed h-full w-full min-h-screen bg-seasalt">
      <NavBar />
      <Container>
        <div className="flex flex-col space-y-16 text-center overflow-auto h-full bg-forest-homepage bg-cover bg-center">
          <h1 className="pt-1/3 font-display text-5xl font-semibold mt-32">Welcome to Log-A-Log!</h1>

          <div className="flex flex-col space-y-6 overflow-scroll pb-40 mb-20 pt-12 h-full">
            <p className="font-body text-xl w-2/3 m-auto">Deforestation poses a formidable annual threat, leading to the loss of more than 7 million hectares of forest cover. This widespread issue significantly impacts our environment and ecosystem. At Log-A-Log, our primary objective is to shed light on this escalating problem that affects millions of people worldwide.</p>

            <p className="font-body text-xl w-2/3 m-auto">Our approach centers around innovative data representation. We employ cutting-edge techniques to achieve real-time tree coverage detection by harnessing the Google Maps API alongside our proprietary foliage recognition algorithms.</p>

            <p className="font-body text-xl w-2/3 m-auto">Our commitment lies in pinpointing deforestation areas with exceptional precision. This level of accuracy allows us to uncover and expose illegal logging practices, right down to precise coordinates. The collective efforts of our organization, along with many other conservation groups, are dedicated to addressing the repercussions of logging, including its impact on indigenous communities, agricultural laborers, and the native rainforest species.</p>

            <p className="font-body text-xl w-2/3 m-auto">In essence, we're working diligently to monitor and combat deforestation, striving to protect the interests of various stakeholders affected by this critical issue.</p>
          </div>

        </div>
      </Container>
    </div>

  );
}

export default Homepage;
