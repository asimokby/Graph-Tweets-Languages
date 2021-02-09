var drawChart = (langsDict) => {
    /*
        This methods first structures the data it gets in the form {y: percent, label: language}.
        Then draw the pie chart usign the library Canvas.JS
    */
    dataToChart = []
    const sum = Object.values(langsDict).reduce((a, b) => a + b, 0);
    for (var key of Object.keys(langsDict)) {
        const percent = (langsDict[key] / sum) * 100;
        if (percent > 0)
        dataToChart.push({ y: percent, label: key })
    }
    var chart = new CanvasJS.Chart("chartContainer", {
        animationEnabled: true,
        title: {
            text: `Languages Percentages - Considering ${sum} Recent Proper Tweets`
        },
        data: [{
            type: "pie",
            startAngle: 240,
            yValueFormatString: "##0.00\"%\"",
            indexLabel: "{label} {y}",
            dataPoints: dataToChart,
        }]
    });
    chart.render();

}


$(document).ready(function() {
    /*
        When the form is submitted, a post request is sent to the server with the username extracted
        from the form. 

        Divs(loading, error..etc) are shown and hidden when they are supposed to.
        
        Data received from the response of the post request is passed to the drawChart function 
        to draw the graph
    */
   
    $('form').on('submit', function(event){  
        $(".chartContainer").hide();  
        $(".loader").show();
        $(".errorOccured").hide();
        $.ajax({
            data: JSON.stringify({ 'username': $('#search').val() }),
            type : 'POST',
            contentType: "application/json",
            url: 'http://127.0.0.1:5000/process',
            // url: 'https://graphlangs.herokuapp.com/process',
            error: function (XMLHttpRequest, textStatus, errorThrown){
                $(".errorOccured").show();
                $(".loader").hide();
                 }
        })
        .done(function(data){
            $(".loader").hide();
            if (data.error){
                $(".errorOccured").show();
            } else {
                $(".chartContainer").show();
                $('#search').val('')
                drawChart(JSON.parse(data))
            }        
        });
        
        event.preventDefault();
    });

});

