$(document).ready(function () {

    var additem = $(".meal3");
    var meal3 = $("<div>");
    additem.append(meal3);

    axios.post("/meal3-api", { headers: { 'Content-Type': 'application/x-www-form-urlencoded' } })
        .then(function (response) {
            var res = response.data;
            console.log(res);
            for (var key in res) {
                console.log(res[key]);
                var html = "<p>" + res[key] + "</p>";
                console.log(html);
                meal3.append($("<div>").html(html));
            }
        })
        .catch(function (error) {
            console.log(error);
            $("#loading-container").remove();
        });
});