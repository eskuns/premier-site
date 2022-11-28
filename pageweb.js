var i=1;
function changeimage(){
	image=document.getElementById("logo");
	if (i==0){
			image.setAttribute("src","logotdc.jpg");
			i=1;
		}
	else {
			image.setAttribute("src","logo1.jpg");
			i=0;
		}

}

function changecolor(){
	document.getElementById("1").style.color="red";
	document.getElementById("2").style.color="green";
	document.getElementById("3").style.color="red";
	document.getElementById("4").style.color="green";
	document.getElementById("5").style.color="red";
	document.getElementById("6").style.color="#fbc02b";
}

function inverse(){
	if ( document.body.style.backgroundColor == "white"){
		document.body.style.backgroundColor = "grey";
		document.body.style.color = "white";
	}else{
		document.body.style.backgroundColor = "white";
		document.body.style.color = "grey";
	}
}

function textechange(){
	document.getElementById("passion").innerHTML="oui oui je suis un geek un vrai";
}

function changeimage2(){
	image=document.getElementById("tim");
	if (i==0){
			image.setAttribute("src","TBLimg.jpg");
			i=1;
		}
	else if (i==1){
			image.setAttribute("src","tim2.jpg");
			i=2;
		}
	else if (i==2){
			image.setAttribute("src","tim3.jpg");
			i=3;
		}
	else if (i==3){
			image.setAttribute("src","tim4.jpg");
			i=0;
	}

}

function alerte(){
	document.getElementById("titre");
	alert("Vous voici chez moi, restez autant de temps que vous le voudrez ^^.");
}

function fontsize(value){
	document.getElementById("pro").style.fontSize = value;
}

function changepolice(){
        var police=document.getElementById("police").value;
		document.body.style.fontSize=police;
}