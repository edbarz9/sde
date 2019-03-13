var newPalette
var newPalName = "custom"

function setcolors() {
  var fsc0 = document.querySelector("#c0").value;
  var fsc1 = document.querySelector("#c1").value;
  var fsc2 = document.querySelector("#c2").value;
  var fsc3 = document.querySelector("#c3").value;
  var fsc4 = document.querySelector("#c4").value;
  var fsc5 = document.querySelector("#c5").value;
  var fsc6 = document.querySelector("#c6").value;
  var fsc7 = document.querySelector("#c7").value;
  var fsc8 = document.querySelector("#c8").value;
  var fsca = document.querySelector("#ca").value;
  var newPalName = document.querySelector("#pal").value;
  document.documentElement.style.setProperty('--c0a', parseInt(fsca)/10);
  document.documentElement.style.setProperty('--c0', fsc0);
  document.documentElement.style.setProperty('--c1', fsc1);
  document.documentElement.style.setProperty('--c2', fsc2);
  document.documentElement.style.setProperty('--c3', fsc3);
  document.documentElement.style.setProperty('--c4', fsc4);
  document.documentElement.style.setProperty('--c5', fsc5);
  document.documentElement.style.setProperty('--c6', fsc6);
  document.documentElement.style.setProperty('--c7', fsc7);
  document.documentElement.style.setProperty('--c8', fsc8);
  document.documentElement.style.setProperty('--c0r', parseInt(fsc0[1]+fsc0[2], 16));
  document.documentElement.style.setProperty('--c0g', parseInt(fsc0[3]+fsc0[4], 16));
  document.documentElement.style.setProperty('--c0b', parseInt(fsc0[5]+fsc0[6], 16));
  document.documentElement.style.setProperty('--c0b', parseInt(fsc0[5]+fsc0[6], 16));

  newPalette = newPalName+`)
    SC0="`+ fsc0.replace("#","")  +`" #BackGround
    SC1="`+ fsc1.replace("#","")  +`" #Red
    SC2="`+ fsc2.replace("#","")  +`" #Green
    SC3="`+ fsc3.replace("#","")  +`" #Yellow
    SC4="`+ fsc4.replace("#","")  +`" #Blue
    SC5="`+ fsc5.replace("#","")  +`" #Pink
    SC6="`+ fsc6.replace("#","")  +`" #Cyan
    SC7="`+ fsc7.replace("#","")  +`" #ForeGround
    SC8="`+ fsc8.replace("#","")  +`" #System
    ;;`
  document.querySelector("#custom-palette").innerHTML = "<pre>" + newPalette + "</pre>"
  savefile()
}

function savefile(){
	uriContent = "data:application/octet-stream," + encodeURIComponent(newPalette);
	document.getElementById("dlink").innerHTML = "<a href=" + uriContent + " download=\""+ newPalName +"\">Download</a>";
}

var desert = {
  sc0:"#1a1813",
  sc1:"#cc3623",
  sc2:"#588054",
  sc3:"#ffff5d",
  sc4:"#596c80",
  sc5:"#b34c48",
  sc6:"#257a99",
  sc7:"#e6d7a8",
  sc8:"#767160"
};

document.getElementById("palfill01").innerHTML = `
    <td>SC1 (Red)</td>
    <td><input type="color" id="c1" value="#e73a3a"></td>
<td></td>
<td></td>
<td style="background-color: `+ desert.sc0 +`">&nbsp;&nbsp;</td>
<td style="background-color: `+ desert.sc1 +`">&nbsp;&nbsp;</td>
<td style="background-color: `+ desert.sc2 +`">&nbsp;&nbsp;</td>
<td style="background-color: `+ desert.sc3 +`">&nbsp;&nbsp;</td>
<td style="background-color: `+ desert.sc4 +`">&nbsp;&nbsp;</td>
<td style="background-color: `+ desert.sc5 +`">&nbsp;&nbsp;</td>
<td style="background-color: `+ desert.sc6 +`">&nbsp;&nbsp;</td>
<td style="background-color: `+ desert.sc7 +`">&nbsp;&nbsp;</td>
<td style="background-color: `+ desert.sc8 +`">&nbsp;&nbsp;</td>
`










