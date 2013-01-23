/**
 * Merge sort in groovy
 */

def mergeSort(int[] arr, int low, int high) {

    if (low < high) {
        
        int middle = low + (high - low)/2 ;
        mergeSort(arr, low, middle)
        mergeSort(arr, middle + 1, high)
        merge(arr, low, middle, high)
    }
    
    return arr; 

}

def merge(int[] arr, int low, int middle, int high) {

    List arrCp1 = arr[low..middle]
    List arrCp2 = arr[middle+1..high]
    int i = low
    int j = 0
    int k = 0
    while(arrCp1.size() > 0 && arrCp2.size() > 0) {
        
        if (arrCp1.get(j) < arrCp2.get(k) ) {
            arr[i] = arrCp1.get(j)
            arrCp1.remove(j)
            //j++
            i++
        } else {
            arr[i] = arrCp2.get(k)
            arrCp2.remove(k)
            //k++
            i++        
        }
    }
    
    arrCp1.each {
        arr[i++] = it
    }
    
    arrCp2.each {
        arr[i++] = it
    }
    
    return arr

}

int[] a = [4,5,2,3,10,8,9,6,5,55,34]

println(mergeSort(a, 0, a.length -1))
