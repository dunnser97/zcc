fetch("/showMeLists").then(response => {
    return response.json();
}).then(data => {
    console.log(data)
    results_output = "<table><tr><th>Subject</th><th>Requester</th><th>Requested</th><th>priority</th></tr>"

    for (var key in data["tickets"]) {
        results_output += "<tr><td>"+data["tickets"][key]['subject']+"</td><td>"+data["tickets"][key]['submitter_id']+"</td><td>"+data["tickets"][key]['created_at']+"</td><td>"+data["tickets"][key]['priority']+"</td></tr>"
    }
    results_output += "</table>"
    document.getElementById("searchresults").innerHTML = results_output;
})