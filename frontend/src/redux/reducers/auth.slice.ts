import { createSlice } from '@reduxjs/toolkit'
import { AuthState } from '@/interface/interface'


const initialState: AuthState = {
    access: null,
    refresh: null,
    is_authenticated: false,
    is_loading: true,
    user: null,
}

const authSlice = createSlice({
    name:'auth',
    initialState,
    reducers:{
        loginRedux : (state, {payload}) => {
            state.access = localStorage.getItem('access');
            state.refresh = localStorage.getItem('refresh');
            state.is_authenticated = true;
            state.is_loading = false;
            state.user = payload;
        },
        logoutRedux: (state) => {
            localStorage.removeItem('acccess');
            localStorage.removeItem('refresh');
            state.access = null;
            state.refresh = null;
            state.is_authenticated = false;
            state.is_loading=true
            state.user = null
        }
    }
})

export default authSlice.reducer
export const { loginRedux, logoutRedux } = authSlice.actions
