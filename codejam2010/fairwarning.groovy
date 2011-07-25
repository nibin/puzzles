/*
 * http://code.google.com/codejam/contest/dashboard?c=433101#s=p1
 * Solution to fair warning problem
 */
def inputText = '''3
3 26000000 11000000 6000000
3 1 10 11
2 800000000000000000001 900000000000000000001'''


//def lst = new File("/opt/codeJam/practice/B-large-practice.in").readLines()
def lst = inputText.readLines()

int testCaseCount = Integer.parseInt(lst[0])
println "Test Case count: ${testCaseCount}"

def compute(Integer n, List aList) {
    
    BigInteger gCd = new BigInteger("0")
    sortedList = aList.sort()
    diffList = []
    for(i in 0..<sortedList.size()) {
        if( (i+1) < sortedList.size() ) {
            BigInteger a = sortedList[i]
            BigInteger b = sortedList[i+1]
            BigInteger c = b.subtract(a)
            diffList.add(c)
        }
    }
    
    if(diffList.size() == 1 )
        gCd = diffList[0]
    else
    {
        gCd = diffList[0]
        diffList[1..<diffList.size()].each {
            gCd = gCd.gcd(it)
            
        }
        
    }
    
    BigInteger result = (-sortedList[0]) + (sortedList[0].divide(gCd) *(gCd))
    if (result < new BigInteger("0")) {
        result = (-sortedList[0]) + ((sortedList[0].divide(gCd).add(new BigInteger("1"))) *(gCd))
    }
    
    return result
    
}

//new File("/opt/codeJam/practice/B-large-practice.result").withWriter { writer-> 
    for (i in 1..testCaseCount) {
        n  = Integer.parseInt(lst[i].split(" ")[0])
        aList = []
        for(j in 1..n) {
            //aList.add(Integer.parseInt(lst[i].split(" ")[j]))
            aList.add(new BigInteger(lst[i].split(" ")[j]))
        }
        
        
        println "Case #${i}: ${compute(n,aList)}"
        //writer << "Case #${i}: ${compute(n,aList)}\r\n"
        
        
    }
//}

println "Done"
​
