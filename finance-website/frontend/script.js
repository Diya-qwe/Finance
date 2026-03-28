function generateInputs(){

let n=document.getElementById("months").value;
let area=document.getElementById("monthInputs");

area.innerHTML="";

for(let i=1;i<=n;i++){

area.innerHTML+=`

<div class="card">
<h3>Month ${i}</h3>

Food <input id="food${i}">
Rent <input id="rent${i}">
Transport <input id="transport${i}">
Entertainment <input id="fun${i}">
Shopping <input id="shopping${i}">
</div>
`;
}
}

function submitData(){

let n=document.getElementById("months").value;

let months=[];

for(let i=1;i<=n;i++){

months.push({
month:i,
food:document.getElementById("food"+i).value,
rent:document.getElementById("rent"+i).value,
transport:document.getElementById("transport"+i).value,
fun:document.getElementById("fun"+i).value,
shopping:document.getElementById("shopping"+i).value
});
}

fetch("http://127.0.0.1:5000/calculate",{
method:"POST",
headers:{"Content-Type":"application/json"},
body:JSON.stringify({
salary:document.getElementById("salary").value,
goal:document.getElementById("goal").value,
months:months
})
})
.then(res=>res.json())
.then(data=>{

localStorage.setItem("financeData",JSON.stringify(data));

window.location.href="dashboard.html";
});
}