import { initializeApp } from "https://www.gstatic.com/firebasejs/9.6.11/firebase-app.js";
import {getFirestore,collection, getDoc, doc} from"https://www.gstatic.com/firebasejs/9.6.11/firebase-firestore.js";
import credentials from "./credentials.js";



const app=initializeApp(credentials);
const db = getFirestore(app);  

const sensors =collection(db,"sensors");
const sensorsData = doc(sensors,"0");
const storico=collection(db,"storico");



var iterations=2;
var storedValue=-1
var updating=0

const updateChecker=(doc)=>{
    
    if(doc.data().updating!==storedValue && storedValue!==-1){
        updating=1;
        iterations=0;
    }

    else if(iterations<2){
        iterations++;
        updating=1;
    }
    else if(iterations<5){
        iterations++;
        updating=0;
    }
    else{
        updating=-1;
        iterations=5;
    }
    storedValue=doc.data().updating;
}

let current

function getDb(){
    return getDoc(sensorsData).then(function(doc){
        current={hum: doc.data().hum,
        light:  doc.data().light,
        temp:  doc.data().temp}
    });
}

function getStorico(){
    let temp=[];
    for(let i=0;i<10;i++){
        let docData=doc(storico,i.toString());
        getDoc(docData).then(function(doc){
            temp.push({temp:doc.data().temp,hum:doc.data().hum,light:doc.data().light,time:doc.data().time});
        }
    );
    }
    return temp;
}




export { current }
export { getStorico }
export { updating }

setInterval(()=>{
    getDoc(sensorsData).then(function(doc){
        updateChecker(doc);
        
    });
    getDb();
}
,2000);