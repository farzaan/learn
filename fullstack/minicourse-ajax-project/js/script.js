
function loadData() {

    var $body = $('body');
    var $wikiElem = $('#wikipedia-links');
    var $nytHeaderElem = $('#nytimes-header');
    var $nytElem = $('#nytimes-articles');
    var $greeting = $('#greeting');

    // clear out old data before new request
    $wikiElem.text("");
    $nytElem.text("");

    // load streetview

    // YOUR CODE GOES HERE!
    var streetVal = $('#street').val();
    var cityVal = $('#city').val();
    var addressStr = streetVal + ', ' + cityVal

    $greeting.text('So, you want to live at ' + addressStr + '?');

    var streetURL = "http://maps.googleapis.com/maps/api/streetview?size=500x200&location=" + addressStr

    $body.append('<img class="bgimg" src="'+ streetURL + '">');

    strNYAPIKey = "0c5e018731cf44268c73430cc664e55f"

    //strNYAPIKey = 'badkey'

    var nyTimesURL = "https://api.nytimes.com/svc/search/v2/articlesearch.json";    
    nyTimesURL = nyTimesURL + '?q=' + cityVal + '&sort=newest&api-key=' + strNYAPIKey;

    console.log(nyTimesURL);

    $.getJSON(nyTimesURL, function(data){
        $nytHeaderElem.text('New York Times Articles About ' + cityVal);
        articles = data.response.docs;
        for(var i = 0; i < articles.length; i++){
            var article = articles[i];
            $nytElem.append('<li class="article">' +
                '<a href="'+ article.web_url+ '">' + article.headline.main+'</a>' +
                '<p>' + article.snippet + '</p>' +
                '</li>');
        };
    }).error(function(e){
        console.log(e)
        $nytHeaderElem.text('New York Times Articles Could Not Be Loaded' + e.toString());
    })


    return false;
};

$('#form-container').submit(loadData);
