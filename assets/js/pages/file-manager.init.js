function getChartColorsArray(e){if(null!==document.getElementById(e)){e=document.getElementById(e).getAttribute("data-colors");if(e)return(e=JSON.parse(e)).map(function(e){var t=e.replace(" ","");return-1===t.indexOf(",")?getComputedStyle(document.documentElement).getPropertyValue(t)||t:2==(e=e.split(",")).length?"rgba("+getComputedStyle(document.documentElement).getPropertyValue(e[0])+","+e[1]+")":t})}}var options,chart,radialChartColors=getChartColorsArray("radial-chart");radialChartColors&&(options={series:[76],chart:{height:150,type:"radialBar",sparkline:{enabled:!0}},colors:["#556ee6"],plotOptions:{radialBar:{startAngle:-90,endAngle:90,track:{background:"#e7e7e7",strokeWidth:"97%",margin:5},hollow:{size:"60%"},dataLabels:{name:{show:!1},value:{offsetY:-2,fontSize:"16px"}}}},grid:{padding:{top:-10}},stroke:{dashArray:3},labels:["Storage"]},(chart=new ApexCharts(document.querySelector("#radial-chart"),options)).render());