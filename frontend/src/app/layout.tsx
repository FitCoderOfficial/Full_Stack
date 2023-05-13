import type { Metadata } from 'next'
import { Inter } from 'next/font/google'
import "../../public/globals.css"
import { ReduxProvider } from '@/redux/store/ReduxProvider'

const inter = Inter({ subsets: ['latin'] })

export const metadata: Metadata = {
  title: 'Create Next App',
  description: 'Generated by create next app',
}

export default function RootLayout({
  children,
}: {
  children: React.ReactNode
}) {
  return (
    <html
      lang="en"
      className='dark'
    >
      <body className={inter.className}>

        <main>
          <ReduxProvider>
            {children}
          </ReduxProvider>
        </main>
      </body>
    </html>
  )
}
