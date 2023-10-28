/** @type {import('next').NextConfig} */
const nextConfig = {
  reactStrictMode: true,
};

module.exports = {
  webpack: (config, { isServer }) => {
    // Register unhandled exception and rejection handlers in production mode
    // if (process.env.NODE_ENV === 'production' && isServer) {
    //   process.on('uncaughtException', (err) => {
    //     console.error('Unhandled Exception:', err);
    //   });

    //   process.on('unhandledRejection', (err) => {
    //     console.error('Unhandled Rejection:', err);
    //   });
    // }

    process.on("uncaughtException", (err) => {
      console.error("Unhandled Exception:", err);
    });

    process.on("unhandledRejection", (err) => {
      console.error("Unhandled Rejection:", err);
    });

    return config;
  },
};
