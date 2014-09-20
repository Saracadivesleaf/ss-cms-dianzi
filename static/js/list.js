function displaySubMenu(li) { 
	var subMenu = li.getElementsByTagName("ul")[0]; 
	var menuTop = li.getElementsByTagName("a")[0];
	subMenu.style.display = "block"; 
	menuTop.style.background = "#00468C";
	menuTop.style.color = "#FFFFFF";
} 
function hideSubMenu(li) { 
	var subMenu = li.getElementsByTagName("ul")[0];
	var menuTop = li.getElementsByTagName("a")[0];
	subMenu.style.display = "none";
	menuTop.style.background = "#FFFFFF";
	menuTop.style.color = "#000000";
} 