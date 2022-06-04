# 크레인 인형뽑기 게임
def solution(board, moves):
    answer = []
    cnt=0

    for x in moves: # while문 해서 moves.pop()하는 것 보다 빠름
        for i in range(len(board)):
            if  board[i][x-1] != 0:
                if answer and answer[-1] == board[i][x-1]:
                    cnt += 1
                    answer.pop()
                else:

                    answer.append(board[i][x-1])
                board[i][x-1] = 0
                break # 안하면 실패뜸! 중요

    return cnt*2