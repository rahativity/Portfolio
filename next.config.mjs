/** @type {import("next").NextConfig} */
const nextConfig = {
  // The pages are files, not routes. beforeFiles runs ahead of Next's own
  // routing, so a request for /about is answered by the copy of /about
  // rather than by the placeholder page.
  async rewrites() {
    return {
      beforeFiles: [
        {
          "source": "/",
          "destination": "/index.html"
        },
        {
          "source": "/about",
          "destination": "/about/index.html"
        },
        {
          "source": "/about/",
          "destination": "/about/index.html"
        },
        {
          "source": "/projects",
          "destination": "/projects/index.html"
        },
        {
          "source": "/projects/",
          "destination": "/projects/index.html"
        },
        {
          "source": "/article",
          "destination": "/article/index.html"
        },
        {
          "source": "/article/",
          "destination": "/article/index.html"
        },
        {
          "source": "/contact",
          "destination": "/contact/index.html"
        },
        {
          "source": "/contact/",
          "destination": "/contact/index.html"
        }
      ],
    }
  },
}

export default nextConfig
