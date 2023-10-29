import React from 'react';
import Container from "@/components/container";
import NavBar from "../components/navbar";
import Link from 'next/link'; // Import the Link component

const rainforestImages = [
  {
    src: 'image1.jpg',
    alt: 'Forest 1',
    text: 'Amazon Rainforest',
    link : '/areas/amazon',
  },
  {
    src: 'image2.jpg',
    alt: 'Forest 2',
    text: 'Siberia/Russia Boreal Forests',
    link: '/',
  },
  {
    src: 'image3.jpg',
    alt: 'Forest 3',
    text: 'Indonesia',
    link: '/',
  },
  {
    src: 'image4.jpg',
    alt: 'Forest 4',
    text: 'Tanzania',
    link: '/',
  },
  // can add more images 
];

function AreasPage() {
  return (
    <div className="flex flex-col items-center">
      <NavBar />
      <Container>
        <div className="flex flex-col space-y-16 pt-24 pb-28 ml-32 mr-32">
          {rainforestImages.map((image, index) => (
            <Link href={image.link} key={index}>
              {/* <a> */}
                <div className="rounded-lg overflow-hidden transition-transform transform hover:scale-105 p-4 w-4/5 mx-auto relative duration-200 shadow-xl hover:shadow-2xl">
                  <div style={{ paddingTop: '25%' }}> {/* Set the padding-top to 25% */}
                    <img
                      src={image.src}
                      alt={image.alt}
                      className="absolute inset-0 w-full h-full object-cover" // Allow the image to stretch to fill the container
                    />
                  </div>
                  <div className="absolute inset-0 flex items-center justify-center">
                    <p className="mt-auto mb-auto text-2xl font-display font-semibold text-white p-2 relative inline-block">{image.text}</p>
                  </div>
                </div>
              {/* </a> */}
            </Link>
          ))}
        </div>
      </Container>
    </div>
  );
}


export default AreasPage;
