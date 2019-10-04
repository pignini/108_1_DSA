# 108_1_Data Structure and Algorithm
I'm 汶穗。Here is my weekly learning notes. :)
  * My [Learning check😀](https://hackmd.io/PFMjkciiRYuTuaYk77Be8Q?both)(Other related topics also put there.)
  * My [CS50 notes🖋](https://github.com/okpersist/CS50/tree/master/2013fall)

# Content
- [week 2](#week-2)
- [week 3](#week-3)
- [week 4](#week-4)

# week 2
 > Topic: Design a linked list

1. What's class?
    * Class，中文常稱類別，可視為創造物件的藍圖或模板。
    * Class描述了目標物件的屬性和方法。舉例來說，我們可以創建一個叫做**狗**的類別，在這個類別中設定屬性比如說品種、名字、年齡。如此一來，每個透過**狗**類別設定的個體，都會具有這兩個屬性。
    * 當我們想創造一隻2歲、名為可可的柴犬，可以在類別設定品種名、名字、年齡三個屬性，使系統自動幫我們創造一隻品種為柴犬、名為可可、年齡兩歲的狗狗。
    * 我們也可以在class設定方法，指定狗狗可以做出的動作，比如裝死、坐下，這樣用前述步驟創造完一個狗狗實體後，我們可以用`名稱.坐下`的方式讓狗狗在系統裡執行坐下。這樣每次在創造一隻新狗狗，或請狗狗執行動作的時候，就不用大費周章重新寫程式，傳入參數或在名稱後加上屬性的方式即可簡單的讓程式運作。

2. What's a linked-list?
   * linked-list由節點`node`與指南`pointer`組成，節點是資料實際存放的點，可散落在記憶體的不同位置，透過指南可以從第一個節點走訪到下一個節點，達成有效利用記憶體空間的目的。
   * 不同於array，array在記憶體中佔去連續的位置，但無法活用零碎的記憶體位置進行連結。
 
3. > My ideas about design a linked-list:
   >> 目前已經寫出想法，但跑出的值是錯誤的，還在找尋邏輯上不對或缺失的地方。
   * 創造`Mylinkedlist`和`node`兩個類別，在`Mylinkedlist`的`def __init__()`中定義自動創立一節點node.val=None以及有走訪功能的node.next來在後續方便找出第一個節點
   * 實際在`addAtHead(val)`從*頭*加入第一個節點，自動把節點值令為傳入的數值，以及建立好該節點的指南指到`None`
   * 透過`addAtTail(val)`從*尾端*加入第二個節點，並且把第二個節點的前一個元素指南到這個節點。
   * 透過`addAtIndex(val)`從*指定的位置*加入節點，並且把該位置的前一個位置的節點指南到此節點，並把此節點指南到下個節點。
   * 透過`get(index)`找到指定位置對應的值
   * 透過`deleteAtIndex(index)`刪除指定位置對應的值
   * 再次透過`get(index)`找到更新linked-list指定位置對應的值

## reference
1. [Python Data Structures #2: Linked List](https://www.youtube.com/watch?v=JlMyYuY1aXU&t=610s)
2. [Data Structures in Python: Singly Linked Lists -- Deletion](https://www.youtube.com/watch?v=gXY_2wsQf3A)
3. [Linked List: Intro(簡介)](http://alrightchiu.github.io/SecondRound/linked-list-introjian-jie.html)
4. [Linked List: 新增資料、刪除資料、反轉](http://alrightchiu.github.io/SecondRound/linked-list-xin-zeng-zi-liao-shan-chu-zi-liao-fan-zhuan.html#series)

###### [🔗CONTENTS](#content)

# week 3
 > Topic : Stack and Queue

1. stack and queue 都是一種儲存資料的方式
2. Why stack?
   * 復原(undo)/回上一頁功能的需求
3. Why Queue?
   * 
4. 記法
   * stack 疊盤，後進先出
   * queue 排隊不能插隊，先進先出

> My ideas about making a mini stack?
   * `top()`:先確認是否至少有一個stack，沒有的話，把傳入的數值令成第一個stack。有的話，把最後一個傳入的令成top。
   * `push()`: 建立往上順序性的堆疊stacks。一樣先確認是否至少有一個stack，沒有的話建立第一個stack同時令為top，有的話把stack建立在第一個stack上面，並把最後一個傳入的值令為top。
   * `pop()`:刪除指定的stack。先找到top stack，回溯到指定的index，刪除該stack。
   * `getMin()`:傳回總共stack的個數。先找到top，往下數到最底層的stack。

## Key takeaway
1. 學習程式的兩個階段
   * 熟悉語法
   * 想法轉成程式碼的流程

## reference
1. [CS50 2017 - Lecture 5 - Data Structures](https://www.youtube.com/watch?v=eZQBx8YJ6Zs)
2. [CS50.tv](http://cs50.tv/2017/fall/)

###### [🔗CONTENTS](#content)

# week 4
> setmatch
## ideas
* 下面例對應的index [0,1,2,3,4,5,6]    [0,1,2,3,4,5,6]
* 假設一 array: a = [2,3,1,4,4,6,4] or [2,1,2,4,4,3,6] or [4,2,1,3,7,11,12]
* 排序後:sorted(a)= [1,2,3,4,4,4,6] or [1,2,2,3,4,4,6] or [1,2,3,4,7,11,12]
* 理想中 array: b = [1,2,3,4,5,6,7]
* 觀察: 
    * 每個位置的數值數值 = 對應的index+1
    * 下一個位置的值等於前一個+1

1. 先把list由小到大排列
2. 從1開始檢查，若下一個不是前一個+1，可能出現的情況：
    * 下一個值比前一個值+2以上 -> 該index有缺失值=index+1
    * 下一個等於前一個 -> 該index有缺失值=index+1，而且此index的值重複了
    > 找到缺失值和重複值可以先存在一個變數內最後一起回傳  

~找出缺少值:檢查每一個位置，每一個數值都要等於該位置的index+1，若不等於可以分3種情況: (1)大於index+2以上 (2)小於index (3)等於index~
> [code](https://github.com/okpersist/108_1_DSA/blob/master/week4/SetMismatch.py)

> Insertion Sort
## ideas

> QuickSort
## What is quicksort?
- 快速排序法：對於一串未排序數字，選一個數字基準點（推薦選中間數），比較基準點左右兩邊的數字，比基準點大的放基準點右邊，比基準點小的放基準點左邊。再從原本的基準點分成的左右兩堆中各選一個數字當基準點（也可選中間數），再重複比較數字大小改變位置。

## ideas
- example: 4, 31, 7, 8, 1, 2

1. 令 `mid_index` = 以((數串的長度//2)-1)選出中間的數。 _*答案有帶小數點時，取最接近商比較小的最大整數_
2. 對中間數取值 `mid_index.val` 
3. 把基準點左右兩堆的數字個別與基準點大小比較




## reference
###### [🔗CONTENTS](#content)
