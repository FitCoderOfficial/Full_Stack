import { configureStore } from "@reduxjs/toolkit";
import authReduxer from '@/redux/reducers/auth.slice'

const store = configureStore({
    reducer: {
        auth: authReduxer,
    }
})

export type RootState = ReturnType<typeof store.getState>
export type AppDispatch = typeof store.dispatch;

export default store