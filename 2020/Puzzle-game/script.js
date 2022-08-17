//console.log('bruh')
function charcreate(xx,yy){
var x = document.createElement('img')
//x.innerHTML = '.'
//x.style.fontSize = '8vw'
x.style.position = 'absolute'
x.style.left = xx
//x.style.color = 'white'
x.style.width = '2%'
x.style.top = yy
x.src = 'download.jpeg'
x.id = 'char'
return x
}

function charcreate(xx,yy){
var x = document.createElement('p')
x.innerHTML = '.'
x.style.fontSize = '8vw'
x.style.position = 'absolute'
x.style.left = xx
x.style.color = 'white'
x.style.top = yy
x.id = 'char'
return x
}



var x = charcreate('80%','10%')
//document.body.appendChild(x)


function objective(x,y){barrie('60','20') 
objectivel = document.createElement('p')
objectivel.innerHTML = '.'
objectivel.style.fontSize = '8vw'
objectivel.id = 'objective'
objectivel.style.position = 'absolute'
objectivel.style.color = 'red'
objectivel.style.left = x + '%'
objectivel.style.top = y + '%'
return objectivel
}
var levels = [ 
[charcreate('80%','20%'), objective('50','20'), 80,20] ,[ ],
[charcreate('90%','0%'), objective('60','30'),90,10] ,[barrie('70','30') , barrie('80','30'),barrie('50','10') ,barrie('70','20')],
[charcreate('70%','20%'), objective('70','0'),70,20] ,[ ],
[charcreate('70%','20%'), objective('50','10'),70,20] ,[],[charcreate('70%','50%'), objective('50','0'),70,50] ,[],
[charcreate('90%','10%'), objective('40','10'),90,10] ,[barrie('70','10') , barrie('80','10') ],

[charcreate('80%','20%'), objective('50','20'), 80,20] ,[barrie('70','20') ],
[charcreate('70%','20%'), objective('50','10'),70,20] ,[barrie('60','20') ],
[charcreate('90%','10%'), objective('40','30'),90,10] ,[barrie('70','10') , barrie('80','10'),barrie('50','10') ,barrie('50','30')]

]

var curlev = 0

for (var i in levels[curlev]){
    try{
    document.body.appendChild(levels[curlev][i])}
    catch{}
}


function barrie(x,y,sm='|'){
objectiv = document.createElement('p')
objectiv.innerHTML = sm
objectiv.style.fontSize = '8vw'
objectiv.id = 'delete'
objectiv.style.position = 'absolute'
objectiv.style.color = 'yellow'
objectiv.style.left = x + '%'
objectiv.style.top = y + '%'
return objectiv

}

//barrier = barrie('60','10') 
//barriers = [ barrie('60','10'), barrie('60','30') , barrie('60','20'),barrie('50','30','___')]


var barriers = levels[curlev+1]

console.log(barriers)

obj = objective('80','10')

//document.body.appendChild(obj)
//document.body.appendChild(barrier)
var once = 0

