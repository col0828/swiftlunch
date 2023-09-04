$(document).ready(function () {

    var additem = $(".meal1");
    var meal1 = $("<div>");
    additem.append(meal1);

    axios.post("/meal1-api", { headers: { 'Content-Type': 'application/x-www-form-urlencoded' } })
        .then(function (response) {
            var res = response.data;
            console.log(res);
            for (var key in res) {
                console.log(res[key]);
                var html = "<p>" + res[key] + "</p>";
                console.log(html);
                meal1.append($("<div>").html(html));
            }
        })
        .catch(function (error) {
            console.log(error);
            $("#loading-container").remove();
        });
});