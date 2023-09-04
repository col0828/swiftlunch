$(document).ready(function () {

    var additem = $(".meal2");
    var meal2 = $("<div>");
    additem.append(meal2);

    axios.post("/meal2-api", { headers: { 'Content-Type': 'application/x-www-form-urlencoded' } })
        .then(function (response) {
            var res = response.data;
            console.log(res);
            for (var key in res) {
                console.log(res[key]);
                var html = "<p>" + res[key] + "</p>";
                console.log(html);
                meal2.append($("<div>").html(html));
            }
        })
        .catch(function (error) {
            console.log(error);
            $("#loading-container").remove();
        });
});