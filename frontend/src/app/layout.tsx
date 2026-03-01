import type { Metadata } from 'next'
import { Inter } from 'next/font/google'
import './globals.css'

const inter = Inter({ subsets: ['latin'] })

export const metadata: Metadata = {
  title: 'Healthcare Clinical AI Assistant',
  description: 'AI-powered clinical documentation for healthcare professionals',
  keywords: ['healthcare', 'AI', 'clinical documentation', 'medical'],
  authors: [{ name: 'Healthcare AI Team' }],
  viewport: 'width=device-width, initial-scale=1',
  themeColor: '#2563eb',
}

export default function RootLayout({
  children,
}: {
  children: React.ReactNode
}) {
  return (
    <html lang="en">
      <body className={inter.className}>{children}</body>
    </html>
  )
}
