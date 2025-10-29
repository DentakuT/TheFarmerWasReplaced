# 現在位置から(desx,desy)まで最短距離で移動
def move_xy(desx,desy):
	nowx,nowy = get_pos_x(),get_pos_y()
	Disx = abs(nowx-desx)
	if Disx < get_world_size() - Disx:
		for _ in range(Disx):
			if nowx < desx:
				move(East)
			else:
				move(West)
	else:
		for _ in range(get_world_size() - Disx):
			if nowx < desx:
				move(West)
			else:
				move(East)
	
	Disy = abs(nowy-desy)	
	if Disy < get_world_size() - Disy:
		for _ in range(Disy):
			if nowy < desy:
				move(North)
			else:
				move(South)
	else:
		for _ in range(get_world_size() - Disy):
			if nowy < desy:
				move(South)
			else:
				move(North)


# List.count(x)
def count(List,x):
	cnt = 0
	for l in List:
		if l == x:
			cnt += 1
	return cnt

# List.index(x)
def index(List,x):
	ind = -1
	for i in range(len(List)):
		if List[i] == x:
			ind = i
			break
	return ind

# sorted(List)
def sorted(List):
	l = len(List)
	if l <= 1:
		return List

	mid = l // 2
	left = sorted(List[:mid])  
	right = sorted(List[mid:]) 

	m_List = []
	i = 0  
	j = 0  
	while i < len(left) and j < len(right):
		if left[i] < right[j]:
			m_List.append(left[i])
			i += 1
		else:
			m_List.append(right[j])
			j += 1
			
	m_List += left[i:]
	m_List += right[j:]
	return m_List
	
# list(reversed(List))
def reversed(List):
	return List[::-1]
	
# Listのコピー
def copy(List):
	return List[:]
	

# 二次元配列におけるmax。List[i][j]が最大値Mを取る場合、返り値は[i,j,M]のリスト
def max2d(List):
	m = -10**13
	ri,rj = -1,-1
	for i in range(len(List)):
		for j in range(len(List[i])):
			if List[i][j] > m:
				m = List[i][j]
				ri,rj = i,j
	return [ri,rj,m]
	
# H行W列のFalseを要素とするリストの作成
def boolList(H,W):
	L = []
	for _ in range(H):
		nL = []
		for _ in range(W):
			nL.append(False)
		L.append(nL)
	return L

# H行W列のFalseを要素とするリストの作成			
def zeroList(H,W):
	L = []
	for _ in range(H):
		nL = []
		for _ in range(W):
			nL.append(0)
		L.append(nL)
	return L
		
# 床関数。x以下の最大の整数
def floor(x):
	return x // 1

# 天井関数。x以上の最小の整数
def ceil(x):
	return -((-x) // 1)
	
# int(x)
def int(x):
	if x >= 0:
		return floor(x)
	else:
		return ceil(x)
	
# 一般的な認識での四捨五入。nはどの桁で四捨五入するかを表す値
#n=0 : 整数 -> round(11.52,0): 12
#n=1 : 小数第1位 -> round(11.52,2): 11.5
#n=-1: 10の位 -> round(11.52,-1); 10
def round(x,n):
	X = x * (10**n)
	if X >= 0:
		Y = int(X + 0.5)
	else:
		Y = int(X - 0.5)
		
	return Y / (10**n)

 
pi = 314159265.36
pi2 = pi * 2
scale = 10**8

# math.sin(x)を10^8倍したもの
# このゲームは小数第二位までしか扱えないので精度を高めるためにこのようにしている
# 実際に使う時には計算の最後に10**8で割るのを忘れないこと 
def sin(x):
	X = x * scale
	while X > pi:
		X -= pi2
	while X < -pi:
		X += pi2
		
	T = X     
	S = X   
	xs = (-1 * X**2) / scale
	t = 10 
	for n in range(1, 100):
		N = (T * xs) / scale
		T = N / ((2 * n) * (2 * n + 1))
		S += T
		if abs(T) < t:
			break
			
	return S

# math.cos(x)を10^8倍したもの
def cos(x):
	X = x * scale
	X += pi / 2
	while X > pi:
		X -= pi2
	while X < -pi:
		X += pi2
		
	T = X     
	S = X   
	xs = (-1 * X**2) / scale
	t = 10 
	for n in range(1, 100):
		N = (T * xs) / scale
		T = N / ((2 * n) * (2 * n + 1))
		S += T
		if abs(T) < t:
			break
			
	return S

# math.tan(x)を10^8倍したもの
def tan(x):
	return sin(x)*(10**8)/cos(x)
	
# 弧度法をラジアンに変換
def radians(deg):
	return deg * (pi / (180*(10**8)))

# ラジアンを弧度法に変換
def degrees(rad):
	return rad * ((180*(10**8)) / pi)
	
	
	
	
	
	
	
	
	
	
	
	
	
	
	
	
	
	
	
	
	
	
	
	
	
	
	
	


