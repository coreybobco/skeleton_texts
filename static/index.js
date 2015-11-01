onload = function(){
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
	var generate_body_button = document.querySelector("generate_body_button");
	generate_body_button.onclick = function () {
		var file_reader = new FileReader;
		$("input[type=file").each(function() {
			// file = 
		});
		var skeleton = document.querySelector("#skeleton_tabs").querySelector(".active").querySelector("textarea").value;
	}
} 

function insertBuildingBlock(insertion) {
	var textarea = document.querySelector("#skeleton_tabs").querySelector(".active").querySelector("textarea");
	textarea.value = textarea.value + " " + insertion;
}

function 