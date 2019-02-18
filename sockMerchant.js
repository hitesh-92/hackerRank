function sockMerchant(n, ar) {
    
    //n = number of socks [e.g 7]
    //ar = array of sock colors [e.e 1,2,1,2,1,3,2] //2 pairs
    let result = 0;

    //array of unique socks
    const unique = ar.filter((v,i,a) => a.indexOf(v) === i);

    //loop unique sock color
    for(i in unique){

    	//track count
    	let match = 0;

    	//find number of matches
    	for(n in ar) if(unique[i] == ar[n]) match++;

    	//if 1 extra remove - no match
    	if(match%2 == 1) match--;

    	//pair so div by 2 and add
    	result += match / 2;
    }
    
    return result
}


sockMerchant(9, [10, 20, 20, 10, 10, 30, 50, 10, 20])