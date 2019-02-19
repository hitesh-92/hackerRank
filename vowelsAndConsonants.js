function vowelsAndConsonants(s) {

	let result = '';
	let cons = '';
	const vowels = ['a', 'e', 'i', 'o', 'u'];

	//split string
	s = s.split("");

	//initial loop for only vowels
	for (let i in s) for (let v in vowels){
		if (s[i] == vowels[v]) result += s[i] + '\n';
	}

	//remove all vowels from array
	for (let v in vowels) s = s.filter(val => val !== vowels[v])

	//add all remaining to result in order
	for (let i in s) result += s[i] + '\n';

	// return result
	console.log(result)
}


vowelsAndConsonants('javascriptloops')

// x = [1,2,3,4,5,6,7,8,9]
// x.splice(4,1)
// console.log(x)