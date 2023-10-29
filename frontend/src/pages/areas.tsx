import React from 'react';
import Container from "@/components/container";
import NavBar from "../components/navbar";
import Link from 'next/link'; // Import the Link component

const rainforestImages = [
  {
    src: 'image1.jpg',
    alt: 'Rainforest 2',
    text: 'Amazon Rainforest',
    link : '/help',
  },
  {
    src: 'image2.jpg',
    alt: 'Rainforest 3',
    text: 'Siberia/Russia Boreal Forests',
    link: '/',
  },
  {
    src: 'image3.jpg',
    alt: 'Rainforest 3',
    text: 'Ethiopia',
    link: '/',
  },
  {
    src: 'image4.jpg',
    alt: 'Chad',
    text: '',
    link: '/',
  },
  // can add more images 
];

function AreasPage() {
  return (
    <div className="flex flex-col items-center">
      <NavBar />
      <Container>
        <div className="grid grid-cols-1 gap-10">
          {rainforestImages.map((image, index) => (
            <Link href={image.link} key={index}>
              <a>
                <div className="rounded-lg overflow-hidden transition-transform transform hover:scale-105 p-4 w-4/5 mx-auto relative">
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
              </a>
            </Link>
          ))}
        </div>
      </Container>
    </div>
  );
}


export default AreasPage;
