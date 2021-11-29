function pagenum(page) {

    fetch("/showMeLists").then(response => {
        return response.json();
    }).then(data => {
        console.log(data)
        var key = 0;
        key = 0 + page*25;
        results_output = "<table><tr><th>Subject</th><th>Requester</th><th>Requested</th><th>priority</th></tr>"
        while ((key < 25 + page*25) && (key < data["tickets"].length)) {
            if (data["tickets"][key])
            results_output += "<tr><td> <a href='/individual_ticket/" + data["tickets"][key]["id"]+"'>"  + data["tickets"][key]['subject'] + "</a></td><td>   " + data["tickets"][key]['submitter_id'] + "   </td><td>   " +
                "" + data["tickets"][key]['created_at'] + "   </td><td>   " + data["tickets"][key]['priority'] + "</td></tr>"
            key += 1;
        }
        results_output += "</table>"
        document.getElementById("searchresults").innerHTML = results_output;
        page_nums = Math.ceil(data["tickets"].length/25)
        pageamt_output = ""
        for (i=0; i<page_nums; i++) {
            pageamt_output += "<button onclick='pagenum(" + (i) + ")'>" + (i+1) + "</button>"
        }
        document.getElementById("pagenums").innerHTML = pageamt_output;
    })
}

function individual_page(ticket_id) {
    fetch(`/showMeIds/${ticket_id}`).then(response => {
        return response.json();
    }).then(data => {
        console.log(data)
    })
}