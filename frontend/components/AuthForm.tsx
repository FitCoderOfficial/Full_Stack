'use client'
import { ChangeEvent, useState } from 'react'
import { Form } from '@/interface/interface'

const AuthForm = ({ process }: { process: string }) => {

    const [form, setForm] = useState<Form>({})
    const handleChange = (e: ChangeEvent<HTMLInputElement>) => {
        setForm({ ...form, [e.target.name]: e.target.value })
    }

    return (
        <div>
            <form action="">
                <h1>{process}</h1>
                <input
                    type="text"
                    placeholder="Username"
                    name="username"
                    className='input'
                    required
                    autoFocus
                    onChange={handleChange}
                />
            </form>
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
        </div>
    )
}

export default AuthForm