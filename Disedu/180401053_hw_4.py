def min_heapify(array, i):
    left = 2 * i + 1
    right = 2 * i + 2
    length = len(array) - 1
    smallest = i
    if left <= length and array[i] > array[left]:
        smallest = left
    if right <= length and array[smallest] > array[right]:
        smallest = right
    if smallest != i:
        array[i], array[smallest] = array[smallest], array[i]
        min_heapify(array, smallest)
#Parametre olarak alınan index ile  çocuklarını karşılaştırıp aralarından en küçüğünü bulur ve bunları sıralayan recursive işlemdir.
#Aldığı parametre bir dizidir.


def build_min_heap(array): 
    for i in reversed(range(len(array)//2)):  #reversed: tersten başlar, değerler azalır.
        min_heapify(array, i)
#Parametre olarak gönderilen dizideki tüm elemanlara heapify uygular.(Dizi Heap haline gelir.)
    

def heapsort(array):
    array = array.copy()
    build_min_heap(array)
    sorted_array = []
    for _ in range(len(array)):
        array[0], array[-1] = array[-1], array[0]
        sorted_array.append(array.pop())
        min_heapify(array, 0)
    return sorted_array
#Gönderilen dizideki kök ile son elemanın yeri değişir, son eleman yeni listeye eklenir, eski listeden silinir ve heapify yapılır.(küçükten büyüğe siralanmış olarak fonksiyondan alınır.)

def insertItemToHeap(HeapArray, item):
    HeapArray.append(item)
    index = len(HeapArray)-1
    if index <= 0:
        return HeapArray
    parent = (index-1)//2
    while parent >= 0 and HeapArray[parent] > HeapArray[index]:
        HeapArray[parent], HeapArray[index] = HeapArray[index], HeapArray[parent]
        index = parent
        parent = (index-1)//2
    return HeapArray
#Parametre olarak gönderilen diziye, yine parametre olarak gönderilen değeri ekleyen fonksiyon(Eğer eklenmek isteyen değer varsa uyarı döndürür.)
#En son dizi heap haline döner.




def removeItemFrom(myArray):
    length = len(myArray)
    if length == 0:
        print("Heap is Empty")
        return myArray
    heapedArray = heapsort(myArray)
    heapedArray[0], heapedArray[-1] = heapedArray[-1], heapedArray[0]
    heapedArray.pop()
    build_min_heap(heapedArray)
    return heapedArray
    
    #Parametre olarak aldığı diziye heapsort uygular. köküyle en son elemanının yerini değiştirir ve en küçük elemanı silerek heap dizisini yeniden oluşturur.
