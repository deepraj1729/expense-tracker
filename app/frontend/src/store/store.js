import { configureStore } from '@reduxjs/toolkit';
import expenseSlice from './reducer';
import { apiTrackerX } from './apiTrackerX';

export const store = configureStore({
    reducer : {
        expense : expenseSlice,
        [apiTrackerX.reducerPath]: apiTrackerX.reducer
    },
    middleware: getDefaultMiddleware => getDefaultMiddleware().concat(apiTrackerX.middleware)
})