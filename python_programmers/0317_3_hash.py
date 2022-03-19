#해쉬 테이블(리스트로 만들기)
# key값을 이용하여 value를 넣을 인덱스를 도출할 해시함수를 만듦/ 만든 인덱스에 value값 저장
# 원소 탐색, 삭제, 추가 ,읽기가 많은 작업일 때 사용
#https://davinci-ai.tistory.com/19
#https://www.fun-coding.org/DS&AL1-6.html

class HashTable:
    def __init__(self):
          self.hash_table = list([0 for i in range(8)])

    def hash_function(self, key): # 인덱스 도출할 함수
        return key % 10

    def insert(self, key, value):
        hash_value_idx = self.hash_function(hash(key))
        self.hash_table[hash_value_idx] = value # 정한 인덱스에 value 저장

    def get(self, key):
        if self.hash_table[key]>=2: # 동일한 key에 여러개의 value가 있을때
            value_arr=[]
            for k,v in self.hash_table:
                if k == key:
                    value_arr.append(v)
            return value_arr
        return self.hash_table[key] 

    def print(self):
        print(self.hash_table)

ht = HashTable() 
ht.insert(1, 'a') 
ht.print() 
ht.insert(2, 'kang') 
ht.print() 
ht.insert(2, 'b') # ('name','kang) 자리에 (2,'b')가 들어감 >> 충돌
ht.print()
print(ht.get(2)) 

# 내장함수 hsah()로 해쉬 키 생성
# hash('Dave')
# >>> 159933939503205923


