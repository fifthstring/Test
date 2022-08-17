var counter = 5
click = 1
document.getElementById('button').onclick = function(){cookie()}
function cookie(){
    counter += click
    document.getElementById('counter').innerHTML = counter
}
toadd = 0
var buttons = document.getElementById("button").innerHTML = '<img src="cookieclicker.jpeg" />';

jobs = [['baker',50,2],['bakery',350,8],['factory',1000,25],['company',5000,100],['conglomerate',12000,250],['monopoly',100000,4000],['potato farmer',1500000,20000],['paperclip factory',10000000,190000],['god',80000000,1000000],['titan',500000000,100000000000],['bonus clicker',1000,5]]

function structure(i){
    console.log(jobs[i])
    if(counter >= jobs[i][1] && jobs[i][0] != 'bonus clicker'){
        counter -= jobs[i][1]
        toadd += jobs[i][2]
        jobs[i][1] *= 1.3
    jobs[i][1] = Math.round(jobs[i][1])
    }
    else if(counter  >= jobs[i][1]){
        counter -= jobs[i][1]
        jobs[i][1] *= 1.3
        jobs[i][1] = Math.round(jobs[i][1])
        click += jobs[i][2]
    }
    gendiv()
}
var masterdiv=  document.createElement('div')
masterdiv.className = 'masterdiv'
function gendiv(){
masterdiv.innerHTML = ''
for (var i in jobs){
    p = document.createElement('button')
    p.id = String(i)
    
    p.innerHTML = jobs[i][0] + '<br>cost:'+jobs[i][1] + '<br>'+jobs[i][2]
    p.onclick = function(){structure(this.id)}
    p.className = 'block'
    if(jobs[i][0] == 'bonus clicker'){
        p.style.backgroundColor = 'rgb(0,0,0)'
        p.style.color = 'white'
        p.innerHTML += ' per click'
    }
    else{
        p.innerHTML += ' per second'
    }


    





    masterdiv.appendChild(p)}
document.body.appendChild(masterdiv)
}
gendiv()
var x = setInterval(function(){
    counter += toadd
    document.getElementById('cps').innerHTML = String(toadd)+' per second'
    document.getElementById('counter').innerHTML = counter
},1000)
