function countingValleys(n, s) {
	//n = number of steps
	//s = array of step topography. U = uphill, D = downhill

	//split path into array
	s = s.split("")

	//variables to track
	let level = 0;
	let valley = false;
	let valleyCount = 0;

	//loop through path
	for(let i in s){

		//increase or decrease level depending on path#
		s[i] == 'U' ? level++ : level--;

		//keep track if in a valley
		if(level < 0) valley = true;
		//add to valley count each time path comes to level0
		else if(valley && level == 0){
			//switch out of valley and add to count
			valley = false;
			valleyCount++;
		}
	}

	// console.log(valleyCount)
	return valleyCount;
}

// countingValleys(8, ['U','D','D','D','U','D','U','U'])
countingValleys(10, 'DUDDDUUDUU')