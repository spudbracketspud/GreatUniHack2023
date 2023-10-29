import React from 'react';
import Container from "@/components/container";
import NavBar from "../components/navbar";


function Homepage() {
  // Text to pre-fill in the tweet
  const tweetText = "Learn more about deforestation with Log-A-Log #Awareness";

  // URL to open the Twitter Web Intent
  const tweetIntentURL = `https://twitter.com/intent/tweet?text=${encodeURIComponent(tweetText)}`;

  return (
    <div className="fixed h-full w-full min-h-screen bg-seasalt">
      <NavBar />
      <Container>
        <div className="flex flex-col space-y-28 text-center">
          <h1 className="pt-1/3 font-display text-5xl font-semibold mt-60">
            Help Spread Awareness!
          </h1>

          <a href={tweetIntentURL} target="_blank" rel="noopener noreferrer">
            <button>Share on Twitter</button>
          </a>
        </div>
      </Container>
    </div>
  );
}

export default Homepage;



 
