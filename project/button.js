var tries = 3;
function getInput() {
	var myInput = document.getElementById("word").value;
	matchInput(correctInput);
  }

 function matchInput(correct) {

	let userInput = document.getElementById("word").value;
	

	let oglength = correct.length;
	let uiLength = userInput.length;
	if(uiLength != oglength) {
		tries = tries - 1;
		if (tries > 0) {
			
			alert("You entered the wrong phrase, you might be a phony!!");
			document.getElementById("tries").innerHTML = "You have " + tries + " tries left."
			captchaGen()
		}
		else {
			window.location.href = "fail.html";
		}
	}
	else {
		
		if(!(correct == userInput)) {
			tries = tries - 1;
			if (tries > 0) {
				
				alert("You entered the wrong phrase, you might be a phony!!");
				document.getElementById("tries").innerHTML = "You have " + tries + " tries left."
				captchaGen()
			}
			else{
				window.location.href = "fail.html";
			}
		}
		else {
			window.location.href = "success.html";
		}
	}
  }

function captchaGen() {

	document.getElementById("tries").innerHTML = "You have " + tries + " tries."

	let src1 = "m_0.png";
	let src2 = "m_1.png";
	let src3 = "m_2.png";
	let src4 = "m_3.png";
	let src5 = "m_4.png";

	let srcs = [];

	let letters = [1, 2, 3, 4, 5];
	let randLetters = randomizeCap(letters);
	let populated = 0;
	var chosenLetter;
	correctInput = '';


	for (let i = 0; i < randLetters.length; i++) {
		populated = populated.toString();
		if(randLetters[i] == 1){
			correctInput = correctInput+'H';
			chosenLetter = document.getElementById("letter"+populated);
			srcs[i] = "m_0.png"; 
		} 
		else if(randLetters[i] == 2){
			correctInput = correctInput+'P';
			chosenLetter = document.getElementById("letter"+populated);
			srcs[i] = "m_1.png";
		}
		else if(randLetters[i] == 3){
			correctInput = correctInput+'U';
			chosenLetter = document.getElementById("letter"+populated);
			srcs[i] = "m_2.png";
		}
		else if(randLetters[i] == 4){
			correctInput = correctInput+'U';
			chosenLetter = document.getElementById("letter"+populated);
			srcs[i] = "m_3.png";
		}
		else if(randLetters[i] == 5){
			correctInput = correctInput+'E';
			chosenLetter = document.getElementById("letter"+populated);
			srcs[i] = "m_4.png";
		}

		populated = parseInt(populated, 10);
		chosenLetter.src = srcs[i];
		populated++;
	}




}


function randomizeCap(lettersArray) {
	let x, y;
    for (let i = lettersArray.length - 1; i > 0; i--) {

        x = Math.floor(Math.random() * (i + 1));
        y = lettersArray[i];
        lettersArray[i] = lettersArray[x];
        lettersArray[x] = y;
    }
    return lettersArray;
}