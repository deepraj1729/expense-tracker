import { createApi, fetchBaseQuery } from '@reduxjs/toolkit/query/react';
import TrackerXConfig from '../config';


const baseURL = process.env.REACT_APP_URL;

export const apiTrackerX = createApi({
    baseQuery: fetchBaseQuery({baseUrl: baseURL}), //mode: "cors"
    endpoints: builder => ({
        getAnalysis : builder.query({
            // get: '/analyze/{month_name}'
            query: (month_name) => "/dashboard/"+month_name,
            providesTags: ['transaction']
        }),

        addTransaction : builder.mutation({
            // post: '/add
            query: (transaction) => ({
                url: "/transaction/add",
                method: "POST",
                body: transaction
            }),
            invalidatesTags: ['transaction']
        }),

        deleteTransaction : builder.mutation({
            // delete: 'delete/{id}
            query: (transactionID) => ({
                url: "/transaction/"+transactionID,
                method: "DELETE"
            }),
            invalidatesTags: ['transaction']
        })

    })
})

export default apiTrackerX;