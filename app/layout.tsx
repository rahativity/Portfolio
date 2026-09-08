import type { ReactNode } from "react"

export const metadata = {
  title: "Md. Sabbir Hossain Rahat — CSE Student & Software Developer",
  description:
    "3rd-year CSE student at Khawaja Yunus Ali University. Building software, exploring Linux, and understanding systems.",
}

export default function RootLayout({ children }: { children: ReactNode }) {
  return (
    <html lang="en">
      <body>{children}</body>
    </html>
  )
}
