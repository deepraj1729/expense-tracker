function getDashboard(data){
    const savings = data.savings;
    const investments = data.investments;
    const netSavings = savings + investments;
    const expenses = data.expenses;

    const dashboard = {
        "savings": netSavings,
        "investments": investments,
        "expenses": expenses
    } 
    return dashboard;
}

function inrFormatting(num) {
    const data = num.toLocaleString('en-IN', {
        maximumFractionDigits: 2,
        style: 'currency',
        currency: 'INR'
    });
    return data;
}

function getCurrentDateAndMonth(){
    const month_list = ["jan","feb","mar","apr","may","jun","jul","aug","sep","oct","nov","dec"];
    const curr_date = new Date();
    const curr_month = month_list[curr_date.getMonth()];
    return {curr_date, curr_month, month_list}
}

function handleCategory(data){
    const id = data.id;
    const month = data.month;
    const year = data.year;
    const tag= data.tag;
    const amount = data.amount;
    const type = data.type;
    const date = data.date;
    const remarks = data.remarks;

    const colors = ["#ff6384","#f9c74f","#36a2eb"]
    let dataObj;

    if(tag === "expense"){
        dataObj = {
            id: id,
            month: month,
            year:year,
            tag: tag,
            color: colors[0],
            amount: amount,
            type: type,
            date: date,
            remarks: remarks
        }
        return dataObj;

    } else if (tag === "savings"){
        dataObj = {
            id: id,
            month: month,
            year:year,
            tag: tag,
            color: colors[1],
            amount: amount,
            type: type,
            date: date,
            remarks: remarks
        }
        return dataObj;

    } else if (tag === "investment"){
        dataObj = {
            id: id,
            month: month,
            year:year,
            tag: tag,
            color: colors[2],
            amount: amount,
            type: type,
            date: date,
            remarks: remarks
        }
        return dataObj;
    }
}

function getGraphConfig(data){
    const expenses = data.expenses;
    const savings = data.savings;
    const investments = data.investments;

    const graphObj = {
        data: {
            datasets: [{
                label: 'TrackerX Dashboard',
                data: [expenses, savings, investments],
                backgroundColor: [
                    "#ff6384",
                    "#f9c74f",
                    "#36a2eb"
                ],
                hoverOffset: 4,
                borderRadius: 30,
                spacing:10
            }]
        },
        options:{
            cutout: 115
        }
    }
    return graphObj;
}


function getLabels(data) {
    const earnings = data.earnings;
    const expenses = data.expenses;
    const savings = data.savings;
    const investments = data.investments;

    let earningsPercentage = 0;
    let expensePercentage = 0;
    let savingsPercentage = 0;
    let investmentPercentage = 0;

    if(earnings!==0){
        earningsPercentage = 100;
        expensePercentage = (expenses/earnings)*100;
        savingsPercentage = (savings/earnings)*100;
        investmentPercentage = (investments/earnings)*100;
    }

    let obj = [
        {
            tag: "Earnings",
            color: "#4caf50",
            amt: earnings,
            percent:earningsPercentage
        },
        {
            tag: "Expenses",
            color: "#ff6384",
            amt: expenses,
            percent: expensePercentage
        },
        {
            tag: "Savings",
            color: "#f9c74f",
            amt: savings,
            percent:savingsPercentage
        },
        {
            tag: "Investments",
            color: "#36a2eb",
            amt: investments,
            percent:investmentPercentage
        }
    ]
    return obj;
} 

export { getLabels, getDashboard, getGraphConfig, handleCategory, inrFormatting, getCurrentDateAndMonth };