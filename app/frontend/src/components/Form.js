import React from "react";
import { useForm } from "react-hook-form";
import {default as api} from '../store/apiTrackerX';
// import { getCurrentDateAndMonth } from '../helpers/config';


export default function Form() {
  const {register,handleSubmit,resetField} = useForm();
  const [addTransaction] = api.useAddTransactionMutation();

//   const {curr_date, curr_month, month_list} = getCurrentDateAndMonth()

  const handleUserInput = (inpData) => {
    const inpObj = inpData;
    let date_arr = inpData.date.split('-');
    let new_date = ""+date_arr[2]+"/"+date_arr[1]+"/"+date_arr[0]
    inpObj.date = new_date
    return inpObj
  }

  const onSubmit = async(data) => {
    if(!data) return;
    const modified_data = handleUserInput(data);
    const response = await addTransaction(modified_data).unwrap();
    resetField('remarks');
    resetField('amount');
  }
  return (
    <div className="form max-w-sm mx-auto w-96">
        <h1 className='font-bold pb-4 text-xl'>Transaction</h1>
        <form id='form' onSubmit={handleSubmit(onSubmit)}>
            <div className="grid gap-4">
                <div className="input-group">
                    <input type="text" {...register('remarks')} placeholder='Salary, House Rent, SIP' className='form-input' />
                </div>
                <div className="input-group">
                    <input type="date" {...register('date')} placeholder='Select Date' className='form-input' />
                </div>
                <select className='form-input' {...register('tag')}>
                    <option value="investment" defaultValue>Investment</option>
                    <option value="expense">Expense</option>
                    <option value="savings">Savings</option>
                </select>
                <select className='form-input' {...register('type')}>
                    <option value="debit"  defaultValue>Debit</option>
                    <option value="credit">Credit</option>
                </select>
                <div className="input-group">
                    <input type="text" {...register('amount')} placeholder='Amount' className='form-input' />
                </div>
                <div className="submit-btn">
                    <button className='border py-2 text-white bg-indigo-500 w-full rounded-md'>Save</button>
                </div>
            </div>    
        </form>
    </div>
  );
}