/**
 * HeapSort algorithm in groovy
 * 
 */

def heapSort(int[] arr) {
    
    constructHeap(arr)
    
    int end = arr.length - 1
    
    while(end > 0) {
    
        int temp = arr[0]
        arr[0] = arr[end]
        arr[end] = temp
        bubbleDown(arr, 0, end - 1)
        end--
        //printHeap(arr)
    }
    
    return arr  

}
/**
 * Constructs heap data structure
 */
def constructHeap(int[] arr) {

    int start = arr.length/2  - 1
    int end = arr.length - 1
    
    //printHeap(arr)
    while(start >= 0) {
        bubbleDown(arr, start, end)
        //printHeap(arr)
        if (start == 0) break
        start--    
    } 
}

/* 
 * Bubble down lower values. Root will have the highest
 * number 
 */
def bubbleDown(int[] arr, int start, int end) {

    int root = start
    // take the last parent
    while ((root*2) +1 <= end) {
        
        int swap = root
        int lchild = (root *2) + 1
        int rchild = (root *2) + 2
        
        if (arr[swap] < arr[lchild]) {
            swap = lchild
        }
        
        if(rchild <= end && arr[swap] < arr[rchild]) {
            swap = rchild        
        }
        
        if(swap != root) {
            int temp = arr[root]
            arr[root] = arr[swap]
            arr[swap] = temp
            root = swap
        } else {
            return arr
         } 
    }
    
    return arr
}

def printHeap(int[] arr) {
    //println()
    arr.each {
        print(" ${it}")
    }
    println()
}

int[] a = [4,2,1,55,33,22,45,33,212123,232,2,222,1]

int[] b = heapSort(a)
printHeap(b)