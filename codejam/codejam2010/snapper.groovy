/*
 * URL: http://code.google.com/codejam/contest/dashboard?c=433101#s=p0
 * Solution to snapper problem
 */


def inputText = '''4
1 0
1 1
4 0
4 47'''



//def lst = new File("/opt/codeJam/practice/A-large-practice.in").readLines()
def lst = inputText.readLines()

int testCaseCount = Integer.parseInt(lst[0])
println "Test Case count: ${testCaseCount}"

def compute(Integer n, Integer k) {
    
    return ((k+1) % (2**n) == 0) ? "ON": "OFF";
    
}
//new File("/opt/codeJam/practice/A-large-practice.result").withWriter { writer-> 
    for (i in 1..testCaseCount) {
        n  = Integer.parseInt(lst[i].split(" ")[0])
        k = Integer.parseInt(lst[i].split(" ")[1])
        
        println "Case#${i}: ${compute(n,k)}"
        //writer << "Case #${i}: ${compute(n,k)}\r\n"
        
        
    }
//}

println "Done"

​