//console.log(obj.style.top)
function showdot(){
    x.style.left = String(pos)+'%'
    x.style.top = String(ypos)+'%'
}
var pos = Number(document.getElementById('char').style.left.slice(0,-1))
var ypos = Number(document.getElementById('char').style.top.slice(0,-1))
opos = pos
oypos = ypos
function compile(){

var barriers = levels[curlev+1]
for(var i in barriers){
    document.body.appendChild(barriers[i])
}
var counter = 0
var pos = levels[curlev][2]
var ypos = levels[curlev][3]
var x = document.getElementById('char')
x.style.left = String(pos)+'%'
x.style.top = String(ypos)+'%'
function bar(p,yp,l,u,xory){
    result = []
    gg = false
    console.log(barriers,425235)
    if(barriers.length == 0){
        console.log('hubert')
        gg = true
    }
    for(var i in barriers){
        if(barriers.length != 0){
        console.log(Number(barriers[i].style.left.slice(0,-1)))

        console.log(132532534)
        console.log(pos)
        console.log('pos')
        dre= false
        if(pos == Number(barriers[i].style.left.slice(0,-1)))
        {
            tgt = true
        }
        else{
            tgt = false
        }
        console.log(tgt)
        if(pos - l >= 40 && pos - l <= 80){
            if( tgt == false){
                dre = true;
                result.push(true)
            }
        }
        if(pos - l >= 40 && pos - l <= 80 && barriers[i].style.top.slice(0,-1) != ypos && dre == false){
            result.push(true)
        }

        
    }
    else{

        gg = true

    }
    }
    console.log(result)
    console.log(barriers.length,result.length)
    if(barriers.length != result.length || gg == false && barriers.length == 0){console.log('bruh')}
    else{pos-=l;console.log(pos);showdot()}
}

function bary(p,yp,l,u,xory){
    result = []
    gg = false
    console.log(barriers,425235)
    if(barriers.length == 0){
        console.log('hubert')
        gg = true
    }
    for(var i in barriers){
        if(barriers.length != 0){
        console.log(Number(barriers[i].style.left.slice(0,-1)))

        console.log(132532534)
        console.log(pos)
        console.log('pos')
        dre= false
        if(ypos == Number(barriers[i].style.left.slice(0,-1)))
        {
            tgt = true
        }
        else{
            tgt = false
        }
        console.log(tgt)
        if(ypos - l >= -10 && ypos - l <= 80){
            if( tgt == false){
                dre = true;
                result.push(true)
            }
        }
        if(ypos - l >= -10 && ypos - l <= 80 && barriers[i].style.left.slice(0,-1) != pos && dre == false){
            result.push(true)
        }

        
    }
    else{

        gg = true

    }
    }
    console.log(result)
    console.log(barriers.length,result.length)
    if(barriers.length != result.length || gg == false && barriers.length == 0){console.log('bruh')}
    else{ypos-=l;console.log(pos);showdot()}
}
    data = document.getElementById('text').value.split('\n')
    //bpos = Number(barrier.style.left.slice(0,2))
    //by = Number(barrier.style.top.slice(0,2))
    //console.log(bpos)
    for (var i in data){
    if(data[i] == ''){
        data.splice(i,1)
    }

    }
    //console.log(data)

    for (var i in data){
        x = document.getElementById('char')

        if(data[i] == 'left'){
            xx = bar(pos,ypos,10,0,true)
         
            
            //console.log(xx)
            x = document.getElementById('char')
            x.style.left = String(pos)+'%'
            x.style.top = String(ypos)+'%'
            x.innerHTML = '.'


        }
        if(data[i] == 'right'){

            xx = bar(pos,ypos,-10,0,true)
            

            x.style.left = String(pos)+'%'
            x.style.top = String(ypos)+'%'
            x.innerHTML = '.'


        }


        if(data[i] == 'up'){
            
            bary(pos,ypos,10,0,true)
            //console.log(ypos)
            x.style.left = String(pos)+'%'
            x.style.top = String(ypos)+'%'
            x.innerHTML = '.'


        }


        if(data[i] == 'down'){
            bary(pos,ypos,-10,0,true)


            //console.log(ypos)
            x.style.left = String(pos)+'%'
            x.style.top = String(ypos)+'%'
            x.innerHTML = '.'


        }
    }
}

function check(){
var x = document.getElementById('char')
var obj = document.getElementById('objective')

if(x.style.left == obj.style.left){
    if(x.style.top == obj.style.top){
        //console.log('win')

        curlev += 2

        var x = document.getElementById('char')
        var obj = document.getElementById('objective')
       
        
    
        for(var i = 0; i < 10; i++){
            try{
                b = document.getElementById('delete')
                b.remove()
            }
            catch{
                break
            }
        }
        x.remove();
        obj.remove();
        for (var i in levels[curlev]){
            try{
                document.body.appendChild(levels[curlev][i])}
             catch{}        
        }

        console.log(levels[curlev+1],131039103901203901293)




        
    var barriers = levels[curlev+1]
    for(var i in barriers){
        document.body.appendChild(barriers[i])
    }
    
    }
}


}

function shi(){
var f = setInterval(function(){ check() }, 500);
}
shi()
