import Container from "@/components/container";
import NavBar from "../components/navbar";


function Homepage() {
  return (
    <div className="fixed h-full w-full min-h-screen bg-seasalt">
      <NavBar />
      <Container>
        <div className="flex flex-col space-y-28 text-center">
          <h1 className="pt-1/3 font-display text-5xl font-semibold mt-60">Welcome to Log-A-Log!</h1>

          {/* TODO add text here */}
          <h2 className="font-body text-xl w-2/3 m-auto">Lorem ipsum dolor sit amet, consectetur adipiscing elit. Nullam hendrerit, turpis eget accumsan posuere, nisi justo eleifend eros, eu eleifend felis odio vel ipsum. Quisque nec erat a nunc bibendum hendrerit. Vivamus vestibulum vel dui non fringilla. Fusce vel lacinia justo. Nullam at pulvinar tellus. Sed ultrices ligula in dolor efficitur, sed tempor mi cursus. Donec auctor, metus at malesuada sagittis, velit erat fringilla augue, nec tristique nunc justo et lectus.</h2>
        </div>
      </Container>
    </div>

  );
}

export default Homepage;
