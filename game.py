import os # 載入作業系統operating system

#讀取檔案
def read_file(filename):
    games = []
    with open(filename, 'r', encoding = 'utf-8') as f:
        for line in f:
            if '遊戲, 價格' in line:
                continue # 跳到下一個迴圈
            name, price = line.strip().split(',') 
            games.append([name, price])
    return games

#讓使用者輸入
def user_input(games):
    while True:
        name = input('請輸入遊戲名稱: ')
        if name == 'q':
            break
        price = input('請輸入遊戲價格: ')
        price = int(price)
        games.append([name, price])
    print(games)
    return games

#印出遊戲
def print_game(games):
    for g in games:
        print(g) 
        print(g[0]) 

#寫入檔案
def write_file(filename, games):
    with open(filename, 'w', encoding = 'utf-8') as f:
        f.write('遊戲, 價格\n') #加入欄位名稱
        for g in games:
            f.write(g[0] + ',' + str(g[1]) + '\n') 

def main():
    filename = 'games.csv'
    if os.path.isfile(filename):#檢查檔案在不在
        print('讀取以前檔案')
        games = read_file(filename)
    else:
        print('歡迎!初次使用')
    games = user_input(games)
    print_game(games)
    write_file('games.csv', games)

main()

#refactor 重構，程式已function重新製作
#1.一個function執行一個動作
#2.有一個main function執行所有動作
#3.輸入物件不重複出現