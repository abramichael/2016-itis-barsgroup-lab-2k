function addToList() {
	var o = document.getElementById("person-name");
	var lst = document.getElementById("list");
	lst.innerHTML += "<p>" + o.value + "<br/>";
	lst.innerHTML += "<i>on " + (new Date()) + "</i></p>";
	o.value = "";

}