function httpGet(name,last_call)
{
    var xmlHttp = null;

    var URL = '/'+name+'/get/last_call='+last_call;
    xmlHttp = new XMLHttpRequest();
    xmlHttp.open( "GET", URL, false );
    xmlHttp.send(null);
    console.log(XMLHttp.responseText);
    return xmlHttp.responseText;
}