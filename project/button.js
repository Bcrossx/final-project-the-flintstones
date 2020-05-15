
function getInput() {
	var myInput = document.getElementById("word").value;
	//alert("Your word is " + myInput)
	matchInput();
  }
 function matchInput() {

	let userInput = document.getElementById("word").value;
	let neededInput = "FreDerick!";
	let oglength = neededInput.length;
	let uiLength = userInput.length;
	if(uiLength != oglength) {
		alert("You entered the wrong phrase, you might be a phony!!");
	}
	else {
		let result = userInput.match(/FreDerick!/g);
		if(!result) {
			alert("You entered the wrong phrase, you might be a phony!!");
		}
		else {
			alert("You entered the correct phrase!");
		}
	}
  }
