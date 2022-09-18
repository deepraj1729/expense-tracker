const TrackerXConfig = {
    name: "tracker-x",
    version: "0.0.1",
    description: "Tracker X",
    endpoints: {
        dashboard_overall:"dashboard/all",
        dashboard_month:"dashboard/{month}",
        add:"transaction/add",
        create:"/create",
        update:"/update",
        delete:"/delete",
        analyze:"/analyze"
    },
}

export default TrackerXConfig;