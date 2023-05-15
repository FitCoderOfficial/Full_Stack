'use client'
import { ChangeEvent, useState } from 'react'
import { Form } from '@/interface/interface'

const AuthForm = ({ process }: { process: string }) => {

    const [form, setForm] = useState<Form>({})
    const handleChange = (e: ChangeEvent<HTMLInputElement | HTMLTextAreaElement>) => {
        setForm({ ...form, [e.target.name]: e.target.value })
    }

    return (
        <div className='h-screen w-screen flex items-center justify-center' style={{background:'url(https://i.stack.imgur.com/vzbuQ.jpg)'}}>
            <form className='relative flex flex-col w-[580px] justify-center gap-y-5 bg-white/[.03] py-10 px-12 backdrop-blur-[3px]'>
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
                <input
                    type="email"
                    placeholder="Email"
                    name="email"
                    className='input'
                    required
                    autoFocus
                    onChange={handleChange}
                />
                <button className='formButton'>{process}</button>
            </form>
        </div>
    )
}

export default AuthForm