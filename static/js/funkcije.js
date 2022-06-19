
function promeniDatum(){
console.log('promeniDatum')
    var datum = document.getElementById("datum");
    window.location.replace(window.location.pathname + `?datum=${datum.value}`);
}