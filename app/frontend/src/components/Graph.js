import React, { useState, useEffect } from 'react';
import { Doughnut } from 'react-chartjs-2';
import {Chart, ArcElement} from 'chart.js';
import {default as api} from '../store/apiTrackerX';
import Labels from './Labels';
import List from "./List";
import Form from './Form';

import { getDashboard,getGraphConfig,inrFormatting,getCurrentDateAndMonth } from '../helpers/config';

Chart.register(ArcElement);


const RenderUI = ({month,handleChange}) =>{
    const {curr_date, curr_month, month_list} = getCurrentDateAndMonth()

    // console.log("Current-month"+curr_month + "  Month selected: "+month);
    const { data, isFetching , isSuccess, isError } = api.useGetAnalysisQuery(month);
    let msg = '';
    
    if(isFetching){
        msg = <div>Fetching</div>;
        return (
            <>
                <div className="flex justify-content max-w-xs mx-auto">
                    {msg}
                </div>

                <div className="grid md:grid-cols-1 gap-4">
                    {/* List */}
                    <List data={data} status={"fetching"}></List>
                </div>
            </>            
        );
    }else if(isSuccess){
        let labelData = data.data.dashboard;
        const dashboard = getDashboard(labelData);
        const config = getGraphConfig(labelData);
        return (
            <>  
                <div className="flex justify-content max-w-xs mx-auto">
                    <div className="item">
                        <div className="chart relative">
                        <Doughnut {...config}></Doughnut>
                        <h3 className='mb-4 font-bold title'>Total
                            <span className='block text-3xl text-emerald-400'>{inrFormatting(dashboard.savings)}</span>
                        </h3>
                        </div> 

                        <div className="flex flex-col py-10 gap-4">      
                            <select className='form-input' value={month} onChange={handleChange}>
                                <option value={curr_month} defaultValue>{curr_month}</option>
                                {
                                    month_list.map((name,index) => {
                                        return(
                                            <option value={name}>{name}</option>
                                        )
                                    })
                                }
                            </select>                      
                        </div>  
        
                        <div className="flex flex-col py-10 gap-4">
                            {/* Labels */}
                            <Labels data={labelData}></Labels>
                        </div> 

                        <div className="flex flex-col py-10 gap-4">
                            {/* Form */}
                            <Form></Form>
                        </div> 

                        
                    </div>
                </div>

                <div className="grid md:grid-cols-1 gap-4" style={{overflowX: 'auto',maxHeight:'120vh'}}>
                    {/* List */}'
                    <List data={data.data} status={"success"}></List>
                </div>
            </>



      );

      }else if(isError){
          msg = <div>Error</div>

          return (
            <>
                <div className="flex justify-content max-w-xs mx-auto">
                  {msg}
                </div>

                <div className="grid md:grid-cols-1 gap-4">
                    {/* List */}
                    <List data={data} status={"error"}></List>
                </div>
            </>

      );
    }
}


export default function Graph() {
    const {curr_date, curr_month, month_list} = getCurrentDateAndMonth()
    const [month, setMonth] = useState(curr_month);
    // const [month, setMonth] = useState("aug");

    const handleChange = (e)=> {
        const month_name = e.target.value;
        if(!month_name) return;
        setMonth(month_name);  
        return (
            <RenderUI month={month} handleChange={handleChange}/>
        ) 
    }

    return (
        <RenderUI month={month} handleChange={handleChange}/>
    )    
}
