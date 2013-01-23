def quickSort(int[] arr, int low, int high) {

    int i = low
    int j = high
    
    int pivot = arr[low + (high-low)/2]
    
    while (i <=j) {
    
        while(arr[i] < pivot) i++
        while(arr[j] > pivot) j--
        
        if(i <=j ) {
            swap(arr, i, j)
            i++
            j--        
        }
    }
    //println("pivot is ${pivot}")
    if (low < j) quickSort(arr, low, j)
    if(i < high) quickSort(arr, i, high)
    return arr
}

def swap(int[] arr, int i, int j) {

    int temp = arr[i]
    arr[i] = arr[j]
    arr[j] = temp
    
    return arr

}

int[] a = [4,2,1,10,5,6,22]

quickSort(a, 0, a.length -1)