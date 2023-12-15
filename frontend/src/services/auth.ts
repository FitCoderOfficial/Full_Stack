import {API} from "./axios"
import { Form } from "@/interface/interface"


export const login = async(credentials: Form) => {
    const {data} = await API.post("login/", credentials)
    localStorage.setItem("access", data.access)
    localStorage.setItem("refresh", data.refresh)
    return data
}

export const register = async(credentials: Form) => {
    const {data, status} = await API.post("users/", credentials)
    return {data, status}
}
