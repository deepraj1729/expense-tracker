import React from 'react'
import { getLabels,inrFormatting } from '../helpers/config';

export default function Labels(props) {
    const data = props.data;
    let labelObj = getLabels(data);
    let labelData = labelObj.map((data, index) => <LabelComponent key={index} data={data}></LabelComponent>);
    return (
        <>
            {labelData}
        </>
    )
}


function LabelComponent({data}){
    if(!data) return <></>;
    return (
        <div className="labels flex justify-between">
            <div className="flex gap-2">
                <div className='w-2 h-2 rounded py-3' style={{background: data.color??'#f9c74f'}}></div>
                <h3 className='text-md'>{data.tag ?? ''}</h3>
            </div>
            <h3 className='font-bold'>  {Math.round(data.percent) ?? 0}%</h3>
            <span style={{color: data.color??'#f9c74f'}}>{inrFormatting(data.amt)}</span>
        </div>
    )
}
