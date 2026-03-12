async function fetchData(){

let res = await fetch("/data")
let data = await res.json()

document.getElementById("soil").innerText = data.soil + " %"
document.getElementById("temp").innerText = data.temperature + " °C"
document.getElementById("humidity").innerText = data.humidity + " %"
document.getElementById("rain").innerText = data.rain ? "Yes" : "No"
document.getElementById("pump").innerText = data.pump

}

setInterval(fetchData,2000)