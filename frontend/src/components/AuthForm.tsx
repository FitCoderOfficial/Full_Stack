'use client'
import { ChangeEvent, FormEvent, useState } from 'react'
import { Form } from '@/interface/interface'
import Link from 'next/link'
import { usePathname } from 'next/navigation'
import { login } from '@/services/auth'


const AuthForm = ({ process }: { process: string }) => {

    const [form, setForm] = useState<Form>({})
    const handleChange = (e: ChangeEvent<HTMLInputElement | HTMLTextAreaElement>) => {
        setForm({ ...form, [e.target.name]: e.target.value })
    }

    const pathname = usePathname()

    const handleSubmit = async (e: FormEvent) => {
        e.preventDefault()
        if (pathname === '/login') {
            try{
                const response = await login(form)
                console.log(response)
            } catch(err) {
                console.log(err)
            }
        console.log(form)
    }}

    return (
        <div className='h-screen w-screen flex items-center justify-center' style={{background:'url(https://i.stack.imgur.com/vzbuQ.jpg)'}}>
            <form 
                className='relative flex flex-col w-[580px] justify-center gap-y-5 bg-white/[.03] py-10 px-12 backdrop-blur-[3px] rounded'
                onSubmit={handleSubmit}>
                <h1 className='text-5xl font-bold text-white'>{process}</h1>
                <input
                    type="text"
                    placeholder="Username"
                    name="username"
                    className="input"
                    required
                    autoFocus
                    onChange={handleChange}
                />
                <input
                    type="password"
                    placeholder="Password"
                    name="password"
                    className='input'
                    required
                    autoFocus
                    onChange={handleChange}
                />

                {pathname === '/register' && (
                    <input
                    type="email"
                    placeholder="Email"
                    name="email"
                    className='input'
                    required
                    autoFocus
                    onChange={handleChange}
                />
                    )}

                {pathname === '/login' ? (
                    <Link 
                        href={'/register'}
                        className='text-[15px] font-semibold text-blue-600 self-end'
                        > No account? Register here
                    </Link>
                 ) : (
                    <Link 
                        href={'/login'}
                        className='text-[15px] font-semibold text-blue-600 self-end'
                        >Already have an account? login here</Link>

                 )
                }
                <button className='formButton'>{process}</button>
            </form>
        </div>
    )
}

export default AuthForm