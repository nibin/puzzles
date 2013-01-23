/**
 * Edit distance algorithm
 */
def editDistance(String s1, String s2) {

    int len1 = s1.size()
    int len2 = s2.size()
    
    int[][] arr = new int[len1+1][len2+1]
    
    for(int i=0;i<=len1; i++) {
        
        arr[i][0] = i
    }
    
    for(int j=0;j<=len2; j++) {
        
        arr[0][j] = j
    }
    
   
    
    for (i=1;i<=len1; i++) {
        for(j=1; j<=len2; j++) {
            if(s1.charAt(i-1) == s2.charAt(j-1)) {
                arr[i][j] = arr[i-1][j-1]
            } else {
                arr[i][j] = minimum(arr[i][j-1]+1, arr[i-1][j]+1, arr[i-1][j-1]+1)                
            }
        
        }
    }
    
   //printArr(arr, len1+1, len2+1)
   
   return arr[len1][len2]

}

def minimum(int a, int b, int c) {

    int min = a
    if(b < min) 
        min = b
    if(c < min)
        min = c
        
    return min
}
def printArr(int[][] arr, int row, int col) {

    for(int i=0; i< row; i++) {
        println()
        for(int j=0; j<col; j++) {
            print(arr[i][j] + " ")        
        }
    
    }
    println()
}

//editDistance("hello","kello")
assert (1 == editDistance("hello","kello"))
assert (2 == editDistance("helloo","kello"))