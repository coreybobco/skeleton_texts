onload = function(){
	var show_output = function() { 
	    var active_output = document.querySelector("#skeletons").querySelector(".active").querySelector("textarea");
	    active_output.value = this.responseText;
	}
	var add_frequency_scale_button = document.querySelector("#add_frequency_scale_button");
	add_frequency_scale_button.onclick = function() {
		var text_choice = document.querySelector("#frequency_scale_text_select").value;
		var frequency = document.querySelector("#frequency_scale_frequency").value;
		var insertion = "{frequency_scale(" +text_choice + "," + frequency +")}";
		insertBuildingBlock(insertion);
	}
	var portmanteau_button = document.querySelector("#add_portmanteau_button");
	portmanteau_button.onclick = function() {
		var text_choice = document.querySelector("#portmanteau_text_select").value;
		var filter_portmanteau = document.querySelector("#filter_portmanteau_source").checked;
		var insertion = "{portmanteau(" + text_choice + ", " + filter_portmanteau + ")}";
		insertBuildingBlock(insertion);
	}
	var generate_body_button = document.querySelector("#generate_body_button");
	generate_body_button.onclick = function () {
		var file_reader = new FileReader;
		$("input[type=file").each(function() {
			// file = 
		});
		var request_obj = {}
		var request_obj.skeleton = document.querySelector("#skeletons").querySelector(".active").querySelector("textarea").value;
		for (var i=0; i < file_contents.length; i++){
			request_obj['file_' + i] = file_contents[i];
		}
		var request_json = JSON.stringify(request_obj);
		var request = new XMLHttpRequest()
		request.addEventListener("load", show_output)
		request.open("post", "./generate", true)
		request.send(request_json)
	}
} 

function insertBuildingBlock(insertion) {
	var textarea = document.querySelector("#skeletons").querySelector(".active").querySelector("textarea");
	textarea.value = textarea.value + " " + insertion;
}