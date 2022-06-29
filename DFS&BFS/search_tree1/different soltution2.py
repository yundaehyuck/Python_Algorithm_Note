from collections import deque


def get_adjacent(current, words):
    for word in words:
        if len(current) != len(word):
            continue

        count = 0
        for c, w in zip(current, word):
            if c != w:
                count += 1

        if count == 1:
            yield word #조건을 만족시키는 word들이 모여있는 제너레이터를 만들어줌


def solution(begin, target, words):
    dist = {begin: 0}
    queue = deque([begin])

    while queue:
        current = queue.popleft() #트리구조 탐색에는 deque & while 반복문이 기본형태

        for next_word in get_adjacent(current, words):
            if next_word not in dist:
                dist[next_word] = dist[current] + 1 #dict를 이용해서 해당 단어의 step수를 관리
                queue.append(next_word)

    return dist.get(target, 0) #target이라는 key가 존재하면 target의 value를 반환하고 없으면 0을 반환
