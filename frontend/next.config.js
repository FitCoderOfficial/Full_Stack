/** @type {import('next').NextConfig} */
const nextConfig = {
    images: {
        remotePatterns: [
            {
                protocol: 'https', 
                hostname: 'localhost',
                port: '8000', 
                pathname: '/**',
            }
        ]
    }
}

module.exports = nextConfig
