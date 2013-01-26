/*
 * http://code.google.com/codejam/contest/dashboard?c=433101#s=p2
 *  Solution to theme park problem
 *  
 * Note: This code took 9 mins to generate results for the large data set.
 *  
 * 
 */

def inputText = '''3
4 6 4
1 4 2 1
100 10 1
1
5 5 10
2 4 2 3 4 2 1 2 1 3'''



//def lst = new File("/opt/codeJam/practice/C-large-practice.in").readLines()
def lst = inputText.readLines()

int testCaseCount = Integer.parseInt(lst[0])
println "Test Case count: ${testCaseCount}"

def compute(Long r, Long k, Integer g, List aList) {
    long cost = 0
    Map indexTosums = [:]
    Map currToNxtPointer = [:]
    int pos = 0
    
    int currentPointer = 0
    int nextPointer = 0
    boolean escapeItAll = false
    
    while(true) { 
        long tempSum = 0
        int groupCount = 0
        escapeItAll = false
        while( tempSum <= k) {
            if(groupCount < g) {
                tempSum += aList[pos]
                pos = (pos+1) % aList.size()
                groupCount++
            }
            else
            {
                escapeItAll = true
                break
            }
        }
        
        if(tempSum > k) {
            pos = (aList.size() + (pos - 1)) % aList.size()
            tempSum -= aList[pos]
        }
        
        
        if(indexTosums.keySet().contains(currentPointer)) {
            //println
            break
        }
        else {
            
            indexTosums.put(currentPointer, tempSum)
            nextPointer = pos
            currToNxtPointer.put(currentPointer, nextPointer )
            currentPointer = pos
        }
        
    }
    
    /*
    println "Debug index to sums"
    indexTosums.each { entry->
        println "${entry.key} ==> ${entry.value}"
    }
    
    println "Debug current to next"
    currToNxtPointer.each { entry->
        println "${entry.key} ==> ${entry.value}"
    }
    */
    
    if(escapeItAll) {
        cost = r * indexTosums.get(0)
    }
    else
    {
        int cursor = 0
        for(i in 0..<r) {
            cost += indexTosums.get(cursor)
            cursor = currToNxtPointer.get(cursor)
            
            /* This code part can be improved if I find the number of nodes in 
             * cyclical pattern and
             * multiply it with the remaining rounds   
             */
        }
    }
    
    return cost
    
    
}

int m = 1
//new File("/opt/codeJam/practice/C-large-practice.result").withWriter { writer-> 
for (i=1; i<lst.size(); i+=2) {
    
    r = Long.parseLong(lst[i].split(" ")[0])
    
    k = Long.parseLong(lst[i].split(" ")[1])
    g = Integer.parseInt(lst[i].split(" ")[2]) // max 1000
    
    
    aList = []
    for(j in 0..<g) {
        aList.add(Long.parseLong( lst[i+1].split(" ")[j] ))
        
    }
    println "Case #${m}: ${compute(r, k, g, aList)}"
    //writer << "Case #${m}: ${compute(r, k, g, aList)}\r\n"
    m +=1
    
}
//}

println "Done"

​
