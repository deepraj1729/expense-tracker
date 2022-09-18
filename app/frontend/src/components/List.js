import React from 'react';
import 'boxicons';
import {default as api} from '../store/apiTrackerX';
import { handleCategory } from '../helpers/config';


const List = ( {data, status}) => {
  let allTransactions;
  let Transactions;

  if(status === "fetching"){
      Transactions = <div>Fetching</div>;
  }else if(status === "success"){
      allTransactions = data.transactions;
      Transactions = allTransactions.slice(0).reverse().map((data, index) => <Transaction key={index} category={data}></Transaction>);
  }else if(status === "error"){
      Transactions = <div>Error</div>
  }

  return (
    <div className="flex flex-col py-6 gap-6 max-w-s">
        <h1 className='py-4 font-bold text-xl'>History</h1>
        {Transactions}
    </div>
  )
}

function Transaction({ category }){
  const [deleteTransaction] = api.useDeleteTransactionMutation();

  const handlerClick = (e) => {
    e.preventDefault();
    deleteTransaction(e.currentTarget.id);
  }

  if(!category) return null;
  let transData = handleCategory(category);

  return (
      <div className="item flex gap-4 bg-gray-50 py-2 rounded-r" style={{borderRight : `8px solid ${transData.color ??  "#e5e5e5"}`}}>  
          <button className='px-3' id = {transData.id} value={transData.id} onClick={handlerClick}>
            <box-icon
              color={transData.color ??  "#e5e5e5"} 
              size="15px" 
              name="trash"
              value={transData.id}>
            </box-icon>
          </button>            
          <span className='block'>
            <span style={{color: "orange"}} >{transData.date ?? ''} </span> {transData.remarks ?? ''}  {transData.type === "debit" ? 
              <span style={{color: "red"}} >{transData.amount}</span> 
              :
              <span style={{color: "rgb(52 211 153 / var(--tw-text-opacity))"}}>{transData.amount}</span>
            }  {/* {transData.tag ?? ''} */}
          </span>
      </div>
  )
}

export default List;