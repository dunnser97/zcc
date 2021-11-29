function pagenum(page) {
    fetch("/showMeLists").then(response => {
        return response.json();
    }).then(data => {
        console.log(data)
        var key = 0 + page*25;
        results_output = "<table><tr><th>Subject</th><th>Requester</th><th>Requested</th><th>priority</th></tr>"
        while (key < 25 + page*25) {
            results_output += "<tr><td>" + data["tickets"][key]['subject'] + "</td><td>" + data["tickets"][key]['submitter_id'] + "</td><td>" + data["tickets"][key]['created_at'] + "</td><td>" + data["tickets"][key]['priority'] + "</td></tr>"
            key += 1;
        }
        results_output += "</table>"
        document.getElementById("searchresults").innerHTML = results_output;
        page_nums = Math.ceil(data["tickets"].length/25)
        console.log(page_nums)
    })
}