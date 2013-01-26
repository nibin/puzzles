/**
 *
 * http://code.google.com/codejam/contest/32003/dashboard
 *
 */

def inputText = '''5
eEEeeeEEeeeEeE...E E.e !0TtKXJ]hZi_|Q8sg[>~DNAnWx$Gf%,k"2L&ydYB
FmM -)m^&U@FM f_
9 0123456789 oF8
Foo oF8 0123456789
13 0123456789abcdef 01
CODE O!CDE? A?JM!.'''

def lst = new File("/mnt/data1/workspaces/funWx/puzzles/data/A-large-practice.bin").readLines()
//def lst = inputText.readLines()

def getIndex(String c, String value) {
	for(i in 0..<value.size()) {
		if(c.equals(value[i]))
			return i
	}
}

def getDecimelValue(String alienNumber, String sourceSet) {

	int base = sourceSet.size()
	int length = alienNumber.size()
	int decValue = 0
	int pow = 0
	for(i in length-1..0) {
		int idx = getIndex(alienNumber[i], sourceSet)

		decValue = decValue + (idx * Math.pow(base, pow))
		//println("DEBUG: idx: ${idx} decValue: ${decValue}")
		pow += 1
	}

	return decValue

}

def compute(String alienNumber, String sourceSet, String targetSet) {

	int num = getDecimelValue(alienNumber, sourceSet)
	int K = targetSet.size()
	String digit = ""
	while ( num != 0 )  {
       int remainder = num % K ;  // assume K > 1
       num       = num / K ;  // integer division
       digit = digit + String.valueOf(remainder) + "-"
    }

    //println("AlienNumber: ${alienNumber} SourceSet: ${sourceSet} TargetSet: ${targetSet} Digit: ${digit} DecV: ${getDecimelValue(alienNumber, sourceSet)}")

    String targetNumber = ""
    String[] digSplits = digit.split("-")
    for(i in digSplits.length-1..0) {    	
    	targetNumber += targetSet[Integer.valueOf(digSplits[i])]
    }

    return targetNumber
}

int testCaseCount = Integer.parseInt(lst[0])
println "Test Case count: ${testCaseCount}"



new File("/mnt/data1/workspaces/funWx/puzzles/data/A-large-practice.result").withWriter { writer-> 
	for (i in 1..testCaseCount) {
	    
	    String[] splits = lst[i].split(" ")
	    String alienNumber = splits[0]
	    String sourceSet = splits[1]
	    String targetSet = splits[2]
	    //println "Case #${i}: ${compute(alienNumber, sourceSet, targetSet)}"
	    writer << "Case #${i}: ${compute(alienNumber, sourceSet, targetSet)}\r\n"    
	}
}

println "Done"