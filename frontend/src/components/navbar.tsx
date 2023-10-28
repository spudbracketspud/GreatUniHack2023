import Link from "next/link";


interface ButtonProps {
  value: string;
  url: string;
  accent?: boolean;
}

const NavBarButton: React.FC<ButtonProps> = (props) => {
  let css = "bg-gray-200 text-eerieblack hover:bg-gray-300";
  let accent_css = "bg-jade text-seasalt hover:bg-jadelight"
    
  return (
    <Link
      href={props.url}
      className={"flex text-base font-semibold font-body h-2/3 m-auto w-36 transition-all ease-in-out duration-200 pl-3 pr-3 rounded-full " + (props.accent ? accent_css : css)}
    >
      <div className="flex flex-row h-full m-auto">
        <h1 className="m-auto text-center">{props.value}</h1>
      </div>
    </Link>
  );
};

function NavBar() {
  return(
    <div className="fixed w-full z-50 font-display justify-between text-cultured h-16 flex flex-row flex-wrap border-b-[1px]">
      <Link href="/" className="mt-auto mb-auto pl-20 pr-8 ">
        <h1 className="mt-auto mb-auto text-2xl font-display font-semibold text-jade">Log-A-Log</h1>
      </Link>

      <div className="flex flex-row flex-wrap pl-8 pr-20 space-x-4">
        {/* TODO add urls */}
        <NavBarButton value="Areas" url="/" />
        <NavBarButton value="Trends" url="/" />
        <NavBarButton value="About Us" url="/" />
        <NavBarButton value="Donate" url="/" accent={true} />
      </div>
    </div>
  );
}

export default NavBar;
